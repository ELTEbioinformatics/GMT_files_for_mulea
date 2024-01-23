import requests
import statistics

with open ("D_melanogaster_uni_flybase.tab", "r") as translate_file:
    flybase_uni = {}
    translate_file.readline()
    for line in translate_file:
        line = line.strip().split("\t")
        if len(line) > 1:
            line[1] = line[1].split(";")
            for flybase_id in line[1]:
                if flybase_id != "":
                    if flybase_id not in flybase_uni:
                        flybase_uni[flybase_id] = []
                    flybase_uni[flybase_id].append(line[0])


with open ("Drosophila_melanogaster_modEncode.txt", "w") as output:
    for fb_id in flybase_uni.keys():
        url = "http://flybase.org/cgi-bin/serveHTdata.cgi?dataset=modENCODE_mRNA-Seq_tissues&FBgn=" + fb_id
        r = requests.get(url)
        if r.status_code == 200:
            output.write(r.text + "\n")


with open("Drosophila_melanogaster_modEncode.txt", "r") as raw_input_file:
    gene_tissue_expression = {}
    for line in raw_input_file:
        if line[0] == "#":
            continue
        line = line.strip().split("\t")
        if len(line) != 8:
            continue
        expression_number = float(line[6])
        if line[2] not in gene_tissue_expression:
            gene_tissue_expression[line[2]] = []
        gene_tissue_expression[line[2]].append({"location": line[5], "level": expression_number})

gene_tissue_expression_filter = {}
for gene in gene_tissue_expression.keys():
    expression_list = [i["level"] for i in gene_tissue_expression[gene]]
    cutoff = statistics.mean(expression_list) + statistics.stdev(expression_list)
    gene_tissue_expression_filter[gene] = [i["location"] for i in gene_tissue_expression[gene] if i['level'] > cutoff]

tissue_gene = {}
for gene in gene_tissue_expression_filter.keys():
    for tissue in gene_tissue_expression_filter[gene]:
        if tissue not in tissue_gene:
            tissue_gene[tissue] = []
        tissue_gene[tissue].append(gene)

with open("ModEncode_Drosophila_melanogaster_tissue_expression_GeneSymbol_Leila.gmt", "w") as output_file:
    output_file.write("# Gmt database for MulEA software (http://www.mulea.org/)" + "\n" + \
                      "# taxon_name: Drosophila_melanogaster" + "\n" + "# taxid: 7227" + '\n' + \
                      "# ID_type: Gene symbol" + "\n" + "# source url: http://www.modencode.org/" + '\n' + \
                      "# source_last_update: 29-08-2020" + "\n" + "# gmt_download_date: 22-09-2020" + "\n" + \
                      "# gmt_file_version: 2" + "\n" + '# gmt_entry_names: Tissue' + '\n' + '\n')
    output_file.write("# Tissue" + "\t" + "Tissue" + "\t" + "Gene set(Gene symbol)" + "\n")
    for tissue in tissue_gene:
        output_file.write(tissue + "\t" + tissue + "\t" + ",".join(tissue_gene[tissue]) + "\n")