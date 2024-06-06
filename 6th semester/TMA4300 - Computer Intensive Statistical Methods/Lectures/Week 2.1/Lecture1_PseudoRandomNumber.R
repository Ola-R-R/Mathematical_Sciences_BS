my_rng = function(x, a=69069069, b=12345, M=2^32){
  
  return((a*x + b)%%M)
}


b = c()
b[1] = my_rng(3)
n = 10000
for(i in 2:n){
  b[i] = my_rng(b[i-1])
}
b = b/(2^32+1)


library(MASS)
#pdf("../part1/graphics/rng.pdf", width=10, height=6)
truehist(b, xlab="")
abline(h=1.0, col=2)
plot(b[1:(n-1)], b[2:n], pch=20, 
     xlab="", ylab="", asp=TRUE)
acf(b)
#dev.off()
