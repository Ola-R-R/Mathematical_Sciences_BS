## Copper-nickel alloy, page 291 in Givens & Hoeting book

y <- c(127.6, 124.0, 110.8, 103.9, 101.5, 130.1, 
       122.0, 92.3, 113.1, 83.7, 128.0, 91.4, 86.2)
x <- c(0.01, 0.48, 0.71, 0.95, 1.19, 0.01, 0.48, 
       1.44, 0.71, 1.96, 0.01, 1.44, 1.96)

ndata <- length(y)

## this function compute the ratio of interest beta_1/beta_0
mylm <- function(y, x){
  
  fit <- lm(y ~ x)
  coefs <- coef(fit)
  theta <- as.numeric(coefs[2]/coefs[1])
  return(theta)
}

originalModel <- lm(y ~ x)
par(mfrow=c(1,1))
plot(fitted(originalModel), y)
abline(0,1, col=2)
plot(residuals(originalModel))
abline(h=0,lty=2)
plot(fitted(originalModel),residuals(originalModel))
abline(h=0,lty=2)

originalFit =  mylm(y,x)


#### boostrap  residuals
B <- 1000

res = originalModel$residuals
fit = originalModel$fitted.values

idx = matrix(sample(1:ndata, ndata*B, replace=T),
             ncol=B, byrow=F)

bootest1 = sapply(1:B, function(i){
  mylm(y = fit[idx[,i]]+res[idx[,i]], x = x[idx[,i]])})

# hist(bootest1, xlab="beta_1/beta_0", freq=F, 
#      main="Histogram of beta_1/beta_0")
# abline(v=mean(bootest1), col="purple")
# abline(v=quantile(bootest1, prob=c(.025, .975)), col="red", lty=2)
# round(mean(bootest1), 3)
# round(quantile(bootest1, prob=c(.025, .975)), 3)

## bootstrap pairs
# decide which observation to include 
#(at random and with replacement)
obs.idx <- matrix(sample(1:ndata, ndata*B, replace=T), ncol=B, byrow=F)
dim(obs.idx)
# apply the regression model to each data subset
bootest2 <- sapply(1:B, function(i){
  mylm(y[obs.idx[,i]], x[obs.idx[,i]])
}
)



library(MASS)
par(mfrow=c(1,2))
truehist(bootest1, prob=TRUE, 
         ylab="Density", xlab=expression(beta[1] / beta[2]), 
         col="lightblue", xlim=range(c(bootest1, bootest2)),
         main="resample residuals")
abline(v=originalFit, col=2, lwd=3)

truehist(bootest2, prob=TRUE, 
         ylab="Density", xlab=expression(beta[1] / beta[2]), 
         col="lightblue", xlim=range(c(bootest1, bootest2)),
         main="resample pairs")
abline(v=originalFit, col=2, lwd=3)

sd(bootest1)
sd(bootest2)

par(mfrow=c(1,1))
hist(bootest1)
abline(v = originalFit, col=2, lwd=3)
abline(v = mean(bootest1), col=3, lwd=3)


# determine bias
mean(bootest1) - originalFit
mean(bootest2) - originalFit

# bias corrected estimate
originalFit - mean(bootest1 - originalFit)
originalFit - mean(bootest2 - originalFit)


# compute 95% CI based on percentile method.
par(mfrow=c(1,1))
plot(sort(bootest1),seq(1:B)/B)

abline(h = c(0.025, 0.975))

abline(v = quantile(bootest1, prob=c(0.025, 0.975)))
quantile(bootest1, prob=c(0.025, 0.975))
