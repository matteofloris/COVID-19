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

### calculate new daily deaths 
df <- data.frame()
for (region in dat$denominazione_regione)
{
s <- subset(dat, dat$denominazione_regione %in% c(region))
s$diff_decessi <- c(0, diff(s$deceduti, lag = 1, differences = 1))
df <- rbind(df, s)
}

ggplot(df, aes(x = as.factor(df$data), y = df$diff_decessi)) + geom_point() + facet_wrap( ~ df$denominazione_regione)+ theme(legend.position = "none")+theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())




