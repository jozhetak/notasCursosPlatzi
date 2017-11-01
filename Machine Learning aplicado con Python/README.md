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

