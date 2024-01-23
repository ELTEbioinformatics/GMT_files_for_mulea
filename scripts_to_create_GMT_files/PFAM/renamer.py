#Downloaded: 27/10/2016 #From PFAM: ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/proteomes/
import os

keys={'Pfam_Uniprot_Marton_4577.gmt':'Pfam_Uniprot_Marton_Zea_mays.gmt', 
'Pfam_Uniprot_Marton_9606.gmt':'Pfam_Uniprot_Marton_Homo_sapiens.gmt', 
 'Pfam_Uniprot_Marton_9544.gmt':'Pfam_Uniprot_Marton_Macaca_mulatta.gmt', 
 'Pfam_Uniprot_Marton_10090.gmt':'Pfam_Uniprot_Marton_Mus_musculus.gmt', 
'Pfam_Uniprot_Marton_10116.gmt':'Pfam_Uniprot_Marton_Rattus_norvegicus.gmt', 
 'Pfam_Uniprot_Marton_9031.gmt':'Pfam_Uniprot_Marton_Gallus_gallus.gmt', 
 'Pfam_Uniprot_Marton_7955.gmt':'Pfam_Uniprot_Marton_Danio_rerio.gmt', 
'Pfam_Uniprot_Marton_7227.gmt':'Pfam_Uniprot_Marton_Drosophila_melanogaster.gmt', 
 'Pfam_Uniprot_Marton_7240.gmt':'Pfam_Uniprot_Marton_Drosophila_simulans.gmt', 
 'Pfam_Uniprot_Marton_6239.gmt':'Pfam_Uniprot_Marton_Caenorhabditis_elegans.gmt', 
 'Pfam_Uniprot_Marton_3702.gmt':'Pfam_Uniprot_Marton_Arabidopsis_thaliana.gmt', 
 'Pfam_Uniprot_Marton_4577.gmt':'Pfam_Uniprot_Marton_Zea_mays.gmt', 
  'Pfam_Uniprot_Marton_559292.gmt':'Pfam_Uniprot_Marton_Saccharomyces_cerevisiae.gmt', 
 'Pfam_Uniprot_Marton_284812.gmt':'Pfam_Uniprot_Marton_Saccharomyces_pombe.gmt', 
 'Pfam_Uniprot_Marton_367110.gmt':'Pfam_Uniprot_Marton_Neurospora_crassa.gmt', 
 'Pfam_Uniprot_Marton_44689.gmt':'Pfam_Uniprot_Marton_Dictyostelium_discoideum.gmt', 
 'Pfam_Uniprot_Marton_83333.gmt':'Pfam_Uniprot_Marton_Escherichia_coli.gmt', 
 'Pfam_Uniprot_Marton_312017.gmt':'Pfam_Uniprot_Marton_Tetrahymena_thermophila.gmt', 
 'Pfam_Uniprot_Marton_224308.gmt':'Pfam_Uniprot_Marton_Bacillus_subtilis.gmt', 
 'Pfam_Uniprot_Marton_83332.gmt':'Pfam_Uniprot_Marton_Mycobacterium_tubercolosis.gmt', 
 'Pfam_Uniprot_Marton_99287.gmt':'Pfam_Uniprot_Marton_Salmonella_typhimurium_LT2.gmt', 
 'Pfam_Uniprot_Marton_1262734.gmt':'Pfam_Uniprot_Marton_Bacteroides_sp_CAG_1060.gmt', 
 'Pfam_Uniprot_Marton_484020.gmt':'Pfam_Uniprot_Marton_Bifidobacterium_bifidum.gmt'}
#replace Uniprot with Uniprot and Uniprot

for k in keys:
	os.rename(k, 
 keys[k])