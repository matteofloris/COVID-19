### this script creates a "facet" view of per-region data

library(ggplot2)

setwd("/Users/matteofloris/Downloads/COVID-19-master/dati-regioni")

dat <- data.frame()
files <- list.files(pattern = "dpc-covid19-ita-regioni-")
for(file in files) { 
  print (file)
  pre <- read.table(file, sep=",", header=T, dec=".")
  pre <- pre[complete.cases(pre), ]
  dat <- rbind(dat, pre)
  #dat <- cbind(dat, pre) 
} 

ggplot(dat, aes(x = as.factor(dat$data), y = dat$nuovi_attualmente_positivi)) + geom_point() + facet_wrap( ~ dat$denominazione_regione)+ theme(legend.position = "none")+theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())


