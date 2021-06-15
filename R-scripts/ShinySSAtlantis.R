setwd("/ocean/rlovindeer/Atlantis/salish-sea-atlantis-model")

library("shiny")
library("dplyr")
library("DT")
library("ggplot2")
library("ncdf4")
library("stringr")

library(shinyrAtlantis)
bgm.file    <- 'SS_ll.bgm'
obj <- make.sh.dist.object(bgm.file)
sh.dist(obj)

grp.file <- 'SS_grps.csv'
prm.file <- '02SS_biology.prm'
obj <- make.sh.prm.object(bgm.file, grp.file, prm.file)
sh.prm(obj)

nc.file <- 'SS_init.nc'
obj <- make.sh.init.object(bgm.file, nc.file)
sh.init(obj)

## ---------------------------- ##
## ~      Hydrodynamics       ~ ##
## ---------------------------- ##
library("shiny")
library("dplyr")
library("DT")
library("ggplot2")
library("ncdf4")
library("stringr")
library("shinyrAtlantis")
exchange.file <- 'inputs/SS_hydro.nc' # what is the structure of this file to be able to be displayed here?
salinity.file <- 'inputs/SS_salt.nc'
temperature.file <- 'inputs/SS_temp.nc'
bgm.file <- 'SS_ll.bgm'
cum.depth <- c(0, 25, 50, 100, 250, 400, 700)

input.object <- make.sh.forcings.object(
  bgm.file = bgm.file,
  exchange.file = exchange.file,
  cum.depth = cum.depth,
  temperature.file = temperature.file,
  salinity.file = salinity.file
)
sh.forcings(input.object)
