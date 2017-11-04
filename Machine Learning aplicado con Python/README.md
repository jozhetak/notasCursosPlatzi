# Introducción
En este curso veremos cómo utilizar ***Machine Learning*** con distintas librerías de Python. Particularmente estaremos utilizando ***Scikit-Learn***, que es una de las más utilizadas en la industria.

En este curso también nos enfocaremos es en entender todo el flujo de trabajo que se hace cuando se resuelve un problema de ***Machine Learning***.

Además de entender muy bien los algoritmos de ***Machine Learning*** que estaremos viendo, veremos otras disciplinas que son tanto o más importantes como el ***Feature Engineering*** y la selección de modelos.

Con este curso serás capaz de resolver problemas difíciles de Machine Learning y aplicarlo tanto en la industria como en tus aplicaciones.

--- Descargar archivo ----

# Importancia de definir el problema en Machine Learning

***Errores comunes*** que se ven cuando no se define bien el problema y se comienza a codear:
- No hay problemas por resolver.
- Existen soluciones más simples.
- No se puede medir el impacto del modelo.
- No se sabe si el problema ya ha sido resuelto antes.
- El problema es imposible de resolver.

***Preguntas clave*** para reconocer el ***tipo de aprendizaje*** que se necesita:
- ¿Qué beneficio se puede generar y para quién?
- ¿Cuál de las siguientes funcionalidades sería más útil para lograr el objetivo?

1. Predecir alguna métrica (Aprendizaje supervisado)
2. Predecir una etiqueta (Aprendizaje supervisado)
3. Agrupar elementos similares.
4. Optimizar un proceso con prueba y error.

***Preguntas clave*** para aterrizar el ***problema de aprendizaje supervisado***:
- ¿De qué tipo es el valor que se quiere predecir?

1. Continuo
2. Discreto

- ¿Cuál es la definición de éxito en una predicción?
- ¿Con qué datos se contaría para hacer esa predicción?
- ¿La pregunta que se está tratando de resolver pertenece a alguna disciplina en particular?
- Considerando nuestra intuición en la disciplina ¿los tatos nos permiten predecir el objetivo?

--- Descargar archivo ---

# Predecir el ingreso de películas de IMDB

Contexto: Somos un ene gubernamental que quiere definir sus políticas de financiamiento de producciones cinematográficas nacionales.

**Reconoce el tipo de aprendizaje que necesitas**

Respondiendo preguntas:

¿Valor que queremos aportar?
1. **Ayudar** a la producción de películas de calidad **que no logran ser autosustentables**

¿Qué funcionalidad podría aportarnos el valor?
2. Nos sería útil saber que películas tienen más dificultad para recuperar en sus presupuestos. Por consiguiente queremos **predeci una métrica**: El ingreso mundial generado por una película.

***Aterriza tu problema de aprendizaje supervisado***
1. Los ingresos de una película conrresponden a ***valores continuos***
2. Mi éxito será ***"qué tan cerca estoy del valor real de ingreso generado por la película"***
3. Me basaré en ***bases de datos públicas de internet***
4. El dominio de trabajo es la ***industria del cine***, en particular de la distribución de películas
5. Sí, de forma general existen bastantes características que me pueden ayudar a saber qué película será exitosa como: ***calidad, actores, presupuesto, etc***


***En resumen***
- Quiero ingresos de películas, para tomar mejores decisiones de financiamiento, con base a una regresión sobre datos de películas extraídos de internet.
- Mi evaluación del éxito será la precisión de mis predicciones.
- Podré apoyarme en conocimientos específicos de de industria.

***Comunicarnos con personas especialistas en la industria para obtener referencias***

# Terminología de Machine Learning
- Líneas: Ejemplos
- Columna: Feature (características, aquí está el arteen ML)
- Cantidad de columnas: Dimensión de los daos
- Output de un algoritmo de ML: Modelo

# Ciclo de Machine Learning
Muchas veces pensamos que hacer ***Machine Learning*** corresponde solamente a implementar un algoritmo de cualquiera de las librerías y con ello ya existe la solución al problema. Pero en realidad existe todo un ciclo de trabajo donde los algoritmos de ***Machine Learning*** son solo una etapa, sin embargo, las demás etapas también son muy importantes y toman su tiempo para lograr los resultados que esperamos.

Hacer ***Machine Learning*** corresponde a trabajar en un ciclo, ir trabajando varias etapas e ir iterando.

***Ciclo de Machine Learning***
- Definición del problema
- Preparación de los datos
- Representación de los datos
- Modelamiento / Algoritmos de ML
- Evaluacion (Que satisfaga las necesidades del negocio, de no ser así repetir el ciclo)

