# Creating GMT files from KEGG data to be used with enrichment analyses

import urllib.request
import os.path
import sys
from datetime import datetime

# species IDs (and TAX IDs):
    # ath - Arabidopsis thaliana (3702)
    # bsu - Bacillus subtilis (224308)
    # bta - Bos taurus (9913)
    # bth - Bacteroides thetaiotaomicron (226186)
    # blo - Bifidobacterium longum (206672)
    # cel - Caenorhabditis elegans (6239)
    # cre - Chlamydomonas reinhardtii (3055)
    # dre - Danio rerio (7955)
    # ddi - Dictyostelium discoideum (352472)
    # dme - Drosophila melanogaster (7227)
    # dpx - Daphnia pulex (6669)
    # dsi - Drosophila simulans (7240)
    # eco - Escherichia coli (511145)
    # gga - Gallus gallus (9031)
    # hsa - Homo sapiens (9606)
    # mcc - Macaca mulatta (9544)
    # mmu - Mus musculus (10090)
    # mtu - Mycobacterium tuberculosis (83332)
    # ncr - Neurospora crassa (367110)
    # ptr - Pan troglodytes (9598)
    # rno - Rattus norvegicus (10116)
    # sce - Saccharomyces cerevisae (559292)
    # stm - Salmonella enterica (99287)
    # spo - Schizosaccharomyces pombe (284812)
    # tet - Tetrahymena thermophila (312017)
    # xla - Xenopus laevis (8355)
    # xtr - Xenopus tropicalis (8364)
    # zma - Zea mays (4577)

species_list = ["ath", "bsu", "bta", "bth", "blo", "cel", "cre", "dre", "ddi", "dme", "dpx", "dsi", "eco", "gga", "hsa",
                "mcc", "mmu", "mtu", "ncr", "ptr", "rno", "sce", "stm", "spo", "tet", "xla", "xtr", "zma"]

# Downloading KEGG Pathways
def download_pathway_id(species_ID):
    '''
    :param species_ID: ID of species in KEGG, there are found in species_list
    :return: output is a dictionary (key is KEGG Pathway ID, value is name of the pathway)
    '''
    if species_ID not in species_list:
        print("Please enter a valid species ID from the following:")
        print("ath - Arabidopsis thaliana",
              "bsu - Bacillus subtilis",
              "bta - Bos taurus",
              "bth - Bacteroides thetaiotaomicron",
              "blo - Bifidobacterium longum",
              "cel - Caenorhabditis elegans",
              "cre - Chlamydomonas reinhardtii",
              "dre - Danio rerio",
              "ddi - Dictyostelium discoideum",
              "dme - Drosophila melanogaster",
              "dpx - Daphnia pulex",
              "dsi - Drosophila simulans",
              "eco - Escherichia coli",
              "gga - Gallus gallus",
              "hsa - Homo sapiens",
              "mcc - Macaca mulatta",
              "mmu - Mus musculus",
              "mtu - Mycobacterium tuberculosis",
              "ncr - Neurospora crassa",
              "ptr - Pan troglodytes",
              "rno - Rattus norvegicus",
              "sce - Saccharomyces cerevisae",
              "stm - Salmonella enterica",
              "spo - Schizosaccharomyces pombe",
              "tet - Tetrahymena thermophila",
              "xla - Xenopus laevis",
              "xtr - Xenopus tropicalis",
              "zma - Zea mays")

    id_pathway = {}
    url = "http://rest.kegg.jp/list/pathway/" + species_ID
    response = urllib.request.urlopen(url)
    pathway_data = response.read()
    pathway_data = pathway_data.decode().split("\n")
    for pathway in pathway_data:
        pathway = pathway.split("\t")
        if len(pathway) == 2:
            pathway[0] = pathway[0].replace("path:", "")
            pathway[1] = pathway[1].rsplit(" -", 1)[0]
            id_pathway[pathway[0]] = pathway[1]
    return id_pathway

