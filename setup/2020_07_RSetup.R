# Setup R for DS Specialization - my customizations

## Customizing RMD outputs
install.packages("rmdformats")
library("rmdformats")

## Starting python to allow python chunks in RMD
library(reticulate)
use_python("C:/Users/PICHAU/anaconda3/python.exe")
