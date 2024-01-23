## installation
## try http:// if https:// URLs are not supported
## source("https://bioconductor.org/biocLite.R")
## biocLite("GO.db")

library("GO.db")
#get the offspings of each GO id with GO.db r package
#Molecular function (MF)
#Biological process (BP)
#Cellular component (CC)

GO_dbInfo()
#               name                                                             value
# 1     GOSOURCENAME                                                     Gene Ontology
# 2      GOSOURCEURL ftp://ftp.geneontology.org/pub/go/godatabase/archive/latest-lite/
# 3     GOSOURCEDATE                                                        2015.09.19
# 4          Db type                                                              GODb
# 5          package                                                     AnnotationDbi
# 6         DBSCHEMA                                                             GO_DB
# 7   GOEGSOURCEDATE                                                        2015-Sep27
# 8   GOEGSOURCENAME                                                       Entrez Gene
# 9    GOEGSOURCEURL                              ftp://ftp.ncbi.nlm.nih.gov/gene/DATA
# 10 DBSCHEMAVERSION                                                               2.1

#all offsprings according to MF
offsp_MF=as.list(GOMFOFFSPRING)

#all offsprings according to BP
offsp_BP=as.list(GOBPOFFSPRING)

#all offsprings according to CC
offsp_CC=as.list(GOCCOFFSPRING)

#lengths
length(offsp_MF)
#[1] 9955
length(offsp_BP)
#[1] 28007
length(offsp_CC)
#[1] 3827

#creating a single list
allGO_offsp=c(offsp_MF, offsp_BP, offsp_CC)

#function to write a list to a file
fnlist=function(x, fil){
  z=deparse(substitute(x))
  cat(z, "\n", file=fil)
  nams=names(x)
  for (i in seq_along(x)){
    cat(nams[i], "\t", x[[i]], "\n", file=fil, append=T)
  }
}
fnlist(allGO_offsp, "allGO_offsp.txt")