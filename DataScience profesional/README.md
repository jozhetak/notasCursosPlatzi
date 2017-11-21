# Notas del curso profesional de Data Science

En este curso vamos a sumergirnos con más profundidad en el mundo de data science:
- Hablaremos de llevar tus cosas a producción
- Tomaremos prototipos de data science y los convertiremos en sistemas de ingeniería
- Navegar a través de elementos de bases de datos, procesos ETL  paneles de control

Lo siguiente es una visión general de Machine Learning que habla sobre la formación de modelos de Machine Learning:
- Diferencia entre aprendizaje no supervisado y supervisado.
- Regresión, clasificación, reducción de dimensionalidad y agrupasión.
- Modelos canónicos de aprendizaje y cuáles son sus usos.

También tendremos una visión general de estadísticas:
- Variables aleatorias, funciones de distribución de probabilidad.
- Inferencia bayesiana.

Las compartiremos el papel de algunas herramienta de flujo de trabajo de un data scientist cubriendo temas como Git, AWS y línea de comandos.

Y, finalmente, hablaremos de experiencias personales sobre cómo construir equipos de data science y las decisiones que tomamos con ellos.

## Llevar tus cosas a producción
***Llevar tus cosas a producción significa tomar tu solución y construirle un sistema de ingeniería*** de modo que podamos olvidarlo e irnos a dormir o trabajar en un problema mejor.

### Pongamos de ejemplo a Spotify
Imagina registrar semanalmente tu playlist de "Descubrimiento Semanal" en ***Spotify*** y clasificar esas preducciones en tu dispositivo. Mediante un cuaderno interactivo construiríamos un modelo matemático que consumiría la actividad que el usuario tiene en la plataforma, es decir, las canciones que ha escuchado, y, a partir de esa actividad, genera recomendaciones de otras canciones que también podría disfrutar. Así que este es en gran medida un problema matemático de ***Machine Learning****.

Todo es un largo proceso el que atravesamos para hacer un prototipo en un cuaderno interactivo y en teoría podemos hacerlo con lápiz y papel, pero de manera más práctca, lo hacemos en un cuadrno interactivo de jupyter,un entorno interactivo de desarrollo.

La brecha entre tener resultados que nos gustan y realmente entregar esas playlist en una forma agradable y consumible a todos los dispositivos de los usuarios de Spotify es bastante grande.

Cuanto mejor entiendas un modelo matemático que estás llevando a producción, mejor será el sistema de producción que puedas crear. Si entiendes cómo funciona el algoitmo que, por ejemplo, está registrando las recomendaciones de Spotify, si entiendes sus posibilidades, su capacidad para ser parelilzado en diferentes servidores, etc. Ese sistema de inageniería que puedas construir a su alrededor sera ***mejor***

No tienes que hacerlo como todo data scientist, pero sí lo suficiente para guiar a tu equipode ingeniería a llevar a cabo esto. Y esto es lo que significa "llevar tus cosas a producción", ***construir un sistema de ingeniería a partir de tu solución de data science***

## Bases de datos SQL o NoSQL

Cuando hablamos de bases de datos hablamos de almacenes de datos SQL o almacenes NoSQL

Un almacén SQL se ocupa de datos más estructurados, así que cuando hablamos de escribir datos en una base de datos hablamos de registros. En realidad un registro es cad cosa que ha pasado.

Por el contrario, una base de dato NoSQL no tiene la misma estructura implícita. De modo que cada regisro podría contener o no cosas diferentes.

Al hablar de bases de datos SQL hablamos acerca de SQLite, MySQL, PostgreSQL y Redshift.

Al hablar de NoSQL vemos MongoDB, que es un almacén de datos para documentos, Redis, un alamcén clave-valor y tanto Giraph como Neo4j son bases de datos gráficas.

Así que, al escoger una base de datos tenemos que hacernos algunas preguntas:
- ¿Qué tipo de consultas haremos sobre estas bases de atos?
- ¿Le estaremos pidiendo a nuestra base de datos pedazos grandes y planos de datos?
- ¿Estaremos haciendo un montón de agregaciones como suma, media o máximo al momento de la consulta?
- ¿O Estaremos escribiendo sobre esta base de datos más que leyendo sobre ella?

Así que l escoger una base de datos, cada situación es diferente. Tu problema tiene diferentes necesidas que el problema de alguien más.

Así que en realidad, para bases de datos, no existe una "talla única".

Usaremos SQL y NoSQL. SQLite es usada para hacer prototipos.

> No tenerle miedo a las diferencias entre bases de datos SQL

## ETL

***ETL*** Es una sigla en inglés para "Extraer, Transformar y Cargar".

Por ejemplo, un proceso ETL podría consumir datos que se generaron en las cabinas de votación en la ciudad de Nueva York, así que quizás cada registro en estos datos en bruto contiene 50 campos diferentes acerca de ese voto. Pero realmente solo nos interesan cuatro campos (nombre, edad, partido político)

Así que quizás nos enganchamos a una APIde esta cabina de votación, extraemos los datos en bruto, y, por supuesto, esa es la fase ***E, "Extraer"***, de ETL.

La siguiente es transformar, así que estos 50 campos podríamos decir: "OK, solo queremos, solo nos interesna cuatro de ellos, el nombre del votante, su edad, su partido político, y, desde luego, por quién votó"

A continuación podemos enviar esto en un formato con elcual vamos a arrojar esos datos a nuestra base de datos. Así que esta es la fase ***T, "Transformar"***. Y finalmente ***"Cargar"***, lo cual implica tomar estos datos y persistirlos en nuestra base de datos.

***Así que, al hablar de ETL y qué tanto hacemos en la labor de llevar nuestras cosas a producción***

Cuando creamos modelos matemátcos queremos datos limpios, datos actuales, y lamanera de obtenerlos es construyendo procesos ETL que efectivamente nos lo traigan.

Nuevamente, como organización estamos tratando con una gran cantidad de datos que vienen de afuera y tomamos esos datos, los transformamos y luego los almacenamos para usarlos como data scientist.

Así que hasta ahora hemos hablado de los procesos ETL como nuestro brazo hacia el mundo exterior.

Como data scientists nos encontramos escribiendo un buen número de procesos ETL, esta no es la parte sexy del trabajo, esta es la parte del trabajo que a las personas, digamos, les emociona menos hacer.

Sin embargo, tener datos limpio para tus modelos de machine learning, quiero decir, es más que indispensable. Con malos datos, ya sabes, hay un dicho en Machine Learning que dice:

> ***"Si entra basura, sale basura"***

