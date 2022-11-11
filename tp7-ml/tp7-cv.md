## Cross validation
### Código create_folds
```R
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
```
### Código cross_validation
```R
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
```

### Resultados (media y desviación estándar de las métricas seleccionadas) de aplicar el clasificador un árbol de decisión en los distintos conjuntos

```
Accuracy 
    AVG:  0.8687939 
    SDe:  0.005745847 
Precission 
    AVG :  0.9575013 
    SDe:  0.00422158 
Sensitivy 
    AVG:  0.9009447 
    SDe:  0.005653142 
Specificity 
    AVG :  0.3317577 
    SDe:  0.04000468 
```