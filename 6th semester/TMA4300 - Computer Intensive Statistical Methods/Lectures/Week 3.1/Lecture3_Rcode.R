
# simulate from Student-t distribution ------------------------------------


n = 6
x1 = rgamma(2000, n/2, n/2)
x2 = rnorm(2000, 0, 1/x1)
plot(x1,x2, main="Joint distribution for x1 and x2")

curve(dt(x,df = n), from = -10, to = 10, n = 1000, lwd = 3, col = 2,
      xlab="", ylab="", main = "marginal distr for x2")

hist(x2, freq=F, breaks = 100, add=T)


curve(dgamma(x,n/2,n/2), from = 0, to = 5, n = 1000, lwd = 3, col = 2,
      xlab="", ylab="", main = "marginal distr for x1")

hist(x1, freq=F, breaks = 100, add=T)



# Mixture of normal distribution ------------------------------------------
data("faithful")

plot(faithful$waiting)
hist(faithful$waiting)


p  = 0.5
mu1 = 1
mu2 = 2
s1 = 0.2
s2 = 0.5


x = seq(-2,5,0.01)
fx = dnorm(x,mu1, s1) * p + dnorm(x,mu2, s2) * (1-p) 

plot(x,fx, type = "l")

nsamples = 10000
x1 = rbinom(n = nsamples, size = 1, prob = p)
y = numeric(nsamples)
y[x1==1] = rnorm(sum(x1==1), mean = mu1, sd = s1)
y[x1==0] = rnorm(sum(x1==0), mean = mu2, sd = s2)

hist(y, breaks = 100, freq = F)
lines(x,fx, type = "l", lwd = 2)


