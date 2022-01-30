# Cleaning the work space #
cat("\f")       # Clear old outputs
rm(list=ls())   # Clear all variables

if(!require("Spectrum")) install.packages("Spectrum")
library("Spectrum")

data <- file.choose()
df <- read.csv(data, header = TRUE, sep = ",")

## Transforming variables ##
df$age <- as.numeric(df$age)
df$anaemia <- as.factor(df$anaemia)
df$creatinine_phosphokinase <- as.numeric(df$creatinine_phosphokinase)
df$diabetes <- as.factor(df$diabetes)
df$ejection_fraction <- as.numeric(df$ejection_fraction)
df$high_blood_pressure <- as.factor(df$high_blood_pressure)
df$platelets <- as.numeric(df$platelets)
df$serum_creatinine <- as.numeric(df$serum_creatinine)
df$serum_sodium <- as.numeric(df$serum_sodium)
df$sex <- as.factor(df$sex)
df$smoking <- as.factor(df$smoking)
df$time <- as.numeric(df$time)
df$DEATH_EVENT <- as.factor(df$DEATH_EVENT)

kmeans_df <- kmeans(df)
plot(kmeans_df)