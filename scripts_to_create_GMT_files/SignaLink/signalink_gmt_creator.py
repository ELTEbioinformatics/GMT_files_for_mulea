def file_converter(input_file, sep):
    '''
    :param input_file: raw file from Signalink
    :param sep: column separator
    :return: [[gene, pathways],[],[],[]...[]]
    '''
    source_target_pathways_data = []
    gene_pathway = []
    with open(input_file, "r") as input_file:
        input_file.readline()
        for line in input_file:
            line = line.strip().split(sep)
            source_target_pathways_data.append([line[0], line[1], line[5], line[6], line[7], line[11]])
        for list_ in source_target_pathways_data:
            if [list_[0], list_[2]] not in gene_pathway and [list_[3], list_[5]] not in gene_pathway:
                gene_pathway.append([list_[0], list_[2]])
                gene_pathway.append([list_[3], list_[5]])
            elif [list_[0], list_[2]] not in gene_pathway:
                gene_pathway.append([list_[0], list_[2]])
            elif [list_[3], list_[5]] not in gene_pathway:
                gene_pathway.append([list_[3], list_[5]])
    return gene_pathway


def gmt_creator(gene_pathway_list, cell_sep, output_file):
    '''
    :param gene_pathway_list: modified input file
    :param cell_sep: cell separator
    :param output_file: pathway - gene list
    '''
    parameter_gene = {}
    for list_ in gene_pathway_list:
        list_[1] = list_[1].split(cell_sep)
        for parameter in list_[1]:
            if parameter:
                if parameter not in parameter_gene:
                    parameter_gene[parameter] = []
                parameter_gene[parameter].append(list_[0])
    with open(output_file, "w") as output:
        for parameter in parameter_gene:
            output.write(parameter + "\t" + parameter + "\t" + "\t".join(parameter_gene[parameter]) + "\n")

gene_pathway_tuple = file_converter("human_0_1_signalink.csv", ";")
gmt_creator(gene_pathway_tuple, ",", "human_pathway.csv")
