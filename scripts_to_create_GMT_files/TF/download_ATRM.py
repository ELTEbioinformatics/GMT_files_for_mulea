import requests
import xlrd
import csv
from datetime import datetime


def downloading_ATRM():
    """
    :return: the function downloads the xlsx file from the website and converts it to a processable csv file
    """
    url = 'http://atrm.cbi.pku.edu.cn/for_download/Regulations_in_ATRM.xlsx'
    resp = requests.get(url)

    with open('test.xlsx', 'wb') as output:
        output.write(resp.content)

    wb = xlrd.open_workbook('test.xlsx')
    sh = wb.sheet_by_name('ATRM')
    with open('ATRM.csv', 'w') as csv_file:
        wr = csv.writer(csv_file)

        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))


def processing_ATRM():
    '''
    :return: output is a dictionary (key is the transcription factor and value is a list of regulated genes)
    '''
    with open('ATRM.csv') as input_file:
        input_file.readline()
        tf_gene = {}
        for line in input_file:
            line = line.split(",")
            if line[2] not in tf_gene:
                tf_gene[line[2]] = []
            tf_gene[line[2]].append(line[3])

        return tf_gene

def write_out_file(tf_gene_dictionary):
    '''
    :param tf_gene_dictionary: dictionary with a key which is the transcription factor
    and with a value which is a list of regulated genes - created by download_TRRUST function
    '''
    with open ("ATRM_Arabidopsis_thaliana_Gene_symbol_Leila.gmt", 'w') as output_file:
        output_file.write("# Gmt database for MulEA software (http://www.mulea.org/)" + '\n' + '# taxon_name: Arabidopsis thaliana'+ '\n' +
                          '# taxid: 3701 '+ '\n' + '# ID_type: Gene symbol' + '\n' + '# source_URL: http://atrm.cbi.pku.edu.cn/index.php' + '\n' +
                          '# source_PMID: 25750178' + '\n' + '# source_version: version 4.0 ' + '\n' + '# source_last_update: 21-07-2017' + '\n' +
                          '# gmt_download_date:' + str(datetime.now()) + '\n' + '# gmt_file_version: 1' + '\n' + '# gmt_entry_names: Transcription factor' + '\n' + '\n'
                          '# Transcription factor' + '\t' + 'Transcription factor' + '\t' + 'Gene set (Gene symbol)' + '\n')
        for tf in tf_gene_dictionary:
            output_file.write(tf + '\t' + tf + '\t' + '\t'.join(tf_gene_dictionary[tf]) + '\n')



# Combine the functions - Downloading and writing out data into the current folder
downloading_ATRM()
tf_dictionary = processing_ATRM()
write_out_file(tf_dictionary)