Si alimentamos datos basura nustros modelos de machine learning nos vamos a ser muy eficaces en nuestro trabajo.

Así que, de nuevo, la comunidad detrás de cada marco es u factor muy impotante al hacer una decisión realmente inteligente para nuestra organización.

### Frameworks populares de ETL
- AWS Data pipeline -> Amazon
- Luigi -> Spotify
- Airflow -> Pinterest
- Pinball -> Pinterest

S3 -> "Super Simple Storage"

> Vas a tener problemas al principio con estos frameworks, pero la comunidad puede ayudarte.

## Mostrar tus datos mediante dashboards

Creo que todos sabes qué es un panel de control. Cuandohablamos de llevar nuestras cosas a producción, la brecha entre tener una solución que nos gusta, en un cuaderno interactivo de desarrollo, y crear ese panel de cntrol, el paso en el medio es en realidad llevar tus cosas a producción.

La creación de paneles de control es solo poner una especie de agradable capa visual encima de eso, una capa que hace muy fácil consumir el trabajo que acabamos de llevar a producción.

Hay varias grandes razones para usar paneles de control.

- La primera es la inteligencia empresarial intena. Estos pueden mostrar cosas como tiempo de actividad del servidor, pueden mostrar cosas como disponibilidad en atención al cliente.

- Otra razón es reducir la carga cognitiva, las fotos son bonitas y simplifican las cosas. Simplemente, como data scientists, eliminar la necesidad de escribir una consulta SQL cada vez que queremos una cierta información es realmente un gran triunfo.

Muchas organizaciones de data science, en especial las más jóvenes, están en la fase en la que otros departamenteos que tienen dudas acerca de los datos de su compañíales envían correos diciendo "oye, ¿puedes escribir una consulta SQL?, porque no sé cómo hacerlo yo." eso no es nada escalable.

> Para un Data Scientist no es una manera eficiente de usar su tiempo

De hecho un panel de control es algo bastante simple. Y muchas personas han creado excelentes infraestructuras para paneles de control algunas son un poco diferentes, algunas son más para producción, algunas son más para orototipos, algo que ctas díade por medio como data scientist. De nuevo, reducr la carga cognitiva, tener la capacidad de ver las cosas gráficamente y, en cierto modo, atar un lindo lazo a tu trabajo realmente hace más fácil enfocarse en otras cosas en problemas que aún no has resuelto.

Así que construir tu propio panel de control, al menos desde ceros, muy probablemente es una pésima idea.

> La capa visual es el panel de control o dashboard

***Looker*** Es una capa delgada de visualización encima de una base de datos PostgreSQL. Es una forma de hacer consultas SQL de PostgreSQL de forma gráfica. Ideal para dejarla en producción de nuestro clientes para que  no nos pidan consultas SQL:

- Nos da una visualización de los datos
- También nos da una interfaz gráfica muy fácil de usar.

> Looker es una herramienta estupenda, ante la experiencia del profesor.

> Construir tu propio panel de control desde cero, probablemente sea una mala idea.

## Repaso por jupyter notebook

Los prototipos de data sciencea menudo nos encontramos utilizando cuadernos interactivo. Estos cuadernos interactivos nos permiten ejecutar código, sin ningún orden en particular. ***Lo que es muy bueno porque el proceso de construir soluciones de data science es a menudo muy iterativo***

En el caso puntual de python usamos un notebook llamado jupyter. Desde la terminal ejecutamos:

```
pip install jupyter
```

Una vez instalado, podemos ejecutar jupyter con:
```
jupyter notebook
```

Es realmente importante entender que Jupyter, de hecho el proyecto Jupyter, esta librería agnóstica al lenguaje. Es decir, podemos usarla con una gran variedad de lenguajes.

Entonces dsde un cuaderno interactivo, podemos cargar datos y podemos inspeccionar esos datos. Podemos crear visualizaciones en línea, por supuesto podemos estas celdas fuera de orden también. Como data scientistesto podría sonar muy natural de hecho, tener este ambiente de trabajo interactivo, flexible, iterativo.

Para algunos ingenieros de software de hecho esta herramienta les parece muy distante, para muchos ingenieros de software donde escribimos scripts, estamos escribiendo código que ejecutamos continuamente, es decir, escribimos algo de código, y ejecutamos el script entero,entonces no tenemos la opción o incluso la noción de ser capaces de ejecutar tan fácil eses script, de alguna forma sin orden, ejecutando la primear línea y luego la cuarta y la tercera, porque lo escribimos como tal para que funcione con cierta cronología.

Si no usas Jupyter existen otras opciones, Rodeo es una, Zeppelin es otra. Lo importante es que explores otrasopiones y nos cuentes como te ha ido.

> La ventaja de un notebook como Jupyter es poder ejecutar iterativamente cierto código sin ejecutar todo el escript completo como si lo hiciéramos por script.

## Ejemplo de inferencia en twitter para producción

***Problema*** Vamos a hacer la pregunta: "¿Cuál es la probabilidad de que un determinado tweet originado en Colombia contnga la palabra 'yo'?"

Vamos a examinar todo el flujo de trabajo de data science: Recoger datos, a continuación limpiarlos, crear un modelo matemático, inspeccionar los resultados, hacer preguntas sobre esos resultados, etc.

- Lo primero que haremos es crear un entorno virtual para mantener nuestro proecto aislado de otros proyectos que tenemos en este equipo.
- Jupyter es un paquete de Python que instalaremos. Lo primero que vamos a hacer es instalar con pip todos estos requisitos de modo que las bibliotecas en el ejemplo de efecto funcionen porque estarán en nuestro equipo.
- La primera biblioteca que usamos es tweepy, Tweep es una forma de interacuar con la API de Twitter. Una API es, digamos una cosa de la que recogemos datos, al menos para este ejemplo en particular.
- Como saben, los tweets pueden contener un monton de basura, emoticones, pueden contener enlaces, puntuación, etc,etc. Para nuestro ejemplo todo lo que nos importa es la palabra "yo". No nos importa si tiene acentos o no y no nos importa si está en mayúsuclas, minúsculas, etc. Así que recorreremos algunos pasos para normalizar nuestros datos y que sea más fácil trabajar con ellos.
- Lo segundo, y lo último que vamos a hacer al recibir un tweet, es guardarlo en nuestra base de datos, así que tenemosdos campos en esta base de datos: La cadena de ID, que es un dentificador único para ese tweet, y también tenemos el text de ese tweet.

