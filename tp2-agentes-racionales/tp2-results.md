# Análisis de los agentes aspiradora
Se evaluó el desempeño de dos **agentes simples reflexivos*, que *suponen* que el entorno es rectangular.  

Ambos agentes tienen un tiempo de vida constante de **1000 acciones**. Las acciones que consumen tiempo de vida son: moverse a la izquierda, moverse a la derecha, moverse arriba, moverse abajo y limpiar.

+ Agente 1: en principio, busca una de las "esquinas" de forma aleatoria, mientras limpia las casillas que detecte sucias. Una vez encontrada la esquina realiza un barrido de extremo a extremo hasta quedarse sin tiempo de vida, o hasta recorrer todo el entorno.

+ Agente 2 (random): realiza de forma aleatoria una secuencia de acciones (arriba, abajo, izquierda, derecha, limpiar, nada) hasta quedarse sin tiempo de vida.

**Medida de rendimiento**: 80% del peso de la medida de desempeño recae en la **proporción de casillas limpiadas sobre el total de casillas sucias**. El 20% de la métrica evalúa en base al **tiempo de vida restante** y una cantidad de acciones igual a: **cantidad de casillas del entorno + cantidad de casillas sucias**.

Para los dos agentes aspiradora se realizaron 10 simulaciones de cada combinación posible entre los tamaños seleccionados de cuadrícula (size) y el de la proporción de la suciedad (dirt ratio).
Tamaños de cuadrículas = (2x2, 4x4, 8x8, 16x16, 32x32, 64x64, 128x128)
Proporción de suciedad = (0.1, 0.2, 0.4, 0.8)

El tamaño de la grilla es el mayor determinante del rendimiento, teniendo en cuenta que el tiempo de vida de la aspiradora permanece constante para todas las simulaciones.

## Resultados del desempeño del agente aspiradora 1 (agent.py)

<p align="center"><img  src="https://i.imgur.com/5QzSimG.png"></p>
<p align="center"><img  src="https://i.imgur.com/S7HmzKu.png"></p>
![Performance Agent 1 by dirt ratio (with size=128 and 64)](https://i.imgur.com/S7HmzKu.png)

| AVERAGE Performance | Dirt Ratio |      |      |      |             |
| ------------------- | ---------- | ---- | ---- | ---- | ----------- |
| **Size**            | 0.1        | 0.2  | 0.4  | 0.8  | Total       |
| 2                   | 1.00       | 1.00 | 1.00 | 1.00 | 1.00        |
| 4                   | 1.00       | 1.00 | 1.00 | 1.00 | 1.00        |
| 8                   | 1.00       | 1.00 | 1.00 | 1.00 | 1.00        |
| 16                  | 1.00       | 1.00 | 1.00 | 1.00 | 1.00        |
| 32                  | 0.83       | 0.76 | 0.67 | 0.52 | 0.70        |
| 64                  | 0.22       | 0.20 | 0.17 | 0.13 | 0.18        |
| 128                 | 0.05       | 0.05 | 0.04 | 0.03 | 0.04        |
| Total               | 0.73       | 0.72 | 0.70 | 0.67 | 0.70        |

## Resultados del desempeño del agente aspiradora 2 (agent_random.py)
<p align="center"><img  src="https://i.imgur.com/07OMNhJ.png"></p>
<p align="center"><img  src="https://i.imgur.com/Gy38Dzs.png"></p>


|AVERAGE of Performance|Dirt Ratio|FIELD3|FIELD4|FIELD5|FIELD6     |
|----------------------|----------|------|------|------|-----------|
|Size                  |0.1       |0.2   |0.4   |0.8   |Grand Total|
|2                     |1.00      |1.00  |1.00  |1.00  |1.00       |
|4                     |1.00      |1.00  |1.00  |1.00  |1.00       |
|8                     |0.96      |0.88  |0.93  |0.94  |0.93       |
|16                    |0.47      |0.48  |0.50  |0.47  |0.48       |
|32                    |0.13      |0.15  |0.14  |0.14  |0.14       |
|64                    |0.07      |0.07  |0.07  |0.04  |0.06       |
|128                   |0.02      |0.02  |0.02  |0.01  |0.02       |
|Grand Total           |0.52      |0.51  |0.52  |0.52  |0.52       |

## Agente 1 vs Agente 2

![Agent1 vs Agent2 (by size)](https://i.imgur.com/PnzRDzR.png)
