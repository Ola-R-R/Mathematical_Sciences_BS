library(geoR)
library(ggplot2)
library(mvtnorm)
require(plotly)
library(gridExtra)

empty <- ggplot()+geom_point(aes(1,1), colour="white")+
  theme(axis.ticks=element_blank(), 
        panel.background=element_blank(), 
        axis.text.x=element_blank(), axis.text.y=element_blank(),           
        axis.title.x=element_blank(), axis.title.y=element_blank())

colors <- colorRampPalette(c("white","royalblue","seagreen","orange","red","brown"))(500)
marginals = function(x)
{
  S = matrix(c(2,0,0,.5),2,2)
  mu = c(2,2)
  m1= 0.5*dnorm(x,mu[1],sqrt(S[1,1]))
  m2 =  0.5*dnorm(x,mu[2],sqrt(S[2,2]))
  
  S = matrix(c(1,-.8,-.8,1),2,2)
  mu = c(.5,sqrt(1-0.5^2))
  m1= m1+0.5*dnorm(x,mu[1],sqrt(S[1,1]))
  m2 =  m2+0.5*dnorm(x,mu[2],sqrt(S[2,2]))
  
  S = matrix(c(2,.5,.5,1),2,2)
  mu = c(.8,sqrt(1-.8^2))
  m1= m1+0.5*dnorm(x,mu[1],sqrt(S[1,1]))
  m2 =  m2+0.5*dnorm(x,mu[2],sqrt(S[2,2]))
  
  S = matrix(c(.3,0,0,3),2,2)
  mu = c(1,-3)
  m1= m1+0.5*dnorm(x,mu[1],sqrt(S[1,1]))
  m2 =  m2+0.5*dnorm(x,mu[2],sqrt(S[2,2]))
  
  
  S = matrix(c(1,0,0,1),2,2)
  mu = c(-5,-5)
  m1= m1+0.5*dnorm(x,mu[1],sqrt(S[1,1]))
  m2 =  m2+0.5*dnorm(x,mu[2],sqrt(S[2,2]))
  
  S = matrix(c(1,-0.4,-0.4,1),2,2)
  mu = c(-5,-1)
  m1= m1+0.5*dnorm(x,mu[1],sqrt(S[1,1]))
  m2 =  m2+0.5*dnorm(x,mu[2],sqrt(S[2,2]))
  
  S = matrix(c(1,-0.4,-0.4,1),2,2)
  mu = c(-5.3,-2.5)
  m1= m1+0.5*dnorm(x,mu[1],sqrt(S[1,1]))
  m2 =  m2+0.5*dnorm(x,mu[2],sqrt(S[2,2]))
  c1 = sum(m1*diff(x)[1])
  c2 = sum(m2*diff(x)[1])
  
  return(list(data.frame(x=x,y=m1/c1),data.frame(x=x,y=m2/c2)))
}

surf = function(x,y)
{
  
  xy = as.matrix(expand.grid(x,y))
  S = matrix(c(2,0,0,.5),2,2)
  mu = c(2,2)
  R = dmvnorm(xy,mean = mu,sigma=S)/2
  S = matrix(c(1,-.8,-.8,1),2,2)
  mu = c(.5,sqrt(1-0.5^2))
  R1 = dmvnorm(xy,mean = mu,sigma=S)/2
  
  S = matrix(c(2,.5,.5,1),2,2)
  mu = c(.8,sqrt(1-.8^2))
  R2 = dmvnorm(xy,mean = mu,sigma=S)/2
  
  S = matrix(c(.3,0,0,3),2,2)
  mu = c(1,-3)
  R3 = dmvnorm(xy,mean = mu,sigma=S)
  
   
  S = matrix(c(1,0,0,1),2,2)
  mu = c(-5,-5)
  R4 = 0.4*dmvnorm(xy,mean = mu,sigma=S)
  
  S = matrix(c(1,-0.4,-0.4,1),2,2)
  mu = c(-5,-1)
  R5 = 0.6*dmvnorm(xy,mean = mu,sigma=S)
 
  S = matrix(c(1,-0.4,-0.4,1),2,2)
  mu = c(-5.3,-2.5)
  R6 = 0.6*dmvnorm(xy,mean = mu,sigma=S)
  
  return(R1+R2+R3+R4+R5+R6)
}


x = seq(-10,4,0.1)
y = seq(-10,4,0.1)

a = surf(x,y)
surf_true = data.frame(as.matrix(expand.grid(x,y)),a)
v <- ggplot(surf_true, aes(Var1, Var2))
v + geom_contour(aes(z = a, color =..level..)) + 
  scale_color_gradient(low = "royalblue", high = "red") +
  ggtitle("Unnormalized target distribution") +
  labs(x="x",y="y") 

