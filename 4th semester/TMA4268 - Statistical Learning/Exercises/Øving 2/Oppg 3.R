library(ISLR)
data(Auto)

str(Auto)

summary(Auto)

quant = c(1,3,4,5,6,7)
sapply(Auto[, quant], range)

sapply(Auto[, quant], mean)

sapply(Auto[, quant], sd)

ReducedAuto = Auto[-c(10:85),]

sapply(ReducedAuto[, quant], range)

sapply(ReducedAuto[, quant], mean)

sapply(ReducedAuto[, quant], sd)

library(GGally)

ggpairs(Auto[,quant]) + theme_minimal()

ggplot(Auto, aes(as.factor(cylinders), mpg)) +
  geom_boxplot(fill="skyblue") +
  labs(title = "mgp vs cylinders")

ggplot(Auto, aes(as.factor(origin), mpg)) +
  geom_boxplot(fill="skyblue") +
  labs(title = "mgp vs origin")