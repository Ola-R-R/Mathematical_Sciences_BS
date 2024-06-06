library(MASS)
set.seed(1)

id <- "1CWZYfrLOrFdrIZ6Hv73e3xxt0SFgU4Ph"  # google file ID
synthetic <- read.csv(sprintf("https://docs.google.com/uc?id=%s&export=download", id))

train.ind = sample(1:nrow(synthetic), 0.8 * nrow(synthetic))
synthetic.train = data.frame(synthetic[train.ind, ])
synthetic.test = data.frame(synthetic[-train.ind, ])

head(synthetic)

# a
library(pls)

pcr_model <- pcr(Y ~ ., data = synthetic.train, validation ="CV")

summary(pcr_model)

validationplot(pcr_model, val.type="MSEP")

plsr_model <- plsr(Y ~ ., data = synthetic.train, validation ="CV")

summary(plsr_model)

validationplot(plsr_model, val.type="MSEP")

# b