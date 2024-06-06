library(MASS)
library(tidyverse)
data(lh)
plot(lh, type="b", pch = 19)
acf(lh)

## Model Based bootstrap
estOrig = arima(lh, order = c(1,0,0), include.mean = TRUE)
residuals = estOrig$residuals

acf_lh = acf(lh, plot = F)

## plot one example of resampled data set
ii = sample(1:48,100,replace = T)
x = numeric(100)
x[1] =  estOrig$coef[2] +residuals[ii[1]]
for(i in 2:100)
  x[i] =  estOrig$coef[2] + estOrig$coef[1]*(x[i-1] - estOrig$coef[2] ) + residuals[ii[i]]
par(mfrow=c(2,1))
plot(x, type="b", pch=19)
abline(v = 100-48, lty =2, col=2)
lines(53:100, lh, col = 2)
acf(x[53:100])
points(0:16, acf_lh$acf, pch = 19, col= 2)

## bootstrap replicates
B = 200
boot_rep1 = matrix(NA,B,2)
for(b in 1:B)
{
  ii = sample(1:48,100,replace = T)
  x = numeric(100)
  x[1] = residuals[ii[1]]
  for(i in 2:100)
    x[i] = estOrig$coef[2] + estOrig$coef[1]*(x[i-1] - estOrig$coef[2] ) + residuals[ii[i]]
  
  est = arima(x[53:100], order = c(1,0,0),  include.mean = TRUE)
  
  boot_rep1[b,] = est$coef
}

par(mfrow = c(1,2))
truehist(boot_rep1[,1], main = "lag1 covariance")
abline(v=estOrig$coef[1], lwd=2)
truehist(boot_rep1[,2], main = "mean")
abline(v=estOrig$coef[2], lwd=2)

apply(boot_rep1,2,mean)
apply(boot_rep1,2,sd)






############ Non-parametric bootstrap
#### moving block bootstrap
L = 3
k = 48/L
ii = sample(1:(48-L+1),k, replace=T)
index = sapply(ii,function(x)seq(from=x,length.out=L)) %>% as.numeric()
lh_new = lh[index]
par(mfrow=c(2,1))
plot(lh[index], type="b", pch=19)
lines( lh, col = 2)

acf(lh[index])
points(0:16, acf_lh$acf, pch = 19, col= 2)

boot_rep2 = matrix(NA,B,2)
for(b in 1:B)
{
  ii = sample(1:(48-L+1),k, replace=T)
  index = sapply(ii,function(x)seq(from=x,length.out=L)) %>% as.numeric()
  boot_rep2[b,] = arima(lh[index], order = c(1,0,0),  include.mean = TRUE)$coef
}

par(mfrow = c(1,2))
truehist(boot_rep2[,1], main = "lag1 covariance")
abline(v=estOrig$coef[1], lwd=2)
truehist(boot_rep2[,2], main = "mean")
abline(v=estOrig$coef[2], lwd=2)

apply(boot_rep2,2,mean)
apply(boot_rep2,2,sd)


### Block of blocks bootstrap

Y = cbind(lh[-length(lh)], lh[-1])
cor(Y[,1],Y[,2])

L = 3
k = ceiling(47/3)

boot_rep3 = numeric(B)

for(b in 1:B)
{
  ii = sample(1:(47-L+1),k, replace=T)
  index = sapply(ii,function(x)seq(from=x,length.out=L)) %>% as.numeric()
  Y_boot = Y[index,]
  boot_rep3[b] = cor(Y_boot[,1],Y_boot[,2])
  
}

par(mfrow=c(3,1))
hist(boot_rep1[,1],xlim=c(0,1), main = "Model based boostrap")
hist(boot_rep2[,1],xlim=c(0,1), main = "Block bootstrap")
hist(boot_rep3,xlim=c(0,1), main = "Block of blocks bootstrap")



  
  