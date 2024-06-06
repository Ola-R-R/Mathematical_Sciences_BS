id <- "1NJ1SuUBebl5P8rMSIwm_n3S8a7K43yP4" # google file ID
happiness <- read.csv(sprintf("https://docs.google.com/uc?id=%s&export=download", id),fileEncoding="UTF-8-BOM")

colnames(happiness)

cols = c('Country.name', 
         'Ladder.score',  # happiness score
         'Logged.GDP.per.capita',  
         'Social.support', 
         'Healthy.life.expectancy', 
         'Freedom.to.make.life.choices',
         'Generosity',  # how generous people are
         'Perceptions.of.corruption')

happiness = subset(happiness, select = cols)
rownames(happiness) <- happiness[, c(1)]

happiness.X = happiness[, -c(1, 2)]
happiness.Y = happiness[, c(1, 2)]
happiness.XY = happiness[, -c(1)]

happiness.X = data.frame(scale(happiness.X))


str(happiness)

library(ggfortify)
pca_mat = prcomp(happiness.X, center = T, scale = T)

autoplot(pca_mat, data = happiness.X, colour = "Black", loadings = TRUE, loadings.colour = "red", 
         loadings.label = TRUE, loadings.label.size = 5, label = T, label.size = 4.5)