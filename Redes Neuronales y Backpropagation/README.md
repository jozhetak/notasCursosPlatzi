# Notas del curso de Redes neuronales y Backpropagation

# Retropropagación: Visión general

# Evaluación de errores
## Función de costo, supuestos y probabilidad
> ***Aprendizaje sin un objetivo no es apendizaje***. Uno puede pensar que si no sabemos a dónde vamos no sabremos si lo estamos haciendo bien o mal. Lo mismo pasa en las redes neuronales.

***Datos importantes***
- Una función de error o ***loss function*** es báscimante la forma como una red neuronal sabe si está haciendo un buen trabajo o no.
- La gradiente o la primera derivada de una función con respecto a los pesos está siempre orientada al lugar donde se reduce más la función de error. Esto nos permite saber si la red neuronal está aprendiendo o no.
- En la vida real de las funciones son no convexas, esto quiere decir que podemos tener distintas soluciones para un mismo problema. Este es uno de los motivos por los cuales toma tanto tiempo entrenar una red neuronal artificial.

## Un ejemplo concreto: Aprendiendo la función XOR

# Optimización automática
## Cuál es el algoritmo de retropropagación
***Datos importantes***
- Los gradientes son básicamente la primer derivada de una función con respecto a un determinado parámetro. En este caso la función de costo y el parámetro es cada uno de los pesos en una red neuronal.
- La técnica de ***Backpropagation*** es responsable de separar de forma no lineal distintas clases que se encuentran en la vida real.
- El ***algoritmo de Backpropagatoion*** se compone de dos pasos:
  - ***Forward Step o paso a paso***. En éste tenemos una proyección de matrices. Tenemos datos de entrada, los pesos y una proyección de los datos de entrada a un nuevo proyecto.
  - ***Backward Step o paso hacia atrás***
- La función de activación no lineal permite encontrar el valor de la primera capa escondida de una red neuronal y se hace una proyección con los pesos, para así obtener el valor sigmoid de esa combinación lineal.


***Backpropagation algorithm***
Existen muchas librerías que lo utilizan como PyTorch, Tensorflow, Caffe...

> El objetivo es encontrar gradientes que básicamente son la primera derivada de una función con respecto a un determinado parámetro.

Aquí se descarga algo

## Actualizar los pesos de la red neuronal utilizando gradientes
***Datos importantes***
- El primer paso del ***algoritmo de Backpropagation (paso hacia adelante)*** está orientado a poder permitir transformar los datos de entrada en la siguiente capa, que es la capa escondida, y finalmente transformar eso a la última capa que es la capa de salida.
- En el segundo paso del ***algoritmo de Backpropagation (paso hacia atras)*** hacemos el proceso anterior pero a la inversa, comenzando por la capa de salida hasta llegar a la capa de entrada.

> Entender los algoritmos de redes neuronales nos ayudarán a optimizar o corregir nuestros algoritmos de Machine Learning según cada librería.

## Propagación hacia atrás
> Aquí se explica a detalle la matemática de las redes neuronales.

## Demo: Aprendiendo a separar clases
***Datos importantes:***
- Una de las premisas de usar redes neuronales es que finalmente tenemos una herramienta que permite separar clases de forma no lineal.
- Una sola linea no es capaz de poder separar las clases.

¿Qué necesitamos para implementar una ***red neuronal*** desde cero?
- Generar la topología de la red neuronal
- Representar los pesos
- Representar las actividades no lineales
- Implementar a función de ***Backpropagation***


