# Ejercitación: Introducción a ML
## 2.4 Exercises. An Introduction to Statistical Learning (2nd Edition)
<br>  

### 1) Para cada cada inciso del (a) al (d), indique si el rendimiento general esperado de un método de aprendizaje estadístico flexible sea mejor o peor que un método inflexible. Justifique su respuesta.  
<br>  

(a) El tamaño de la muestra n es extremadamente grande, y el número de predictores p es pequeño.  

El rendimiento, cuando el verdadero $f$ no es lineal, será **mejor** utilizando un **método flexible**. Con un tamaño de muestra extremadamente grande un método lo suficientemente flexible logrará un mejor ajuste (fitting) de la curva de $f$. Además, tener una cantidad pequeña de predictores, reduce el tiempo de cómputo para encontrar $\hat{f}$.

(b) El número de predictores p es extremadamente grande y el número de observaciones n es pequeño.  

El rendimiento será **peor** utilizando un método flexible, frente a uno inflexible. Un gran número de predictores incrementa el costo de encontrar $\hat{f}$. Al disponer de pocas observaciones y ya que en general los métodos flexibles tienen mayor varianza, un pequeño cambio en los datos de entrenamiento pueden llevar a grandes cambios en $\hat{f}$. En esta situación un **método inflexible** funcionará mejor.  

(c) La relación entre los predictores y la respuesta es altamente no lineal.  

El rendimiento será **mejor** utilizando un método flexible. Un **método inflexible** capturará mejor la no-linealidad de la relación entre los predictores y la respuesta.  

(d) La varianza de los términos de error, es decir, $σ^2 = Var(ϵ)$, es extremadamente
alto.  

El rendimiento será **peor** utilizando un método flexible frente a uno inflexible. Para evitar ajustar los datos al ruido en los datos, generalmente es mejor utilizar un **método inflexible**.  

### 2) Explique si cada escenario es un problema de clasificación o de regresión, e indique si nos interesa más la inferencia o la predicción. Por último, indique n y p.
<br>
(a) Recogemos un conjunto de datos sobre las 500 empresas más importantes de Estados Unidos. Para cada empresa registramos los beneficios, el número de empleados, el sector y el salario del CEO. Nos interesa saber qué factores aﬀectan el salario del CEO. 

Es un problema de regresión, ya que el salario del CEO es una variable continua. En este escenario nos interesa inferir como los factores citados influyen en el salario del CEO.  
n = 500.  
p = 3 (beneficios, nº de empleados y sector)  .

(b) Estamos pensando en lanzar un nuevo producto y queremos saber si será un éxito o un fracaso. Recogemos datos sobre 20 productos similares lanzados anteriormente. Para cada producto hemos registrado si fue un éxito o un fracaso, el precio cobrado por el producto, el presupuesto de marketing, el precio de la competencia y otras diez variables.  

Es un problema de clasificación, ya estamos clasificando productos de acuerdo al *éxito* o *fracaso* del mismo. Nos interesa predecir si nuestro producto tendrá éxito o no, por lo tanto la inferencia no nos incumbe.  
n = 20.  
p = 13 (precio, presupuesto de marketing, precio de la competencia y 10 variables más).

(c) Estamos interesados en predecir el cambio porcentual del tipo de cambio USD/Euro en relación con los cambios semanales en los mercados de valores mundiales. Por lo tanto, recogemos datos semanales para todo el año 2012. Para cada semana registramos el % de cambio del USD/Euro, el % de cambio del mercado estadounidense, el % de cambio del mercado británico y el % de cambio del mercado alemán.  

En este escenario el problema presentado es de regresión y predicción. Nos interesa predecir un valor de una variable continua, que es el cambio % en el tipo de cambio USD/Euro.  
n = cantidad de semanas en el año 2012.  
p = 3 (cambio % mercado EEUU, cambio % mercado británico, cambio % mercado alemán).

### 5) ¿Cuáles son las ventajas y desventajas de un enfoque muy flexible (frente a un enfoque menos flexible) para la regresión o la clasificación? ¿En qué circunstancias podría ser preferible un enfoque más flexible a uno menos flexible? ¿Cuándo puede ser preferible un enfoque menos flexible?  
 <br>

