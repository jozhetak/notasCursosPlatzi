# -*- coding: utf-8 -*-
# Importamos las librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Esta línea permite que los gráficos sean renderizados directamente e
## en nuestro notebook. Notebook tiene comandos mágicos como el siguient
%matplotlib inline

# Carguemos en un pandas dataframe nuestra
## base de datos.
movies = pd.read_cav('...vol/datasets/peliculas.csv', encoding='utf-8') # Cargamos los datos
type(movies)
movies.head() # Los primeros datos del DataFrame

# Cuántas lineas y columnas tiene nuestro datagrame
### Un dataframe en una estructura de datos que se compone de
### los elementos siguientes
movies.shape

# Visualizar todas las columnas
movies.columns
# Visualizar índices (vertical)
movies.index

# Visualizar columnas, manera 1
columna1 = movies('movie_title') # Nombre de la columna
columna1.head()
columna1

# Visualizar linea
linea = movies.loc[10,:]
linea

# Visualizar columnas, manera 2
movies.loc[:,'movie_title'].head

# Intentemos inspeccionar nuestros datos y entenderlos mejor
movies.info() # Información de lo que hay en el DataFrame

# Separar las columnas numéricas con las de texto
movies.dtypes # Muestra los tipos de las columnas
movies.dtypes == float # Verifica uno a uno si son float
movies.dtypes == int # Verifica que todos sean int

(movies.dtypes == int) | (movies.dtypes == float) # Or
movies.dtypes == object # Como pandas maneja las columnas de texto
num = (movies.dtypes == int) | (movies.dtypes == float)
num
num.index # Imprime el indice
for el in num.index:
    print(el)
num_cols = [c for c in num.index if num[c]]
num_cols # Imprime solo las columnas que tienen numeros, hay formas más fáciles

obj = (movies.dtypes == objetc)
obj_cols = [c for c in obj.index if obj[c]]
obj_cols # Imprime solo las columnas con texto

movies_num = movies[num_cols] # DataFrame con solo las columnas numéricas

# Estadísticas de las columnas numericas
movies_num.describe() # Descripcion de las estdísticas

# Estadísticas de las columnas de texto
## Para hacer nuestro primer modelo más simple para este trabajaremos
## solo con columnas numérica
movies_num['duration'].hist() # Obtener en un histograma
movies_num['imdb_score'].hist()
# Budget es la inversión de las peliculas
movies_num['budget'].hist() # Aquí las columnas no se ven por las escalas
mask = (movie_num['budget'] > 1e9).values_counts()
mask # Filtramos los valores
movies[mask]
# Casi nunca vamos a recibir una base de datos limpia
## Debemos limpiarlas de datos falsos,con los gráficos podemos
## podemos ver los problemas y limpiar los valores
## En el dataset del profesor hay errores en la columnas de
## ingresos y presupuestos


# Importar BDD thenumbers. Ahora manejaremos los datos faltantes (nulos o Nan)
pd.read_csv('../vol/datasets/thenumbers.csv')
financials = pd.read_csv('../vol/datasets/thenumbers.csv')
financials = financials[['movie_title','production_budget','wordwide_gross']]
financials
financial.shape
movies.shape

# Para concatenar necesitamos que tengan el mismo número de index
movies_num = pd.concat([movies_num, movies['movie_title']],axis=1)
movies_v2 = pd.merge(financials,movies_num,on='movie_title',how='left')
movies_v2.shape

# Ahora solucionaremos el problem de los datos faltanes (nulos o NaN)
### Los datos faltantes generan problemas con muhos algoritmos de ML.
### Es por esto que existen distintas estrategias para lidir
### con ellos
help(pd.Series.value_counts)
# Cuando dice NaN, está bien
# Los true debe ser mayor que los false
movies_v2.notnull().apply(pd.Series.value_counts)
(movies_v2 != 0).apply(pd.Series.value_counts)

# Uno puede tomar muchas decisiones pero todas deben estar justificados
available = ((movies_v2 != 0) & (movies_v2.notnull()))
available.all(axis=1).value_counts()

# No podemos entrenar nuestro algoritmos con datos cuya
## variable objetio no esta definida o sea nula (valor falso).
## Eliminemos esas lineas

mask = avaiable['worldwide_gross']
movies_v2 = movies_v2[mask]

# Ver valores, ni iguales a 0 ni nulos, todos deberían ser true
((movies_v2 != 0) & (movies_v2.notnull())).worldwide_gross.value_counts()

# En este punto nuestra base de datos está limpia
# En el caso de las features que no son la variable objetivo una mejor
## solucion para lidiar con los datos faltantes es reemplazar
## estos datos por otros que sean manejables y no afecten la
## calidad de las predicciones. La estrategia más común es
## utilizar la media de todos los ejemplos para la feature data

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_Values=np.nan, strataegy='mean', axis=1)
movies_v2.drop('movie_title', axis=1) # Verificar las columnas
movies_v2.drop('duration', axis=1)
movies_v2.head()
values = imputer.fit_transfor(movies_v2, axis=1)
values = imputer.fit_transform(movies_v2)
movies_v2.values # Con nan
values # Sin nan
x = pd.DataFrame(values)
x.columns = movies_v2.columns
x.index = movies_v2.index
x.head() # DataFrame limpio y listo para trabajar
x.to_csv('../vol/intermediate_resuts/X.csv',index=False)

# --------------------------------------------------------

# Antes de entrenar un modelo, aprendamos sobre el funcionamiento
## y la API de scikit-learn

import numpy as np
import pandas as pd

'''
Scikit-Learn es la librería más usada de Machine Learning
Learning tradicional. La libreria incluye funcionalidades de:
    - Procesamiento de datos en skelearn.preprocessing
    - Algoritmos de Machine Learning en sklearn.linear_model,
      sklearn.svm, sklearn.ensemble, y muchos más.
    - Evalucación de modelos en sklearn.model_selection y
      sklearn.metrics
'''

'''
Scikit-Learn sigue muy de cerca los resultados de la investigación
e implementa losreslutados más maduros y probados en sus módulos.
La documentación extensa muestra como la librería es un compendio
de conocimiento en Machine Learning llevado a software
'''

# Una structura de datos esencial en scikit-learn es el
## ESTIMADOR