> Para las personas, ya sabes, que están trabajando en data science y adquiriendo habilidades, practicando, etc, es importante que sepan estas cosas, ya sabes, no se supone que se despierten  las entiendan. No se suponen que despierten y digan: "Ok, para escribir datos en una base de datos definitivamente debo crear un cursor, tengo que ejecutar una sentencia, etc"

Así que, hemos sentado las bases para la recolección y limpieza de los datos, y, finalmente la persistencia de esos datos desde la API de Twitter.

Instalar los requerimientos con
```
sudo pip install -r requeriments.txt
```

***Tweepy*** Librería para interactuar con la API de Twitter en Python.

 Guardamos los resultados obtenidos en una bases de datos local

 En la documentación de Twitter está la información para usar su API.

 El "_" al inicio de una función o variable es para indicar a otros desarrolladores que no debe usarse fuera de la instancia. Es una convención.

> "Es importante que sepan estas cosas, ya sabes, no se supone que se despierten y las entiendan. No se supone que despierten y digan: "OK, para escribi datos en una base de datos definitivmente debo crear un cursor tengo que ejecutar una sentencia, etc'. Hacemos estas cosas porque quienes escribieron la documentación nos muestran cómo hacerlo. Y después de un tiempo se vuelve muy natural. Ya sabes, ya no consultamos la documentación, se vuelve algo natural, etc. Pero en un comienzo es importante entender.

## Creando nuestro modelo matemático

Vamos a construir nuestro modelo matemático para responder nuestra pregunta original (***¿Cuál es la probabilidad de que un tweet en Colombia contenga la palabra "YO"?***)

Lo primero que es importante explicar es una distribución beta, una distribución beta es una distribución de probabilidad canónica usada para mostrar incertidumbre alrededor de cada posible probabilidad, una probablidad por supuesto siendo un número entre 0 y 1, siendo la verdader probabilidad del proceso.

Entonces entremos a esto un poco más, de nuevo la pregunta es:

***¿Cuál es la probabilidad de que un tweet dado en Colombia contenga la palabra "yo"?***

Entonces la respuesta va a ser un número entre 0 y 1 por definición de lo que es una probabilidad y esta distribución de probabilidad es una distribución beta es efectivamente una tabla de consulta para los datos dados que hemos observado y por supuesto limpiada y persistida, etc.

Una distribución beta es una función que oma dos parámetros, el primero es alpha y el segundo beta, entonces para interpretar una distribución beta vemos la altura de la curva y la altura de la curva es proporcional a la probabilidad de dibujar el valor por debao de él en el eje x.

--- Continuar esta clase y automatización ---

# Machine Learning

## Un poco de contexto sobre machine learning
Ya hemos hecho bastante de data science en este curso sin tocar realmente machine learning y para muchas personas esto puede parecer muy extraño.

***Machine Learning*** es muy importante. Pero lo más importante que debemos entender acerca de machine learning es que ya sabes, debemos formular los problemas de una forma que pueda ser pasada a los modelos de machine learning para interpretar.

Y que la formulación de problemas realemente es la habilidad en data science que toma el mayor tiempo para perfeccionar, el mayor tiempo para desarrollar.

Los modelos de machine learning normalmente, sin importar el tipo, se crean para dos fines:

- El primero es I&D, Investigación y Desarrollo
- El segundo fin es la predicción.

Pero en muchos casos, en la práctica, hay una serie de delgada línea entre ¿sabes qué? si de verdad funciona bien en estas situaciones de, digamos, predicción multiclase o lo que sea es lgo con lo que en cierto modo estamos de acuerdo.

Así que, ¿en qué se diferencian los modelos de machine learning de los modelos estadísticos tradicionales?

En la mayoría de los casos, un modelo estadístico se efectúa tomando en cuenta un comportamiento previo, en el caso de un modelo de machine learning podemos llegar sin nada, aunque la respuesta puede ser menos acertada, es por eso que hablamos en esta parde de investigación y predicción.

Leer artículo de "Doctor Breiman" titulaod "The Two culures". Trata de las diferencias entre modelos matemáticos y modelos de machine learning. El construyó el modelo ***Random Forest***

Los modelos de ***Machine learning*** funcionan porque tenemos muchos datos y el poder de cómputo para procesarlos.

## Entrenando un modelo de Machine Learning

Machine Learning es el proceso de enseñarles a las computadoras a entender patrones en los datos, destinado a imitar ese proceso de cómo los humanos: "Nosotros intuimos patrones en los datos y luego entendendemos esos patrones, y hacemos predicciones"

***El ejemplo al que más cariño le tengo de hecho es el de un radiólogo***

Quién busca en los rayos X y dice, bien estos rayos X muestran un tumor, y el otro de hecho no tienen un tumor.

Y entonces como humanos ¿cómo hacemos esto? ¿Cómo un radiólo interpreta esto?

Y la forma en la que lo hacemos es viendo rayos X, consultando con expertos, y diciendo: "OK,aquí hay unos rayos X" y el experto dice: "este es un tumor", aquí hay otros y el experto dice: "estos no tienen un tumor" Y conforme pasa el tiempo como radiólogos aprenden, cad día, viendo nuevos datos, nuevos ejemplos.

Y comenzamos a entender los patrones más y más, mejor y mejor.

Lo primero que entender sobre modelos de machine learning s que ellos realmente están haciendo lo mismo. Ellos están tomando esa imagen insertada con una etiqueta, y están entendiendo, intuyendo, descubriendo patrones en esa imagen, que relaciona las diferentes cosas que están presentes o no en esaimagen, con la pregunta: ¿Tenemos un tumor presente o no?

Y las diferencias fundamentales entre un humano y un modelo de machine learning son esas dos cosas que he mencionado antes, la cantidad de datos que ese modelo puede recibir y la velocidad a la que el modelo puede consumir esos datos.

¿Cómo tomamos una foto y la cuantificamos o codificamos en números? Una sobre las maneras ***canócicas*** de hacer esto, es que una fto no es nada más que un conjunto de píxeles, y cada pixel tiene un valor numérico que describe el color de ese pixel.

***Otro tipo de modelo de machine learning son los que se llaman modelos no supervisados***

Por ejemplo como niño, ya sabes, si te pegas con algo y duele, lo que no pasí aquí es alguien diciendo:

**"Si te pegas con esto, si haces esta acción, va a doler"**

Entonces estos modelos no supervisados, la diferencia fundamental en términos matemáticos es el vector de etuquetas atadas a nuestros ejemplos. Pero aún podemos pasar ejemplos a un modelo de machine learning, y hacer que hasta cierto punto entienda la structura en este modelo.

