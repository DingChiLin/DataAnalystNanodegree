setwd('~/Documents/GitHub/DataAnalystNanodegree/R_test/EDA_Course_Materials/lesson2')

df <- read.csv('reddit.csv')
l <- levels(df$age.range)
print(l)
t <- table(df$age.range)
print(t)

library(ggplot2)
plot = qplot(data = df, x = age.range)
print(plot)

df$age.range <- ordered(df$age.range, levels=c('Under 18', '18-24', '25-34', '35-44', '45-54', '55-64', '65 or Above'))
plot2 = qplot(data = df, x = age.range)
print(plot2)
