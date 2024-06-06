y = 3
tau_x = 0.01

full_conditional = function(x, tau_x, log=T, y_obs=y)
{
  d = -0.5 * tau_x * x^2 - exp(x) + x*y_obs
  if(log) return(d)
  else return(exp(d))
}

f_I = function(x, y_obs = y, tau_x)
{
   return(- tau_x*x + y_obs - exp(x))
}


f_II  = function(x,  tau_x)
{
  return(-tau_x-exp(x))
}

gauss_app = function(x,x0, y_obs =  y, tau_x, log=T)
  { 
    a = full_conditional(x0, y_obs, tau_x) - 
      f_I(x0, y_obs, tau_x)*x0 + 0.5*f_II(x0,  tau_x)*x0^2
    b <- f_I(x0, y_obs, tau_x) - f_II(x0, tau_x)*x0
    c <- -f_II(x0, tau_x)
    
    res = exp(-0.5*c*x^2+b*x)
    sd = sqrt(1/c)
    mean = b/c
    return(list(app = res, mean = mean, sd = sd))
  }

const1 = integrate(full_conditional,log=F, tau_x=tau_x, lower = -Inf, upper = Inf)$value
mode = optimise(full_conditional, tau_x=tau_x, lower = -10, upper = 10, maximum = T)$maximum
####
x0 = 2
x = seq(-1,4,0.1)
curve(exp(full_conditional(x, tau_x = tau_x))/const1, from = -1, to=4, 
      lwd=2, col=2, ylab="x", xlab="")
approx= gauss_app(x,x0 = x0, y_obs =  y, tau_x = tau_x, log=T)
curve(dnorm(x, mean = approx$mean, sd = approx$sd), add=T)  
points(x0,0, pch = 19, col=2)
points(approx$mean, 0, pch = "*", cex=1.5)

####
x0 = 0
curve(exp(full_conditional(x, tau_x = tau_x))/const1, from = -1, to=4, 
      lwd=2, col=2, ylab="", xlab="x")
approx= gauss_app(x,x0 = x0, y_obs =  y, tau_x = tau_x, log=T)
curve(dnorm(x, mean = approx$mean, sd = approx$sd), add=T)  
points(x0,0, pch = 19, col=2)
points(approx$mean, 0, pch = "*", cex=1.5)

####
x0 = mode
curve(exp(full_conditional(x, tau_x = tau_x))/const1, from = -1, to=4, 
      lwd=2, col=2, ylab="", xlab="x")
approx= gauss_app(x,x0 = x0, y_obs =  y, tau_x = tau_x, log=T)
curve(dnorm(x, mean = approx$mean, sd = approx$sd), add=T)  
points(mode,0, pch = 19, col=2)
points(approx$mean, 0, pch = "*", cex=1.5)