Tenemos muchos algoritmos de ***Machine Learning*** y separando un poco:

- Regresión y clasificación serán modelos supervisados
- Agrupamiento y reducción de dimensionalidad serán modelos no supervisados.

Con Machine learning podemos procesar más datos.

Los modelos no supervisados son: Agrupamiento y reducción de dimensionalidad.

Los modelos supervisados son de regresión.

## Modelos de regresión, clasificación, clustering y reducción de dimensionalidad

### Regresión
***Los modelos de regresión que predicen valores continuos***
Entonces, por ejemplo, un modelo de regresión podría predecir el número de minutos que el TransMilenio, que es el transporte público aquí en Bogotá, estaría retrasado en una determinada parada en un día determinado; podría predecir el número de votante que una cabina de votación en Minneapolis necesitaría albergar; o podría predecir el número de pulgadas de lluvia que el desierto de Atacama recibiría el próximo año.

Y los modelos de regresión, por supuesto, son algoritmos de aprendizaje supervisado.

Así los modelos de regresión, por supuesto, son algoritmos de aprendizaje supervisado.

Así que le alimentamos a estos modelos ejemplos que tienen, ya sabes, algún ejemplo codificado en el espacio vectorial.

### Clasificación
Los modelos de clasificación predicen una etiqueta. Esto podría ser binaria en el caso del ejemplo de Twitter. "Si, mi tweet contiene esta palabra clave" o "no, no la contiene"

Podría ser: "¿Quién ganaría las elecciones presidenciales de los Estados Unidos? ¿Hillary o Trump?

"Lo que por supuesto es un problema de clasificación binaria."

### Algoritmos de agrupamiento
El agrupamiento se usa a menudo como un paso exploratorio en el análisis de datos. Y por supuesto, este es un tipo de ***algoritmo de machine learning no supervisado***

Un ejemplo es agrupar canciones en Spotify codificadas como datos de frecuencia, mejor, datos de frecuencia de audio.

¿Cuántos tipos diferentes de canciones tenemos aproximadamente?

Es una canción alegre, canciones lentas, canciones con bajo, etc. Quizás tomamos esto com un paso exploratorio antes de aplicar etiquetas a cada canción de Spotify. De modo que quizás Sopitfy podría tener una pestaña de géneros donde dicen: "Puedes ordenar tu música por el tipo de género en el que cae"

Para algoritmos de agrupamiento hacemos una distinción entre verdaderos algoritmos de agrupamiento y algoritmos de partición:

- Un algoritmo de partición pone cada punto que tenemos dentro de algún grupo. Básicamente hace una partición de nuestros datos, divide nuestros datos, estratifica nuestros datos dentro de grupos distintos.
- Un algoritmo de agrupamiento aplica alguna lógica por a cual solo está poniendo un punto dentro de un grupo si pasa ciertos criterios. Y posiblemente, si no lo hace, lo está dejando completamente por fuera.

### Reducción de dimensionalidad
Finalmente hablaremos de algoritmos de reducción de dimensionalidad. Que es reducir un conjunto de vectores desde una cierta alta dimensionalidad hasta una baja dimensionalidad.

- El primero es visualización:
    En dos dimensiones es muy fácil ¿verdad? Si nuestos datos, tienen dos dimensiones los ponemos en un plano x-y. Quizás tenemos un grupo por acá, un grupo por acá. Quizás vemos cómo diferentes valores varían entre sí, a medida que un valo sube, normalemnte otro baja, etc, etc. En 20,000 dimensines en teoría podemos hacerlo, es decir, del mismo modo en que podemos construir visualizaciones en dos dimensiones. El punto es que el espaco de 20,000 dimensiones existe, justo como el espacio en dos dimensiones. Pero como humanos en realdad estamos lmitados por nuestra propia intuición, nuesra propia capacidad de mirar fotos y entender lo que realmente nos están diciendo.
    Como humanos, el espacio en dos dimensiones tiene sentido para nosotros.

- La segunda el costo computacional:
    Debido a que somos capaces de capitalizar la redundancia en nuestros datos y proyectar esos datos desde un espacio dimensional mayo y hasta un espacio dimesional menor sin perder las diferencias entre los puntos de datos. De nuevo, podemos representar nuestros datos en un espacio dimensional menor. Y cuando pasamos estos vectores más pequeños a algoritmos de machine learning por spuesto cuanta menor es la dimensión en la que residen nuestros datos más rapidamente pueden trabajar nuestros algoritmos.

Algoritmo de k-means y clustering. Dormir con tus datos.

