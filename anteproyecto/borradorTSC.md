# Borrador. Reinforcement Learning for Traffic Signal Control


## Descripción

Optimizar tiempos de espera de los vehículos, mediante una política "justa" tanto como para el conjunto total de vehículos como para el individuo.

Para extrar información de la intersección del semáforo y enviar ordenes para cambiar los tiempos del semáforo usaré las APIs de **Python** proporcionadas por **SUMO**.

## Posibles características del método utilizar. 

### Agente/s  

+ Sistema Agente monolítico. Semáforos bajo el control de un sistema centralizado.

+ Sistema Multi-Agente. Compuesto por un conjunto de semáforos comunicados entre sí (total o parcialmente) dentro del mismo entorno.

### Algortimos.
+ Q-Learning
+ Q-Deep-Learning

## Posible Workflow del sistema de control de tráfico

![](./images/Workflow-of-the-Traffic-Control-System.png)


## Modelos de tráfico

+ Macroscópico:  
    + los modelos describen relaciones entre la velocidad, densidad y flujo.
    + Análogo a fenómenos físicos. como dinámica de fluidos.  
    <br>    
+ Mesoscópico:  

    + los vehículos viajan en "paquetes" homogéneos.  

    <br>  

+ Microscópico:
    + en cada paso la velocidad y posición de cada vehículo es recalculada.

**Nagel schreckenberg model**. Modelo microscópico 1-D

![](./images/vehicleModel.gif)


## Diseño del entorno

![](./images/Deep-reinforcement-learning-framework-for-traffic-light-control.png)

+ Estados

    Por cada vehículo:  
    + Posición
    + Velocidad

    ![](./images/trafficState.png)

+ Acciones

+ Recompensas


## Métricas

+ Tiempo de espera promedio

+ Tiempo de espera por vehículo

+ Cantidad de veces que se detiene un vehículo ($|V_i|=0$)


