# Fundamentos de la Inteligencia Artificial

## **Inteligencia artificial débil**  

"*Son aquellas máquinas que pueden actuar **como si** fueran inteligentes*."

Hay quienes afirman que una inteligencia artifical débil es posible, "Cada aspecto del aprendizaje o cualquier otra característica de la inteligencia puede describirse con tanta precisión que se puede hacer que una máquina lo simule" (McCarthy et al., 1955). Mientras que otros niegan esta posibilidad, "La inteligencia artificial perseguida dentro del culto al computacionalismo no tiene ni el más mínimo atisbo de producir resultados duraderos" (Sayre, 1993). Claramente la imposibilidad de la inteligencia artificial depende de cómo se defina. Los filósofos tienen interés en el problema de comparar dos arquitecturas: la del humano, con la de la máquina, **¿pueden las máquinas pensar?** 

**Test de Turing**  

Alan Turing, en su famoso paper "Computing Machinery and Intelligence" (1950), sugiere que en vez de preguntar si las máquinas pueden pensar, deberíamos preguntar si las máquinas pueden pasar un test de comportamiento inteligente, al cual se le llamó **test de Turing**. Este test consiste en que una persona con el rol de *interrogador* tenga una conversación con un programa, y si este engaña a esta persona, haciendole creer que estaba conversando con una persona, el programa pasa el test.   

