# Notas del curso

***Big Data*** Es una cantidad masiva de datos que no puede ser procesada por una sola persona.

**Data Scientist** Es la persona que detecta patrones en un conjunto de datos, requiere habilidades de Programación, Estadística y Negocios. Debes ser muy bueno en cada uno de esos tres como lo serían los expertos en cada cambo. Es decir un unicornio.

> Un Data Scientist conoce estadística mejor que todos los programadores.

***Machine Learning*** Es la unión entre programación y estadística y matemáticas.

> ***Data Science*** es ***Machine Learning*** aplicando conocimientos en negocios.

Una de las formas en que se está usando Data Science es la conducción de coches automáticos. Tratan de imitar lo que hace un ser humano en la conducción.

Todo el tema consiste en crear modelos matemáticos con Machine Learning y automatizar el proceso.

### ¿Qué pasa cuando buscas algo en Google?
- ***Input*** Lo que buscas.
- ***Output*** La lista de páginas que Google predice que puede estar relacionado con tu búsqueda en unos milisegundos de trillones de páginas.

Google es más ingeniería que matemática.

### Playlist de Spotify
Es otro logro grande de Data Science, en el que cada semana te presenta una lista de canciones que podrían gustarte. Está construido sus algoritmos de tal forma que puedan predecir tus gustos y preferencias más que las mismas persones.

### Retos de un Data Scientist
Una empresa nos contrata para determinar el por qué sus usuarios se están yendo de la plataforma

- Una semana típica en el trabajo (Este trabajo no toma una semana)
  - Análisis exploratorio: Entender cuáles son los factores y comportamientos.
  - Construir un modelo matemático: Automatizar el proceso de predicción.
  - Construir un sistema para automatizar el modelo: Si el sistema funciona podemos automatizar este proceso.
  - Coordinar con el negocio: Transmitir el valor del trabajo realizado.
  - Explicar los resultados: Comunicar los resultados a las personas relacionadas con los datos (explicarlos de forma muy fácil para que todos nos entiendan).

  Está genial :D

- Un año típico:
  - Desarrollar relaciones con personas en la gerencia (entender el negocio para traducirlo en datos) y obtener los datos que necesitamos. No trabajamos solos.
  - Evangelizar una cultura de datos dentro de la empresa. Debemos estar nuestros argumentos con resultados y hechos, modelos estadísticos, modelos de Machine Learning etc. Todo está basados en números y si no entiendes algo pide ayuda.
  - Construir herramientas para uso interno de la empresa.
  - Construir sistemas y features para usuarios externos. 
  - Construir y mantener sistemas de ingeniería ETL (External Transform Load) Consumir datos externos, filtrar por aquellos que sean útiles y almacenarlos en Base de Datos.

Para ser Data Scientist, es estar siempre leyendo, participando, publicando y dialogando. ***No podemos ser Data Scientist si no estamos integrado en la comunidad de Data Scientist***. Debemos saber lo que está pasando en la comunidad.

### ¿Por qué surge Data Science ahora y no antes?
Existen dos cosas que han permitido esto:
- La gran cantidad de datos cada minuto, estos datos podemos utilizarlos para predecir por medio de estos de datos. ***Mucho de datos*** tipo Everest :D
- El poder de procesamiento de datos está disponible actualmente para todos. Podemos procesar una buena cantidad de datos en nuestra máquina. También tenemos acceso a la nube ***Podemos acceder a múltiples servidores que nos den una cantidad de procesamiento que nos hacen llorar***. Las computadoras más potentes van volviéndose más rápidas y menos caras en la medida que pasan los años.

### ¿En cuáles campos trabajan Data Scientist?
Actualmente todas las industrias buscan dar valor a sus datos y contratar data scientist.

Existen los Data Scientist académicos, se encargan avanzar más el campo desde teórico.

Los Data Scientist de la industria, enriquecer el negocio de las empresas, ganar usuarios, construir features para externos.

> Los ***Data Scientist*** son muy bien tratadas, muy bien pagadas.

***No se necesita PhD*** para trabajar en la industria, lo importante es lo que podamos hacer.

### ¿Cuáles habilidades y herramientas usamos?

***Matemáticas*** Estadística, Machine Learning (Álgebra Lineal), Optimización.

***Ingeniería*** Python, R, Scala. (Si lo hacemos a mano tardaríamos mucho para crear modelos matemáticos con reconocimiento de imágenes). ***R*** No tiene muchas librerías para hacer web Apps. Con ***Python*** podemos crear sistemas. Con ***Scala*** es mucho más rápido que Python por ser compilado. Los ***Data Scientist*** están usando mucho más escala. ***Osmandi*** recuerda, no es solo crear modelos matemáticos, también tenemos que crear aplicaciones con los resultados obtenidos para los clientes externos.

Antes de escribir código deberíamos respondernos:
- ¿Cuál es nuestro objetivo?
- ¿Cuál es la pregunta exacta?
- ¿Cómo definimos el éxito?

