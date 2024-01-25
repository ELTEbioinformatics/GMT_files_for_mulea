# A script, which takes one or more GMT files and maps all of the identifiers from a choosen database to another choosen database.


# Import relevant packages
import subprocess
import argparse
import logging
import math
import json
import time
import sys
import os


# Define the logging format 
logging.basicConfig(format = '%(asctime)s | %(levelname)s: %(message)s', level = logging.INFO)


# Define the function to parse the arguments
def parse_args(args):
    help_text = \
        """
        === MulEA ID mapping script ===
        Script to map all of the necessary identifiers from a GMT files.
        """

    parser = argparse.ArgumentParser(description=help_text)

    # Add input files list argument
    parser.add_argument("-i", "--input-files",
                        help="<list for the input files> [mandatory]",
                        type=str,
                        dest="input_files",
                        action="store",
                        required=True)

    # Add output files list argument
    parser.add_argument("-o", "--output-files",
                        help="<list for the output files> [mandatory]",
                        type=str,
                        dest="output_files",
                        action="store",
                        required=True)

    # Add the choosen from database
    parser.add_argument("-fd", "--from-database",
                        help="<from database, where mapping from> [mandatory]",
                        type=str,
                        dest="from_database",
                        action="store",
                        required=True)

    # Add the choosen to database
    parser.add_argument("-td", "--to-database",
                        help="<to database, where mapping to> [mandatory]",
                        type=str,
                        dest="to_database",
                        action="store",
                        required=True)

    # Add the choosen taxonomy identifier (optional)
    parser.add_argument("-tax", "--tax-id",
                        help="<taxonomy identifier of the species> [optional]",
                        type=int,
                        dest="tax_id",
                        action="store",
                        required=False)

    # Parse the arguments
    results = parser.parse_args(args)

    # Return the parsed arguments
    return results.input_files, results.output_files, results.from_database, results.to_database, results.tax_id


# Define the function to get the UniProt JobID
def GetUniProtJobID(number_id):

    # Create a command file
    JobIDFile = open(f"UniProtJobID_number{number_id}.txt", 'wb')
    command_file = f"UniProtJobCommand_number{number_id}.sh"
    running_command = ["bash", command_file]
    subprocess.run(running_command, stderr = subprocess.PIPE, stdout = JobIDFile)

    # Open the JobID file and get the JobID
    with open(f"UniProtJobID_number{number_id}.txt", 'r') as jobid_result:

        for line in jobid_result:
            line = line.strip().split('"')

            return line[3]


# Define the function to check the status of the UniProt JobID
def CheckingStatus(number_id, JobID):

    # Create a status file
    JobIDStatusFile = open(f"UniProtJobIDStatus_number{number_id}.txt", 'wb')
    checking_command = ["curl", "-i", f"https://rest.uniprot.org/idmapping/status/{JobID}"]
    subprocess.run(checking_command, stderr = subprocess.PIPE, stdout = JobIDStatusFile)

    # Open the status file and get the status
    with open(f"UniProtJobIDStatus_number{number_id}.txt", 'r') as jobid_status:

        for line in jobid_status:

            if not line.startswith("{"):
                continue

            line = line.strip().split('"')

            return line[3]


# Define the function to get the results of the UniProt JobID
def GetResults(number_id, JobID):

    JobIDResultFile = open(f"UniProtJobIDResults_number{number_id}.json", 'w')
    checking_command = ["curl", "-s", f"https://rest.uniprot.org/idmapping/stream/{JobID}"]
    subprocess.run(checking_command, stderr = subprocess.PIPE, stdout = JobIDResultFile)

# Start the MulEA GMT Mapping script
print("")
logging.info("### Start the MulEAIDMapping.py script!")

# Define the input arguments
input_files, output_files, from_database, to_database, tax_id = parse_args(sys.argv[1:])

print("")
# Write out the given input files
logging.info(f"### Your choosen input files are: ")
for inp in input_files.split(","):
    print('      ', inp)

print("")
# Write out the given output files
logging.info(f"### Your choosen output files are: ")
for outp in output_files.split(","):
    print('      ', outp)

print("")
# Write out the given from and to databases
logging.info(f"### Your choosen FromDatabase: {from_database}")
logging.info(f"### Your choosen ToDatabase: {to_database}")

# Write out the given taxonomy identifier, if it is given
if tax_id:
    logging.info(f"### Your choosen taxonomy identifier: {tax_id}")

else:
    logging.warning(f"### You DID NOT choose a taxonomy identifier!")

logging.info("### Parameters are fine, starting...")
print("")
# Collect all of the identifiers from the input file
sys.stdout.write("[ RUNNING ] ### Collect all of the identifiers from the input file!")
print("")

# Define the necessary variables
mapping_dictionary = {}
MappingIDs = {}
MappingIDsEdited = []

# Open the input file and collect the identifiers into a dictionary
for input_file in input_files.split(","):

    with open(input_file, 'r') as gmt:
        sys.stdout.write(f"Opening the file: {input_file}")
        print("")

        for gmt_line in gmt:

            if gmt_line.startswith("#"):
                continue

            gmt_line = gmt_line.strip().split('\t')

            for index in range(2, len(gmt_line)):

                if gmt_line[index] not in MappingIDs:
                    MappingIDs[gmt_line[index]] = None

sys.stdout.write("[   DONE   ] ### Collect all of the identifiers from the input file!")
print("")
print("")

