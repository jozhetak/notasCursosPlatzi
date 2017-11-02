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


