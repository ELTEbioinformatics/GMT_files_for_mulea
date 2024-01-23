#!/bin/sh

#get the newest version manually, it gets updated almost daily
wget "http://pathvisio.org/data/bots/gmt/wikipathways.gmt"

#list of species (the ones that aren't interesting in terms of MulEA are in brackets): 
#Pan troglodytes, Homo sapiens, Danio rerio, Caenorhabditis elegans, (Populus trichocarpa), Rattus norvegicus, Mus musculus
#Drosophila melanogaster, Gallus gallus, (Equus caballus), Arabidopsis thaliana, (Anopheles gambiae), Oryza sativa, (Sus scrofa)
#Bos taurus, Saccharomyces cerevisiae, (Canis familiaris)

declare -a SpeciesList=("Pan troglodytes" "Homo sapiens" "Danio rerio" "Caenorhabditis elegans" "Rattus norvegicus" "Mus musculus" "Drosophila melanogaster" "Gallus gallus" "Arabidopsis thaliana" "Oryza sativa" "Bos taurus" "Saccharomyces cerevisiae")

#separate species from the whole database

for i in "${SpeciesList[@]}"
do
	grep -i "$i" wikipathways.gmt > "wikipathways_${i}_Marton.gmt"
done