Hay un algoritmo de dimensionalidad llamad t-SNE (Distributed Stochastic Neighbors Embedding. También PCA. Todos esos son algoritmos de dimensionaldad.

### Modelos canónicos y para qué los usamos
Averiguar qué modelo funciona mejor en qué situación es 100% cuestión de práctica. Por supuesto existen criterios de orientación. Pero participar en competencias de modelos predictivos,
leer publicaciones de blogs, y hacer estas cosas en el trabajo simplemente viendo cómo se desarrollan son realmente los únicos pasos para obtener esta intuición.
Regresión Lineal
Los modelos de regresión lineal deben usarse en casos en los que creemos que existe una relación lineal entre cada una de nuestras características, de nuestras entradas, las cuales son sinónimos, y nuestra salida.
Sí, que nuestros datos de hecho se ajustan a una tendencia lineal, por lo tanto:
No tan poderoso
Por esta razón, en casos de tareas de regresión, se supone que es uno de los primeros modelos que pruebes, sólo como un punto de partida.
Maquinas de Vectores de soporte
Este es normalmente un algoritmo de clasificación, pero también tiene varianza, de modo que puede ser usado para regresión.
Lo que hacen las máquinas de vectores de soporte es hallar el llamado “hiperplano de máxima separación” para dos clases de puntos en un espacio de n dimensiones.
Entonces, si graficamos nuestros puntos, si visualizamos nuestros datos y observamos una separación lineal entre estos datos entonces las máquinas de vectores de soporte probablemente son un algoritmo que querremos explorar.
Random Forest.
Random forest es en realidad nuestro primer algoritmo no lineal en este conjunto.
Y lo que hace, lo que eso significa es que si existen relaciones no lineales entre cada una de nuestras entradas y nuestras salidas un random forest puede descubrir esos patrones mucho mejor de lo que lo haría un modelo de regresión.
Los random forest ajustan no sólo un árbol de decisión sino una gran cantidad de árboles de decisión. Y realmente hacen esto en una especie de forma no intuitiva, de hecho. Debido a que en lugar de ajustar cada árbol de decisión en todos los datos es decir, todas las filas, todos nuestros ejemplos, así como todas las características, lo que hacen en cambio es ajustar esos árboles de decisión, cada uno, en un subconjunto aleatorio de las filas y un subconjunto aleatorio de las columnas.
Los modelos de random forest también introducen este concepto muy interesante, muy divertido
en machine learning que es el de agrupación. La idea es que, en lugar de ajustar un árbol de decisión, ajustar muchos débiles y promediar sus votos.
Redes Neuronales
Las redes neuronales no son un algoritmo nuevo. Es algo que ha existido por aproximadamente 75 años. La razón por la que ahora funcionan tan bien son las cantidades masivas de datos, con los cuales entrenar estas redes, que generamos, y también los recursos de cómputo que tenemos fácilmente disponibles con los cuales procesar los datos ya mencionados.
El otro punto para aclarar también es cuando hablamos acerca de aprendizaje profundo, El aprendizaje profundo es casi un sinónimo de redes neuronales.
Las redes neuronales son normalmente cosas que tienen capas escondidas entre ellas
y aprendizaje profundo hace referencia a una red neuronal con muchas capas escondidas, que son una red profunda.
Empleamos redes neuronales profundas para entrenarse en lotes grandes de imágenes, audio, video.
Así que para hacer esto en un marco de tiempo razonable y haciendo uso de esto del hardware especializado, de nuevo, la tarea de ingeniería es bastante pesada.

---

> ***Modelos canónicos***

Las competencias de kaggle.com es un buen lugar para obtener práctica. 

> ***Ramdon Forest***

> ***Scikit learning***

> ***Transformation kernel***

> ***Aloritmo de Breiman***

> ***Agrupación***

> ***Redes neuronales***

> Un Data Scientist propuso un día usar GPUs, actualmente NVIDIA produce tarjetas gráficas exclusivas para redes neuronales. También Google las produce con tensor.

### Más modelos canónicos
La vectorización de ese modelo de negocios realmente es el primer paso para poder hacerle un modelo predictivo.
De nuevo, ¿sabes? personalmente tengo esta creencia de que muchas de las entidades del mundo real, las personas en un nivel emocional y nuestras interacciones en el mundo, pueden ser codificadas en números, pueden ser codificadas en términos matemáticos y esto es de lo que se trata realmente convertir cosas en vectores.
También hemos hablado sobre codificar imágenes, video, etc. en espacio vectorial, hablamos sobre que cada imágen tendrá diferentes pixeles, cada pixel tendrá un valor para el color que este toma, y al convertir estos valores en una gran lista, en un gran vector, los números que de nuevo, existen cómo un punto en largo espacio de n dimensiones. Y lo que hemos hecho es codificar esa entidad del mundo real en números.
Y entonces conforme progresas en Machine Learning vas encontrando formas cada vez más creativas de hacerlo.
Vamos a hacer este proceso en un ejemplo en breve, digamos que para nuestra tarea de predicción para predecir el número de mililitros de medicamento a administrar en un hospital.
Tenemos cien diferentes pacientes, y cada uno existe en el espacio tridimensional, lo que significa que tienen 3 características. Así que nuestro set de entrenamiento, nuestra matriz de entrenamiento va a ser de (100 x 3) va a tener cien filas y tres columnas.
A continuación tenemos un vector de respuestas, de el número de mililitros que históricamente, ha sido administrado a cada uno de estos pacientes. Y entonces, nuestro set de entrenamiento de (100 x 3) y nuestro vector, el cual efectivamente tiene cien diferentes columnas si quieres pensar verticalmente, y una sola columna.
Una vez que codificamos las cosas al espacio vectorial, para poder pasarlas a nuestro modelo de Machine Learning, así es como nuestra data se tiene que ver.
Cuando construimos modelos de machine learning todo es un “hiper parámetro” en otras palabras todo es una perilla que puedes girar o no girar.
Desde las características que creas para tus datos, para los modelos que eliges, para los hiper parámetros con los que parametrizas esos modelos.

---

Los puntos viven en un espacio dimensional, cada dimensión es un atributo.

En Machine learning todo es un parámetro

> Debemos implementar nuestra propia métrica de error.

> Se usan derivadas de las funciones como una métrica de error.

> Classification: F1-Score, Logistc Loss, Accuracy, AUC ROC.

> K-Fold -> Cross Validation (Dividir la data en lotes y en cada lote 90% entrenamiento y 10% validación)

> Regresión: Mean Squared Error, Mean Average Error, Mean Absolute Error.

> Es verdaderamente importante configurar tu flujo para ser muy iterativo, para poder hacer iteraciones rápido. Porque sino, esto se vuelve frustrante... las cosas se atascan, muy rápido, muy fácilmente.

> Cross validation.

> No es recomendable construir tus modelos de Machine Learning desde el inicio. Existen software que tienen estos modelos preconstruidos para ti.

> Construir los algoritmos manualmente desde cero es una increíble forma de aprender. Por supuesto en machine learning al igual que en ingeniería de software construimos capas de abstracción sobre las cosas.

> No necesitamos saber cómo funcionan los algoritmos de machine learning para usarlos. Pero mientras mejor entenderemos qué está pasando bajo el capó de nuestros modelos de machine learning, mejor podemos hacer mejoras, corregir errores...

## Itera rápido o muere lento
Somos data scientists y también somos ingenieros de software. Tenemos que implementar estos modelos en código. Así que hay un elemento muy práctico para hacer esto:
“Itera Rápidamente o Muere Lentamente”
Invertir tiempo en suavizar tu flujo de trabajo por adelantado es realmente importante. Es la diferencia entre ajustar modelos geniales y tener resultados estupendos, y quizás solamente, ya sabes, juguetear con tres o cuatro
Generalmente no es recomendable crear tus propios modelos de machine learning desde cero.
En lenguajes que son populares para data science, por ejemplo Python, por ejemplo R, existen paquetes de software que tienen estos modelos pre-construidos para ti.
Por supuesto en machine learning como en ingeniería de software construimos capas de abstracción encima de las cosas. Así que, por ejemplo, otro profesor de Platzi el otro día estaba dando un gran ejemplo sobre manejar un auto y cómo se relaciona con la ingeniería de software.Como desarrollador de software, como data scientist, podrías programar,
ya sabes, alguien que presione el pedal de ese carro.Y, dado que el pedal es presionado, ese auto empezará a moverse.
Sin embargo, para crear un programa que usa ese pedal, que interactúa con ese pedal
y crear un programa que funcione no necesariamente tienes que saber lo que está pasando bajo el capó de ese auto. Y esto es lo que se llama una "capa de abstracción "
Sin embargo, cuanto mejor entendamos ese carro, mejor entendamos lo que está pasando bajo el capó de nuestros modelos de machine learning, mejor podremos usarlos, y serán, digamos, más intuitivos los cambios que podamos hacerles y más íntimamente entenderemos por qué están actuando de la manera en que actúan.
No podemos impedir que alguien implemente sus propios algoritmos. Pero al construir sistemas de producción, en la mayoría de los casos un algoritmo pre-construido en una biblioteca como scikit-learn, en bibliotecas en R, es probablemente suficiente para tus necesidades.

> Iterate Quickly, or Die Slowly.

> Hiper parámetros

## Recolectando y limpiando nuestros datos. Aquí crearemos un modelo de Machine Learning
La idea es es crear un modelo de machine learning para detectar insultos en redes sociales.
Entonces tenemos al favorito de todos: Donald J. Trump.
Vamos a usar machine learning para hacer esto. Este va a ser un problema de aprendizaje supervisado. Vamos a tomar datos que hemos recogido previamente, cada uno es un comentario en una red social, y tiene una etiqueta vinculada. Y por supuesto esta es una tarea de aprendizaje supervisado.
En este ejemplo utilizamos varias bibliotecas:
Re, que es la biblioteca de expresiones regulares en Python, y string.
Pandas
Sklearn.
Lo primero que hacemos es cargar nuestros datos. Para hacer esto vamos a usar la función read.csv de pandas. Como nota al pie, el módulo E/S de pandas es fenomenal. Realmente facilita consumir datos desde una variedad de fuentes, intuir el esquema de esos datos, etc.
Antes hablamos de que las relaciones en los datos en muchos casos cambiarán fundamentalmente con el tiempo. Yo no pensaría que decir algo como: “eres estúpido” sería un mayor insulto hoy de lo que habría sido hace cinco años. Y por supuesto podría estar equivocado pero ese es mi propio primer instinto.
Y seguimos por algunos casos puntuales donde podemos inferir que cierto conjunto de palabras son un insulto.
Ahora que hemos recorrido el proceso de cargar nuestros datos, limpiar nuestros datos, inspeccionar nuestros datos y visualizar nuestros datos, estamos listos para empezar a crear modelos, hacer validación cruzada de estos y averiguar qué hiper parámetros nos dan el modelo que mejor predice.

---

Con el algoritmo que vamos a crear es para predecir si un tweet contiene palabras de insulto

> En Jupyter podemos obtener documentación en línea ("librería?") Con el signo ?

> n-grama -> Colección de segmentos de texto (una más de una palabra) bi-gram, tri-gram, etc.

## Implementando nuestros modelos de Machine Learning

Ahora que dividimos nuestros datos de entrenamiento y nuestros datos de validación
para hacer validación cruzada, de nuevo, la idea es imitar el escenario de predicción, para hacernos una idea realista de cómo se desempeñará nuestro modelo al momento de predecir, sin predecir realmente en datos de prueba.
Así que aquí vamos a ajustar un modelo con datos de entrenamiento.
Previamente había dicho que al crear modelos de machine learning probablemente no hagas uno propio, o no, al menos en una situación de producción probablemente no hagas uno propio. La razón es es porque bibliotecas como scikit-learn hacen estos modelos realmente fáciles de usar
y han sido “probados en batalla” por muchas organizaciones a lo largo de muchos años.
De modo que instanciar un modelo de machine learning y ajustar ese modelo en scikit-learn
es realmente tan fácil como lo siguiente:
Son simplemente dos líneas y uno podría haber pensado que sería un montón de trabajo, ajustar estos modelos pero en realidad no lo es.
Un modelo es este objeto LogisticRegression. Tiene muchos parámetros diferentes, todos ellos con valores por defecto.
Así que al ajustar modelos en scikit-learn usar los valores por defecto nunca es una mala idea.
Por supuesto probablemente queremos desviarnos de esos valores en algún punto del proceso.
Pero empezar con lo que scikit-learn pre formula es por lo general una jugada inteligente.

--- 

Debemos dejar variables que sean fáciles de recordar o reconocer a otros programadores.

## Creando y ejecutando nuestro pipeline
Desafortunadamente, como data scientists pasamos la mayoría de nuestro tiempo recolectando datos, limpiando datos, explorando estos datos, haciendo preguntas sobre estos datos, leyendo, pensando y hablando con otras personas.
Construir modelos de machine learning es muy importante y muy divertido, es esta tarea atractiva que todos quieren hacer, pero es desafortunadamente donde pasamos la minoría de nuestro tiempo.
Hemos llegado a la parte del proceso donde comenzamos a construir modelos y comenzamos construyendo muchos.
Así que aquí tendremos en verdad un poco de diversión.
Bien, recuerda de las diapositivas anteriores que “todo es un hiper parámetro.” Desde la forma en la cuál agregamos características los datos hasta el modelo que usamos, hasta cómo combinamos esos modelos, y hasta cómo parametrizamos esas transformaciones de características, etc.

---

> En la creación de nuestros modelos de Machine Learning es la parte más divertida pero donde pasamos menos tiempo

> Random Forest

Recuerda que vamos iterando sobre los parámetros.

En el notebook uno escribe una frase en inglés y el algoritmo va a predecir si es un insulto o no.

# Estadística
## Estadística y su aplicación en Data Science
La estadística es en realidad un lenguaje a través del cual podemos comprender el mundo. Hace dos cosas principales por nosotros:
La primera es que la estadística nos da una manera de cuantificar con precisión y comunicar la incertidumbre. Ésta podría ser incertidumbre acerca de cierto parámetro de un modelo de machine learning hacia otro data scientist, podría ser incertidumbre acerca de cierto proceso de negocios hacia una persona en la dirección.
La estadística también nos da una mejor comprensión de nuestra organización. Y nos permite tomar decisiones más sobrias y auto conscientes en este respecto. Estas decisiones se basan en lo que dicen los datos en lugar de una especie de presentimiento que quizás tuvimos en camino a nuestro trabajo.
Entonces, si alguien viene a nosotros y dice:
¿Cuál es la probabilidad de sacar entre dos y cinco?"
Podemos decir: “bueno, es 1/3 porque los valores entre dos y cinco en el intervalo abierto son tres y cuatro, lo cual abarca dos de nuestros seis valores. Así que, de nuevo, eso nos da 1/3.”
En el mundo real en la mayoría de los casos tenemos exactamente lo contrario:
Observamos datos, así que estamos viendo ese dado. No vemos a la persona que lo lanza,
realmente no sabemos qué es ese dado. Solamente vemos una lista de números, vemos cuatro, cinco, dos, dos, seis, cuatro, tres, uno, etc.
La idea es: cuantos más datos observamos, mejor podemos inferir cuál es el verdadero proceso que genera esos datos.
Para comprender cómo llevar a cabo la inferencia estadística lo primero que debemos entender es qué son las variables aleatorias.
Una variable aleatoria es: "algo que puede tomar muchos valores diferentes."
Una vez más: algo que puede tomar muchos valores diferentes.
Así que algunos ejemplos de algo que puede tomar muchos valores diferentes, podría ser el color de la camisa que personalmente uso los lunes.
De modo que este podría tomar los valores, bueno, para los que me conocen probablemente es gris, o azul, o alguna variación de verde claro.
OK, nuevamente, esa es una variable aleatoria.

---

> Es una manera de cuantificar con precision y comunicar la incertidumbre.

> ***Inferencia*** La espada más brillante de la estadística.

## Distribuciones de probabilidad
Una distribución de probabilidad es realmente una tabla de búsqueda para ver qué tan probable es un resultado. Esos resultados son los valores de una variable aleatoria.
Así que cuando vemos una distribución de probabilidad que parece un montón de bloques
eso es lo que estamos haciendo, es sólo visualizar las probabilidades de observar cada uno de estos eventos.
Las variables aleatorias además pueden ser de 2 tipos:
Continuas: Pueden tomar cualquier valor dentro del espectro de números reales, por ejemplo: al decir entre 4 y 5 años existen los valores: 4.7, 4.9, 4.6242424242, etc.
Discreta: No hay valores intermedios que podamos observar, se pueden ver como "categorías, por ejemplo: decir que tenemos el color azul, verde, rojo, no se puede decir que tengo 0.5 de azul y 0.3 de verde.
Y justo para cada tipo de variable aleatoria tenemos funciones de distribución de probabilidad distintas:
Las funciones de densidad de probabilidad son las funciones de distribución de probabilidad
para variables aleatorias continua.

Las funciones de masa de probabilidad son las funciones de distribución de probabilidad
para variables aleatorias discretas.
Las funciones de densidad de probabilidad nos ofrecen un conjunto de información extremadamente rica sobre el cual basar las decisiones. Desafortunadamente, en el mundo real no se nos dan funciones de distribución de probabilidad.
Así que, lo que la estadística nos permite hacer es observar datos que recogemos en el mundo real y trabajar hacia atrás, tomar esos datos e inferir cuál podría ser la FDP subyacente que generó esos datos.

---

Repasar conceptos básicos de estadística para ingenieros.

> La probabilidad se calcula en el área bajo la curva de una función.

## Inferencia Estadística
Una distribución empírica no es nada más que una representación visual de lo que hemos visto hasta ahora. En cambio, las distribuciones teóricas, son una imagen de lo que realmente está pasando desde el interior hacia afuera.
Y entonces en un caso teórico, pensamos del problema en reversa.
Muchos matemáticos nos nos han dado muchas distribuciones de probabilidad canónicas que,
en teoría, describen el comportamiento de algún tipo de evento dado.
Y entonces, distribuciones exponenciales describen eventos de supervivencia, las distribuciones beta pueden describir giros de monedas, las distribuciones de Poisson describen cosas que toman valores enteros, distribuciones de Dirichlet, distribuciones gama, distribuciones binomiales,
distribuciones de Wishart, etc.

> Distribución empírica

> Repasar estadística

> Proceso de Poisson

> ***Rompiendo a pared*** Es estar afuera observando el número de bolas de paintball que tocan tierra cada hora. Identificar la variable aleatoria que cambia los valores.

> Variable aleatoria de Poisson

> Estadística Bayesiana.

> Inferencia Bayesiana.

## Ejemplo de un modelo estadístico en un Testing A/B
Aquí se usa lo de la inferencia Bayesiana, como Data Scientist se hace muy seguido

> La idea es maximizar el clic en botón azul y rojo

> ¿Inferencia Bayesiana?

> Distribución posteriori ¿?

> Ensayo de Bernoulli.

> Variables aleatorias de Bernoulli

> Cadenas de Markov

> Prencentil ¿?

Hay muchos tipos de distribuciones

# Herramienta clave que usa un Data Scientist
## Herramientas que todos necesitamos
Para ser un miembro efectivo de un equipo profesional de data science, hay un set de herramientas de ingeniería de software que todos necesitamos saber.
Es muy fácil pensar que en tu viaje a través de data science, que lo único que importa es construir modelos geniales de machine learning, construyendo modelos de inferencia estadística, etc.
Pero la realidad es que cuando trabajamos como data scientist nos encontramos haciendo unas cuantas cosas.
Vamos a cubrir tres herramientas principales, la primera es AWS o Amazon Web Services, la cual es una colección de servicios de cómputo basados en la nube
La segunda son los comandos de la terminal que usamos para explorar datos en la terminal.
Y la tercera es GIT siendo un lenguaje de control de versiones que usamos para colaborar efectivamente en una base de código\Ncon otros data scientists e ingenieros de software.

> Si eres una persona que entiende por completo cómo construir redes neuronales desde cero, cómo construir complejos modelos jerárquicos de inferencia Bayesina. Aprender las siguientes herramientas no es un gran desafío.

## Servicios en la nube de Amazon: AWS/EC2
Cuando estamos ejecutando un sitio web, tenemos que poner el código de ese sitio en una computadora, y esta computadora es más coloquialmente conocida como un servidor. Las personas que acceden a ese sitio solicitan la información a ese servidor, y ese servidor envía respuestas de regreso a esas personas accediendo al sitio.
De nuevo, este servidor no es más que una computadora.
Típicamente para tener el servidor, para ejecutar el servidor, lo rentamos de un proveedor de servicios de nube. Podemos rentar esto ya sea por poco tiempo o a largo tiempo,
a un proveedor como AWS, de Amazon Web Services.
AWS tiene muchos servicios, como por ejemplo:
EC2 que significa Elastic Cloud y estos son servidores virtuales en la nube.
S3 significa almacenamiento Super Simple Storage, y es un lugar para guardar una gran cantidad de datos y documentos, son como discos duros en la nube.
Redshift, es un almacenamiento SQL basado en columnas, y lo primero es que por supuesto las bases de datos necesitan espacio para almacenar sus datos, y entonces si una organización por ejemplo tiene 50 Terabytes de datos que almacenar.

- EC2 -> Elastic Cloud
- S3  -> Super Simple Storage
- Redshift -> Base de datos

## Obteniendo y explorando datos desde nuestra linea de comandos

Con curl hacemos solicitudes http para obtener archivos y datos desde el servidor

Para saber la solicitud de un enlace en crhome solo hay que inspeccionar el elemento, entrar en red y presionar el botón para que capture

Se deben descargar los archivos y todo el set de datos en el sevidor. Descargarlo en local para luego pasarlo al servidor es prohibitivo

> cut, set, head, uniq, wc, curl, head, sort, 

> Filtrar e interactuar con los datos de un DataSet con bash


## Git
Git es un lenguaje muy popular para el control de versiones, y una herramienta que usamos para colaboración de proyectos.
Al trabajar con otros desarrolladores es realmente importante que todos se mantengan organizados.
Entonces Git es su propio lenguaje, al igual que Python, al igual que Ruby, al igual que R, etc.pero es un poco diferente. El alcance de Git es extremadamente limitado, nos ayuda a hacer “control de versiones” de nuestro código.
Si quieres aprender más sobre Git tenemos un curso enfocando a esto

--- Terminar de ver esta clase y la de inferencia de Twitter

# Construyendo un equipo de data science
## Construyendo un equipo de Data Science
En el 2016 un equipo de Data Scientist es de aproximadamente de 5 a 10 personas. Es muy raro encontrar a una organización con más de 50 Data Scientist.

## Ingeniero de datos, creadores de producto y data scientists.

> Data Engineers es de las primeras contrataciones que deben hacerse en un equipo de data science.

> Un Data Engineer es más experto en el área de ingeniería de software que en la parte de las matemáticas y se encarga de llevar a producción.

> Modelo incrustado vs modelo aislado (Embedded vs Siloed).

# ¿Qué sigue?
## ¿Qué sigue?
Data science vive en linea, desde libros de texto, hasta competencias, cursos en línea, foros hasta Data Scientist como tu y yo.

Sé un tornado, consume, consume y consume. Desde competencias de modelos predictivos en Kaggle hasta ir a reuniones, leer libros, hasta crear y publicar proyectos personales.

La cantidad de información que necesitamos conocer como data scientist es mucho mayor y solamente crecer más rápido de lo que una persona podría consumir en su vida.

Entonces probablemente, canceles tus planes de jugar videojuegos con tus amigos y todos los demás compromisos socials no urgentes y ponte a trabajar.

Yo te prometo que ser data scientist es realmente muy divertido.

## Cierre del curso
Las herramientas de ingeniería que usamos en el día a día: Git, AWS y línea de comandos.

## Contenido complementario

> Con este curso, esperamos que todos ustedes estén un poco más cerca de cargos profesionales como Data Scientist. Afortunadamente, por estos días parece que todos están contratando data scientist.

> Desafortunadamente, sin embargo, no todos los cargos de data scientist son creados iguales. Así que buscar tu primer trabajo en data science y leer as descripciones del trabajo.

***Postulaciones negativas***
1. ¿Cómo leemos descripciones de trabajo de cargo de data science? Cuando hay descripción del empleo que no son convenientes:
    - Nos gustaría que tú, nos gustaría que esta persona nos ayude a darle sentido a nuestros datos.
        Lo que esto significa es que la empresa no tiene definido lo que hará el data scientist.

2. ¿Y si dice que eres la primera contratación? "Estamos creando nuestro equipo de data science y necesitamos esta persona para que dirija el esfuerzo"
    Ser la primera contratación no es necesariamente malo, pero ya sabes, después de tomar este curso como estudiantes leyendo descripciones de trabajo probablemente este es tu primer trabajo de data science. De modo que tu primer cargo, probablemente no quieres estar en una posición en la que eres la primera contratación. 
    De nuevo, lo que ellos en realidad te están pidiendo es que tena ese tercer lado del triángulo, el lado de negocios del triángulo, comprender cómo traducir problemas de negocios en problemas de data sciece.

    Te están pidiendo que tengas esa información y ya sabes, si esta es nuestra primera oportunidad en data science  esa es una habilidad que casi... que normalmente viene después de las otras dos. Es algo que se desarrolla con experiencia.

3. "Nos gustaría que nos ayudaras a construir nuestra infraestructura de datos"
    Lo que es es en efecto es una especie de cargo de ingeniería de datos disfrazado. En un futuro puede separse, pero al 2016 a los data scientist realmente casi por necesidad, se les pide que lo hagan todo. Y entonces, como aprovechándose de este hecho muchas compañias disfrazarán lo que realmente son cargos de ingenieros de datos y los llamarán "trabajos de data science".

***Postulaciones positivas***
1. Construiremos una infraestructura para recomendaciones, haremos inteligencia empresarial interna.
    Una empresa que dice esto, esta claramente o en apariencia ha considerado detalladamente la relación que el equipo de data sciece tendrá con otros departamentos y concretamente los problemas en los que estarán trabajando.

2. Estas son las personas con las que trabajarás.
    Si sabemos que estaremos trabajando con un puñado de ingenieros de datos, probablemente no pasaremos la mayoría de nuestro tiempo construyendo nuestra infraestructura ETL, probablemente pasaremos el tiempo construyendo modelos matemáticos, lo que para muchos de nostrotros es más donde nos gustaría vivir.

3. Enumerar los otros agentes de negocios con los que trabajarás.

    Transformar los problemas del negocio a problemas de data science es muy importante pero ello viene con la experiencia. Conocer quién trabajará con nosotros nos dará una idea cómo desarrollar esa habilidad durante nuestro cargo.

    Si dice que estaremos trabajando con, ya sabes, un vicepresidente de data science que es una especie de coducto entre la dirección y el equipo de data science. Probablemente sabemos que esta persona tiene mucha experiencia siendo este conducto, siendo la persona entre el problema de negocios y el problema de data science. Y realmente nos ayudará a desarrollar esa habilidad que es tan importante, esa visión de negocios en esa organización.

Es importante saber que no todos los cargos son creados iguales, es muy importante ser paciente al escoger tu primer cargo en data science y ser muy crítico al leer las ofertas de trabajo.

> Ahora que hemos terminado nuestro curso de Data Science y aprendido un poco más acerca de cómo abordar nuestros primer cargo en Data Science ahora deberíamos estar listos para tomarnos el mundo de data science. ***Suerte en el camino a todos***.
