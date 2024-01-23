import requests


def download_RegulonDB():
    '''
    :return: dictionary (key is the transcription factor and value is a list of regulated genes)
    '''
    with open('TF-TG_network.txt', 'w') as output:
        url = "http://regulondb.ccg.unam.mx/menu/download/datasets/files/network_tf_gene.txt"
        r = requests.get(url)
        if r.status_code == 200:
            output.write(r.text + "\n")

def process_file(raw_file):
    tf_gene = {}
    with open(raw_file) as tf_data:
        for tf in tf_data:
            if tf[0] == '#':
                continue
            tf_regulation = tf.split("\t")
            if tf_regulation[0] not in tf_gene:
                tf_gene[tf_regulation[0]] = set()
            tf_gene[tf_regulation[0]].add(tf_regulation[1])

    return tf_gene

def write_out_file(tf_gene_dictionary):
    '''
    :param tf_gene_dictionary: dictionary with a key which is the transcription factor
    and with a value which is a list of regulated genes - created by download_TRRUST function
    '''
    with open ("RegulonDB_Escherichia_coli_Gene_symbol_Leila.gmt", 'w') as output_file:
        output_file.write("# Gmt database for MulEA software (http://www.mulea.org/)" + '\n' + '# taxon_name: Escherichia coli K-12'+ '\n' +
                          '# taxid: 83333 '+ '\n' + '# ID_type: Gene symbol' + '\n' + '# source_URL: http://regulondb.ccg.unam.mx/' + '\n' +
                          '# source_PMID: 26527724' + '\n' + '# source_version: release 10.7 ' + '\n' + '# source_last_update: 05-04-2020' + '\n' +
                          '# gmt_download_date: 24-09-2020' + '\n' + '# gmt_file_version: 2' + '\n' + '# gmt_entry_names: Transcription factor' + '\n' + '\n'
                          '# Transcription factor' + '\t' + 'Transcription factor' + '\t' + 'Gene set (Gene symbol)' + '\n')
        for tf in tf_gene_dictionary:
            output_file.write(tf + '\t' + tf + '\t' + ','.join(tf_gene_dictionary[tf]) + '\n')


# Calling the functions
data = download_RegulonDB()
result = process_file("TF-TG_network.txt")
write_out_file(result)

