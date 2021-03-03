library(readr)
library(ggmap)
Manhattan_Coordinates <- read_csv("Manhattan_Coordinates.csv")
low_estimates_db <- read_csv("low_estimates_db.csv")
setwd('imgs')


for(row in 2:nrow(low_estimates_db)) {
  c = toString(low_estimates_db[row,][[1]])
  Manhattan_Coordinates[c] = t(low_estimates_db[row,][-1])
  png(paste(gsub(":", "_", c), ".png", sep=""))
  
  print(qmplot(Longitude, Latitude, data=Manhattan_Coordinates, maptype = "toner-lite", col=Manhattan_Coordinates[c], main=c) + scale_colour_gradient2( low="cyan", mid="purple", high="red2", midpoint=11, limits=c(7,16)))
  dev.off()
}

