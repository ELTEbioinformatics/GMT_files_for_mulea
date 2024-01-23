import subprocess
import gzip

file_names = [("https://www.pathwaycommons.org/archives/PC2/v12/PathwayCommons12.All.hgnc.gmt.gz","PathwayCommons12.All.hgnc.gmt.gz", "Gene symbol", "Pathway_Commons_Homo_sapiens_GeneSymbol_Leila.gmt"),
              ("https://www.pathwaycommons.org/archives/PC2/v12/PathwayCommons12.All.uniprot.gmt.gz","PathwayCommons12.All.uniprot.gmt.gz", "Uniprot", "Pathway_Commons_Homo_sapiens_Uniprot_Leila.gmt")]


for file_tuple in file_names:
    process = subprocess.Popen(["wget",file_tuple[0]])
    process.wait()

    with gzip.open(file_tuple[1], "r") as input:
        with open(file_tuple[3], "w") as output:
            output.write("# Gmt database for MulEA software (http://www.mulea.org/)" + "\n" + "# taxon_name: Homo sapiens" + "\n" + \
                 "# taxid: 9606 " + '\n' + "# ID_type: " + file_tuple[2] + "\n" + "# source_URL: www.pathwaycommons.org/" + "\n" + \
                 "# source_PMID: 21071392" + "\n" + "# source_version: Version 12 " + "\n" +\
                 "# source_last_update: 18-09-2019" + "\n" + "# gmt_download_date: 24-09-2020" + "\n" +\
                 "# gmt_file_version: 2 " + "\n" + "# gmt_entry_names: Pathway ID " + "\n" + "\n")
            output.write('# Pathway ID' + "\t" + "Pathway" + "\t" + "Gene set (" + str(file_tuple[2]) + ")" + "\n")
            count = 1
            for line in input:
                line = line.decode('utf8')
                line = line.strip().split("\t")
                data = line[1].split(":")
                pathway = data[1].split(";")
                pathway_id = "PC_" + str(count) + "\t"
                count += 1
                output.write(pathway_id + "\t" + pathway[0] + "\t" + "\t".join(line[2:]) + "\n")


