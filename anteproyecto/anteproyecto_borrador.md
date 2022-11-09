# Controlador dinámico de semáforo usando reinforcement learning
### Código del projecto: TSCRL
### Integrantes: Juan Martín Morales
<br>  

## Introducción

Los semáforos son el principal árbitro para gestionar tráfico en intersecciones, y actualmente la gran mayoría tienen una programación con ciclos fijos que han sido determinados gracias a información histórica o mediante alguna estrategia particular. Además estos no tienen en consideración el tráfico en tiempo real y debido a esto la eficiencia del tráfico es baja. Una mala gestión del tráfico puede causar numerosos problemas, tales como retrasos en los conductores, un gran desperdicio de energía, mayores emisiones de carbono y de óxidos nitrosos, los cuales empeoran la calidad del aire, y también accidentes de tráfico.  

## Solución propuesta

La idea principal para reducir las problemáticas descritras, es controlar las luces del semáforo utilizando una política que se ajuste dinámicamente al tráfico actual. Para esto propongo utilizar un modelo de reinforcement learning, dónde el agente será el controlador de semáforos y el entorno estará modelado por un proceso de decisión de Markov, el cuál está representado por $<S,A,P,R>$, dónde $S$ es el espacio de estados, $A$ es el espacio de acciones, $P$ es la función de probabilidad de transición de estados y $R$ es la función de recompensas.  

La eficiencia de dicho método será evaluada utilizando las siguientes métricas:

+ Tiempo de espera promedio.
+ Tiempo de espera por vehículo.
+ Cantidad de detenciones promedio.
+ Cantidad de detenciones por vehículo.

Las métricas más importantes a minimizar son, el **tiempo de espera promedio** de todos los vehículos, por simulación, y la **cantidad de detenciones promedio**, por simulación-

## Modelo de reinforcement learning para el control de semáforos

+ Agente: el controlador de semáforos de la intersección.

+ La política de control se obtiene mapeando desde los estados del tráfico hacia las acciones de control "óptimas".

+ Estados: información de la **posición** y **velocidad** de cada vehiculo en la intersección. También es posible que tenga información de otras intersecciones vecinas **(a decidir)**.

+ Acciones

+ 

![](./images/reinforcement_learning_traffic_model.png)


## Métricas