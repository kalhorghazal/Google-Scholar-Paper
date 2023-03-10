install.packages("scatterplot3d")
install.packages("ggExtra")
install.packages("GGally")
install.packages("ggcorrplot")
install.packages("ggplot2")

library(scatterplot3d)
library(ggExtra)
library(GGally)
library(ggcorrplot)
library(ggplot2)

myData <- read.csv("communities_data.csv")

options(rper.plot.width=200, rper.plot.height=200)

myData <- myData[(myData$community_size !=1), ]
myData <- myData[complete.cases(myData), ]

myData$log_mean_h_index = log(myData$Mean.h.index+1, 10)

myData$log_mean_citation = log(myData$Mean.Citation.Count+1, 10)

myData$log_size = log(myData$Community.Size+1, 10)

numericVars <- myData[c("log_size", "log_mean_citation", "log_mean_h_index")]
corr <- cor(numericVars)
p.mat <- cor_pmat(numericVars)

colnames(numericVars) <- make.names(c("Log (Community Size)", "Log (Mean Citation Count)", 
                                      "Log (Mean h-index)"))

ggpairs(numericVars,
        columnLabels = gsub('.', ' ', colnames(numericVars), fixed = T), 
        lower = list(continuous = wrap("smooth", colour= "seagreen3")),
        diag = list(continuous = wrap("barDiag", fill= "plum2", colour="purple")),
        upper = list(corSize=6), axisLabels = "show")
