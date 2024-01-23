# -*- coding: utf-8 -*-

import pandas as pd


data_xls = pd.read_excel('miRTarBase_MTI.xlsx', 'miRTarBase', index_col=None, encoding="utf-8")  #had to manually rename the worksheet 
                                                                        #since it was in traditional chinese
                                                                        #originally
data_xls.to_csv('miRTarBase_MTI.csv', encoding='utf-8', index=False, header=False)



list_of_species = ['Arabidopsis thaliana', 'Caenorhabditis elegans', 'Danio rerio',
               'Homo sapiens', 'Gallus gallus', 'Mus musculus', 'Rattus norvegicus', 
                  'Xenpopus tropicalis','Drosophila melanogaster']
weak_experimental_evidences = ['Microarray', 'pSILAC']
results = {}
mirnaID = {}

with open('miRTarBase_MTI.csv', 'r') as mirna:
    for line in mirna:
        rows = line.strip().split(',')
        if rows[2] in list_of_species and rows[6] not in weak_experimental_evidences:
            if rows[2] not in results:
                results[rows[2]] = {}
            if rows[1] not in results[rows[2]]:
                results[rows[2]][rows[1]] = set()
            results[rows[2]][rows[1]].add(rows[3])
            if rows[1] not in mirnaID:
                mirnaID[rows[1]] = rows[0]
print(results)
for species in results:
    with open('mirna_%s_genesymbol.gmt' %species, 'w') as outfile:
        for mirna in results[species]:
            outfile.write('%s\t%s\t%s\n' %(mirna, mirnaID[mirna], '\t'.join(list(set(list(results[species][mirna]))))))




