## Pregunta 2.10 de AIMA 3º edición
Considerar una versión modificada del entorno de la aspiradora del ejercicio 2.8, en dónde el agente es **penalizado un punto por cada movimiento**.  

**Especificaciones de la aspiradora del ejercicio 2.8**:  
+ La medida de rendimiento recompensa un punto por cada cuadrado limpiado en cada paso de tiempo, durante una "vida útil" de 1000 pasos de tiempo.
+ La "geografía" del entorno se conoce a priori (figura 2.2), pero la distribución de la suciedad y la ubicación inicial del agente no. Los cuadrados limpios permanecen limpios y la succión limpia la casilla actual. Las acciones Left y Right mueven al agente a la izquierda y a la derecha excepto cuando este cuando esto lleve al agente fuera del entorno, en cuyo caso el agente permanece donde está.
+ Las únicas acciones disponibles son: *Left*, *Right* y *Suck*.
+ El agente percibe correctamente su ubicación y si esa ubicación contiene suciedad.

Responder: 

**a. ¿Puede un agente simple reflexivo ser perfectamente racional para este entorno? Explique.**

Ya que el agente no se detiene hasta haber consumido su "vida útil", el rendimiento decae en gran medida. Por lo tanto, este no es perfectamente racional, ya que no maximiza su medida de rendimiento.

**b. ¿Y con un agente reflexivo con estado? Diseñar tal agente.**

Un agente reflexivo, con conocimiento del estado del entorno y que además *se detiene* al saber que el entorno se encuentra "limpio", y que pueda realizar un barrido de extremo a extremo si es racional. Si el entorno se amplia a dos dimensiones, y por lo tanto se agregan las acciones "Up" y "Down", entonces el agente no es perfectamente racional: Aunque su rendimiento puede llegar a ser alto, este no es máximizado.

**c. ¿Cómo cambiarían las respuestas de a y b, si las percepciones del agente dan el estado de limpieza/suciedad de cada slot del entorno?**  

Si el agente puede conocer el estado de limpieza/suciedad de cada slot del entorno, entonces si puede ser perfectamente racional utilizando un algoritmo que calcule el recorrido óptimo.  


## Pregunta 2.11 de AIMA 3º edición

Considere una versión modificada del entorno de la aspiradora del Ejercicio 2.8, en la que la geografía del entorno (su extensión, límites y obstáculos) es desconocida, al igual que la configuración inicial de la suciedad. (El agente puede ir hacia arriba y hacia abajo, así como hacia la izquierda y la derecha).  

Responder:

**a. ¿Puede un agente reflejo simple ser perfectamente racional para este entorno? Explique.**  

Ya que el agente no recibe penalización como antes, es posible que la aspiradora maximice su rendimiento siempre y cuando el tamaño del entorno no sea muy grande. Ya que se requerirían más de 1000 movimientos y no se alcanzaría a limpiar completamente el entorno. En limitados entornos, si puede ser perfectamente racional.

**b. ¿Puede un agente reflejo simple con una función de agente aleatoria superar a un agente reflejo simple?**  

No lo superaría, ya que aún en un entorno no muy grande podría succionar casillas que esten limpias, podría volver a una celda ya visitada.
    

**c. ¿Puedes diseñar un entorno en el que tu agente aleatorizado tenga un mal rendimiento? Muestre sus resultados.**  
    
Aumentando el tamaño del entorno, el agente con comportamiento aleatorio disminuirá su rendimiento. Lo mismo al aumentar la cantidad de obstáculos, aumentan las probabilidades de que el agente se encuentre "atrapado".

<p align="center"><img  src="https://i.imgur.com/07OMNhJ.png"></p>

En el gráfico izquierdo se observa como el rendimiento disminuye a medida que aumenta el tamaño de un entorno cuadrado.

**d. ¿Puede un agente de reflejo con estado superar a un agente de reflejo simple?**  

Un agente de reflejo con estado si puede superar a un agente de reflejo simple. Al conocer el estado de su entorno, el agente se detendrá una vez que haya limpiado todas las casillas. Esta mejora se debería observar mejor en entornos dónde se requiera más vida útil (>1000), debido a que teniendo un "estado del mundo" el agente sabría identificar que casillas ya ha observado, y así evitar gastar movimientos en estas casillas. 


