library(FrF2)

set.seed(123)

FrF2(nruns = 8, nfactors = 3, replications = 2, randomize = TRUE)

salt <- rep(c(-1, 1), 8)

lokk <- rep(c(-1, -1, 1, 1), 4)

kjele <- rep(c(-1, -1, -1, -1, 1, 1, 1, 1), 2)

tid <- c(102.61, 95.8, 94.26, 88.09, 120.34, 101.29, 85.63, 92.38, 96.91, 103.6, 95.23, 96.1, 107.32, 102.6, 109.51, 94.16)

fit <- lm(tid ~ (salt + lokk + kjele)^3)

summary(fit)

effekt <- 2 * fit$coeff

effekt

MEPlot(fit)

IAPlot(fit)

cubePlot(fit, "salt", "lokk", "kjele", size = 0.27, cex.lab = 1.5, cex.clab = 0.75)

rres <- rstudent(fit)

plot(fit$fitted, rres)

qqnorm(rres)
qqline(rres)

library(nortest)

ad.test(rstudent(fit))

