library(ggplot2)
data(diamonds)
#print(qplot(data=diamonds, x=price, breaks=seq(0,2000,20), color=cut))

#----------------#
# Problem Set 3
#----------------#

library(gridExtra)
#q1 = qplot(data=subset(diamonds, cut=='Fair'), x=price)
#q2 = qplot(data=subset(diamonds, cut=='Good'), x=price)
#q3 = qplot(data=subset(diamonds, cut=='Very Good'), x=price)
#q4 = qplot(data=subset(diamonds, cut=='Premium'), x=price)
#q5 = qplot(data=subset(diamonds, cut=='Ideal'), x=price)
#print(grid.arrange(q1, q2, q3, q4, q5, ncol = 2))

#print(by(diamonds$price, diamonds$cut, summary))
#print(by(diamonds$price, diamonds$cut, max))

#q = qplot(x = price, data = diamonds) + facet_wrap(~cut, scales="free")
#print(q)

#q = qplot(x = log10(price/carat+1), data = diamonds) + facet_wrap(~cut, scales="free")
#print(q)

#q = qplot(x = color, y = price, data = diamonds, geom='boxplot') + coord_cartesian(ylim=c(0,9000))
#print(q)

#q = qplot(x = color, y = price/carat, data = diamonds, geom='boxplot') + coord_cartesian(ylim=c(1000,6000))
#print(q)

# = qplot(x = carat, data = diamonds, geom='freqpoly', breaks=seq(1.5,5.5,0.1))
#print(q)

#----------------#
# Problem Set 4
#----------------#

#p = ggplot(data = diamonds, aes(x=x,y=price)) + geom_point()
#print(p)

c = with(diamonds, cor.test(x,price))
print(c)

#p = ggplot(data = diamonds, aes(x = depth, y = price)) +
#  geom_point(alpha = 1/100) + 
#  scale_x_continuous(breaks=seq(43,79,2))
#print(p)

#p = ggplot(data = subset(diamonds, price<max(diamonds$price)*0.99 & carat<max(diamonds$carat)*0.99), aes(x=carat,y=price)) + 
#  geom_point()
#print(p)

diamonds$volume = diamonds$x * diamonds$y * diamonds$z
#p = ggplot(data = subset(diamonds, volume<=800 & volume>0), aes(x=volume,y=price)) + 
#  geom_point(alpha = 1/10) + 
#  ylim(c(0,20000)) + 
#  geom_smooth(method = lm)
#print(p)

library(dplyr)
diamondsByClarity <- diamonds %>%
  group_by(clarity) %>%
  summarise(mean_price = mean(price),
            median_price = median(price),
            min_price = min(price),
            max_price = max(price),
            n = n()) %>%
  arrange(clarity)

diamonds_by_clarity <- group_by(diamonds, clarity)
diamonds_mp_by_clarity <- summarise(diamonds_by_clarity, mean_price = mean(price))

diamonds_by_color <- group_by(diamonds, color)
diamonds_mp_by_color <- summarise(diamonds_by_color, mean_price = mean(price))

p1 = ggplot(data=diamonds_mp_by_clarity, aes(x=clarity, y=mean_price)) + 
  geom_bar(stat='identity')
p2 = ggplot(data=diamonds_mp_by_color, aes(x=color, y=mean_price)) + 
  geom_bar(stat='identity')

#grid.arrange(p1,p2)

#----------------#
# Problem Set 5
#----------------#

#p = ggplot(data=diamonds, aes(price)) + 
#  facet_wrap( ~ color) +
#  geom_histogram(aes(color=cut))
#print(p)

#p = ggplot(data=diamonds, aes(x=table, y=price)) + 
#  geom_point(aes(color=cut))
#print(p)

#p = ggplot(data=subset(diamonds, volume<max(volume)*0.1), aes(x=volume, y=price)) + 
#  geom_point(aes(color=clarity)) +
#  coord_trans(y = 'log10') +
#  scale_color_brewer(type = 'div')
#print(p)

p = ggplot(data=diamonds, aes(x=cut, y=price/carat)) + 
  geom_jitter(aes(color=color)) +
  facet_wrap( ~ clarity) +
  scale_color_brewer(type = 'div')
print(p)
