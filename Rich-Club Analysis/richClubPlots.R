clubs <- read.csv("richClubCoefs.csv")
library(ggplot2)

clubs$lab <- paste("(", clubs$X, ", ", round(clubs$Computer.Science, 2), ")")
comp = ggplot() +
geom_line(data = clubs, aes(x = X, y = Computer.Science), size =1, 
          color="dodgerblue3") +
  geom_point(data = clubs[which.max(clubs$Computer.Science), ], color="deeppink", 
             aes(x = X, y = Computer.Science), size=3, shape=8) +
  geom_text(data = clubs[which.max(clubs$Computer.Science),], 
            aes(X+1, Computer.Science+0.1, label=lab))+
  ggtitle("Computer Science") +
  xlab('Degree') +
  ylab('Rich-Club Coefficient') +
  theme_light() + theme(plot.title = element_text(vjust = -11, hjust=0.07, size=8.5),
                        axis.text=element_text(size=9)) 
comp


phClub = clubs[complete.cases(clubs$Physics.and.Astronomy), ]
phClub$lab <- paste("(", phClub$X, ", ", round(phClub$Physics.and.Astronomy, 2), ")")
physics = ggplot() +
  geom_line(data = phClub, aes(x = X, y = Physics.and.Astronomy), size =1, 
            color="dodgerblue3") +
  geom_point(data = phClub[which.max(phClub$Physics.and.Astronomy), ], color="deeppink", 
             aes(x = X, y = Physics.and.Astronomy), size=3, shape=8) +
  geom_text(data = phClub[which.max(phClub$Physics.and.Astronomy),], 
            aes(X+0.5, Physics.and.Astronomy+0.12, label=lab))+
  ggtitle("Physics and Astronomy") +
  theme_light() + theme(plot.title = element_text(vjust = -11, hjust=0.07, size=8.5)) +
  xlab('Degree') +
  ylab('Rich-Club Coefficient')
physics

agClub = clubs[complete.cases(clubs$Agricultural.and.Biological.Sciences), ]
agClub$lab <- paste("(", agClub$X, ", ", round(agClub$Agricultural.and.Biological.Sciences, 2), ")")
agri = ggplot() +
  geom_line(data = agClub, aes(x = X, y = Agricultural.and.Biological.Sciences), size =1, 
            color="dodgerblue3") +
  geom_point(data = agClub[which.max(agClub$Agricultural.and.Biological.Sciences), ], color="deeppink", 
             aes(x = X, y = Agricultural.and.Biological.Sciences), size=3, shape=8) +
  geom_text(data = agClub[which.max(agClub$Agricultural.and.Biological.Sciences),], 
            aes(X+0.5, Agricultural.and.Biological.Sciences+0.06, label=lab))+
  ggtitle("Agricultural and Biological Sciences") +
  theme_light() + theme(plot.title = element_text(vjust = -11, hjust=0.07, size=8.5)) +
  xlab('Degree') +
  ylab('Rich-Club Coefficient')
agri

bioClub = clubs[complete.cases(clubs$Biochemistry..Genetics.and.Molecular.Biology), ]
bioClub$lab <- paste("(", bioClub$X, ", ", round(bioClub$Biochemistry..Genetics.and.Molecular.Biology, 2), ")")
bio = ggplot() +
  geom_line(data = bioClub, aes(x = X, y = Biochemistry..Genetics.and.Molecular.Biology), size =1, 
            color="dodgerblue3") +
  geom_point(data = bioClub[which.max(bioClub$Biochemistry..Genetics.and.Molecular.Biology), ], color="deeppink", 
             aes(x = X, y = Biochemistry..Genetics.and.Molecular.Biology), size=3, shape=8) +
  geom_text(data = bioClub[which.max(bioClub$Biochemistry..Genetics.and.Molecular.Biology),], 
            aes(X+0.5, Biochemistry..Genetics.and.Molecular.Biology+0.1, label=lab))+
  ggtitle("Biochemistry, Genetics and Molecular Biology") +
  theme_light() + theme(plot.title = element_text(vjust = -11, hjust=0.07, size=8.5)) +
  xlab('Degree') +
  ylab('Rich-Club Coefficient')
bio


require(gridExtra)
grid.arrange(comp, physics, agri, bio, ncol=2)
