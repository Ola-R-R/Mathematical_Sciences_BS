library(dplyr)
library(ggplot2)
library(tidyr)

# Simulate from normal distribution using rejection sampling --------------


## simulate from double exponential----------------------------------
density_double_exponential <- function(x, lambda){
  return(lambda/2 *
           exp(-lambda * abs(x)))
}
logdensity_double_exponential <- function(x, lambda){
  return(log(lambda/2) 
           -lambda * abs(x))
}

simulate_double_exponential =  function(nsamples, lambda)
{
  #here i have "cheated" and used r function to sample from exponential 
  #and binomial!!!
  z = rexp(nsamples, lambda)
  y = sample(c(0,1), nsamples,
             prob=c(0.5,0.5), replace=TRUE)
  x = c(z[y==0], -z[y==1])
  return(x)
}
ll = 3
x = simulate_double_exponential(1000, lambda = ll)
hist(x, freq = F, n =100)
curve(density_double_exponential(x,lambda = ll), from = -10,
      to = 10, add =T, lwd = 2)


# Rejection sampling to simulate from N(0,1) ------------------------------


#compute constant c (as function of lambda)
const = function(lambda)
  return(sqrt(2/pi) * exp(0.5*lambda^2)/lambda)

logconst = function(lambda)
  return(log(sqrt(2/pi))  + (0.5*lambda^2) -log(lambda))

# how does c varies with lambda?
curve(const, from = 0, to = 3)
points(c(0.5,1,2), const(c(0.5,1,2)), pch = 19, col = 2)

curve(logconst, from = 0, to = 3)
points(c(0.5,1,2), logconst(c(0.5,1,2)), pch = 19, col = 2)

curve(dnorm(x), from = -5, to = 5)
curve(density_double_exponential(x,lambda = 1) * const(lambda =1), from = -10,
      to = 10, add =T, lwd = 2)
curve(density_double_exponential(x,lambda = .5)* const(lambda =.5), from = -10,
      to = 10, add =T, lwd = 2, col = 2)
curve(density_double_exponential(x,lambda = 2)* const(lambda =2), from = -10,
      to = 10, add =T, lwd = 2, col = 3)



rej_sampling = function(n, ll)
{
  # simulate from double exponential
  x  <- simulate_double_exponential(nsamples = n, 
                                       lambda=ll) 
  # generate from the unif[0,1]
  u <- runif(n) 
  
  # compute log accept probbaility
  log_alpha <- -logconst(ll) + dnorm(x, log = T) -
    logdensity_double_exponential(x, lambda = ll)
  
  ind <- u < exp(log_alpha)
  accepted <- x[ind]
  return(list(z = accepted,
              proposed = x,
              alpha = exp(log_alpha),
              n = sum(ind)))
}

nsamples = 10000
# lambda = 1
s1 = rej_sampling(n = nsamples, ll  = 1)
hist(s1$z, freq = F)
curve(dnorm, from = -5, to = 5, add=T, lwd = 2)

# lambda = 0.5
s2 = rej_sampling(n = nsamples, ll  = 0.5)
hist(s2$z, freq = F)
curve(dnorm, from = -5, to = 5, add=T, lwd = 2)


# lambda = 2
s3 = rej_sampling(n = nsamples, ll  = 2)
hist(s3$z, freq = F)
curve(dnorm, from = -5, to = 5, add=T, lwd = 2)

#number  of accepted
s1$n
s2$n
s3$n

# illustration of weigts
par(mfrow =  c(2,1))
curve(density_double_exponential(x, lambda = 1), from = -5, to = 5)
curve(dnorm, add=T, lwd = 2, col = 2)

plot(s1$proposed, s1$alpha, pch = 19, cex = 0.1, xlim = c(-5,5))


# Illustration of importance sampling -------------------------------------

## plot the best proposals and the target together
par(mfrow = c(1,1))
curve(dnorm(x)/(0.5*dexp(abs(x), rate  = 1)), from = -4, to = 4,  
      col = 3, lwd=2, ylab="", lty=3)
curve(0.5*dexp(abs(x), rate  = 1), col = 2, lwd=2, add=T)
curve(dnorm(x), from =-4, to =4, lwd=3, add=T, lty=2)
legend("topleft", c("f(x)/g(x)", "f(x)", "g(x)" ), 
       col= c(3, 1,2), lwd=c(2,2, 2), lty = c(3,2,1))


## Try rejection sampling
finish = 0
while(finish==0)
{  
  ## step-by-step illustration  
  ## 1.) sample from the proposal distribution
  sample.x = simulate_double_exponential(1,lambda =1)
  
  ## 2.) Compute the acceptance probability alpha
  alpha = dnorm(sample.x)/(const(1) * dexp(abs(sample.x), rate  = 1))
  
  ## 3.) Generate a helping variable U from a uniform(0,1)
  u = runif(1, 0, 1)
  points(sample.x, u * const(1) * dexp(abs(sample.x), rate  = 1), pch = 19)
  Sys.sleep(1)
  ## 4.) Check if we accept it
  if(u <= alpha){
    y = sample.x
    col = "blue"
    points(sample.x,u * const(1) * dexp(abs(sample.x), rate  = 1), col=col, pch = 19)
    finish = 1
  } else {
    col = "red"
    points(sample.x,u * const(1) * dexp(abs(sample.x), rate  = 1), col=col, pch = 19)
  }
  Sys.sleep(2)
}    



# Weighted resampling -----------------------------------------------------

# use weighted resampling to generate from N(0,1) using 
# double exp as proposal

compute_weights = function(samples, lambda)
{
  lnum = dnorm(samples, log = T)
  lden = log(lambda/2) -lambda * abs(samples)
  weights = exp(lnum-lden)
  W = sum(weights)
  return(weights/W)
}

n = 10000
lambda = 1
proposals = simulate_double_exponential(n, lambda )
weights =  compute_weights(proposals, lambda)
resamples = sample(size = n/2, 
                   x = proposals, 
                   prob = weights, 
                   replace = T)

# black dots are proposals
p1 = data.frame(x = seq(-5,5, 0.01)) %>%
  mutate(norm = dnorm(x),
         dexp = lambda /2 *exp(-lambda * abs(x))) %>%
  pivot_longer(-x) %>%
  ggplot() + geom_line(aes(x,value, color = name, group =name)) +
  geom_point(data = data.frame(val =proposals), aes(x = val, y = 0), size = 1.5)

p1


resamples_df = data.frame(x = resamples) %>%
  group_by(x) %>% summarise(n = n()) %>%
  mutate(n = n/sum(n))

# p1+geom_segment(data = data.frame(x = proposals, 
#                                   y = weights*10^3), 
#                 aes(x=x,xend=x,y=0,yend=y))
p1+geom_segment(data = data.frame(x = proposals, 
                                  y = weights*10^3), 
                aes(x=x,xend=x,y=0,yend=y), color = rgb(.8,.8,.8,.05)) # +
  # geom_segment(data = resamples_df,
  #              aes(x=x,xend=x,y=0,yend=n*50), color = rgb(0, 0, 0,.15), size = 2)



ggplot(data = data.frame(x = resamples, dn = dnorm(resamples))) +
  geom_histogram(aes(x, y = ..density..), bins = 100) +
  geom_line(aes(x,dn), lwd = 2, color = "red")




