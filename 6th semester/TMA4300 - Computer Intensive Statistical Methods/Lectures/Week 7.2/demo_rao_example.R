## Rao-example using MCMC and two different proposal strategies:
##
## 1. independence sampler
## 2. random walk proposal


# target (posterior) distribution on log-scale asssuming a uniform prior
target <- function(theta, y, scaled=FALSE){
  res<- y[1]*log(2+theta) + 
    (y[2]+y[3])*log(1-theta)+y[4]*log(theta)
  res[theta<0 | theta>1] = NA
  if(!scaled) return(res)
  else return(res-max(res,na.rm=T))
}

### plot to show the target and the proposals in the independence sampler
data <- c(125, 18, 20, 34)

if(TRUE)
{
  mymean <- optimize(target, y=data, lower = 0, upper = 1, maximum = TRUE)$maximum
  # take the negative second derivative (Hessian) of the log-likelihood
  a <- -1*(-data[1]/(2+mymean)^2 - (data[2]+data[3])/(1-mymean)^2 - data[4]/mymean^2)
  # the variance is approximately the inversion of the negative Hessian
  mystd <- sqrt(1/a)
  
  par(mfrow=c(2,1))
  curve(exp(target(theta=x,y=data, scaled=T)), from = 0 , to = 1, lwd=3, ylab="",
        main = "Natural scale")
  abline(v=mymean)
  sd = mystd*1
  curve(dnorm(x, mean=mymean, sd=sd)/dnorm(mymean, mean=mymean, sd=sd), 
        from = 0, to = 1, add=T, col = 2, lwd=3)
  sd = mystd*2
  curve(dnorm(x, mean=mymean, sd=sd)/dnorm(mymean, mean=mymean, sd=sd), 
        from = 0, to = 1, add=T, col = 3, lwd=3)
  legend("topleft", c("target","indep proposal F=1", "indep proposal F=2"), 
         lwd=3,col=c(1,2,3))
  
  curve((target(theta=x,y=data, scaled=T)), from = 0 , to = 1, lwd=3, ylab="",
        main = "Log scale")
  abline(v=mymean)
  sd = mystd
  curve(dnorm(x, mean=mymean, sd=sd, log = T) - 
          dnorm(mymean, mean=mymean, sd=sd, log = T), from = 0, to = 1, add=T, col = 2, lwd=3)
  sd = mystd*2
  curve(dnorm(x, mean=mymean, sd=sd, log = T)/dnorm(mymean, mean=mymean, sd=sd, log = T), 
        from = 0, to = 1, add=T, col = 3, lwd=3)
}

mcmc_indep <- function(M, y, F){
  
  # store samples here
  xsamples <- rep(NA, M)
  
  # Idea: Normal Independence proposal with mean equal to the posterior
  # mode and standard deviation equal to the standard error or to 
  # a multiple of the standard error.
  mymean <- optimize(target, y=y, lower = 0, upper = 1, maximum = TRUE)$maximum
  
  # negative curvature of the log-posterior at the mode
  
  # take the negative second derivative (Hessian) of the log-likelihood
  a <- -1*(-y[1]/(2+mymean)^2 - (y[2]+y[3])/(1-mymean)^2 - y[4]/mymean^2)
  # the variance is approximately the inversion of the negative Hessian
  mystd <- sqrt(1/a)
  
  ##################################################################
  ## Alternative using optim instead of optimize. Optim directly returns the Hessian.
  #     eps <- 1E-9
  #     mycontrol <- list(fnscale=-1, maxit=100)
  #   
  #     ml <- optim(0.5, target, y=data, control=mycontrol, hessian=T, 
  #                 method="L-BFGS-B", lower=0+eps, upper=1-eps)
  #     mymean <- ml$par
  #     mystd <- sqrt(-1/ml$hessian)
  ##################################################################
  
  # factor to blow up standard deviation
  factor=F
  yes <- 0
  no <- 0
  
  # use as initial starting value mymean
  xsamples[1] <- mymean
  
  # MH-Iteration
  for(k in 2:M){
    # value of the past iteration
    old <- xsamples[k-1]
    
    # propose new value
    proposal <- rnorm(1, mean=mymean, sd=mystd*factor)
    
    # compute acceptance ratio
    posterior.ratio <-  exp(target(proposal, data)-target(old, data))
    if(is.na(posterior.ratio)){
      # happens when the proposal is not between 0 and 1 
      # => acceptance probability will be 0
      posterior.ratio <- 0
    }
    proposal.ratio <- exp(dnorm(old, mymean, mystd*factor, log=T)-
                            dnorm(proposal, mymean, mystd*factor, log=T))
    
    # get the acceptance probability
    alpha <- posterior.ratio*proposal.ratio
    
    # accept-reject step
    if(runif(1) <= alpha){	
      # accept the proposed value
      xsamples[k] <- proposal
      # increase counter of accepted values
      yes <- yes + 1
    }
    else{
      # stay with the old value
      xsamples[k] <- old
      no <- no + 1
    }
  }
  
  # acceptance rate
  cat("The acceptance rate is: ", round(yes/(yes+no)*100,2), "%\n", sep="")
  return(list(samples = xsamples, mean_prop = mymean, sd_prop = mystd*factor))
}


