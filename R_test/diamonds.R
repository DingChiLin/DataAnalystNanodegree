library(ggplot2)
data(diamonds)
#print(qplot(data=diamonds, x=price, breaks=seq(0,2000,20), color=cut))

library(gridExtra)
q1 = qplot(data=subset(diamonds, cut=='Fair'), x=price)
q2 = qplot(data=subset(diamonds, cut=='Good'), x=price)
q3 = qplot(data=subset(diamonds, cut=='Very Good'), x=price)
q4 = qplot(data=subset(diamonds, cut=='Premium'), x=price)
q5 = qplot(data=subset(diamonds, cut=='Ideal'), x=price)
#print(grid.arrange(q1, q2, q3, q4, q5, ncol = 2))

#print(by(diamonds$price, diamonds$cut, summary))
#print(by(diamonds$price, diamonds$cut, max))

q = qplot(x = price, data = diamonds) + facet_wrap(~cut, scales="free")
#print(q)

q = qplot(x = log10(price/carat+1), data = diamonds) + facet_wrap(~cut, scales="free")
#print(q)

q = qplot(x = color, y = price, data = diamonds, geom='boxplot') + coord_cartesian(ylim=c(0,9000))
#print(q)

q = qplot(x = color, y = price/carat, data = diamonds, geom='boxplot') + coord_cartesian(ylim=c(1000,6000))
#print(q)

q = qplot(x = carat, data = diamonds, geom='freqpoly', breaks=seq(1.5,5.5,0.1))
print(q)

