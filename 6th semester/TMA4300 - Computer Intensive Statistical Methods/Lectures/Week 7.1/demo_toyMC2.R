simMC_pois10_mcmc <- function(n, lambda = 10, x_start){
  
  x <- numeric(n)
  # create an initial value
  x[1] <- x_start
  
  for(i in 2:n){
    tmp <- x[i-1]
    
    # generate a uniformly distributed random variable
    u1 <- runif(1)
    if(u1 < 0.5){
      # if the current value is zero we stay at zero
      # otherwise we go to tmp-1
      if(tmp==0){
        x_star = tmp
      } else {
        x_star = tmp -1
      }
    } else {
      # if u1 >= 0.5 our proposal is one larger than 
      # the current value
      x_star <- tmp + 1
    }
    # get the acceptance prob.
    if(x_star > tmp){
        alpha = lambda/x_star
    }else if(x_star < tmp){
        alpha = tmp/lambda
    } else {
        alpha = 1
    }
    
    if(alpha > 1){
      x[i] <- x_star
    } else {
      u2 <- runif(1)
      if(u2 < alpha){
        x[i] <- x_star
      } else{
        x[i] <- tmp
      }
    }
  }
  return(x)
}


## show traceplots
trace1 <- simMC_pois10_mcmc(10000, x_start = 10)
trace2 <- simMC_pois10_mcmc(100, x_start = 0)
trace3 <- simMC_pois10_mcmc(100, x_start = 30)

par(mfrow=c(3,1))
plot(trace1, type="l", xlab="Iteration", ylab="x")
plot(trace2, type="l", xlab="Iteration", ylab="x")
plot(trace3, type="l", xlab="Iteration", ylab="x")

## show histograms

plot_dist <- function(trace, until, limits){

  if(until > length(trace)){
    stop("the trace is not long enough!")
  }

  my_x = 0:20
  my_y = dpois(my_x, lambda=10)
  tmp <- factor(trace[1:until], levels=0:20)
  tab <- table(tmp)
  plot(my_x, my_y, type="b", col=2, xlab="x", ylab="Density", 
    main=paste("Iteration", until), ylim=limits)
  lines(0:20, tab/length(tmp), type="h", cex=1.2)
}

trace1 <- simMC_pois10_mcmc(5000, x_start = 0)

par(mfrow=c(3,1), cex.lab=1.2)
plot_dist(trace1, 50, limits=c(0,0.2))
plot_dist(trace1, 500, limits=c(0,0.2))
plot_dist(trace1, 5000, limits=c(0,0.2))

