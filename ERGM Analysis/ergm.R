install.packages("igraph")
install.packages("ergm")
install.packages("intergraph")

library(igraph)
library(magrittr)
library(dplyr)
library(ergm)
library(intergraph)

graph <- read.graph("full.graphml", format = "graphml")

ergmNetwork <- intergraph::asNetwork(graph)

ergmNetwork

fit <- ergm(ergmNetwork ~ edges + nodematch("Field.of.Interest") + nodematch('Country') + 
	nodematch('Institute ID') + nodematch('Gender') + nodecov('Citation.Count') + nodecov('h.index'))

summary(fit)
