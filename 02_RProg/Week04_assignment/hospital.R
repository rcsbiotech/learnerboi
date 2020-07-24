## topic 1

## Too many vars!

#### 1. 30 days mortality for heart attack ####
outcome <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
head(outcome)

outcome[, 11] <- as.numeric(outcome[, 11])
hist(outcome[, 11])

### Quiz

1. 

best("SC", "heart attack")

2.

best("NY", "pneumonia")