mcmc_rw <- function(M, y, d){
  
  # store samples here
  xsamples <- rep(NA, M)
  
  # Idea: Use a random walk proposal: U(theta^(k) - d, theta^(k) + d)
  
  yes <- 0
  no <- 0
  
  # specify a starting value
  xsamples[1] <- 0.5
  
  # MH-Iteration
  for(k in 2:M){
    # value of the past iteration
    old <- xsamples[k-1]
    
    # propose new value
    proposal <- runif(1, old-d, old+d)
    
    # compute acceptance ratio
    posterior.ratio <-  exp(target(proposal, data)-target(old, data))
    if(is.na(posterior.ratio)){
      # happens when the proposal is not between 0 and 1 
      # => acceptance probability will be 0
      posterior.ratio <- 0
    }
    # the proposal ratio is equal to 1 as we have a symmetric proposal distribution
    proposal.ratio <- 1
    
    # get the acceptance probability
    alpha <- posterior.ratio*proposal.ratio
    
    # accept-reject step
    if(runif(1) <= alpha){	
      # accept the proposed value
      xsamples[k] <- proposal
      # increase counter of accepted values
      yes <- yes + 1
    }
    else{
      # stay with the old value
      xsamples[k] <- old
      no <- no + 1
    }
  }
  
  # acceptance rate
  cat("The acceptance rate is: ", round(yes/(yes+no)*100,2), "%\n", sep="")
  return(xsamples)
}
## data
data <- c(125, 18, 20, 34)
# number of iterations
M <- 10000
xsamplesF1 <- mcmc_indep(M=M, F=1, y=data)
xsamplesF2 <- mcmc_indep(M=M, F=2, y=data)
xsamplesRW <- mcmc_rw(M=M,   d  = sqrt(12)/2*0.1, y=data)
xsamplesRW2 <- mcmc_rw(M=M,   d  = 0.001, y=data)

## some plots
# Independence proposal F=1
par(mfrow=c(3,3))
# traceplot
plot(xsamplesF1$samples, type="l")
# autocorrelation plot
acf(xsamplesF1$samples)
# histogram
hist(xsamplesF1$samples, nclass=100, xlim=c(0.4,0.8), prob=T)

# Independence proposal F=2
plot(xsamplesF2$samples, type="l")
acf(xsamplesF2$samples)
hist(xsamplesF2$samples, nclass=100, xlim=c(0.4,0.8), prob=T)

# RW proposal
plot(xsamplesRW2, type="l")
acf(xsamplesRW2)
hist(xsamplesRW2, nclass=100, xlim=c(0.4,0.8), prob=T)

par(mfrow=c(1,2))
hist(xsamplesF1$samples, nclass=100, xlim=c(0.4,0.8), prob=T)
curve(dnorm(x, mean  = xsamplesF1$mean_prop, sd = xsamplesF1$sd_prop), 
      from = 0, to = 1, add=T, lwd = 2, col = 2)
hist(xsamplesF2$samples, nclass=100, xlim=c(0.4,0.8), prob=T)
curve(dnorm(x, mean  = xsamplesF2$mean_prop, sd = xsamplesF2$sd_prop), 
      from = 0, to = 1, add=T, lwd = 2, col = 2)