# Downloading genes in pathways
def download_gene_list(pathway_id):
    '''
    :param pathway_id: input dictionary (key is KEGG Pathway ID, value is name of the pathway),
    created by download_pathway_id function
    :return: output is a new dictionary (key is tuple - (pathway ID, pathway name) - and value is a list of genes in the pathway)
    '''

    pathway_genes = {}
    for id in pathway_id:
        url_2 = "http://rest.kegg.jp/get/" + id
        response = urllib.request.urlopen(url_2)
        gene_data = response.read()
        gene_data = gene_data.decode().split("\n")
        is_good_row = False
        for row in gene_data:
            if row[0:4] == "GENE":
                is_good_row = True
            elif row[0:4] == "    " and is_good_row == True:
                is_good_row = True
            elif row[0:4] == "COMP":
                is_good_row = False
            elif row[0:4] == "    " and is_good_row == False:
                is_good_row = False
            elif row[0:4] != "    " and is_good_row == True:
                is_good_row = False

            if is_good_row:
                row = row.replace(row[0:12], "")
                row = row.split(" ")
                if ";" in row[2]:
                    gene = row[2].replace(";", "")
                else:
                    gene = row[0]
                if (id, pathway_id[id]) not in pathway_genes:
                    pathway_genes[(id, pathway_id[id])] = []
                pathway_genes[(id, pathway_id[id])].append(gene)
    return pathway_genes


# Writing out the results to a given or current folder
def write_out_file(pathway_and_gene_list, output_name, location = ""):
    '''
    :param species_ID: ID of species in KEGG, there are found in species_list
    :param pathway_and_gene_list: dictionary (key is tuple - (pathway ID, pathway name) - and value is a list of genes in the pathway),
    created by download_gene_list function
    :param output_name: name of the output file
    :param location: place of output files (optional, is it isn't given files are saved in current folder)
    '''
    date = str(datetime.now())
    with open(os.path.join(location, output_name), "w") as output_file:
        output_file.write("# Gmt database for MulEA software (http://www.mulea.org/)" + "\n" + "# source url: http://www.genome.jp/kegg/pathway.html"  +
                          '\n' + "# gmt_download_date: " + date + "\n" + "# gmt_entry_names: gene symbol"+ "\n" + '# gmt_id_type: KEGG Pathway ID' + '\n' +'\n')
        output_file.write("# Pathway ID" + "\t" + "Pathway name"+ "\t" + "Gene set" + "\n")

        for pathway, gene_list in pathway_and_gene_list.items():
            output_file.write(pathway[0] + '\t' + pathway[1] + "\t" + "\t".join(gene_list) + "\n")


# Combine functions - Downloading and writing out pathways and gene lists
# (location isn't given, data will be saved in the current folder)

try:
    pathway_id = download_pathway_id(sys.argv[1])
    pathway_gene_dictionary = download_gene_list(pathway_id)
except IndexError:
    print("Please enter valid species ID from the following:")
    print("ath - Arabidopsis thaliana",
          "bsu - Bacillus subtilis",
          "bta - Bos taurus",
          "bth - Bacteroides thetaiotaomicron",
          "blo - Bifidobacterium longum",
          "cel - Caenorhabditis elegans",
          "cre - Chlamydomonas reinhardtii",
          "dre - Danio rerio",
          "ddi - Dictyostelium discoideum",
          "dme - Drosophila melanogaster",
          "dpx - Daphnia pulex",
          "dsi - Drosophila simulans",
          "eco - Escherichia coli",
          "gga - Gallus gallus",
          "hsa - Homo sapiens",
          "mcc - Macaca mulatta",
          "mmu - Mus musculus",
          "mtu - Mycobacterium tuberculosis",
          "ncr - Neurospora crassa",
          "ptr - Pan troglodytes",
          "rno - Rattus norvegicus",
          "sce - Saccharomyces cerevisae",
          "stm - Salmonella enterica",
          "spo - Schizosaccharomyces pombe",
          "tet - Tetrahymena thermophila",
          "xla - Xenopus laevis",
          "xtr - Xenopus tropicalis",
          "zma - Zea mays")
    exit(1)


try:
    output_file = write_out_file(pathway_gene_dictionary, sys.argv[2])  # as a third parameter location can be added
except IndexError:
    print("Please give an output file name")
    exit(1)


# Running the script from the terminal:
# Go to the folder where this script is located
# python name_of_this_script species_id outputfile_name
# e.g. python download_kegg.py cel c_elegans_KEGG.gmt