# Cleaning the work space #
cat("\f")       # Clear old outputs
rm(list=ls())   # Clear all variables

if(!require("Spectrum")) install.packages("Spectrum")
if(!require("factoextra")) install.packages("factoextra")
library("Spectrum")
library("factoextra")

data <- file.choose()
df <- read.csv(data, header = TRUE, sep = ",")


for (i in 1:ncol(df)) {
  if(length(unique(df[,i])) < 5) {
    df[,i] = as.factor(as.character(df[,i]))
  }
  else if(length(unique(df[,i])) > 10) {
    df[,i] = as.numeric(df[,i])
  }
}

str(df)

# K-means
df_k <- df[,c(1,3,5,7,8,9,12)]
kmeans_df <- kmeans(df_k, 2)
fviz_cluster(kmeans_df, data = df_k, geom = "text", ellipse.type = "norm", palette = "jco", ggtheme = theme_minimal())

# Dbscan
dbscan_df <- dbscan::dbscan(df_k, eps = 0.7, minPts = 5)
fviz_cluster(dbscan_df, df_k, stand = FALSE, ellipse = TRUE, geom = "point")




