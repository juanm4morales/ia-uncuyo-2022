## Ejercicio 2)
### A partir del archivo arbolado-publico-mendoza-2021-train.csv, responder las
siguientes preguntas:  

### a. ¿Cual es la distribución de las clase inclinacion_peligrosa?
![](./plots/propArboles_inclinacion_peligrosa)

|    inclinacion_peligrosa       |   cantidad      |   %               |
| ------------------------------ | --------------- | ----------------- | 
| 0                              | 22661           | 88.76             |  
| 1                              | 2871            | 11.24             |

Como se puede observar las observaciones del dataset están muy desbalanceadas, ya que solo un 11.24% de los datos pertenecen a árboles con una inclinación peligrosa.

### b. ¿Se puede considerar alguna sección más peligrosa que otra?  


![](./plots/cantArboles_inclinacion_peligrosa_seccion)  
*Cantidad de árboles discriminados por variable: inclinacion_peligrosa, agrupados por seccion*  

Teniendo en cuenta el desbalanceo de observaciones en cuanto al atributo inclinacion_peligrosa, agrupado por seccion, **no es posible** **asegurar** que una **seccion más peligrosa que otra**.

![](./plots/propArboles_inclinacion_peligrosa_seccion)  
*Proporción de árboles con inclinación peligrosa, agrupados por sección*

Ignorando la falta de observaciones en las distintas secciones, se observa que en las secciones 2,3,4 y 5 hay una pequeña diferencia en cuanto a proporción de árboles con inclinación peligrosa vs árboles sin inclinación peligrosa.  


### c. ¿Se puede considerar alguna especie más peligrosa que otra?  


![](./plots/cantArboles_inclinacion_peligrosa_especie)  
*Cantidad de árboles discriminados por variable: inclinacion_peligrosa, agrupados por especie*  

![](./plots/propArboles_inclinacion_peligrosa_especie)
*Proporción de árboles con inclinación peligrosa, agrupados por especie*

Al igual que con las secciones, tampoco es posible considerar que una especie es más peligrosa que otra.

## Ejercicio 3)
### Histogramas de frecuencia para la variable $circ\_tronco\_cm$.

![](./plots/histograma_circ_tronco_cm_100bins)  
*100 bins*  


![](./plots/histograma_circ_tronco_cm_8bins) 
*8 bins*   

### Histograma de frecuencia para la variable $circ\_tronco\_cm$, separando por la clase $inclinacion\_peligrosa$

![](./plots/histograma_circ_tronco_cm_40bins_inclinacion_peligrosa)
*40 bins*  

### Gráfico de barras para la nueva variable categórica $circ\_tronco\_cm\_cat$  

![](./plots/histograma_circ_tronco_cm_cat)

**Criterio de corte**
```
circ_tronco_cm_cat=
    ifelse(circ_tronco_cm<50, "bajo",
        ifelse(circ_tronco_cm<125, "medio",
            ifelse(circ_tronco_cm<200, "alto",
                "muy alto"))))
```