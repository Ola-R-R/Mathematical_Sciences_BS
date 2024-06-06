library(MASS)

set1 = as.data.frame(mvrnorm(n = 1000, mu = c(2,3), Sigma = matrix(c(1,0,0,1), ncol = 2)))
colnames(set1) = c("x1", "x2")
set2 = as.data.frame(mvrnorm(n = 1000, mu=c(2,3), Sigma = matrix(c(1,0,0,5), ncol=2)))
colnames(set2) = c("x1", "x2")
set3 = as.data.frame(mvrnorm(n = 1000, mu=c(2,3), Sigma = matrix(c(1,2,2,5), ncol=2)))
colnames(set3) = c("x1", "x2")
set4 = as.data.frame(mvrnorm(n = 1000, mu=c(2,3), Sigma = matrix(c(1,-2,-2,5), ncol=2)))
colnames(set4) = c("x1", "x2")

install.packages("patchwork")
library(patchwork)
library(GGally)

p1 = ggplot(set1, aes(x1,x2)) + geom_point() + labs(title = "set1") + theme_minimal()
p2 = ggplot(set2, aes(x1,x2)) + geom_point() + labs(title = "set2") + theme_minimal()
p3 = ggplot(set3, aes(x1,x2)) + geom_point() + labs(title = "set3") + theme_minimal()
p4 = ggplot(set4, aes(x1,x2)) + geom_point() + labs(title = "set4") + theme_minimal()
(p1 + p2) / (p3 + p4)

