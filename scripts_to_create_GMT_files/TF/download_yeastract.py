import urllib3
import gzip
from datetime import datetime


def download_Yeastract():
    '''
    :return: dictionary (key is the transcription factor and value is a list of regulated genes)
    '''
    tf_gene = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://www.yeastract.com/download/RegulationTwoColumnTable_Documented_2013927.tsv.gz')

    with open("test.gz", "wb") as output:
        output.write(bytes(r.data))

    with gzip.open("test.gz") as test_file:
        for line in test_file:
            line = str(line.strip()).replace("b", "").replace("'", "")
            tf_regulation = line.split(";")
            if tf_regulation[0] not in tf_gene:
                tf_gene[tf_regulation[0]] = []
            tf_gene[tf_regulation[0]].append(tf_regulation[1])

    return tf_gene

def write_out_file(tf_gene_dictionary):
    '''
    :param tf_gene_dictionary: dictionary with a key which is the transcription factor
    and with a value which is a list of regulated genes - created by download_TRRUST function
    '''
    with open ("Yeastract_Saccharomyces cerevisiae_Gene_symbol_Leila.gmt", 'w') as output_file:
        output_file.write("# Gmt database for MulEA software (http://www.mulea.org/)" + '\n' + '# taxon_name: Saccharomyces cerevisiae'+ '\n' +
                          '# taxid: 559292'+ '\n' + '# ID_type: Gene symbol' + '\n' + '# source_URL: http://www.yeastract.com/' + '\n' +
                          '# source_PMID: 29036684' + '\n' + '# source_version: release 2017' + '\n' + '# source_last_update: June 2017' + '\n' +
                          '# gmt_download_date:' + str(datetime.now()) + '\n' + '# gmt_file_version: 1' + '\n' + '# gmt_entry_names: Transcription factor' + '\n' + '\n'
                          '# Transcription factor' + '\t' + 'Transcription factor' + '\t' + 'Gene set (Gene symbol)' + "\n")
        for tf in tf_gene_dictionary:
            output_file.write(tf + '\t' + tf + '\t' + '\t'.join(tf_gene_dictionary[tf]) + '\n')


# Calling the functions
data = download_Yeastract()
result = write_out_file(data)