**Ventajas**: **menor bias** (*sesgo*). Lo que nos lleva a cometer menos errores en la aproximación de $f$.  

**Desventajas**: **mayor varianza**, por lo tanto un pequeño cambio en los datos de entrenamiento conllevan a cambios significantes en $\hat{f}$.

Un enfoque flexible es preferible cuando:

+ La relación entre predictores es altamente no lineal.  

+ Cuando el objetivo principal del problema es predecir.

+ Cuando el error irreducible $Var(ϵ)$ es bajo.

+ Cuando la cantidad de observaciones es alta. 

Un enfoque inflexible es preferible cuando no se dan las situaciones anteriores.  


### 6) Describa las diferencias entre un enfoque de aprendizaje estadístico paramétrico y no paramétrico. Cuáles son las ventajas de un enfoque paramétrico de regresión o clasificación (frente a un enfoque no paramétrico)? ¿Cuáles son sus desventajas?  

<br>

Los **métodos paramétricos**, en un principio asumen la forma de la **función mediante un model**o que tendrá ciertos **parámetros** a calcular.  Los **métodos no paramétricos** no asumen explícitamente la forma de $f$ mediante un modelo, sino que intentan **encontrar** un $f$ que se **aproxime** a los valores observados.

Un enfoque paramétrico de regresión o clasificación **reduce el problema de la estimación de $f$** a la estimación de un conjunto de parámetros. Asumiendo una forma paramétrica para $f$ se simplifica el rpboelam de estimar $f$, ya que generalmente es mucho más fácil estimar el conjunto de parámetros del modelo. 

Una desventaja de este enfoque paramétrico es que el **modelo** que elegimos **no suele coincidir con la verdadera $f$**. Si el modelo elegido se aleja demasiado de la verdadera $f$, entonces nuestra estimación será pobre. Para solucionar esto podemos elegir **modelos más flexibles**, pero en general ajustar a un modelo más flexible requiere estimar **más parámetros** y pueden llevar a un **sobreajuste** (*overfitting*) de los datos.  

### 7) La siguiente tabla proporciona un conjunto de datos de entrenamiento que contiene seis observaciones, tres predictores y una variable de respuesta cualitativa.  


| Obs | X1 | X2 | X3 | Y     |
|-----|----|----|----|-------|
| 1   | 0  | 3  | 0  | Red   |
| 2   | 2  | 0  | 0  | Red   |
| 3   | 0  | 1  | 3  | Red   |
| 4   | 0  | 1  | 2  | Green |
| 5   | −1 | 0  | 1  | Green |
| 6   | 1  | 1  | 1  | Red   |

### Supongamos que deseamos utilizar este conjunto de datos para hacer una predicción para Y cuando X1 = X2 = X3 = 0 utilizando K-vecinos más cercanos. 

(a) Calcule la distancia euclidiana entre cada observación y el punto de prueba, X1 = X2 = X3 = 0. 


$d_E(X_0,Obs_1) = 3.0$  
$d_E(X_0,Obs_2) = 2.0$  
$d_E(X_0,Obs_3) = 3.162278$  
$d_E(X_0,Obs_4) = 2.236068$  
$d_E(X_0,Obs_5) = 1.414214$  
$d_E(X_0,Obs_6) = 1.732051$  


(b) ¿Cuál es nuestra predicción con K = 1? ¿Por qué?  

$Y$ va a valer lo que vale el vecino más próximo a nuestro punto de prueba. Este vecino es el de la observación nº 5, por lo tanto $Y_0 = Green$.

(c) ¿Cuál es nuestra predicción con K = 3? ¿Por qué?  

Los tres vecinos más cercanos son las observaciones nº 2, 5 y 6. Dos de estos vecinos tienen el valor $Red$ y uno el valor $Green$. Por lo tanto $Y_0 = Red$

(d) Si la frontera de decisión de Bayes en este problema es altamente no lineal, ¿esperaríamos que el mejor valor de K fuera grande o pequeño? ¿Por qué?  

Esperaríamos que el mejor valor de K fuera **pequeño**. A medida que K aumenta, el método KNN se vuelve menos flexible y produce una frontera de decisión que se aproxima a la lineal. Cuando K es chico, la frontera de decisión se vuelve más flexible y se **aproxima mejor** a la **frontera de decisión de Bayes** planteada.