library(lubridate)
library(ggplot2)
setwd('~/Documents/GitHub/DataAnalystNanodegree/R_test/')
df = read.csv('birthdaysExample.csv')
df$month = c(apply(df[1], 2, function(x) month(mdy(x))))
df$day = c(apply(df[1], 2, function(x) day(mdy(x))))

q = qplot(data = df, x = month)
print(q)

q = qplot(data = df, x = day)
print(q)
