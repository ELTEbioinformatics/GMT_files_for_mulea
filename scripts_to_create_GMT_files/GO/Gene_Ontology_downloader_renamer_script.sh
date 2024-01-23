#get all databases for all species from GO site
#unify names

#Dyctiostelium discoideum
wget http://current.geneontology.org/annotations/dictybase.gaf.gz

gunzip dictybase.gaf.gz
mv dictybase.gaf gene_association.dictyBase

#Escherichia coli
wget http://current.geneontology.org/annotations/ecocyc.gaf.gz

gunzip ecocyc.gaf.gz
mv ecocyc.gaf gene_association.ecocyc

#Drosophila melanogaster
wget http://current.geneontology.org/annotations/fb.gaf.gz

gunzip fb.gaf.gz
mv fb.gaf gene_association.fb

#Gallus gallus
wget http://geneontology.org/gene-associations/goa_chicken.gaf.gz

gunzip goa_chicken.gaf.gz

mv goa_chicken.gaf gene_association.chicken

#Bos taurus
wget http://geneontology.org/gene-associations/goa_cow.gaf.gz

gunzip goa_cow.gaf.gz

mv goa_cow.gaf gene_association.cow

#Homo sapiens
wget http://geneontology.org/gene-associations/goa_human.gaf.gz

gunzip goa_human.gaf

mv goa_human.gaf gene_association.human

#Oryza sativa
wget http://geneontology.org/gene-associations/gene_association.gramene_oryza.gz

gunzip gene_association.gramene_oryza.gz

#Mus musculus
wget http://current.geneontology.org/annotations/mgi.gaf.gz
gunzip mgi.gaf.gz
mv mgi.gaf gene_association.mgi

#Schizosaccharomyces pombe
wget http://current.geneontology.org/annotations/pombase.gaf.gz
gunzip pombase.gaf.gz
mv pombase.gaf gene_association.pombase

#Saccharomyces cerevisiae
wget http://current.geneontology.org/annotations/sgd.gaf.gz
gunzip sgd.gaf.gz
mv sgd.gaf gene_association.sgd

#Rattus norvegicus
wget http://current.geneontology.org/annotations/rgd.gaf.gz
gunzip rgd.gaf.gz
mv rgd.gaf gene_association.rgd

#Arabidopsis thaliana
wget http://current.geneontology.org/annotations/tair.gaf.gz
gunzip tair.gaf.gz
mv tair.gaf gene_association.tair

#Caenorhabditis elegans
wget http://current.geneontology.org/annotations/wb.gaf.gz
gunzip wb.gaf.gz
mv wb.gaf gene_association.wb

#Danio rerio
wget http://current.geneontology.org/annotations/zfin.gaf.gz
gunzip zfin.gaf.gz
mv zfin.gaf gene_association.zfin
