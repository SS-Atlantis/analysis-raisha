## Feeding

setwd("/ocean/rlovindeer/Atlantis/salish-sea-atlantis-model")

library(ReactiveAtlantis)
prm.file <- '/ocean/rlovindeer/Atlantis/salish-sea-atlantis-model/02SS_Biology.prm'
grp.file <- 'SS_grps.csv'
nc.file <- 'SS_init.nc'
bgm.file <- 'SS_ll.bgm'
cum.depths <- c(0, 25, 50, 100, 250, 400, 700)
feeding.mat(prm.file, grp.file, nc.file, bgm.file, cum.depths)

## Comparison with previous run

setwd("/ocean/rlovindeer/MOAD/analysis-raisha/SSmodel_outputs")

nc.out.current <- 'output-25yr/outputSalishSea.nc'
nc.out.previous <- 'output-20yr/outputSalishSea.nc'
groups.csv <- '/ocean/rlovindeer/Atlantis/salish-sea-atlantis-model/SS_grps.csv'
bgm.file <- '/ocean/rlovindeer/Atlantis/salish-sea-atlantis-model/SS_xy.bgm'
cum.depths <- c(0, 25, 50, 100, 250, 400, 700)
compare(nc.out.current, nc.out.old = nc.out.previous, grp.csv = groups.csv, bgm.file=bgm.file, cum.depths=cum.depths)

nc.initial <- '/ocean/rlovindeer/Atlantis/salish-sea-atlantis-model/SS_init.nc'
nc.current <- 'output-20yr/outputSalishSea.nc'
grp.csv <- '/ocean/rlovindeer/Atlantis/salish-sea-atlantis-model/SS_grps.csv'
prm.file <- '/ocean/rlovindeer/Atlantis/salish-sea-atlantis-model/02SS_Biology.prm'
growth.pp(nc.initial, grp.csv, prm.file, nc.current)

grp.csv <- '/ocean/rlovindeer/Atlantis/salish-sea-atlantis-model/SS_grps.csv'
prm.file <- '/ocean/rlovindeer/Atlantis/salish-sea-atlantis-model/02SS_Biology.prm'
diet.file <- 'output-20yr/outputSalishSeaDietCheck.txt'
food.web(diet.file, grp.csv)
food.web(diet.file, grp.file, diet.file.bypol)

biom        <- 'output-20yr/outputSalishSeaBiomIndx.txt'
diet.file   <- 'output-20yr/outputSalishSeaDietCheck.txt'
bio.age     <- 'output-20yr/outputSalishSeaAgeBiomIndx.txt' ## optional file. just if you want to check the predation by age
grp.csv     <- '/ocean/rlovindeer/Atlantis/salish-sea-atlantis-model/SS_grps.csv'
## Predation by Age
predation(biom, grp.csv, diet.file, bio.age)
## No predation by Age
predation(biom, grp.csv, diet.file, bio.age = NULL)