# Change the identifiers if it is necessary and removes the following characters from the IDs: ;, ', /, {, (, , &# and whitespace
for m in MappingIDs:

    if ";" in m:
        MappingIDsEdited.append(m.split(";")[0])
        continue

    if "'" in m:
        continue

    if "/" in m or "{" in m or "(" in m or " " in m or "&#" in m:
        continue

    if "ZEAMMB73" in m:
        alternative_id = f"ZEAMMB73_{m}"
        MappingIDsEdited.append(alternative_id)

    MappingIDsEdited.append(m)

# Count the number of the collected IDs
number_of_results = len(MappingIDsEdited)

sys.stdout.write(f"### The number of collected IDs is: {number_of_results}!")
print("")

# Check and define the number of the API requests from the UniProt API
NumberOfChunksOfResults = number_of_results / 5000
Reminder = number_of_results % 5000
NumberAPIRun = math.ceil(NumberOfChunksOfResults)

sys.stdout.write(f"### The number of running the API request: {NumberAPIRun}")
print("")
print("")

# Define the indexes for the UniProt API runs
if NumberAPIRun == 1:
    start_number = 0
    end_number = number_of_results

if NumberAPIRun > 1:
    start_number = 0
    end_number = 5000

# Run the UniProt API requests after each other
for y in range(1, NumberAPIRun + 1):
    MappingIDsFinal = ",".join(MappingIDsEdited[start_number:end_number])

    sys.stdout.write(f"\r[ RUNNING ] ### Run the UniProt API request number #{y}!")

    # Create a shell script for the UniProt API request
    with open(f"UniProtJobCommand_number{y}.sh", 'w') as out:

        MappingIDsFinal_final = f'"{MappingIDsFinal}"'
        from_database_final = f'"{from_database}"'
        to_database_final = f'"{to_database}"'
        tax_id_final = f'"{tax_id}"'

        if tax_id:
            out.write(f"curl --form 'from={from_database_final}' \--form 'to={to_database_final}' \--form 'ids={MappingIDsFinal_final}' \--form 'taxId={tax_id_final}' \https://rest.uniprot.org/idmapping/run")

        else:
            out.write(f"curl --request POST 'https://rest.uniprot.org/idmapping/run' --form 'ids='{MappingIDsFinal}'' --form 'from='{from_database}'' --form 'to='{to_database}''")

    # Get the UniProt JobID
    JobID = GetUniProtJobID(y)

    # Checking until we get the relevant JobID
    while "http" in JobID:

        JobID = GetUniProtJobID(y)
        time.sleep(1)

    # Check the status of the UniProt JobID and continue if it is still running
    JobStatus = CheckingStatus(y, JobID)

    while(JobStatus == "RUNNING"):

        JobStatus = CheckingStatus(y, JobID)
        time.sleep(1)

    # Get the results of the UniProt JobID
    GetResults(y, JobID)

    sys.stdout.write(f"\r[   DONE   ] ### Run the UniProt API request number #{y}!")
    print("")

    # Define the indexes for the next UniProt API run
    start_number += 5000

    if y == NumberAPIRun - 1:
        end_number += Reminder

    else:
        end_number += 5000

    sys.stdout.write(f"### The JobID was: {JobID}!")
    print("")

    sys.stdout.write("\r[ RUNNING ] ### Creating the mapping dictionary!")

    # Open the results of the UniProt API request and create a dictionary from the results
    with open(f"UniProtJobIDResults_number{y}.json", 'r') as json_results:

        for line in json_results:
            line = json.loads(line.strip())

            for result in line["results"]:

                if result["from"] not in mapping_dictionary:
                    mapping_dictionary[result["from"]] = []

                mapping_dictionary[result["from"]].append(result["to"])

    sys.stdout.write("\r[   DONE   ] ### Creating the mapping dictionary!")
    print("")
    print("")

sys.stdout.write("\r[ RUNNING ] ### Writing out the results!")

# Open the input and output file and write out the results
for z in range(0, len(input_files.split(","))):

    input_file = input_files.split(",")[z]
    output_file = output_files.split(",")[z]
    output_logfilename = output_file.split(".")[0]
    output_logfile= f"{output_logfilename}.log"

    # Open the input and output file and write out the results
    with open(input_file, 'r') as gmt, open(output_file, 'w') as out_final, open(output_logfile, 'w') as outlog:

        # Write out the header of the output file
        for gmt_line in gmt:

            if gmt_line.startswith("#") or gmt_line.startswith('\n'):
                out_final.write(gmt_line)
                outlog.write(gmt_line)
                continue

            # Define the new IDs and the IDs which were not found in the UniProt database
            gmt_line = gmt_line.strip().split('\t')
            NewIDs = []
            OutLogIDs = []

            # Iterate through the IDs and replace them with the UniProt IDs
            for index in range(2, len(gmt_line)):

                if gmt_line[index] in mapping_dictionary:
                    NewIDs.append(mapping_dictionary[gmt_line[index]][0])

                else:
                    OutLogIDs.append(gmt_line[index])

            # Define the final output
            NewIDsFinal = '\t'.join(NewIDs)

            # Write out the results
            out_final.write(gmt_line[0] + '\t' + gmt_line[1] + '\t' + NewIDsFinal + '\n')

            # Check if there are IDs which were not found in the UniProt database and write them out
            if len(OutLogIDs) != 0:
                OutLogIDsFinal = '\t'.join(OutLogIDs)
                outlog.write(gmt_line[0] + '\t' + gmt_line[1] + '\t' + OutLogIDsFinal + '\n')

sys.stdout.write("\r[   DONE   ] ### Writing out the results!")
print("")
print("")
# Finish the script
logging.info("The MulEAIDMapping.py script finished successfully! Nice job! :)")
print("")
