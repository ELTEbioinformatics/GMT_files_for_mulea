read.table("Bands_Homo_sapiens_Ensembl_Marton", sep="\t", header = FALSE)
read.table("Bands_Mus_musculus_Ensembl_Marton", sep="\t", header = FALSE)
read.table("Bands_Rattus_norvegicus_Ensembl_Marton", sep="\t", header = FALSE)
read.table("Bands_Drosophila_melanogaster_Ensembl_Marton", sep="\t", header = FALSE)

Hs<-aggregate(Bands_Homo_sapiens_Ensembl_Marton$V2, by=list(Bands_Homo_sapiens_Ensembl_Marton$V1), paste, collapse="\t")
Mm<-aggregate(Bands_Mus_musculus_Ensembl_Marton$V2, by=list(Bands_Homo_sapiens_Ensembl_Marton$V1), paste, collapse="\t")
Rn<-aggregate(Bands_Rattus_norvegicus_Ensembl_Marton$V2, by=list(Bands_Homo_sapiens_Ensembl_Marton$V1), paste, collapse="\t")
Dm<-aggregate(Bands_Drosophila_melanogaster_Ensembl_Marton$V2, by=list(Bands_Homo_sapiens_Ensembl_Marton$V1), paste, collapse="\t")

    
write.table(Hs, "Bands_Homo_sapiens_Ensembl_Marton.gmt", sep="\t", row.names = FALSE, col.names = FALSE, quote = FALSE)
write.table(Mm, "Bands_Mus_musculus_Ensembl_Marton.gmt", sep="\t", row.names = FALSE, col.names = FALSE, quote = FALSE)
write.table(Rn, "Bands_Rattus_norvegicus_Ensembl_Marton.gmt", sep="\t", row.names = FALSE, col.names = FALSE, quote = FALSE)
write.table(Dm, "Bands_Drosophila_melanogaster_Ensembl_Marton.gmt", sep="\t", row.names = FALSE, col.names = FALSE, quote = FALSE)
