# b

# c
library(tidyverse)
library(palmerpenguins)  # Contains the data set 'penguins'.
data(penguins)

names(penguins) <- c("species", "island", "billL", "billD", "flipperL", "mass", "sex", 
                     "year")

Penguins_reduced <- penguins %>% dplyr::mutate(mass = as.numeric(mass), flipperL = as.numeric(flipperL), 
                                               year = as.numeric(year)) %>% drop_na()

# We do not want 'year' in the data (this will not help for future predictions)
Penguins_reduced <- Penguins_reduced[, -c(8)]

set.seed(4268)
# 70% of the sample size for training set
training_set_size <- floor(0.7 * nrow(Penguins_reduced))
train_ind <- sample(seq_len(nrow(Penguins_reduced)), size = training_set_size)
train <- Penguins_reduced[train_ind, ]
test <- Penguins_reduced[-train_ind, ]

set.seed(123)
library(tree)

# i
species_tree <- tree(species ~ ., data = train, split = "gini")
plot(species_tree, type = "uniform")
text(species_tree, pretty = 1)

# ii
species_cv <- cv.tree(species_tree, K = 10)
species_cv

# iii
plot(species_cv$size, species_cv$dev, type = "b", xlab = "Terminal nodes", ylab = "Misclassifications")
prune_tree = prune.misclass(species_tree, best = 4)
plot(prune_tree, type = "proportional")
text(prune_tree, pretty = 1)

tree.pred.prune <- predict(prune_tree, prune_tree$species[test, ], type = "class")
confMat <- confusionMatrix(tree.pred.prune, prune_tree$species[test, ]$species)$table
1 - (sum(diag(confMat))/sum(confMat[1:2, 1:2]))
