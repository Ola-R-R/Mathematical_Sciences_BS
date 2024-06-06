## ESTIMATION OF RARE EVENTS

#### We want to estimate P(X%in%[2,2.5]) when X comes from
#### a N(0,1) distribution

### We use monte carlo estimation
### and importance sampling with two different proposals g(x)

## set the limits of the interval i want to estimate the probability
lo = 2.5
up = 3

## True value the probability
## I can compute it analytically!!
true_value = pnorm(up, 0, 1) - pnorm(lo, 0, 1)
true_value

res = matrix(NA, 4, 2)
res[1,1] = true_value
## Define the indicator function for the chosen interval
## this is the function that is called h(x) in the slides
Ind =  function(x, m1 = lo, m2 = up)
  {
    return(x>=m1 & x<=m2)
  }

## set the number of samples
nsamples = n =1000


## Monte Carlo Estimate of the probability
z = rnorm(nsamples)
MC_est = mean(Ind(z))
MC_est_var = var(Ind(z)) / n
res[2,] = c(MC_est, MC_est_var)

par(mfrow=c(1,1))
hist(z, freq =F, xlim = c(-3,10), n = 100)
abline(v = c(lo,up), lty=2, lwd = 3)


## IS with normal proposal centered at the middle of the interval
# sample from the proposal
sd_proposal = 1
x1 = rnorm(nsamples, mean = (up+lo)/2, sd = sd_proposal)
# compute the importance weights
w1 = dnorm(x1)/dnorm(x1, mean = (up+lo)/2, sd = sd_proposal) 

hist(x1, col = 2, freq = F, add = T, n = 100, alpha = 0.4)
abline(v = c(lo,up), lty=2, lwd = 3)

points(x1,w1, col = 3, pch = 19)
IS_est1 = mean(w1*Ind(x1))
IS_est1_var = var(w1*Ind(x1)) / n
res[3,] = c(IS_est1, IS_est1_var)


#curve(dnorm(x, mean  = 0, sd = 1, log = T), from = -1, to  = 6)
#curve(dnorm(x, mean = 0, sd = 0.1, log = T), from = -1, to  = 6, col = 2, add = T)

IS_est1b = sum(w1 * Ind(w1)) / sum(w1)


## IS with uniform proposal


## NB: here we cannot use the self-normalizing form because it requires that the proposal is positive 
## everywhere where the target density is positive
## the normal form of the IS estimator requires only that g(x)>0 where h(x)f(x)>0

x2 = runif(nsamples, min = lo, max = up)
w2 = dnorm(x2)/dunif(x2, min = lo, max = up) 

hist(x2, col = 2, freq = F,  n = 100, alpha = 0.4)
points(x2,w2, col = 4)
IS_est2 = mean(w2*Ind(x2))
IS_est2_var =var(w2)/n
res[4,] = c(IS_est2, IS_est2_var)

library(tidyverse)

data.frame(model = c("Monte Carlo Est", paste("N(",(up+lo)/2, ",1) proposal" ), paste("Unif(",up,",",lo, ") proposal" )),
           mean = res[-1,1], sd =  sqrt(res[-1,2])) %>%
  mutate(lower = mean-2*sd, upper = mean+2*sd) %>%
  ggplot() + geom_errorbar(aes(x = model, ymin = lower, ymax = upper)) +
  geom_point(aes(x = model, y = mean), color = "red") +
  geom_hline(yintercept = res[1,1], lty = 2) + 
  xlab("") + ylab("")




## Look at the convergence of the estimators
mc = cumsum(Ind(z))/1:nsamples
is1 = cumsum(Ind(x1)*w1)/1:nsamples
is_prop = cumsum(Ind(x2)*w2)/1:nsamples

data.frame(mc = mc,
           is1 = is1,
           is2 = is_prop,
           n = seq_along(mc)) %>%
  pivot_longer(-n) %>%
  ggplot()+geom_line(aes(x = n, y = value,group = name, color = name))+
geom_hline(yintercept = res[1,1], lty = 2) 
  

#################EXAMPLE 2 #####################
##### change of parameters in gamma distribution

## parameters for the target gamma distribution
s_targ = 1.3
r_targ  = 2

## parameters from the proposal target distribution
s_prop = 3
r_prop = 2

curve(dgamma(x, shape = s_targ, scale = r_targ), from = 0, to = 10)
abline(v = s_targ*r_targ)
curve(dgamma(x, shape = s_prop, scale = r_prop), from = 0, to = 10, add = T, col = 2)
abline(v = s_prop*r_prop, col = 2)
legend("topright", lwd = 2, col = c(1,2), c("target", "proposal"))


## simulate from the proposal distribution
nsamples = 1000
x1 = rgamma(nsamples, shape = s_prop, scale = r_prop) 

## compute the importance weights
lw1 = dgamma(x1, shape = s_targ, scale = r_targ, log = T) - 
  dgamma(x1, shape = s_prop, scale = r_prop, log = T) # w = f(x)/g(x)
## standard Importance estimator
est1 = cumsum(x1 * exp(lw1))/1:nsamples

## self-normalizinf importance estimator
est2 = cumsum(x1 * exp(lw1))/cumsum( exp(lw1))
plot(est1, type="l", ylim=range(c(est1, est2)))
lines(est2, type="l", col = 2)
abline(h = s_targ*r_targ, lty = 2, col = 3)


#### EXAMPLE 3 ######################### 
## target N(0,1)
## proposal t(3)
library(zoo)

df = 2
curve(dnorm(x), from = -3, to = 3, lwd =  2)
curve(dt(x, df = df), from = -3, to = 3, add=T, col = 2, lwd = 2)
legend("topleft", lwd = 2, col = c(1,2), c("target", "proposal"))

nsamples = 1000
x1 = rt(nsamples, df = df)
w1 = dnorm(x1)/dt(x1,df=df)
m1 = cumsum(x1*w1)/1:nsamples
plot(m1, type = "l")
abline(h=0)

curve(dnorm(x)/dt(x,df=df), from = -5, to = 5)


## 
## target t(3)
## proposal N(0,1) ns
set.seed(1545212)
nsamples = 10000
x2 = rnorm(nsamples)
w2 = dt(x2,df=2)/dnorm(x2)
plot(cumsum(x2*w2)/1:nsamples, type = "l")
abline(h=0, col = 2)

plot(w2)
curve(dnorm(x), from = -5, to = 5)
curve(dt(x, df = df), from = -5, to = 5, add=T, col = 2)

curve(dt(x,df=df)/dnorm(x), from = -5, to = 5)

