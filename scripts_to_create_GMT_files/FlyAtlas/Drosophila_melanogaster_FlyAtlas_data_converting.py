import statistics

with open("Drosophila_melanogaster_FlyAtlas_anatomy.txt", "r") as raw_input_file:
    gene_tissue_expression = {}
    for line in raw_input_file:
        if line[0] == "#":
            continue
        line = line.strip().split("\t")
        if len(line) != 8:
            continue
        expression_number = float(line[5])
        if line[1] not in gene_tissue_expression:
            gene_tissue_expression[line[1]] = []
        gene_tissue_expression[line[1]].append({"location": line[4], "level": expression_number})

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

with open("FlyAtlas_Drosophila_melanogaster_EnsemblID_Leila.gmt", "w") as output:
    for tissue in tissue_gene:
        output.write(tissue + "\t" + tissue + "\t" + "\t".join(tissue_gene[tissue]) + "\n")