Este no es el final del proceso, se debe iterar hasta que en alguna de las iteraciones salga la solución al problema
- Producción (Fin del proceso)

> La navaja de Ockham o Principio de Parsimonia: La solución más simple casi siempre es la mejor. Comenzar por lo más simple e ir repitiendo el ciclo haciendo el algoritmo más complejo solo si es necesario.

Los features son donde más impacto hay en el rendimiento en Machine Learning

# Configuración del ambiente de trabajo con Docker
Vamos a configurar el ambiente de trabajo con Docker. Aquí se explica el proceso de instalación con Docker

# Construcción de contenedores Docker
***Datos Importantes***
- Los contenedores de Docker son similares a una ballena virtual y se pueden crear de forma automática con DockerFile, que va a crear una imagen y desde esa imagen se generan todos los contenedores que necesitamos.
- ararads - base Es un ambiente típico, muy fácil de usar de librerías PyData.
- Antes de instanciar un contenedor hay que asegurarnos de crear un directorio que se llame vol, esto dentro de la carpeta. Esto es importante porque cada vez que se requiera disponibilizar archivos en el contenedor podamossolo hacer un drag and drop y llevarnos a vol.

La url del Docker File en github es
git clone https://github.com/JuanPabloMF/arara-docker-stacks.git

Entrar en ararads-base
sudo docker build -t base:1.0 .

Creamos un directorio ***vol*** para conectar

sudo docker run -ti --name ambiente-ml -v ~/paltzi-ml/vol:/home/juanpablo/work/vol -p 8889:8888 ds-tf:1.0 start-notebook.sh --NotebookApp.token=''

Si ingresamos en 8889, debemos acceder ya a jupyter

# Qué es y cómo se utiliza Numpy

***Datos importantes***
- ***Numpy*** Es una librería muy importante para el ecosistema de ***Python*** ya que es la base de todos los cálculos científicos y muchas de las librerías de ***Machine Learning***
- ***Scikit-Learn*** Con sus modelos, cuando retorna un resultado, en general lo retorna en un formanto ***Numpy***
- La API ***Numpy*** tiene muchas similitudes con ***Pandas***
- ***Numpy*** Reemplaza de forma más eficiente lo que podría ser un tipo de lista. En las listas podemos tener conjuntos de elementos numéricos. Sin embargo las listas no logran manejar datos de dos dimensiones
- Las listas no poseen métodos que sin prácticos para hacer aritmética.
- Es importante saber que otros lenguajes de programación poseen librerías altamente optimizadas para hacer cálculos numéricos con vectores de datos. ***Numpy*** es esa librería para el lenguaje de programación ***Python***
- np.linspace es una función que permite crear un array de una dimensión de números entre 0 y 1.
- Los ***array*** a diferencia de otros objetos ***Python*** están fuertemente tipificados.Esta tipificación fuerte es necesaria porque es una de las cosas que permite que esta librería sea más rápida que ocupar listas, por ejemplo.

***Instalación del entorno de trabajo***

git clone https://github.com/JuanPabloMF/arara-docker-stacks.git
cd arara-docker-stacks/ararads-base
sudo docker build -t ararads-base:1.0 .
cd ../ararads-tf-cpu
sudo docker build -t ararads-tf-cpu:1.0 .


En nuestra carpeta de trabajo
mkdir vol
sudo docker run -ti --name platzi-ml -v ~/platzi-ml/vol:/home/juanpablo/work/vol -p 9000:8888 ararads-tf-cpu:1.0 start-notebook.sh --NotebookApp.token=''

Entender la creación de Array en Numpy. Tal parece que es muy importante dominar Numpy
- Array de uno o más dimensiones
- Se usa display(variable) para ver el resultado de la variable.
- Comparar arrays => np.array_equal(array1,array2)
- Los que parecen un texto en azul se hace con html

***Creamos las imágenes de Docker y subásmolas a hub.docker.com***

- Operaciones aritméticas con vectores en Numpy.
- Leer a documentación de Numpy y practicar mucho.
- Numpy corre en velocidad en ***C***
- Tratar ocupar funciones nativas de Numpy y no a bucles for para que corra a velocidad de **C**
- Obtener la Media y Mediana con Numpy 

> Al empezar el ciclo lo debemos hacer de la manera más sencilla posible para obtener feedback de los datos y verificar que nuestro algoritmo funcione correctamente.  

# Vamos a resolver el problema como lo haría un Data Scientist en su lugar de trabajo

## Cargar los datos necesarios para el proyecto
- importar las librerías numpy, pandas, maltplotlib, seaborn

