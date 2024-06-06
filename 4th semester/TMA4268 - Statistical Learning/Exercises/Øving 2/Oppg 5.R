set.seed(2) # to reproduce
M <- 100 # repeated samplings, x fixed
nord <- 20 # order of polynomials
#------
x <- seq(from = -2, to = 4, by = 0.1)
truefunc <- function(x) {
   return(x ˆ 2)
}
true_y <- truefunc(x)
error <- matrix(rnorm(length(x) * M, mean = 0, sd = 2),
                nrow = M,
                byrow = TRUE)
ymat <- matrix(rep(true_y, M), byrow = T, nrow = M) + error # Each row is a simulation
#------
predictions_list <- lapply(1:nord, matrix, data = NA, nrow = M, ncol = ncol(ymat))
for(i in 1:nord){
   for(j in 1:M){
      predictions_list[[i]][j, ] <- predict(lm(ymat[j,] ~ poly(x, i, raw = TRUE)))
   }
}
# Plotting -----
library(tidyverse) # The tidyverse contains ggplot2, as well as tidyr and dplyr,
# which we can use for dataframe manipulation.
list_of_matrices_with_deg_id <- lapply(1:nord, function(poly_degree) cbind(predictions_list[[poly_degree]], simulation_num = 1:M, poly_degree))
# Now predictions_list is a list with 20 entries, where each entry is a matrix
# with 100 rows, where each row is the predicted polynomial of that degree.
# We also have a column for the simulation number, and a column for polynomial degree.
# Extract each matrix and bind them to one large matrix
stacked_matrices <- NULL
for (i in 1:nord) {
   stacked_matrices <-
      rbind(stacked_matrices, list_of_matrices_with_deg_id[[i]])
}
stacked_matrices_df <- as.data.frame(stacked_matrices)
# Convert from wide to long (because that is the best format for ggplot2)
long_predictions_df <- pivot_longer(stacked_matrices_df, !c(simulation_num, poly_degree), values_to = "y")
# Now we can use ggplot2!
# We just want to plot for degrees 1, 2, 10 and 20.
plotting_df <- cbind(long_predictions_df, x = x) %>% # adding the x-vector to the dataframe
   filter(poly_degree %in% c(1, 2, 10, 20)) # Select only the predictions using degree 1, 2, 10 or 20
ggplot(plotting_df, aes(x = x, y = y, group = simulation_num)) +
   geom_line(aes(color = simulation_num)) +
   geom_line(aes(x = x, y = xˆ2), size = 1.5) +
   facet_wrap(~ poly_degree) +
   theme_bw() +
   theme(legend.position = "none")