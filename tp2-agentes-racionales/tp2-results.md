## Resultados del desempeño del agente aspiradora (agent.py)

Se realizaron 10 simulaciones de cada combinación posible entre los tamaños seleccionados de cuadrícula (size) y el de la proporción de la suciedad (dirt ratio).
Tamaños de cuadrículas = (2x2, 4x4, 8x8, 16x16, 32x32, 64x64, 128x128)
Proporción de suciedad = (0.1, 0.2, 0.4, 0.8)

El tamaño de la grilla es el mayor determinante del rendimiento, teniendo en cuenta que el tiempo de vida de la aspiradora permanece constante para todas las simulaciones.

![Performance vs Size](https://i.imgur.com/yvPr0QK.png)

| AVERAGE of Performance | Dirt Ratio |      |      |      |             |
| ---------------------- | ---------- | ---- | ---- | ---- | ----------- |
| Size                   | 0.1        | 0.2  | 0.4  | 0.8  | Grand Total |
| 2                      | 1.00       | 1.00 | 1.00 | 1.00 | 1.00        |
| 4                      | 1.00       | 1.00 | 1.00 | 1.00 | 1.00        |
| 8                      | 1.00       | 1.00 | 1.00 | 1.00 | 1.00        |
| 16                     | 1.00       | 1.00 | 1.00 | 1.00 | 1.00        |
| 32                     | 0.83       | 0.76 | 0.67 | 0.52 | 0.70        |
| 64                     | 0.22       | 0.20 | 0.17 | 0.13 | 0.18        |
| 128                    | 0.05       | 0.05 | 0.04 | 0.03 | 0.04        |
| Grand Total            | 0.73       | 0.72 | 0.70 | 0.67 | 0.70        |