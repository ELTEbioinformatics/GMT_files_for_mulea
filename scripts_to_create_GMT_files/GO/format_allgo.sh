#!/bin/sh

awk 'NR>1' allGO_offsp.txt | sort | perl -pe 's/NA//g' | perl -pe 's/ \n/\n/g' | awk -F"\t" '{print $1"\t"$1" "$2}' | perl -pe 's/  / /g' | perl -pe 's/  / /g' | perl -pe 's/         /       /g'> allGO_offsp_formatted.txt