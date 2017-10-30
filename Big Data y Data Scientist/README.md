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
