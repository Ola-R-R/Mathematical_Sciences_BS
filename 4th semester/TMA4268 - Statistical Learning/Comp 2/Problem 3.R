# b
library(MASS)
library(gam)

str(Boston)
set.seed(1)

boston <- scale(Boston, center = T, scale = T)

train.ind = sample(1:nrow(boston), 0.8 * nrow(boston))
boston.train = data.frame(boston[train.ind, ])
boston.test = data.frame(boston[-train.ind, ])

gam_model <- gam(medv ~ rm + s(ptratio, df = 3) + poly(lstat, 2), data = boston.train)

plot(gam_model)
