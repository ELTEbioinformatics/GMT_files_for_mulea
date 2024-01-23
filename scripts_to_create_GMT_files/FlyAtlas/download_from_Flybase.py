import requests

with open ("D_melanogaster_uni_flybase.tab", "r") as translate_file:
    uni_flybase = {}
    translate_file.readline()
    for line in translate_file:
        line = line.strip().split("\t")
        line[2] = line[2].split(";")
        for flybase_id in line[2]:
            if flybase_id != "":
                if line[0] not in uni_flybase:
                    uni_flybase[line[0]] = []
                uni_flybase[line[0]].append(flybase_id)

with open ("Drosophila_melanogaster_FlyAtlas_anatomy.txt", "w") as output:
    for uniprot, flybase_list in uni_flybase.items():
        for flybase in flybase_list:
            url = "http://flybase.org/cgi-bin/serveHTdata.cgi?dataset=FlyAtlas&FBgn=" + flybase
            r = requests.get(url)
            if r.status_code == 200:
                output.write(r.text + "\n")
