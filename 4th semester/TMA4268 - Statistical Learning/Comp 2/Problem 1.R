library(MASS)

str(Boston)
set.seed(1)

boston <- scale(Boston, center = T, scale = T)

train.ind = sample(1:nrow(boston), 0.8 * nrow(boston))
boston.train = data.frame(boston[train.ind, ])
boston.test = data.frame(boston[-train.ind, ])

# a
library(leaps)
# Forward
regfit_fwd = regsubsets(medv~., data = boston.train, nvmax = 13, method = "forward")
summary(regfit_fwd)
regfit_fwd_summary <- summary(regfit_fwd)
regfit_fwd_summary$outmat
plot(regfit_fwd_summary$adjr2, main = "Forward Stepwise Selection", xlab = "Number of Predictors", ylab = "Adjusted R-squared", type = "l")
#regfit_fwd_summary$adjr2
#which.max(regfit_fwd_summary$adjr2)
#plot(regfit_fwd, scale = "adjr2")

# Backward
regfit_bwd = regsubsets(medv~., data = boston.train, nvmax = 13, method = "backward")
summary(regfit_bwd)
regfit_bwd_summary <- summary(regfit_bwd)
regfit_bwd_summary$outmat
plot(regfit_bwd_summary$adjr2, main = "Backward Stepwise Selection", xlab = "Number of Predictors", ylab = "Adjusted R-squared", type = "l")
#regfit_bwd_summary$adjr2
#which.max(regfit_bwd_summary$adjr2)
#plot(regfit_bwd, scale = "adjr2")


# c
library(glmnet)
# i
y <- boston.train$medv
x <- data.matrix(boston.train[, c("crim", "zn", "indus", "chas", "nox", "rm", "age", "dis", "rad", "tax", "ptratio", "black", "lstat")])
cv_model <- cv.glmnet(x, y, alpha = 1, nfolds = 5)
plot(cv_model)

# ii
best_lambda <- cv_model$lambda.min
best_lambda

# iii
best_model <- glmnet(x, y, alpha = 1, lambda = best_lambda)
coef(best_model)