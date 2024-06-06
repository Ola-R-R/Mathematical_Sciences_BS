
### Queue 

## The function computes the minimum 
## time it take for the number of person in the system to reach N

simulate_queue = function(lambda_arrival, 
                          shape_leave, 
                          scale_leave,
                          N = 7, 
                          nsamples = 1000, 
                          do.plot = F)
  ## parameters for the arrival exponential distribution
  ## lambda_arrival 
  ## mean arrival time  = 1/lambda_arrival
  
  ## parameters for the service gamma distribution
  ## shape_leave 
  ## scale_leave 
  ## mean service time  = shape*scale
{
  res = numeric(nsamples)
  for( i in 1:nsamples)
  {
    # initialize
    X = 0
    DT = 0
    t = 0
    x = 0
    delta_arrival  = rexp(n = 1, rate = lambda_arrival)
    t_arrival = t + delta_arrival
    while(x<N) 
      ## stop simulating if we reach the state N
    {
      if(x==0)
      {
        t = t_arrival
        x = x + 1
        delta_arrival  = rexp(1, rate = lambda_arrival)
        t_arrival = t + delta_arrival
        delta_leave = rgamma(1, shape = shape_leave, scale = scale_leave)
        t_leave = t + delta_leave
        X = c(X,x)
        DT = c(DT, delta_arrival)
        }
      else{
        if(delta_arrival<delta_leave)
        {
          t = t_arrival
          DT = c(DT, delta_arrival)
          x = x + 1
          X = c(X,x)
          delta_arrival  = rexp(1, rate = lambda_arrival)
          t_arrival = t + delta_arrival
        }
        else
        {
          t = t_leave
          DT = c(DT, delta_leave)
          x = x-1
          X = c(X,x)
          if(x>0)
          {
            delta_leave = rgamma(1, shape = shape_leave,  scale = scale_leave)
            t_leave = t + delta_leave
          }  
        }
      }
     
    }
    res[i] = t
    if( do.plot & i<5)
    { 
      plot(cumsum(DT), X, type="s", ylab="N clients", xlab="time")
      readline("press key to continue")
    }
  }
  return(res)
}


r1 = simulate_queue(lambda_arrival = 1, 
                    shape_leave = 1, 
                    scale_leave = 1, 
                    do.plot = T)

## increase mean interarrival time
r2 = simulate_queue(lambda_arrival = 0.8, 
                    shape_leave = 1, 
                    scale_leave = 1,
                    do.plot = T)
## increase mean service time
r3 = simulate_queue(lambda_arrival = 1, 
                    shape_leave = 1.5, 
                    scale_leave = 2,
                    do.plot = T)

plot(density(r1), col = 1)
lines(density(r2), col = 2)
lines(density(r3), col = 3)


