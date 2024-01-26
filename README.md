
<!-- README.md is generated from README.Rmd. Please edit that file -->

# GMT files for mulea

<!-- badges: start -->

[![GitHub
issues](https://img.shields.io/github/issues/ELTEbioinformatics/muleaData)](https://github.com/ELTEbioinformatics/muleaData/issues)
[![GitHub
pulls](https://img.shields.io/github/issues-pr/ELTEbioinformatics/muleaData)](https://github.com/ELTEbioinformatics/muleaData/pulls)

<!-- badges: end -->

Here we provides ontologies (gene and protein sets) in a standardised
*GMT* (Gene Matrix Transposed) format that can be read to the
[`mulea`](https://github.com/ELTEbioinformatics/mulea) R packace to
calculate comprehensive overrepresentation and functional enrichment
analyses. We provide these *GMT* files for 27 different model organisms,
ranging from *Escherichia coli* to human, all acquired from publicly
available data sources. The *GMT* files are provided with multiple gene
and protein identifiers such as *UniProt* protein IDs, *Entrez*, *Gene
Symbol*, and *Ensembl* gene IDs. The GMT files are provided in the
[GMT_files](https://github.com/ELTEbioinformatics/GMT_files_for_mulea/tree/main/GMT_files)
folder and the scripts we applied to create them are available in the
[scripts_to_create_GMT_files](https://github.com/ELTEbioinformatics/GMT_files_for_mulea/tree/main/scripts_to_create_GMT_files)
folder. Also there is a script for mapping between different ID types at
[scripts_to_create_GMT_files/ID_mapping_scripts](https://github.com/ELTEbioinformatics/GMT_files_for_mulea/tree/main/scripts_to_create_GMT_files/ID_mapping_scripts)
folder.

The GMT files can be downloaded and read with the `mulea::read_gmt()`
function. *i.e.*

``` r
mulea::read_gmt(file = "Transcription_factor_TFLink_Drosophila_melanogaster_LS_GeneSymbol.gmt")
```

Or can be loaded directly from this github repository. *i.e.*

``` r
mulea::read_gmt(file = "https://raw.githubusercontent.com/ELTEbioinformatics/GMT_files_for_mulea/main/GMT_files/Drosophila_melanogaster_7227/Transcription_factor_TFLink_Drosophila_melanogaster_LS_GeneSymbol.gmt")
```

Besides, we also created the
[`muleaData`](https://github.com/ELTEbioinformatics/muleaData)
ExperimentHubData Bioconductor package to ease browsing and readeing the
ontologies.

List of species we cover:

- *Arabidopsis thaliana*
- *Bacillus subtilis*
- *Bacteroides thetaiotaomicron VPI-5482*
- *Bifidobacterium longum*
- *Bos taurus*
- *Caenorhabditis elegans*
- *Chlamydomonas reinhardtii*
- *Danio rerio*
- *Daphnia pulex*
- *Dictyostelium discoideum*
- *Drosophila melanogaster*
- *Drosophila simulans*
- *Escherichia coli*
- *Gallus gallus*
- *Homo sapiens*
- *Macaca mulatta*
- *Mus musculus*
- *Mycobacterium tubercolosis*
- *Neurospora crassa*
- *Pan troglodytes*
- *Rattus norvegicus*
- *Saccharomyces cerevisiae*
- *Salmonella enterica subsp. enterica serovar Typhimurium str. LT2*
- *Schizosaccharomyces pombe*
- *Tetrahymena thermophila*
- *Xenopus tropicalis*
- *Zea mays*

Type, name, link and citation of the databases we cover:

|                                     |                                                                                        |                                                                                                                                                                    |                                                                                                                                                                                                |
|-------------------------------------|:--------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| **Ontology category**               |                                   **Ontology name**                                    |                                                                  **Short description of content**                                                                  |                                                                                         **Reference**                                                                                          |
| **Gene expression**                 |                          [FlyAtlas](http://www.flyatlas.org/)                          |                                                   Tissue specific expression data for *Drosophila melanogaster*.                                                   |                      Chintapalli,V.R. *et al.* (2007) Using FlyAtlas to identify better *Drosophila melanogaster* models of human disease. *Nat Genet*, **39**, 715–720.                       |
|                                     |                        [ModEncode](http://data.modencode.org/)                         | Functional characterization (cell line, temporal expression, tissue expression, treatment) of elements for *Caenorhabditis elegans* and *Drosophila melanogaster*. |                The Modencode Consortium *et al.* (2010) Identification of functional elements and regulatory circuits by *Drosophila* modENCODE. *Science*, **330**, 1787–1797.                |
| **Genomic location**                |                                   Chromosomal Bands                                    |                                                                Location of genes on the chromosome.                                                                |                                                       Martin,F.J. *et al.* (2023) Ensembl 2023. *Nucleic Acids Res,* **51**, D933–D941.                                                        |
|                                     |                                   Consecutive genes                                    |                                                              *n* consecutive genes on the chromosome.                                                              |                                                                                                                                                                                                |
| **miRNA regulation**                | [miRTarBase](https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2022/php/index.php) |                                                       Experimentally validated miRNA - target interactions.                                                        |            Huang,H.-Y. et al. (2022) miRTarBase update 2022: an informative resource for experimentally validated miRNA–target interactions. Nucleic Acids Res, **50**, D222–D230.             |
| **Gene Ontology**                   |                            [GO](https://geneontology.org/)                             |                                            Gene Ontology (GO) categorizes genes into unified categories and attributes.                                            |                                      The Gene Ontology Consortium *et al.* (2023) The Gene Ontology knowledgebase in 2023. *Genetics*, **224**, iyad031.                                       |
| **Pathway**                         |                   [Pathway Commons](https://www.pathwaycommons.org/)                   |                                                       Collection of biological pathway and interaction data.                                                       |                    Rodchenkov,I. et al. (2020) Pathway Commons 2019 Update: integration, analysis and exploration of pathway data. *Nucleic Acids Res*, **48**, D489–D497.                     |
|                                     |                           [Reactome](https://reactome.org/)                            |                                                       Collection of biological pathway and interaction data.                                                       |                                             Jassal,B. *et al.* (2020) The reactome pathway knowledgebase. *Nucleic Acids Res*, **48**, D498–D503.                                              |
|                                     |                           [Signalink](http://signalink.org/)                           |                                              Interaction database focussing on pathways and interactions of pathways.                                              |                     Csabai,L. *et al.* (2022) SignaLink3: a multi-layered resource to uncover tissue-specific signaling networks. *Nucleic Acids Res*, **50**, D701–D709.                      |
|                                     |                     [Wikipathways](https://www.wikipathways.org/)                      |                                                       Collection of biological pathway and interaction data.                                                       |                                            Martens,M. *et al.* (2021) WikiPathways: connecting communities. *Nucleic Acids Res*, **49**, D613–D621.                                            |
| **Protein domain**                  |                             [PFAM](http://pfam.xfam.org/)                              |                                                                 Protein domain structure database.                                                                 |                                         Mistry,J. *et al.* (2021) Pfam: The protein families database in 2021. *Nucleic Acids Res*, **49**, D412–D419.                                         |
| **Transcription factor regulation** |                            [ATRM](http://atrm.gao-lab.org/)                            |                                             Transcription factor - target gene interactions for Arabidopsis thaliana.                                              | Jin,J. et al. (2015) An *Arabidopsis* transcriptional regulatory map reveals distinct functional and evolutionary features of novel transcription factors. *Mol Biol Evol*, **32**, 1767–1773. |
|                                     |                    [dorothEA](https://saezlab.github.io/dorothea/)                     |                                                Transcription factor - target gene interactions for human and mouse.                                                |             Garcia-Alonso,L. *et al.* (2019) Benchmark and integration of resources for the estimation of human transcription factor activities. *Genome Res*, **29**, 1363–1375.              |
|                                     |                      [RegulonDB](https://regulondb.ccg.unam.mx/)                       |                                          Transcription factor - target gene interactions for *Escherichia coli* bacteria.                                          |        Tierrafría,V.H. *et al.* (2022) RegulonDB 11.0: Comprehensive high-throughput datasets on transcriptional regulation in *Escherichia coli* K-12. *Microb Genom*, **8**, 000833.         |
|                                     |                             [TFLink](https://tflink.net/)                              |                              Small- and lagre-scale transcription factor - target gene interactions for human and 6 model organisms.                               |              Liska,O. *et al.* (2022) TFLink: an integrated gateway to access transcription factor–target gene interactions for multiple species. *Database*, **2022**, baac083.               |
|                                     |                       [TRRUST](https://www.grnpedia.org/trrust/)                       |                                                     Transcription factor - target gene interactions for human.                                                     |              Han,H. *et al.* (2018) TRRUST v2: an expanded reference database of human and mouse transcriptional regulatory interactions. *Nucleic Acids Res*, **46**, D380–D386.              |
|                                     |                         [Yeastract](http://www.yeastract.com/)                         |                                          Transcription factor - target gene interactions for *Saccharomyces cerevisiae*.                                           |    Teixeira,M.C. *et al.* (2018) YEASTRACT: an upgraded database for the analysis of transcription regulatory networks in Saccharomyces cerevisiae. *Nucleic Acids Res*, **46**, D348–D353.    |

## Citation

To cite the GMT files in publications use:

Ari E, Ölbei M, Gul L, Bohár B (2024). muleaData: ExperimentalData
Bioconductor Package for the mulea R Package, Contains Genes Sets for
Functional Enrichment Analysis in GMT File Format. R package version
0.99.0, <https://github.com/ELTEbioinformatics/muleaData>.
