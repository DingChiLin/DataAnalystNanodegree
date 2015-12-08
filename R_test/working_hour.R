setwd('~/Documents/GitHub/DataAnalystNanodegree/R_test/')
library(readxl)
df <- read_excel("indicator_hours_per_week.xlsx")
country <- c()
year <- c()
working_hour <- c()

titles = names(df)
for(i in 1:nrow(df)){
  for(j in 2:ncol(df)){
    if(!is.na(df[i,j])){
      print(df[i,1])
      country <- c(country, df[i,1])
      print(titles[j])
      year <- c(year, titles[j])
      print(df[i,j])
      working_hour <- c(working_hour, df[i,j])
    }
  }
}

tidy_df = data.frame(country, year, working_hour) 

q = qplot(data = tidy_df, x = working_hour)
print(q)

q = qplot(data = tidy_df, x = year, y=working_hour, geom='boxplot')
print(q)

q = qplot(data = tidy_df, x = working_hour)+ facet_wrap(~country, scales="free")
print(q)

