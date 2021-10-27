# data.table 
library(data.table)
netflix <- fread("netflix_titles.csv")
netflix[, .(number_of_titles = .N), by =type]
a=45
a
