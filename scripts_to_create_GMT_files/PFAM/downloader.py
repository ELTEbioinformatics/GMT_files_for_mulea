#Downloaded: 27/10/2016 #From PFAM: ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/proteomes/
import urllib.request
import gzip
import glob
import os

PfamList = [9606, 9598, 9544, 10090, 10116, 9031, 8364, 7955, 7227, 7240, 6239, 3702, 4577, 559292, 284812, 367110, 44689, 3055, 312017, 83333, 224308, 83332, 99287, 1262734, 484020]

def get_uniprot_data(pfamID):
    urllib.request.urlretrieve('http://www.uniprot.org/uniprot/?sort=score&desc=&compress=no&query=organism:%s&fil=&force=no&preview=true&format=tab&columns=id,database(Pfam)' % pfamID, '%s.tsv' % pfamID)


#http://www.uniprot.org/uniprot/?sort=score&desc=&compress=no&query=organism:9606&fil=&force=no&preview=true&format=tab&columns=id,database(Pfam)


for i in PfamList:
    get_uniprot_data(i)


#def get_pfam_data(pfamID):
#    urllib.request.urlretrieve('ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/proteomes/%s.tsv.gz' % pfamID, '%s_pfam.tsv.gz' % pfamID)

#for i in PfamList:
#    get_pfam_data(i)

