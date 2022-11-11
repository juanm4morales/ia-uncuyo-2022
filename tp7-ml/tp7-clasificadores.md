## Clasificador aleatorio y clasificador por clase mayoritaria
### Matriz de confusión para el clasificador aleatorio

```
     [,1] [,2]
[1,] 2866 2806
[2,]  342  366
```
### Matriz de confusión para el clasificador por clase mayoritaria
```
     [,1] [,2]
[1,] 5672    0
[2,]  708    0
```
### Descripción de las matrices generadas:  
<br>  

[,1] y [,2] son las columnas que representan la **Referencia**. 

[1,] y [2,] son las filas que representan la **Predicción**.  

**[,1] = [1,] = 0** (inclinacion_peligrosa = no)  

**[,2] = [2,] = 1** (inclinacion_peligrosa = si)  

### Métricas clasificador aleatorio

```
[1] "Métricas clasificador aleatorio"
Sensitivity:  0.8933915 
Specifity:  0.1153846 
Precision:  0.5052891 
Negative Predictive Value:  0.5169492 

Accuracy:  0.5065831 
```

### Métricas clasificador por clase mayoritaria

```
[1] "Métricas clasificador clase mayoritaria"
Sensitivity:  0.8890282 
Specifity:  NaN 
Precision:  1 
Negative Predictive Value:  0 

Accuracy:  0.8890282 
```