RW_MCMC_demo = function(nsamples, sd = 2)
{
  contour(x,y,matrix(a,length(x), length(y)), nlevels = 20)
  readline(prompt = "Press <Enter> to continue...")
  
  start = c(0,0)
  points(start[1], start[2], pch = "X", col=2)
  readline(prompt = "Press <Enter> to continue...")
  
  sample = c()
  rejected = c()
  n_acc = 0
  for(i in 1:nsamples)
  {
    print(i)
    prop.x = rnorm(1,mean = start[1], sd  = sd)
    prop.y = rnorm(1,mean = start[2], sd = sd)
    
    if(i<10)
    {
      
      lines(c(start[1], prop.x),c(start[2], prop.y), col = "blue", lwd = 2)
      readline(prompt = "Press <Enter> to continue...")
    }
    ltarget.start = log(surf(start[1], start[2]))
    ltarget.prop = log(surf(prop.x, prop.y))
    lprop.start = dnorm(start[1], mean = prop.x, log = T) +  
                  dnorm(start[2], mean = prop.y, log = T)
    
    lprop.prop = dnorm(prop.x[1], mean = start[1], log = T) +  
      dnorm(prop.y, mean = start[2], log = T)
    
    acc = min(1,exp(ltarget.prop-ltarget.start+lprop.start-lprop.prop))
    u = runif(1)
    {
      if(u<acc)
      {
        if(i<10)
          {
          lines(c(start[1], prop.x),c(start[2], prop.y), col = "green", lwd = 2)
          readline(prompt = "Press <Enter> to continue...")
          }
          start = c(prop.x,prop.y)
         sample = rbind(sample,start)
         n_acc = n_acc+1
      }
      else
      {
        if(i<10)
        {
        lines(c(start[1], prop.x),c(start[2], prop.y), col = "red", lwd = 2)
          readline(prompt = "Press <Enter> to continue...")
        }
        sample = rbind(sample,start)
        rejected = rbind(rejected,c(prop.x,prop.y))
      }
    }
  }
  points(sample)
  colnames(sample) = c("x","y")
  sample = as.data.frame(sample)
  return(list(sample = sample, rejected = rejected, nacc = n_acc))
}

par(mfrow=c(1,1))
marg = marginals(seq(-10,10,0.1))
res = RW_MCMC_demo(2000, sd = 2)
points(res$rejected, col = 2)  

sample = res$sample


## plot the estimated density and the marginals (red is the truth)
p <- ggplot(sample, aes(x,y))
p = p + geom_density_2d() +  
  geom_contour(data = surf_true, mapping = aes(Var1, Var2, z = a), color = "red")


p1 = ggplot(sample, aes(x)) + geom_histogram(aes(y=..density..)) + 
  geom_line(data = as.data.frame(marg[[1]]), aes(x,y), col = "red")
p2 = ggplot(sample, aes(y)) + geom_histogram(aes(y=..density..)) + 
  coord_flip() + 
  geom_line(data = as.data.frame(marg[[2]]), aes(x,y), col = "red")

grid.arrange(p1, empty, p, p2, ncol=2, nrow=2, widths=c(3.5, 1.5), 
             heights=c(1.5, 3.5))

## traceplot of the marginals
p1 = ggplot(sample, aes(x=seq_along(x), y=x)) + geom_line() + 
  labs(x="",y="") + ggtitle("Trace for x")
p2 = ggplot(sample, aes(x=seq_along(y), y=y)) + geom_line() + 
  labs(x="",y="")+ ggtitle("Trace for y")
grid.arrange(p1,p2)

## 3D plot
p_true = plot_ly(x=x,y=y,z=matrix(a, length(x), length(y)),
                 scene ='scene1',
                 type = "surface",colors=colors, showscale=FALSE)


kd = MASS::kde2d(x = sample$x, y = sample$y, n=50)
p_est <-  plot_ly(x=kd$x,y=kd$y,z=kd$z,scene = 'scene2',
                  type = "surface",colors=colors, showscale=FALSE)

axx <- list(
  gridcolor='rgb(255, 255, 255)',
  zerolinecolor='rgb(255, 255, 255)',
  showbackground=TRUE,
  backgroundcolor='rgb(230, 230,230)'
)

p = subplot(p_true, p_est) %>%
  layout(scene = list(domain=list(x=c(-10,5),y=c(-10,5)),
                      xaxis=axx, yaxis=axx, zaxis=axx,
                      aspectmode='cube'),
         scene2 = list(domain=list(x=c(-10,5),y=c(-10,5)),
                       xaxis=axx, yaxis=axx, zaxis=axx,
                       aspectmode='cube'))
p
