import csv
import sys


species_list = ['zfin', 'pombase', 'rgd', 'cow', 'human', 'wb', 'tair', 'sgd', 'mgi', 'fb', 'ecocyc', 'dictyBase', 'chicken']


def GO_conv(species):

    go2def = {}
    banned_evidence_codes = ['IRD', 'ND', 'IBD', 'NR', 'IKR']

    with open("GOid_name_namespace_def.tsv", 'r') as metadata_file:
        for rows in metadata_file:
            cells = rows.strip().split('\t')
            if cells[1] not in go2def:
                go2def[cells[0]] = cells[1]
    
    results = {}           

    with open('gene_association.%s' % species, 'r') as infile:
        for line in infile:
            if line[0] == '!':
                continue
            cols = line.strip().split('\t')
            if cols[7] not in banned_evidence_codes:
                if cols[4] not in results:
                    results[cols[4]] = cols[2]
    #print(results)

    csv.field_size_limit(sys.maxsize)

    row_data = []

    with open('allGO_offsp_formatted.txt', 'r') as infile:
        reader = csv.reader(infile, delimiter='\t')
        for line in reader:
            # ID remains unchanged, so keep the first value
            row = [line[0]]
            
            # Split the string into individual elements in a list
            id_codes = line[1].split(' ')
            #print(id_codes)
            # List comprehension to look for ID in the dictionary and return the
            # name stored against it
            translated = [results.get(item) for item in id_codes]
            #print(translated)
            translated = [item for item in translated if item != None]
            translated2 = list(set(translated))


            # Add translated to the list that we are using to represent a row
            row.extend(translated2)

        # Append the row to our collection of rows
            row_data.append(row)
    #print(row_data)


    go_gn2 = {d[0]: d[1:] for d in row_data} #dictionary from row_data

    
    new_dict = {k:v for k,v in go_gn2.items() if v} #remove empty lits from the values
    #print(new_dict)

    with open('GO_%s__Marton.gmt' % species,'w') as file:
        for pf in new_dict:
            try:
                file.write('%s\t%s\t%s\n' % (pf, go2def[pf], '\t'.join(go_gn2[pf])))
            except KeyError:
                continue


for i in species_list:
    GO_conv(i)


    pass
