
# coding: utf-8

# ## Generic GMT converter for flat .csv, .tsv etc files
# 
# A typical .gmt format file looks like the following:
# 
# R-HSA-5576886	Phase 4 - resting membrane potential	ENSG00000082482	ENSG00000095981	ENSG00000099337	ENSG00000100433	ENSG00000123700	ENSG00000124249	ENSG00000124780	ENSG00000135750	ENSG00000152315	ENSG00000164626	ENSG00000168135	ENSG00000169427	ENSG00000171303	ENSG00000173338	ENSG00000182324	ENSG00000182450	ENSG00000184185	ENSG00000184261	ENSG00000186795
# 
# The values are separated by tabs. The first two parameters are of higher significance, these contain the names and other auxillary data (IDs, type of experiment, alternate names) of the values listed.
# 
# Input parameters are:
# input_file = .csv, .tsv primary resource file
# 
# list_of_species = a list of strings containing the species in question
# 
# list_of_filters = a list of strings containing unwanted parameters if any
# 
# param1 = integer corresponding to the index of the column of the first parameter in the row ("R-HSA-5576886" in our example)
# 
# param2 = integer corresponding to the index of the column the second parameter in the row ("Phase 4 - resting membrane potential" in our example)
# 
# colnum_listed_values = integer corresponding to the index of the column of the values to be listed (from 0 - n)
# 
# separator = separator used by the input file (examples: ',', '\t')
# 
# colnum_sp = integer corresponding to the index of the column that holds the name of the species (from 0 - n)
# 
# colnum_filter = integer corresponding to the index of the column that holds the filtering criteria
# 

# In[10]:

def gmt_converter(input_file,list_of_species,
                  list_of_filters,param1,param2,
                  colnum_listed_values,separator, 
                  colnum_sp, colnum_filter):
    results = {}
    param2_values = {}
    with open(input_file, 'r') as raw_data:
        for line in raw_data:
            #read in the input file separator - by - separator
            cells = line.strip().split(separator)
            if cells[colnum_sp] in list_of_species and cells[colnum_filter] not in list_of_filters:
            #if the line contains the species we want and no filtering value add them to the dict
                if cells[colnum_sp] not in results:
                    results[cells[colnum_sp]] = {}
                if cells[param1] not in results[cells[colnum_sp]]:
                #add the first parameter to the corresponding species in the dict
                    results[cells[colnum_sp]][cells[param1]] = []   
                results[cells[colnum_sp]][cells[param1]].append(cells[colnum_listed_values])
                #list the listed values
                if cells[param1] not in param2_values:
                #add the second parameter
                    param2_values[cells[param1]] = cells[param2] 
    
    for sp in results:
        with open('Reactome_Ensembl_Marton_%s.gmt' %sp, 'w') as file:
            for j in results[sp]:
                file.write('%s\t%s\t%s\n' %(j, param2_values[j], '\t'.join(results[sp][j])))



gmt_converter(input_file = 'Ensembl2Reactome_All_Levels.txt', list_of_species = ['Arabidopsis thaliana', 'Caenorhabditis elegans', 'Dyctiostelium discoideum', 'Bos taurus','Danio rerio',
               'Homo sapiens', 'Gallus gallus', 'Xenpopus tropicalis', 'Drosophila melanogaster'], list_of_filters = ['IBA', 'IRD', 'ND', 'IBD', 'NR', 'IKR'], param1 = 2, param2 = 3, colnum_listed_values = 0, separator = '\t', colnum_sp = 5, colnum_filter = 4)