## Inspección de los tipos de datos
- La ***inspección de los datos***  se da para tener conocimiento de la salud de los datos que tenemos, saber si vienen limpios o no, y también porque se quiere tener un entendimiento cuantitativo de ellos. Parte de esto es mirar gráficos estadísticos y entender diferentes propiedades numéricas de las columnas.
- A diferencia de Numpy, Pandas no solo permite cargar datos numéricos, sino también datos de texto.
- El método info nos va a mostrar la cantidad completa de columnas con la cantidad de elementos no nulos que ha en esas columnas, y pot último muestra el tipo de cada columna.

## Inspección cuantitativa y de salud de los datos

Se detectó un problema. La BDD fue creada sin diferenciar: 
- La moneda en la que se ingresaba el presupuesto y el ingreso
- La zona del país en la se registró el ingreso

***Es muy común recibir bases de datos con datos falsos***

***La solución es buscar una base de datos con esos valores que nos interesan y mezclarlas***

> Vale más tener ***Datos de calidad*** que tener datos sucios.

> Los datos faltantes generan errores en los algoritmos de Machine Learning

## Limpiar los datos

## Manejo de datos faltanes

## El objeto estimador de Scikit-Learn
***Datos importantes***
- Por como fue diseñado ***Scikit-Learn***, existe una API muy fácil de ocupar y muy unificada. Esta unificación se da por un objeto que se llama *estimador* que tiene en todos los casos y para el algoritmo de Machine que sea, una API que es común y 3 métodos que son clave.
- ***Scikit-Learn*** posee muchos modelos, se pueden implementar tanto, regresiones lineales como regresiones regularizadas, árboles de decisión, SDMs, etc.
- ***Scikit-Learn*** COntiene todos los modelos que son usados hoy en día, y una de las virtudes de esta librería es que sigue muy de cerca lo que pasa en a investigación.
- ***Scikit-Learn*** Es la librería más usada de ***Machine Learning General***, no de ***Machine Learning Especializado***, para ello está la librería de ***Tensor FLow*** y sirve casi exclusivamente para modelos de ***Deep Learning***.

>Para poder escoger el estimador apropiado, una excelente guía es el ***cheatsheet*** siguiente, hecho por uno de los core-dev de scikit-learn. El que lo hizo es el que más aporta a la librería.

