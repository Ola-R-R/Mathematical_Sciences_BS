library(MASS)

ntimes = 1000
sd = 0.4

mcmc_RW = function(sd, ntimes = 1000)
{
  x = numeric(ntimes)
  x[1] = runif(1)
  for(i in 2:ntimes)
  {
    x_prop = rnorm(1,mean = x[i-1], sd = sd)
    alpha = min(1, exp(-0.5*(x_prop^2-x[i-1]^2)))
    if(runif(1)< alpha)
      x[i]=x_prop
    else
      x[i] = x[i-1]
  }
  return(x)
}

x1 = mcmc_RW(0.1, 1000)
x2 = mcmc_RW(2, 1000)
x3 = mcmc_RW(30, 1000)
par(mfrow=c(3,1))
plot(x1, type="l", main=paste(expression(sigma), "=", 0.2))
plot(x2, type="l", main=paste(expression(sigma), "=", 2))
plot(x3, type="l", main=paste(expression(sigma), "=", 20))

par(mfrow=c(3,1))
truehist(x1, xlim = c(-5,5))
curve(dnorm(x), from = -5, to = 5, lwd=2, add=T)
truehist(x2, xlim = c(-5,5))
curve(dnorm(x), from = -5, to = 5, lwd=2, add=T)
truehist(x3, xlim = c(-5,5))
curve(dnorm(x), from = -5, to = 5, lwd=2, add=T)



