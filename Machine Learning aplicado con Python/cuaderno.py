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

# Implementamos un modelo simple de regresion primero
X = pd.read_csv('../vol/intermediate_results/X.csv')
X
y = X['worldwide_gross']
X = X.drop('wordlwide_gross', axis=1)
from sklearn.model_selection import train_test_split
X_train, x_test,y_train, y_test = train_test_split(X,y,test_size=0.4) # 60% para entrenamiento y 40% para test
print(len(X))
print(len(X_train))
print(len(X_test))
x.head(1)

# Nota, todas tablas son numéricas
from sklearn.linear_model import Lasso
model = Lasso()
model.fit(X_train, y_train) # Sale un warning pero no hay problema
predicted = model.predict(X_test)
predicted
predicted.shape
import matploitlib.pyplot as plt
%matplotlib inline
plt.hist(predicted)
plt.hist([predicted, y_test]); # Dibuja un histograma más fino

# Evaluemos de forma mas fina el comportamiento de nuestro modelo
'''
Los estimadores y las funciones de sklearn vienen con el máximo
de argumentos con valores por defecto que suelen ser las mejores
opciones si no tenemos algún conocimiento particular del problema.
En este caso particular la función estimador.score ya viene con
una de las métricas de sklearn.metrics, que es la métrica sklearn.metric.r2_score
'''


'''
EL score R2 de una regresión es una de las formas más comune de entender
su poder predictivo. Este mientras másc cerca de 1 este, mejor es
'''

'''
Los valores que puede tomar son de -infinito hasta 1. Un Score R2 negativo es,
malo, ya que la regresión es peor que si simplemente eligiéramos
un valor fijo como redicción para todos los puntos, la media.'''

model.score(X_test, y_test) # Estimar sobre datos nuevos


residuals = y_test - predicted
plt.scatter(y_test,residuals) # Aquí deben mantenerse unidos y no patrones
ap_residuals = np.abs(residuals)/y_test # Conertirá a valores absolutos
plt.scatter(y_test,ap_residuals)
lap_residuals =np.log(ap_residuals) # El gráfico logaritmoco de mejor forma
plt.hist(lap_residuals,bins=100, normed=1, histtype='step', cumulative=True); #Con el ; no muestra el output sino solo el gráfico


# Esto es para mostrar "Tenemos un 50% de los datos a un -10$ de error"
plt.hist(lap_residuals,bins=100, normed=1, histtype='step', cumulative=True); #Con el ; no muestra el output sino solo el gráfico
plt.axis([-2,0,0,1])
np.power(np.exp(1)*np.ones(5), np.linspace(-2,0,5))

# Feature Engineering
### Visualizar interdependencia entre variables
import padas as pd
X = pd.read_csv('../vol/intermediate_results/X.csv').drop('worldwode_gross', axis=1)
import seaborn as sns
%matploit inline
X.corr()

sns.heatmap(X.corr()) # Más bonito


# Hypercubo es un cubo en dimensión superior
import matploitlib.pyplot as plt
import numpy as np

x = np.arange(1,15)
y = np.power(0.1,1/x)
plt.plot(x,y) # Calcula las aristas en varios dimensiones

########## Análisis exploratorio

##### Continuando con el análisis exploratorio
Z3 = pd.concat([X,y], axis=1)
sns.heatmap(Z3.corr())

# Métodos de selcción automática de features
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_regression
selector = SelectectKBest(mutual_info_regression, k=4)
selector.fit(X,y)

scores = selector.scores
plt.rcParams["figure.figsize"] = [12,8] # Configurar para que el gráfico se vea mejor
plt.xticks(np.arange(7),list(X.columns)); # Visalizar leyenda

### Guardaremos las 5 features entregadas por la interpretacion de
#### nuestra regresion Lasso
X2 = X[['production_budget', 'title_year', 'duration.1' 'cast_total_faceook_likes', 'imdb_score']]
X3 = X[['production_budget', 'cast_total_facebook_likes', 'imdb_score']]

### Veamos los resultados del modelo con estas features
X_train, X_test, y_train, y_test = train_test_split(X,y)

cols2 = ['production_budget', 'title_year', 'duration.1', 'cast_total_facebook_likes', 'imdb_score']
X2_train, X2_test, y2_train, y2_test = X_train[cols2], X_test[cols2], y_train, y_test
cols3 = ['production_budget', 'cast_total_facebook_likes', 'imdb_score']
X3_train, X3_test, y3_train, y3_test = X_train[cols3], X_test[cols3], y_train, y_test

len(X_train)

from sklearn.linear_model import Lasso
model11 = Lasso()
model12 = Lasso()
model13 = Lasso()
model11.fit(x_train,y_train)
model12.fit(X2_train,y3_train)
model13.fit(X2_train,y3_train)

# Machine Learning es muy iterativo, hay que probar cada método de ataque
## Nuesta unica forma de saber que las cosas están funcionando
## es probando el modelo y viendo sus resultados
## En este caso bajar las dimensiones (features) no fue muy
## significativa pero si hubiesen sido 50 si lo hubiésemos
## notado la diferecia
print(model11.score(X_test,t_test))
print(model12.score(X2_test,t_test))
print(model13.score(X3_test,t_test))

# ------------

# Creación de features
### Escalamiento de los datos
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.mode_selection import train_test_split
X = pd.read_csv('../vol/intermediate_results/X.csv')
y = X['worldwide_gross']
X = x.drop('worldwindw_gross', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X,y)

from sklearn.preprocessing import StandardScaler
scaler = StandarScaler()
scaler.fit(X_train)

scaler.mean_

scaler.scale_

X

X.values

scaler.transform(X_train)

X_train_scaled, X_test_scaled = (sclaer.transform(X_train), scaler.transfor(X_test))

##### Entrenamos el modelo
from sklearn.linear_model import Lasso
model = Lasso()
model_scaled = Lasso()
model.fir(X_train, y_train)
model_scaled.fit(X_train_scaled, y_train) # Saldrá un warning pero está bien
### para que no salgan los warnings clocar al principio del notebook
import warnings
warnings.simplefilter("ignore")

print(model.score(X_test, y_test)
print(model_scaled.score(X_test_scaled,y_test)

### Simplificando las transformaciones (Re-escalamiento) con pipelines
from sklearn.pipeline import make_pipeline
model_scaled = make_pipeline(StandardSclaer(),
                            Lasso())
model_scaled.fit(X_train, y_train)

print (model_scaled.score(X_test, y_test))

### Crear nuevas features de forma automática
A = (np.arange(6).reshape(3,2)
A

### De 2 columnas tendremos 6 columnas
from sklearn.preprocessing import PolynomialFeatures
transformer = PolynomialFeatures(2)
transformer.fit(A)
transformer.transform(A)

### Para hacerlo más rápido
from sklearn.preprocessing import PolynomialFeatures
transformer = PolynomialFeatures(2)
transformer.fit_transform(A)

X.shape
transformer = PolynomialFeatures(2)
transfomer.fit_transform(X).shape # De 7 pasamos a 36 features
## lo que hace este transform es crear más features con polinomios
## y mientras más features tenemos más combinaciones posibles podemos hacer
## Tener cuidado con este polinomio porque podemos crear features muy grandes

model_poly = make_pipeline(PolynomialFeatures(2),
    Lasso())
model_poly.fit(X_train, y_train)
model_poly.score(X_test, y_test)
# Para este caso no fue muy significativo el escalamiento de features. Pero en otros
## en que el profesor estuvo trabajando en un proyecto que si fue muy util.

