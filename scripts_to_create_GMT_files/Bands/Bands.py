
bands = {}

with open('Bands_Homo_sapiens_Genesymbol_Marton', 'r') as f:
    for lines in f:
        cells = lines.strip().split('\t')
        if len(cells) == 3:
            if cells[0] not in bands:
                 bands[cells[0]] = {"subCategory":set(), "genes":set()}
                 bands[cells[0]]["subCategory"].add(cells[1])
            
print(bands)