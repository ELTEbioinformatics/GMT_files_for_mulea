import requests


species_information = [("https://www.grnpedia.org/trrust/data/trrust_rawdata.mouse.tsv","TRRUST_Mus_musculus_GeneSymbol_Leila.gmt", "Mus musculus", "10090"),
                       ("https://www.grnpedia.org/trrust/data/trrust_rawdata.human.tsv", "TRRUST_Homo_sapiens_GeneSymbol_Leila.gmt", "Homo sapiens", "9606")]


# Downloading mouse data from TRRUST
def download_TRRUST(filename, url):
    '''
    :param url: link of the data from the website
    :return: dictionary (key is the transcription factor and value is a list of regulated genes)
    '''
    with open(filename, 'w') as output:
        r = requests.get(url)
        if r.status_code == 200:
            output.write(r.text + "\n")


def process_file(raw_file):
    tf_gene = {}
    with open(raw_file) as tf_data:
        for tf in tf_data:
            tf_regulation = tf.split("\t")
            if len(tf_regulation) == 4:
                if tf_regulation[0] not in tf_gene:
                    tf_gene[tf_regulation[0]] = []
                tf_gene[tf_regulation[0]].append(tf_regulation[1])

    return tf_gene

# Writing out the results
def write_out_file(tf_gene_dictionary, output_name, taxon_name, taxid):
    '''
    :param tf_gene_dictionary:  dictionary with a key which is the transcription factor
    and with a value which is a list of regulated genes - created by download_TRRUST function
    :param output_name: name of the output file
    :param taxon_name: name of the taxon
    :param taxid: species taxid
    :return: file
    '''

    with open (output_name, 'w') as output_file:
        output_file.write("# Gmt database for MulEA software (http://www.mulea.org/)" + '\n' + '# taxon_name:' + taxon_name + '\n' +
                          '# taxid: ' + taxid + '\n' + '# ID_type: Gene symbol' + '\n' + '# source_URL: http://www.grnpedia.org/trrust/' + '\n' +
                          '# source_PMID: 29087512' + '\n' + '# source_version: version 2' + '\n' + '# source_last_update: 16-04-2018' + '\n' +
                          '# gmt_download_date:' + '\n' + '# gmt_file_version: 2' + '\n' + '# gmt_entry_names: Transcription factor' + '\n' + '\n'
                          '# Transcription factor' + '\t' + 'Transcription factor' + '\t' + 'Gene set (Gene symbol)' + '\n')
        for tf in tf_gene_dictionary:
            output_file.write(tf + '\t' + tf + '\t' + ','.join(tf_gene_dictionary[tf]) + '\n')



# Combine the two functions - Downloading and writing out data into the current folder
for species in species_information:
    raw_filename = 'TF-TG_network_' + species[2] + ".txt"
    data = download_TRRUST(raw_filename,species[0])
    result = process_file(raw_filename)
    write_out_file(result, species[1], species[2], species[3])