![](http://scikit-learn.org/stable/_static/ml_map.png)

## Implementar un modelo de regresión (Lasso)


## Overfitting y Underfitting

Son dos factores que debemos tener muy en cuenta.
- ***Unferfitting*** (Subajuste) Se presenta cuando un modelo no puede capturar la tendencia de los datos. Es generalmente el resultado de un modelo extremadamente simple.
- ***Overfitting*** (Sobreajuste) Se presenta cuando un algoritmo está perfectamente adaptado a los datos con los que lo entrenamos, pero si trataran de predecir nuevos datos, lo más probable es que nos de error.

Para saber si estamos bien, el error de entrenamiento y de test deben ser bajos. También su diferencia.

--- Poner nota de coeficiente de correlación en evaluado modelo---
--- Indicar recomendaciones de R^2 ---

Un buen score R^2 es importante para una regresion. Pero no lo
es todo. De esta forma general los scores hay que complementarlos
con visualizaciones de los datos ya que una métrica no logra
siempre encodear todas las caraceristísticas de una distribució
de probabilidades. Un ejemplo es:

![](http://blog.revolutionanalytics.com/downloads/DataSaurus%20Dozen.gif)

# Feature Engineering

## Feedback del modelamiento
> El diseño de feature puede llegar a ser más importante que la optimización en Machine Learning. Esto es porque al encodear de buena forma nuestro Feature podemos lograr un excelente rendimiento.

Mejorar la performance de nuestros modelos no solo pasa por optimizar sus parámetros.
Una de las partes clave  según algunos expertos la más importante, es la de ***diseñar la representación en la que se entregan los datos a los modelos para que estos los procesen***.
Esto equivale, en palabras más simples, en definir de forma inteligente las features (columnas) de nuestras tablas de datos.

***Ejemplo de feature engineerin***:
El problema:
Supongamos que estamos tratando de resolver el problema siguiente:
- Tenemos un problema de reconocer si ciertos datos con una sola feature son de una clase 1 o de una clase 2 (por ejemplo "el producto está deficiente" o "el producto esta funcional").
- Por tanto estamos resolviendo una ***clasificación***.
- Para esta clasificación decimos tomar un SVM, que es un modelo poderoso que funciona buscando la "mejor" recta que separa los puntos de cada clase.

> Cuando hablamos de ***diseñar feature*** estamos hablando de poder transformar y definir nuevas columnas de nuestra tabla de datos. Recuerden que una ***feature*** en nuestro caso va encodeada en una de las columnas de una tabla de datos X que estamos trabajando.

--- Colocar imagen de clasificación ---

> El diseño de feature no es una ciencia exacta.

### Principios de diseño de Features
Diseñar tus features es un arte más que una ciencia (por lo que en general te recomendamos ganar experiencia leyendo artículos científicos y viendo soluciones:
1. ***Features Informativas***: Tus features son más útiles mientras más correlación tengan tu variable objetivo.
2. ***Features Independientes***: Para no tener redundancias tus features deberían ser lo más independientes posibles entre ellas.
3. ***Cantidad de Features controlada***: Nuestra intuición nos falla en dimensiones superiores a 3 (ver vídeo maldición de la dimensionalidad). En la que mayoría de los casos aumentar a cantidad de features afecta negativamente la performance si no contamos con una gran cantidad de datos. Por último pocas features aseguran una mejor interpretabilidad de los modelos. No usar 100 cuando nuestros datos no son más de 100.

Ejemplo de Feature informativa y Feature no informativa

- Predecir el precio de una casa en función de sus metros cuadrados.
- Predecir el precio de una casa en función de a temperatura del mar.

Es importante entender la correlación entre la feature y la variable objetivo. Más sobre esto en los siguientes vídeos.

***Visualizar interdependencia entre variables***

#### La maldición de la dimensión
> Nuestras intuiciones no funcionan tan bien cuando vamos a una dimensión superior a 3.

Datasaurus Dozen y Anscombe's quartet
Utilidad de la capacidad de entender los datos en 1,2 y 3 dimensiones del ojo humano.

Maldición de la dimensionalidad:
En ***Dimensiń superior o igual a 4***, nuestra capacidad de entender los datos se pierde, ***y aún peor fenómenos extraños/contraproducentes ocurren***

***Ejemplo 1:***
Qué tan largo debe tener cada arista de un hypercubo de dimension p que capture 10% del volumen de un hypercubo de volumen 1 que lo contiene?

> Mientras más crece la dimensión de los datos, más datos necesito para obtener una parte de la información de dichos datos. Esto es para cuando tenemos muchas Features.

> No es bueno manejar muchas dimensiones a menos que tengamos un buen control.

--- Ver Análisis exploratorio cuando lo arreglen ---

## Continuación con el análisis exploratorio
> Uno no se puede fiar de que los datos están limpios

## Métodos de selección automática de feaures
Sklearn posee una series de métodos para seleccionar las mejores features...

Del análisis univariante obtenemos que las mejores fetaures son:
- production_budget
- cast_total_facebook_likes
- budget

### Creación de features
> Una de las formas de crear features es con ***escalamiento de los datos***

Diversos algoritmos son sensibles a la escala en la viene cada feature. ***Re-escalarios*** puede traer significativas mejoras de rendimiento.

Existen distintas estrategias de escalamiento de tus features, pero ***la más común es la estandarización*** donde convertimos la variable para que la distribución de ésta siga una distribución que es Gausaiana de media 0 y de desvicación estándar 1.

### Simplificar las transformaciones con pipelines

> Las regresiones no necesita ***Re-escalamiento***. En Sciket-Learning es más fácil usar ***sklearn.pipeline.make_pipeline***. 

### Creación de features de forma automática
**PolynomialFeatures** transforma una matriz (A1,A2) a (1,A1,A2,A1^2 ,A1 * A2, A2^2)


### Creación de más features
Las features categóricas que tienen una cantidad de valores posibles limitadas. Ejemplo: Género, países... Y transformar en números (label an code) pero tener cuidado entre las distancias en vectores.

Lo mejor es usar Encoding one-hot


### Selección de features y la maldición de la dimensionalidad

***Pirámide de Maslow del Machine Learning***

- Hay un reto aquí

## Modelos y evaluación más avanzada
### Cross Validation
Método de validación para saber qué tan bueno va a ser nuestro modelo

### Selección de modelos
Debemos estar en un punto medio, ni muy complejo ni muy sencillo
Usar la version 0.19 porque tiene una función que usaremos en esta sección

> Busquemos siempre el máximo del score de test. Eso le va a decir cuál es el mejor parámetro para su modelo.

> El modelo usado aquí necesitan más datos para que funcionen.

***¿Cómo solucionar overfitting y el underfitting?***
Varianza alta:
- Conseguir más ejemplos
- Reducir cantidad de features
- Aumentar coeficiente de regularización

Bias alto:
- Más features
- Modelo más complejo

Mal resultado general:
- Probar otro algoritmo/familia de modelos, quizás las hipótesis del modelo (el modelo usado) no son cumplidos por tu dataset. Es decir, estamos usando el modelo incorrecto, las curvas de validación y aprendizaje nos pueden servir para este propósito

### Introducción a Ensembles y Árboles de Decisión
Ensembles es un modelo moderno compuesto de modelos más pequeño, lo que hace es comparar los resultados sus modelos y escoger cuál modelo es el que mejor se adapta.

Hay algoritmos simples y otros todo terreno

> Ver el algoritmo de árbol en el curso de algoritmos

***graphiz*** es una librería basada en C. Sirve para llevarlo a grafos. Nos muestra el algoritmo usando Ensembles en forma de diagrama.

### Random Forest y Gradient Boosting Trees

> Si conocen el sitio web kaggle.com, es un sitio que organiza competencias con premios bastante importantes y con datos reales que vienen de las empresas socias de kaggle.com. En general los que ganan, suelen usar mucho el Random Forest y el Gradient Boosting Trees y luego esos modelos lo usan en Ensembler (Compara diversos modelos y ellos votan, el mejor es el elegido)

Se usa el proceso de baggin¿? 

***Chris Albon*** --> Destacado en la comunidad de Data Science
***Leo Breiman*** --> Creador del Random Forest

Tenemos un score mejor que en Lasso (Random Forest)

En ***Gradient Boosted Trees*** Es más complejo de optimizar que Random Forest, funciona con otro mecanismo en este caso Boosting. Una lógica de ensambla modelos de aprendizaje débil.

Ambos modelos son muy poderosos.

### Optimización de hiperparámetros

- Fijar un learning rate alto
- Fijar parámetros de los árboles
- fijados estos parámetros, elegir el mejor número de estimadores que conforman el ensemble.
- (tarea) Con el learning rate dado y el número de estimadores óptimos optimizar los parámetros de los árboles.

> Hay blogs de expertos que recomiendan qué valore darle a los árboles para que funcionen. Ejemplo GradientBoostingRegressor.

Con todo lo realizado aquí optimizó enormemente el score (R^2)


### Conclusiones

> Es muy importante que vean todos los ejercicios a lo largo de él. Hay mucha información en este curso, manejamos muchas librerías y de forma profesional. Por lo que estos ejercicios les ayudarán a asimilar los conocimientos adquiridos.


***Recursos***
- Reddit /machinelearning y /learnmachinelearning (Preferido del profesor, uno enfocado a los avances en la industria y el otro es más pedagógico.
- Analytics Vidhya y KD Nuggets
- kaggle.com y There is no Free Hunch (es un blog) (Kaggle además de competencias tiene una parte pedagógica. Algunos cuentan sus secretos para optimizar sus algoritmos y ganar las competencias.
- Arxiv, papers -> Publicaciones científicas. Para saber lo que se está haciendo.
- Libros: "Pattern Recognition and Machine Learning" c.Bishop y "Elements of Statiscal Learning".

***Próximos pasos, consejos de cierre***
- Matemáticas
- Praxis: Feature Engineering, Model Selection y Tuning. (Copiar Features que hacen las personas expertas)
- Deep Learning para NLP y Computer Vision. ***Deep Learning*** es mu muy bueno para el reconocimiento de imágenes y reconocimiento de texto.
- Reto: Aprender Machine Learning Bayesiano.

> ***Machine Learning Bayesiano*** es una rama apasionante de Machine Learning donde se ocupa conocimiento experto como el de las Features, pero en este caso para hacer un modelamiento matemático, un modelamiento probabilístico que al final entrega resultados con un rendimiento excelente y el ***Machine Learning Bayesiano*** hoy en día está tratando de abarcar casi todas las áreas y las está reinventando de cierta forma por lo cual es un desafío interesante si quieren llegar un día a ser expertos a nivel mundial en el tema.

***Nos invitó a iniciar discusiones por twitter y a ser parte de la comunidad científica del Machine Learning***


# Recomendaciones del profesor para ser experto en Data Science y Machine Learning
### Pasos:
1. Leer el libro ***Introduction to  Machine Learning with Python*** de Andreas Muller
2. Resolver uno de estos dos problemas en ***Kaggle***
   - Titanic
   - Housing dataset
3. Durante la fase 2 apoyarse en los materiales que recomiendo en el cierre del curso (sobre todo reddit y y blogs)
4. Después de eso ya deberías pasar a temas específicos, como redes neuronales, time series forecast o aprendizaje reforzado

