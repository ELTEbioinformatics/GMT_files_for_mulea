import subprocess
import gzip

species_data = []

with open("ensembl_species_details.csv") as data:
    data.readline()
    for line in data:
        line = line.strip().split("\t")
        link = line[0].split("/")
        species_data.append(line)

def ensemble_file_converter(input_file):
    location_gene_info = {}
    gene_info = []
    with gzip.open(input_file, "rb") as input_file:
        for line in input_file:
            line = line.decode('utf8')
            if line[0] == "#":
                continue
            line = line.strip().split("\t")
            if line[2] == 'gene':
                ids = line[8].split(";")
                gene_info_list = (line[0], line[3], line[4], ids[0])
                gene_info.append(gene_info_list)
                if gene_info_list[0] not in location_gene_info:
                    location_gene_info[gene_info_list[0]] = []
                location_gene_info[gene_info_list[0]].append(gene_info_list)
    return location_gene_info


def write_output(output, species_info, location_gene_info, gene_num):
    with open(output, "w") as output:
        output.write("# Gmt database for MulEA software (http://www.mulea.org/)" + "\n" + "# taxon_name: " + species_info[1] + "\n" + \
             "# taxid: " + species_info[2] + '\n' + "# ID_type: " + species_info[3] + "\n" + "# source_URL: " + species_info[4] + "\n" + \
             "# source_PMID: " + species_info[5] + "\n" + "# source_version: " + species_info[6] + "\n" +\
             "# source_last_update: " + species_info[7] + "\n" + "# gmt_download_date: " + species_info[8] + "\n" +\
             "# gmt_file_version: " + species_info[9] + "\n" + "# gmt_entry_names: " + species_info[10] + "\n")
        output.write("# Chromosome location" + "\t" + "Chromosome location"+ "\t" + "Gene set (Locus ID)" + "\n")
        for location in location_gene_info:
            sorted(location_gene_info[location], key=lambda x: x[1])
            genes = []
            for gene_info_list in location_gene_info[location]:
                gene_id = gene_info_list[3]
                i = gene_id.replace("gene_id ", "").replace('"', "")
                genes.append((gene_info_list[1], gene_info_list[2], i))
                if len(genes) == gene_num:
                    gene_set = [i[2] for i in genes]
                    location = location.replace("Chromosome", " ")
                    output.write("chro" + " " + location + ' ' + genes[0][0] + "-" + genes[4][1] + "\t" +
                                 "chro" + " " + location + ' ' + genes[0][0] + "-" + genes[4][1] + "\t" +
                                 "\t".join(gene_set ) + "\n")
                    del genes[0]


for list_ in species_data:
    link = list_[0].split("/")

    process = subprocess.Popen(["wget", list_[0]])
    process.wait()

    result = ensemble_file_converter(link[-1])

    out_name = "Ensembl_" + str(list_[1]) + "_5genes_LocusID_Leila.gmt"
    write_output(out_name, list_, result, 5)

    out_name = "Ensembl_" + str(list_[1])+ "_10genes_LocusID_Leila.gmt"
    write_output(out_name, list_, result, 10)


    out_name = "Ensembl_" + str(list_[1])+ "_20genes_LocusID_Leila.gmt"
    write_output(out_name, list_, result, 20)

    process_3 = subprocess.Popen(["rm", link[-1]])
    process_3.wait()


