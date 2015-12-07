setwd('~/Documents/GitHub/DataAnalystNanodegree/R_test/EDA_Course_Materials/lesson3')

df <- read.delim('pseudo_facebook.tsv')
summary(df)

plot = qplot(data = df, x = dob_day) +
  scale_x_discrete(breaks=1:31) +
  facet_grid(gender ~ dob_month)
  #facet_wrap(~dob_month, ncol=3)

print(plot)