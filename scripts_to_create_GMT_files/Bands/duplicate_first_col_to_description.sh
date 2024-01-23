sed -i 's/_/ /g' Bands_Drosophila_melanogaster_Flybase_Marton.gmt 



sed -r 's/^(\S+)\t/\1\t\1\t/g' Bands_Drosophila_melanogaster_Flybase_Marton.gmt 

