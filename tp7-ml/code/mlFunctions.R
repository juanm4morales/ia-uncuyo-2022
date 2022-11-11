library(rpart)
library(recipes)
library(dplyr)
library(tibble)
#library(rpart.plot)


random_predictor <- function(dataframe) {
  dataframe$prediction_prob <- runif(nrow(dataframe))
  return(dataframe)
}

random_classifier <- function(dataframe) {
  if ("prediction_prob" %in% colnames(dataframe)){
    dataframe <- dataframe %>% mutate(prediction_class = if_else(prediction_prob>0.5,1,0))
  } else {
    print("Column \'prediction_prob\' doesnt exist in the dataframe")
  }
  return(dataframe)
}


get_confussionMatrix <- function(d_binomial) {
  confussion_matrix <- matrix(0, nrow=2, ncol=2)
  # true Positive
  confussion_matrix[1,1] <- nrow(d_binomial %>% filter(target==0 & prediction==0))
  # false negative
  confussion_matrix[2,1] <- nrow(d_binomial %>% filter(target==1 & prediction==0))
  # false Positive
  confussion_matrix[1,2] <- nrow(d_binomial %>% filter(target==0 & prediction==1))
  # true negative
  confussion_matrix[2,2] <- nrow(d_binomial %>% filter(target==1 & prediction==1))
  return(confussion_matrix)
}

biggerclass_classifier <- function(dataframe) {
  
  true_count <- length(dataframe %>% filter(inclinacion_peligrosa==1))
  false_count <- length(dataframe %>% filter(inclinacion_peligrosa==0))
  dataframe <- dataframe %>% mutate(prediction_class = if_else(true_count>false_count,1,0))
}

get_sensitivity <- function(matrix){
  sensitivity <- (matrix[1,1])/(matrix[1,1]+matrix[2,1])
}

get_specifity <- function(matrix){
  specifity <- (matrix[2,2])/(matrix[2,2]+matrix[1,2])
}

get_precision <- function(matrix){
  precision <- (matrix[1,1])/(matrix[1,1]+matrix[1,2])
}

get_negativePredictive <- function(matrix){
  negPredValue <- (matrix[2,2])/(matrix[2,2]+matrix[2,1])
}

get_accuracy <- function(matrix){
  accuracy <- (matrix[1,1]+matrix[2,2])/(matrix[1,1]+matrix[1,2]+matrix[2,1]+matrix[2,2])
}

get_metrics <- function(matrix){
  cat("Sensitivity: ",get_sensitivity(matrix),"\n")
  cat("Specifity: ",get_specifity(matrix),"\n")
  cat("Precision: ",get_precision(matrix),"\n")
  cat("Negative Predictive Value: ",get_negativePredictive(matrix),"\n")
  cat("Accuracy: ",get_accuracy(matrix),"\n")
  cat("\n")
}

create_folds <- function(dataframe,k){
  folds <- list()
  fold_size <- nrow(dataframe)/k
  remain <- 1:nrow(dataframe)
  for (i in 1:k){
    fold <- sample(remain, fold_size-1, replace=FALSE)
    folds[[i]] <- fold
    if (i==fold_size){
      folds[[i]]<-remain
    }
    remain <- setdiff(remain,fold)
  }
  return(folds)
}

cross_validation <- function(dataframe, k){
  # vectors to store metrics
  accuracyV <- rep(-1,times=k)
  precisionV <- rep(-1,times=k)
  sensitivityV <- rep(-1,times=k)
  specificityV <- rep(-1,times=k)
  
  
  train_formula <- formula(inclinacion_peligrosa ~altura+
                             especie+
                             circ_tronco_cm+
                             long+
                             lat
  )
  
  folds <- create_folds(dataframe, k)
  
  for (i in 1:length(folds)){
    fold <- folds[[i]]
    
    train <- dataframe[-fold,]
    test <- dataframe[fold,]
    
    # handles the missing levels that does not exist in the training data (factor especie)
    # using recipes
    rec <-
      recipe(inclinacion_peligrosa ~ altura+
               especie+
               circ_tronco_cm+
               long+
               lat,
             data = train) %>%
      step_other(especie) %>%
      prep()
    
    new_train <- bake(rec, new_data=train)
    new_test <- bake(rec, new_data=test)
    #
    train.model <- rpart(train_formula, data=new_train, cp = 0.0001)
    predictions <- predict(train.model, new_test, type="class")
    
    d_binomial_cv <- tibble("target" = new_test$inclinacion_peligrosa, "prediction" = predictions)
    
    cM <- get_confussionMatrix(d_binomial_cv)
    
    accuracyV[i] <- get_accuracy(cM)
    precisionV[i] <- get_precision(cM)
    sensitivityV[i] <- get_sensitivity(cM)
    specificityV[i] <-  get_specifity(cM)
  }
  avg_acc  <- mean(accuracyV)
  avg_prec <- mean(precisionV)
  avg_sens <- mean(sensitivityV)
  avg_spec <- mean(specificityV)
  sd_acc  <- sd(accuracyV)
  sd_prec <- sd(precisionV)
  sd_sens <- sd(sensitivityV)
  sd_spec <- sd(specificityV)
  cat("Accuracy \n")
  cat("    AVG: ", avg_acc, "\n")
  cat("    SDe: ", sd_acc, "\n")
  cat("Precission \n")
  cat("    AVG : ", avg_prec, "\n")
  cat("    SDe: ", sd_prec, "\n")
  cat("Sensitivy \n")
  cat("    AVG: ", avg_sens, "\n")
  cat("    SDe: ", sd_sens, "\n")
  cat("Specificity \n")
  cat("    AVG : ", avg_spec, "\n")
  cat("    SDe: ", sd_spec, "\n")
}