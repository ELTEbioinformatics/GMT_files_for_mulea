#Downloaded: 27/10/2016 #From PFAM: ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/proteomes/
import urllib.request
import gzip
import glob
import os

PfamList = [9606, 9598, 9544, 10090, 10116, 9031, 8364, 7955, 7227, 7240, 6239, 3702, 4577, 559292, 284812, 367110, 44689, 3055, 312017, 83333, 224308, 83332, 99287, 1262734, 484020]

"""
def get_uniprot_data(pfamID):
    urllib.request.urlretrieve('http://www.uniprot.org/uniprot/?sort=score&desc=&compress=no&query=organism:%s&fil=&force=no&preview=true&format=tab&columns=id,database(Pfam)' % pfamID)

for i in PfamList:
    get_uniprot_data(i)

def get_pfam_data(pfamID):
    urllib.request.urlretrieve('ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/proteomes/%s.tsv.gz' % pfamID, '%s_pfam.tsv.gz' % pfamID)

for i in PfamList:
    get_pfam_data(i)

for gzips in PfamList:
    inF = gzip.open('%s_pfam.tsv.gz' % gzips, 'rb')
    outF = open('%s_pfam.tsv' % gzips, 'wb')
    outF.write( inF.read() )
    inF.close()
    outF.close()
"""
def pfamconv(taxid):
    results = {}
    pfam_defs = {}

    with open('%s_pfam.tsv' % taxid, 'r') as metadata_file:
        for rows in metadata_file:
            if rows[0] == "#":
                continue
            cells = rows.strip().split('\t') #definitions are in the 6th col
            if cells[5] not in pfam_defs:
                pfam_defs[cells[5]] = cells[6]

    with open('%s.tsv' % taxid) as input_file:
        for line in input_file:
            cols = line.strip().split('\t')
            try:
                pfams = [i for i in cols[1].split(';') if i != '']
            except IndexError:
                continue
        
            for pfam in pfams:
                if pfam not in results:
                    results[pfam] = set()
                results[pfam].add(cols[0])

    with open('Pfam_Uniprot_Marton_%s.gmt' % taxid, 'w') as file:
        for pf in results:
            try:
                file.write('%s\t%s\t%s\n' % (pf, pfam_defs[pf], '\t'.join(list(set(list(results[pf]))))))
            except KeyError:
                continue


for i in PfamList:
	pfamconv(i)