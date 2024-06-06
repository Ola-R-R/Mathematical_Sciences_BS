library(tidyverse)
library(ggplot2)

nsamples = 10000
u = runif(nsamples)


## SIMULATE EXPONENTIAL VALUE
lambda  = 2
x = -1/lambda * log(u)

## check that it is correct


# compare densitity
hist(x, freq =F, n = 100)
lines(seq(0,5,0.01), dexp(seq(0,5,0.01,), rate = lambda), col = 2, lwd =2)

# compare known characteristics

# mean
data.frame(nsamples = 1:nsamples,
           mean = cumsum(x)/(1:nsamples)) %>%
  ggplot() + geom_line(aes(nsamples, mean)) +
  geom_hline(yintercept = 1/lambda, color = "red") +
  ggtitle("mean")
  
  # variance
  data.frame(nsamples = 1:nsamples,
             mean = cumsum(x)/(1:nsamples),
             mean2 = cumsum(x^2)/(1:nsamples)) %>%
    mutate(var = mean2-mean^2) %>%
    ggplot() + geom_line(aes(nsamples, var)) +
  geom_hline(yintercept = 1/lambda^2, color = "red") +
    ggtitle("variance")

  
  
## SIMULATE CAUCHY DISTRIBUTION
nsamples = 10000
u = runif(nsamples)
x = tan(pi*(u-0.5))

hist(x,freq = F, n = 10000, xlim = c(-10,10))
lines(seq(-10,10,0.1), dcauchy(seq(-10,10,0.1)), col = 2, lwd = 2)

data.frame(nsamples = 1:nsamples,
           mean = cumsum(x)/(1:nsamples)) %>%
  ggplot() + geom_line(aes(nsamples, mean))  +
  ggtitle("mean")



## SAMPLING FROM UNIT CIRCLE
nsamples = 1000
theta = runif(nsamples, -pi/2,pi/2)
u = runif(nsamples)

# solution 1

x = u*cos(theta)
y = u*sin(theta)
plot(x,y, asp = 1)

#solution 2
theta = runif(nsamples, -pi/2,pi/2)
u2 = runif(nsamples)
x = sqrt(u2)*cos(theta)
y = sqrt(u2)*sin(theta)
plot(x,y, asp = 1)