![](https://upload.wikimedia.org/wikipedia/commons/e/e4/Turing_Test_version_3.png)  

Hay varias objeciones a la posibilidad de máquinas inteligentes, inluyendo prácticamente todas las que se han planteado en el último medio siglo desde que se publicó el paper.

### **Objeciones a la posibilidad de máquinas inteligentes**  
#### **El argumento de la incapacidad**

El "argumento de la incapacidad" afirma que "una máquina nunca puede hacer X". Entre algunas de las incapacidades según Turing tenemos la imposibilidad de: ser gentil, tener iniciativa, diferenciar el bien del mal, enamorarse.

Está claro que las computadoras pueden hacer muchas cosas tan bien, o mejor que los seres humanos. Estas han hecho significantes descubrimiento en la astronomía, matemáticas, química, biología, como también han sabido jugar ajedrez, ensamblar partes en una línea de ensamblaje, etc. Esto no significa que las computadoras usen percepción y comprensión en la realización de estas tareas, ya que éstas no forman parte del comportamiento. También es correcto afirmar que hay muchas tareas en las que las computadoras no destacan, incluida la tarea de mantener una conversación abierta.

#### **La objeción matemática**
Es bien sabido, a través del trabajo de Turing (1936) y Gödel, que ciertas preguntas matemáticas son en principio irrespondibles por sistemas formales particulares. El teorema de incompletitud de Gödel es el más famoso ejemplo de esto. En resumen, para cualquier sistema axiomático formal F lo suficientemente poderoso para hacer aritmética, es posible construir una llamada sentencia de Gödel G(F) con las siguientes propiedades:  
+ G(F) es una sentencia de F, pero no se pude demostrar dentro de F.
+ Si F es consistente, entonces G(F) es verdadero.

Filósofos como J. R Lucas han afirmado que este teorema muestra que las máquinas son inferiores a los humanos, debido a que las máquinas son sistemas formales que están limitados por el teorema de la incompletitud, mientras que los humanos no poseen dicha limitación. Esta afirmación ha generado décadas de controversia y de argumentos que cuestionan este punto de vista:

+ Primero, el teorema de incompletitud de Gödel se aplica solo a sistemas formales con potencia suficiente para realizar aritmética. Esto incluye a las máquinas de Turing, las cuales son la base de la afirmación anterior, que afirma que las computadoras son máquinas de Turing, lo cual no es tan cierto. Las máquinas de Turing son infinitas, mientras que las computadoras son finitas, y cualquier computadora puede ser descrita como un sistema en lógica proposicional, que no está sujeto al teorema de incompletitud de Gödel.

+ Segundo, los seres humanos se han comportado de forma inteligente durante miles de años, incluso antes de inventar las matemáticas, por lo que es poco probable que el razonamiento matemático formal desempeñe algo más que un papel perisférico en lo que significa ser inteligente.

+ El tercero, y más importante, incluso si admitimos que los ordenadores tienen limitaciones en lo que pueden demostrar, no hay pruebas de que los humanos sean inmunes a esas limitaciones. Es demasiado fácil demostrar rigurosamente que un sistema formal no puede hacer X, y luego afirmar que los humanos pueden hacer X utilizando su propio método informal, sin dar ninguna prueba de esta afirmación. De hecho es imposible demostrar que los humanos no están sujetos al teorema de incompletitud de Gödel, porque cualquier prueba rigurosa requeriría una formalización del supuesto talento humano no formalizable, y por tanto se refutaría a sí misma.


#### **El argumento de la informalidad**
Una de las críticas mas influyentes y persistentes a la IA es la del "argumento de la informalidad del comportamiento". Esencialmente, esta es la afirmación de que el comportamiento humano es, por lejos, muy complejo para ser capturado por un simple conjunto de reglas. La incapacidad de capturar todo en un conjunto de reglas lógicas es llamada el **problema de la clasificación** en IA.


## **Inteligencia artificial fuerte**
"*Compuesta por máquinas que **realmente** piensan con inteligencia*."  

Muchos filósofos concuerdan que una máquina que pase el *test de Turing* no es una máquina que realmente piense. Sino que ha demostrado que solo puede simular este "pensar".  

Hay quienes se centran en que la máquina pueda sentir **emociones**, otros en la **consciencia**, y otros se centran en la **intencionalidad**, es decir, en la pregunta de si las supuestas creencias, deseos y otras representaciones de la máquina son realmente sobre algo en el mundo real.

Turing sostiene que la pregunta ¿pueden pensar las máquinas? está mal definida, y cuestiona el ¿por qué deberíamos insistir en un estándar más alto para las máquinas que para los humanos?. Si al fin y al cabo, en la vida ordinaria nunca tenemos pruebas directas sobre los estados mentales internos de otros humanos.  

Hay una cuestión de hecho en juego: los humanos tienen mentes reales, y las máquinas pueden o no tenerlas. Para abordar esta cuestión tenemos que entender cómo es que los humanos tienen mentes reales, y no sólo cuerpos que generan procesos neurofisiológicos. Los esfuerzos filosóficos por resolver este problema **mente-cuerpo** están directamente relacionados con la cuestión de si las máquinas pueden tener mentes reales

El problema **mente-cuerpo** fué analizado por primera vez en profundidad por el filósofo y matemático francés René Descartes. El consideró la actividad mental del pensamiento y los procesos físicos del cuerpo, llegando a la conclusión de que ambos deben existir en ámbitos separados, lo que ahora llamaríamos una teoría **dualista**. En su contraparte está la teoría **monista** de la mente a menudo llamado físicalismo, esta afirma que la mente no está separada del cuerpo, que los estados mentales son estados físicos. La mayoría de los filósofos modernos de la mente son fisicalistas de una u otra forma, y el fisicalismo permite, al menos en principio, la posibilidad de una **IA fuerte**. El problema de los fisicalistas es explicar como los estados físicos pueden ser simultáneamente estados mentales.

### **Estados mentales y el cerebro en una cubeta**
Filósofos fisicalistas han intentado explicar lo que significa decir que una persona, y por extensión, una computara, está en un estado mental particular. Se han enfocado en particular en los **estados intencionales**. Estos son estados tales como creer, conocer, desar, temer, etc, que se refieren a algún aspecto del mundo exterior.  

Si el fisicalismo es correcto, debe ser el caso en el que una descripción apropiada del estado mental de una persona está *determinada* por el estado del cerebro de esa persona. Por lo tanto, si actualmente estoy concentrado en comer una hamburguesa de forma consciente, mi estado cerebral instantáneo es un caso de la clase de estados mentales "saber que no está comiendo una hamburguesa". No importan las configuraciones de todos los átomos de mi cerebro y de otros, sino que el punto clave es que el mismo estado del cerebro no podría corresponder a un estado mental fundamentalmente distinton, como el conocimiento de que uno está comiendo una banana.

El experimento mental del **cerebro en una cubeta** pone en juicio el punto anterior. Bajo imaginación, consiste en remover el cerebro del cuerpo al nacer y colocarlo en una cuba que mantendría al cerebro, permitiendole crecer y desarrollarse. Al mismo tiempo se alimentaría con señales eléctricas desde una computadora, simulando enteramente un mundo ficticio, y las señales motrices emitidas desde el cerebro sería interceptadas y usadas para modificar la simulación apropiadamente. De hecho la vida simulada que usted vive replicaría exactamente la vida que habría vivido si si cerebro no hubiera sido colocado en la cuba, incluyendo la simulación de comer hamburguesas simuladas. Así, usted podría tener un estado cerebral idéntico al de alguien que está comiendo realmente una hamburguesa de verda, pero sería literalmente falso decir que tiene el estado mental "sabiendo que uno está comiendo una hamburguesa".  
<br>
![brain in the vat](https://static.wikia.nocookie.net/psychology/images/f/f7/Barin_in_a_vat_%28en%29.png/revision/latest?cb=20070227002849)
<br>
Este ejemplo parece contradecir la visión de que los estados del cerebro determinan estados mentales. Una forma de resolver este dilema es decir que el contenido de los estados mentales pueden ser interpretados desde dos puntos de vista diferentes. El punto de vista del **"contenido amplio"**, dónde el contenido de los estados mentales implica tanto el estado cerebral como la historia del entorno. El punto de vista del **"contenido estrecho"**, en cambio, sólo considera el estado cerebral. El contenido estrecho de los estados cerebrales de un verdadero comedor de hamburguesas y de un "comedor de hamburguesas" en el cerebro en la cubeta, es el mismo en ambos casos.  

### Funcionalismo y el experimento de reemplazo de cerebro

La teoría del **funcionalismo** dice que un estado mental es cualquier condición causal intermedia entre la entrada y la salida. Dos sistemas cualesquiera con procesos causales isomórficos tendrían los mismos estados mentales.  

Las afirmaciones del funcionalismo se ilustran más claramente con el experimento de reemplazo del cerebro. El planteamiento es el siguiente: Supongamos que la neurofisiología se ha desarrollado hasta el punto de comprender perfectamente el comportamiento de entrada-salida y la conectividad de todas las neuronas del cerebro humano. Supongamos que además podemos construir dispositvos electrónicos microscópicos que imitan este comportamiento, y que pueden interconectarse sin problemas con el tejido neuronal. Por último, supongamos que alguna técnica quirúrgica milagrosa puede sustituir neuronas individuales por los dispositos electrónicos correspondientes sin interrumpir el funcionamiento del cerebro en su conjunto. El experimento consiste en sustituir gradualmente todas las neuronas de la cabeza de alguien por dispositivos electrónicos.  

Se analizan las posibilidades de como respondería el sujeto de forma externa e interna, durante y terminada la cirugía. Hay 3 posibles conclusiones:

1. Los mecanismos causarles de la conciencia que generan este tipo de salidas en cerebros normales siguen operando en versiones electrónicas, que por tanto es consciente.
2. Los eventos mentales conscientes en el cerebro normal no tienen conexión causal con el comportamiento, y estas faltan en el cerebro electrónico, que por tanto no es consciente.
3. El experimento es imposible, y por lo tanto escpecular sobre esto carece de sentido.

Patricia Churchland señala que los argumentos funcionalistas que operan a nivel de neurona también pueden operar a nivel de cualquier unidad funcional más grande: como un grupo de neuronas o el cerebro entero. Esto significa que, si se acepta la idea de que el experimento de sustitución del cerebro muestra que el cerebro de reemplazo es consciente, entonces también se debe creer que la conciencia se mantiene cuando todo el cerebro es sustituido por un circuito que actualiza su estado, y mapea desde las entradas hasta las salidas a través de una enorme tabla de búsqueda

### **Naturalismo biológico y la Sala China**

El **naturalismo biológico** de John Searle(1980) ha planteado un fuerte desafío al funcionalismo, según el cual los estados mentales son características emergentes de alto nivel que son causadas por proceso físicos de bajo nievel en las neuronas, y lo que importa son las propiedades de las neuronas. Así pues, los estados mentales no pueden duplicarse sólo sobre la base de algún programa que tenga la misma estructura funcional con el mismo comportamiento de entrada-salida; requeriríamos que el programa se ejecutara en un arquitectura con el mismo poder causal que las neuronas. Para apoyar su punto de vista, Searle describe un sistema hipotético que claramente ejecuta un programa y pasa el test de Turing, pero que igualmente no entiende nada de sus entradas y salidas. Su conclusión es que ejecutar el programa adecuado (es decir, tener las salidas correctas) no es una condición suficiente para ser una mente.  

El sistema consiste de un humano, el cual entiende solo inglés equipado con un libro de reglas, escrito en inglés, y varias pilas de papel, algunas en blanco y otras con inscripciones indescifrables (El humano entonces juega el rol de CPU, el libro de reglas es el programa, y las pilas de papel son dispositivos de almacenamiento). El sistema se encuentra dentro de una sala con una pequeña abertura al exterior. A través de la abertura aparecen trozos de papel con símbolos indescifrables. El humano encuentra los símbolos correspondientes en el libro de reglas y sigue las instrucciones. Las instrucciones pueden incluir la escritura de símbolos en nuevas tiras de papel, la búsqueda de símbolos en las pilas, la reorganización de las pilas, etc. Al final, las instrucciones harán que uno o varios símbolos se transcriban en un papel que se transmite al mundo exterior.  
<br>
![](https://theness.com/neurologicablog/wp-content/uploads/2015/10/c-room.gif?w=640)  
<br>
Hasta aquí, todo bien. Pero desde el exterior, vemos un sistema que recibe información en forma de frases en chino y genera respuestas en chino que son "inteligentes". Searle argumenta entonces: la persona en la habitación no entiende el chino. El libro de reglas y las pilas de papel, siendo solo trozos de papel, no entienden chino. Por lo tanto, no hay comprensión del chino. *Por lo tanto, según Searle, ejecutar el programa correcto no genera necesariamente comprensión*.

### **Conciencia, qualia y la brecha explicativa**

La **conciencia** se suele dividir en aspectos como la comprensión y la autoconciencia. El aspecto en el que nos enfocaremos es el de la *experiencia subjetiva*: por qué se *siente* algo al tener ciertos estados cerebrales (por ejemplo, al comer una hamburguesa), mientras que presumiblemente no se siente nada al tener otros estados físicos (por ejemplo, al ser una roca). El término técnico para referirse a la naturaleza intrínseca de la experiencias es **qualia** (del latín, "tales cosas").  

Es difícil explicar cómo las popiedades físicas dan lugar a la manera en que las cosas se sienten bajo la experiencia subjetiva. A esta dificultad se la conoce como **brecha explicativa**. El comportamiento de una computadora puede explicarse adecuadamente solo pos sus componentes físicos, en este caso no existe tal brecha.

![](https://qph.cf2.quoracdn.net/main-qimg-c4dc3af406c851a11f46b801eae9ea05.webp)


## **La ética y los riesgos de desarrollar inteligencia artificial**

![](https://www.androidauthority.com/wp-content/uploads/2018/02/yapay-zeka-silikon-vadisi.jpg)
Todos los científicos e ingenieros se enfrentan a consideraciones éticas sobre cómo deben actuar en sus trabajo. Detrás de un software, que de alguna forma interactúa con personas, también hay una responsabilidad ética a la hora de como este realiza sus tareas, de misma manera con la IA. La IA deja algunos planteamientos que son interesantes de ver:  

- **La gente podría perder su trabajo por la automatización**.
El surgimiento de nuevas tecnologías de automatización, generalmente ha derivado en la disminución de personal humano en ciertas tareas. Con el nuevo auge de la IA sucede algo similar, pero en muchos ámbitos como puede ser el económico, metereológico, farmaceútico, etc.

- **La gente podría tener demasiado (o muy poco) tiempo libre**.
Software con IA puede reducir la cantidad de trabajo que tiene que emplear un trabajador, debido a que una parte de sus tareas es realizada por este. En el caso de las industrias intensivas, trabajar más implica ganar más, y gracias a la IA podemos aumentar el ritmo de nuestro trabajo.

- **La gente podría perder su sentido de ser única**.
Aprender y perfeccionarnos en nuestra profesión nos aporta sensación de ser únicos en lo que hacemos. El hecho de que una o varias IA´s puedan realizar las mismas tareas masivamente, pueden generar una carencia de esa sensación.

- **Los sistemas de IA podrían utilizarse para fines no deseados**.
De la misma manera en que la IA puede solucionar muchos problemas. También puede generar nuevos problemas para otros. El mejor ejemplo es el uso militar.

- **El uso de los sistemas de IA podría dar lugar a una pérdida de responsabilidad**.
Si las tareas asignadas a una IA, se ejecutan incorrectamente ¿quien asume la responsabilidad de dicho fallo?. En el ámbito médico, un mal diagnóstico puede resultar catastrófico para el paciente. Si el diagnóstico lo realiza un médico, la negligencia es relativamente fácil de probar, y la culpa debe asumirla el médico. ¿Y en el caso de una IA?

- **El éxito de la IA podría significar el fin de la raza humana**.
Casi cualquier tecnología tiene el potencial de causar daños en las manos equivocadas, pero con la IA y la robótica, tenemos el problema de que las manos equivocadas pueden pertenecer a la propia tecnología.  

## Conclusiones
Si bien hasta el momento solo hemos desarrollado IA débil, esta es muy importante en distintas áreas de las ciencias, la industria y el entretenimiento. Gracias a soluciones con IA se han hecho grandes avances científicos, que probablemente no se hubieran logrado, sobre todo teniendo en cuenta el recurso del tiempo. El hito de desarrollar una IA fuerte sigue siendo un gran desafío, del cual es incluso complicado estimar su fecha.  

Es importante determinar que características debe tener una IA, por lo tanto, lograr una definición. A lo largo de la historia se han hecho varias preguntas como: ¿que es la mente?, ¿esta debe estar asociada a un cuerpo?, ¿la inteligencia se puede determinar externamente?, si solo se puede determinar internamente ¿como lo hacemos en humanos?. Otro debate filósofico es sobre ¿como se observa la consciencia?, y si esta debe estar presente en la IA. La consciencia puede no ser más que una característica adicional, la cual es muy díficil de entender formalmente, y por lo tanto de implementar artificialmente. Estos debates y preguntas, por más que pertenezcan más a la filosofía, son interesantes de leer, ya que acompañan al conocimiento técnico y científico.  

Todo software que construimos, posiblemente termine interactuando con personas, de forma directa o indirecta. Hay casos en los que quizás no es interesante analizar el impacto que tendrá nuestro software, pero otros más críticos si lo son. Como puede ser, por ejemplo, un sofware que maneje un dispositivo de radioterapia. Con software que utiliza IA sucede el mismo problema ético, con el añadido de nuevos planteamientos.  