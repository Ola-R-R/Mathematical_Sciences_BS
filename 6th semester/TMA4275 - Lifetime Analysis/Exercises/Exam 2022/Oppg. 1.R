S_T <- c(1.11,1.13,1.35,1.40,1.83,2.16,2.22,2.25,2.40,2.65)

C_T <- c(1,0,1,0,0,1,1,0,1,0)

T_j <- (S_T*C_T)[(S_T*C_T)>0]

A <- c()
for (i in T_j) {
  A <- c(A, 1/(length(S_T[S_T >= i])))
}
A <- cumsum(A)

Sig_2 <- c()
for (i in T_j) {
  Sig_2 <- c(Sig_2, 1/(length(S_T[S_T >= i])^2))
}
Sig_2 <- cumsum(Sig_2)

CI_U <- c()
CI_L <- c()

z <- qnorm(1-.05/2)

for (i in 1:length(T_j)) {
  CI_U <- c(CI_U, A[i]*exp(z * sqrt(Sig_2[i])/A[i]))
}
for (i in 1:length(T_j)) {
  CI_L <- c(CI_L, A[i]*exp(-z * sqrt(Sig_2[i])/A[i]))
}

plot(c(0,T_j,3),c(0,A,A[length(A)]),type = "s",xlim = c(0,3),ylim = c(0,3.5),main = "Elson-Aalen estimator w. 95% percent C.I.",xlab = "Time", ylab = "Value", lwd = 3)
lines(c(0,T_j,3),c(0,CI_U,CI_U[length(CI_U)]),type = "s", lwd = 1.5, lty = 2)
lines(c(0,T_j,3),c(0,CI_L,CI_L[length(CI_L)]),type = "s", lwd = 1.5, lty = 2)