Debemos entender lo mejor posible el espacio de trabajo antes de programar. El el profesor dice que es en la parte donde debemos pasar la mayor parte del tiempo o bien conseguir el equilibrio asta sentarnos a programar.

***No debemos sentarnos a programar sin saber bien lo que estamos haciendo***

Los DataSets son datos que conseguimos para estudiar datos, en esta página podemos encontrar muchos:
[Datasets | Kaggle](https://www.kaggle.com/datasets)

### Configurando un NoteBook

Vamos a la carpeta del proyecto, para esto creamos un entorno virtual, para tener las dependencias instaladas solo en este proyecto.

Necesitamos instalar una librería llamada Jupyter y Pandas

Recuerda:
- ***Dataframe*** es una serie de datos organizados en filas y columnas.
- ***Panda Series*** es el tipo de datos de cada columna.

Creamos un entorno virtual:
mkvirtualenv data-science-principiantes

En Archlinux:
virtualenv data-science-principiantes

Para activarlo:
source data-science-principiantes/bin/activate

Para desactivarlo:
deactivate

Ahora ya tenemos un entorno virtual limpio.

Isntalamos librería
pip install jupyter

No me funciona ***pip*** así que instalé jupyter por pacman

Correr jupyter
jupyter notebook

Abrir el archivo de pokemon

El dataset de pokemon es de kaggle.com/dataset

Conn **!** es para interactuar con el notebook en la terminal. 

Shift + Enter para correrlo.

Alt + Enter para crear una nueva línea

"!pip install pandas" para instalar pandas.

"pip para python2 y pip3 para python3"

!ls -> Enlistar los archivos del directorio

dir(data["Total"]) -> Muestra todos los métodos del objeto.

En todo el notebook se usa pandas, debo aprender todas sus posibilidades

> Primero es la pregunta antes del código

Debemos usar un par de librerías:
Matplotlib:
pip install matplotlib
%matplotlib inline -> Para dibujar (ver distribución de los datos en un histograma)

seaborn
Crea visualizaciones informativas (gráficos muy bonitos)
!pip install seaborn

Verificar los valores mínimos y máximos
data['Attack'].min()
data['Attack'].max()

"Aggregation" -> Agrupar datos, y hacer preguntas

Nota: Instalar pandas en la computadora

Con seaborn se hacen cosas muy interesantes con los datos, vale mucho la pena revisar las tres librerías (pandas, seaborn y matploitlib) con más detalle.

### Workflow típico de un Data Scientist
¿Cuál es la probabilidad que un tweet que viene de Colombia contiene la palabra yo?
1 - El primer paso es formular muy bien la pregunta
2 - Una vez definida esta pregunta debemos recopilar datos
3 - Una vez tengamos los datos debemos limpiarlos

***Recueda***:
La ambigüedad no va bien con las computadoras (especificar con coordenadas y datos preciso)

Los espacios geográficos lo establecemos en una caja

***Dormir con tus datos*** Enterarte de forma íntima de lo que está pasando con tus datos.

### Recolectar datos, limpiar datos y dormir con tus datos
Debemos familiarizarnos con los datos, conocerlos y visualizarlos de las formas que sea necesario.

Esta etapa puede incluir:
- Computar estadísticos sumarios
- Crear visualizaciones
- Visualizar la relación de una variable contra otra.

***Dormir con tus datos*** Es hacer todas las visualizaciones posibles con los datos y en la medida que mejor lo hagamos haremos mejores modelos con menores iteraciones. Enterarnos de forma íntima, inspeccionarlos, analizarlos, visualizarlos.

### Modelos de datos
Típicamente construiremos modelos matemáticas para:
***Investigación*** Nos enteraremos de la relación entre un input y output de un sistema. Como no tenemos los recursos para correr todo un día una máquina que esté revisando esto, lo dejamos solo en la mañana porque es más probable.
***Predicción*** Predecir un comportamiento de output de acuerdo a inputs.

¿Cuándo no necesitamos de construir un modelo matemático?
- Datos al azar. ???
- Cantidad de datos. Con 100 observaciones no sabemos todo, pero con 100x10^⁹ sí podemos saberlo todo :D

La limpieza de datos la haremos en local con los 100 datos que tenemos descargados.

### Construir un modelo
- La probabilidad de un número que vive de 0 hasta 1.
- ***Beta distribución***, es cuantificar la incertidumbre de ser la probabilidad subyacente verdadera.
- Visualizamos una tupla, el primero es el valor X y el segundo el valor Y.

Mientras más datos, mejor podemos entender un proceso.

***Buscar información de Beta Distribución***
***Revisar con más detalle del notebook de twitter***

### Validar el modelo y predecir el futuro
Una vez tenemos un modelo construido debemos asegurarnos que este funciona, un método para validar un modelo es la regresión lineal con la cual computando un coeficiente de determinación, este nos dice el porcentaje de a variación de una variable del modelo.

En un modelo que nos muestre la cantidad de medicamento que ha tomado un paciente, para validarlo con regresión lineal el coeficiente tendríamos que multiplicarlo por la variable que es el peso del paciente.

Validando este modelo tendremos la confianza si pasamos otro peso al modelo nos pueda predecir cuánto medicamento debe suministrarse a un paciente.

***Predicción*** Predecir la dosis de medicamento que debería suministrarse.

Vamos a tener el modelo entrenado y con nuevos datos debemos predecir in output con nuevos inputs, para evaluarlo nos oca juzgar su precisión con datos que no fueron usados en el entrenamiento del modelo.

***La confianza que podemos tener al extrapolar la ecuación lienal***

### Comunicar resultados
> Como Data Scientist nos pagan para entender el mundo de una manera matemáticamente más rigurosa que todos los demás. Por ello nos toca comunicar nuestros resultados a otros Data Scientist y quienes no tengan conocimientos del mismo.

> Comunicarse muy bien es algo Santo. Hacer que el dueño de la empresa sienta que ha invertido muy bien la plata que gastó.

Einstein "Si tu no puedes explicar algo de una manera muy simple, no lo entiendes nada bien"

***Investigar Beta Distribution PDF y Beta Distribution CDF***

***Un requisito muy muy importante como Data Scientist*** Saber comunicar lo que he hecho, por eso nos pagan y así somos efectivos en la organización pues con la capacidad de obtener resultados muy importantes e impactantes. Y usarlos en conjunto, pues colaborando con las demás personas de trabajo, del negocio o de la organización en cuestión.

### Hacer que las máquinas hagan todo
Después de construir un modelo matemático no queremos hacerlo funcionar manualmente. Para esto construiremos sistemas para automatizar este proceso, veamos cómo.

> Hasta este punto solo hemos trabajado con dos lados del triángulo, el de matemática y el de negocio. Ahora solo nos falta el de ingeniería.

Básicamente, una vez construimos el modelo matemático no queremos presionar botones toda la noche para hacerlo correr manualmente, entonces para que nosotros podamos trasladarnos a otros problemas del negocio construimos sistemas ingenieriles para automatizar el proceso como codificar problemas de negocio en código y codificarlos a un espacio vectorial.

### Objetos del mundo real en el espacio vectorial y métricas de distancia

***Es más sencillo si ubicamos todas las características en tuplas con los identificadores de los elementos***

Existen varias estrategas para codificar patrones, para esto debemos codificar en términos numéricos, mientras mayor creatividad al construir estos mayor cantidad de patrones  puedes encontrar.

Por ejemplo, si quisiéramos encontrar patrones de las compras en una tienda podríamos tomar el peso, valor, y dimensiones de los productos, peros podríamos ser más creativos.

Podemos medir todos los identificadores únicos de las personas que han comprado el producto en las últimas cuatro semanas, a través de todos los productos solo fueron cinco personas distintas, esto lo representamos en una lista de cinco números (cada persona).

Representarlos con identificadores únicos tanto de productos como clientes, ejemplo 5 números por cada elemento de e-comerce (peso, precio, ...)

De esta forma podemos saber cuántas veces ha sido comprado un producto en un lapso de tiempo definido.

Posibles representaciones:
- Si el producto fue comprado por las personas 1,2,5 tendríamos una lista [1,1,0,0,1]...
- Si representamos qué productos fueron comprados por cada una de as personas tendríamos 5 listas.

Si estas listas las graficamos plano de X y Y, visualizando una lista de tuplas y si lo hacemos con más dimensiones da exactamente igual.

Analizar las gráficas:
Si dos puntos en el gráfico se encuentran juntos uno al otro, esos dos puntos se comportan de una manera similar, si tenemos dos puntos lejanos se comportan de una manera diferente. Esto lo medimos de una escala de 0 a 1, usando las métricas de distancia usando coordenadas del espacio vectorial.

Similaridad entre las distancias de los puntos, los métricos son:

- Distancia de manhattan
- Distancia de jacard
- Distancia de euclidiana
- Distancia cosine

Con estas métricas podemos construir sistemas de recomendación.

### Ejemplo de espacio vectorial y métricas de distancia
Aquí usamos el archivo foursquare_checkins.zip

Un [enlace](https://sites.google.com/site/yangdingqi/home/foursquare-dataset) del data set.

Vamos a construir un sistema de recomendación
Funciones usadas:
- data.unique() -> Vistas únicas
- data.drop_duplicate() -> Remover duplicados
- data[\'checkin\'] = 1 -> Agrega columna con valor 1
- data.shape -> Dimensiones
- set() -> Usuarios únicos

***Recuerda***
La similaridad se puede medir entre la distancia de dos puntos en el espacio vectorial.

Convertir las entidades o atributos a evaluar al espacio vectorial (tuplas) es todo cuestión de creatividad.
