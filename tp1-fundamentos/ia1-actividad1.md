### 1) Ejemplos de aplicaciones de inteligencia artificial 
### **OpenWorm**  
Proyecto científico open source para crear el primer organismo virtual mediante computadoras. Este fué inicialmente impulsado gracias a una exitosa campaña de kickstarter. Está liderado por Stephen Larson, CEO de MetaCell, compañia que desarrolla software aplicado a neurociencias.  

El organismo elegido es la lombriz Caenorhabditis elegans. El mismo mide apróximadamente 1 mm, y posee uno de los sistemas nerviosos más simples (302 neuronas con cerca de 5500 conexiones), debido a esto se dispone del conectoma completo (mapa de las conexiones del cerebro). Con solo 1000 células, resuelve problemas básicos como la alimentación, reproducción y evitar depredadores. A pesar de que el gusano está bien estudiado en biología, una comprensión profunda y basada en principios de la bilogía de este organismo sigue siendo difícil de alcanzar.  

![OpenWorm](https://d.ibtimes.co.uk/en/full/1420989/worm-connectome-openworm.jpg?w=600&f=36151e18593fe6065f80e079b17c7a10)

La idea inicial fué simular todos los compartimientos de esta lombriz mediante computadoras y código, esto utilizando datos derivados de experimentos científicos llevados a cabo durante la última década. El objetivo secundario es permitir, a través de simulación, experimentos in-silico sin precedentes de células vivas para impulsar la próxima generación de análisis de sistemas biológicos avanzados, biología sintética, descubrimiento de fármacos utilizando computación, y modelado dinámico de enfermedades.


Las principales áreas del proyecto son:  
+ **Modelado neuromecánico con Sibernetic**.
Mediante un algoritmo llamado Smoothed Particle Hydrodynamics (SPH) es posible simular el cuerpo del gusano y su entorno usando GPU. [Video de la simulación](https://www.youtube.com/watch?v=SaovWiZJUWY&ab_channel=MikeVella).

+ **Motor de simulación Geppetto**.  
Plataforma modular de código abierto que permite la simulación interactiva.
[Live Demo](https://live.geppetto.org/).
+ **Ánalisis de movimiento**.
El equipo de análisis de movimiento está trabajando con una base de datos existente de movimiento de gusanos reales para hacer las comparaciones críticas.
+ **Motor de optimización**.  
Utiliza técnicas de optimización como algoritmos genéticos para ayudar a llenar los vacíos en conocimiento de la electrofisiología de las células musculares y neuronas.
+ **Recopilación y representación de datos**.  
Uno de los desafíos presentados es encontrar formas de integrar múltiples conjuntos de datos. OpenWorm mantiene el modelo abierto para poder hacer frente a diferentes estructuras de datos. Además es necesario comprender qué nos dice este conjunto de datos mediante representación visual.
+ **Alcance comunitario**.  
La construcción de la comunidad de ciencia abierta de OpenWorm siempre está en curso.
+ **Integración músculo-neurona**.  
+ **Robot C. elegans**.  

El proyecto OpenWorm ofrece el [código en GitHub](https://github.com/openworm/OpenWorm).  

Web oficial: [openworm.org](https://openworm.org/)  


Conferencia del cofundador Stephen Larson: [A worm is our best bet to unlock the secrets of the brain | Stephen Larson | TEDxBangalore](https://www.youtube.com/watch?v=RY2-0-QsuTE&ab_channel=TEDxTalks)

### **MuseNet**
Red neuronal profunda de la organización OpenAI, la cual puede generar canciones (rítmo, melodía, armonía) de 4 minutos, con 10 instrumentos diferentes  y utilizando estilos desde el country hasta Mozart y los Beatles. MuseNet utiliza la misma tecnología no supervisada de propósito general que GPT-2, un modelo transformador a gran escala entrenado para predecir el siguiente token en una secuencia, ya sea audio o texto.

Esta red neuronal no está capacitada para tener conocimientos sobre la teoría musical, sino más bien atiende a las estructuras de las composiciones musicales, con sus patrones, ritmos y estilos.

Tiene dos modos de generar música: un modo simple, y otro avanzado. En el **modo simple** se escucharán muestras aleatorias pregeneradas. Uno elige el compositor o estilo, una intro opcional de una pieza famosa, y luego se comienza a generar la canción. En el **modo avanzado** se puede interactuar directamente con el modelo.

![Compose in the style of Chopin, starting with Mozart´s Rondo alla Turca.](https://radiocantilo.com/wp-content/uploads/2019/05/7939e2f3-d2e6-43c2-8197-eaf450b41733.png)  

MuseNet genera cada nota calculando las probabilidades de todas las notas e instrumentos posibles. El modelo cambia para hacer que sus elecciones de instrumentos sean más probables, pero siempre existe la posibilidad de que elija otra cosa. Una dificultad a la que se enfrenta es a la ahora de hacer combinaciones extrañas de estilos instrumentos (como Chopin con bajo y batería). Estas combinaciones suenan poco naturales.

En el momento de la generación, podemos condicionar el modelo para crear muestras en un estilo elegido al comenzar con una entrada tal como: [Rachmaninoff Piano (Soundcloud)](https://soundcloud.com/openai_audio/rachmaninoff?in=openai_audio/sets/musenet).  

MuseNet utiliza los kernels de recálculo y optimizados de [Sparse Transformer](https://openai.com/blog/sparse-transformer/) (red neuronal para predicción de lo que sigue en una secuencia, ya sea de texto, imágenes o sonido) para entrenar una red de 71 capas con 24 cabezas de atención.

MuseNet ha sido entrenada con una gran recopilación de archivos MIDI de diferentes estilos musicales, entre ellos jazz, pop, clásico, estilos africanos, estilos indios, y más.

![](https://miro.medium.com/max/1400/1*6he8jJFn5DQ5-xIac8L5Uw.jpeg)  

[Página web de MuseNet](https://openai.com/blog/musenet/).

Otro proyecto de OpenAI, orientado a la composición de piezas musicales, es [Jukebox](https://openai.com/blog/jukebox/). Esta red neuronal genera música como MuseNet, pero lo hace con archivos de audio crudos (wav, mp3, flac, etc), lo cual posibilita más opciones a la hora de componer. El resultado producido por Jukebox tiene menor calidad respecto a MuseNet, ya que la mayoría de las canciones no disponen de todos los canales(instrumentos) de su grabación. Aún así, Jukebox ofrece mayor robustez y por lo tanto posibilidades, una de estas incluye la generación de voces y sus respectivas letras.

### 2) ¿Qué se entiende por inteligencia artificial?  

Yo entiendo el concepto de inteligencia artificial como al conjunto de capacidades observables que tiene un objeto no vivo (físico o virtual)creado por el ser humano, tales como: reconocer datos, tomar decisiones y aprender de ellos, y generar nueva información a partir de estos datos (entradas) y de su retroalimentación.


![](https://carpentries-incubator.github.io/machine-learning-librarians-archivists/fig/ep-02-ai-graph.png)  

<br />
Algunas definiciones de inteligencia artificial:  

<br />  


*"[La automatización de] actividades que asociamos con el pensamiento humano, actividades tales como la toma de decisiones, la resolución de problemas, el aprendizaje"* (Bellman).  

*"El estudio de los cómputos que hacen posible percibir, razonar y actuar"* (Winston).

*"La inteligencia computacional es el estudio del diseño de agentes inteligentes."* (Pool et al.).


### 3) ¿Que se entiende por Inteligencia?
Capacidad de:
- Recibir información mediante estímulos (sonido, luz, presión, electricidad), responder a estos estimulos, aprender y crear nuevo conocimiento a partir de esta información. Todo esto mediante uso del razonamiento y la creatividad.

### 4) ¿Qué se entiende por artificial?
Característica que posee un objeto al ser creado por el ser humano y que no es encontrado de forma natural.
