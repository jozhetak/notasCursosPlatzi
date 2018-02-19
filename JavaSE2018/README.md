# Notas del curso de Java SE 2018

# El origen de Java

Java fue creado en 1991 creado por James Gosling, y en 2009 fue comprado por oracle.

Categorías:
JavaSE: Java Standard Edition, los fundamentos del lenguaje.
JavaEE: Java Enterprise Edition, aplicaciones web.
JavaME: Java MicroEdition, es la usada en teléfonos viejos. No está muy vigente.

# Creando un entorno de desarrollo

JDK: Java Development Kit, es un kit de desarrollo. Librerías, clases, y lo necesario.
JRE: Java Runtime Environment, para correr java. Es la máquina virtual de Java.

java -version : La versión de Java
javac : El conjunto de acciones de java

# Definiendo la versión de Java

Podemos usar por defecto la versión de Java.

# HolaMundo.java

Los archivos de Java siempre tienen que empezar por mayúsculas.

El nombre de la clase debe ser el mismo que el del archivo.

Compilamos con ***javac HolaMundo.hava***

Corremos con ***java HolaMundo***

# Método Main

Es el punto de entrada de una aplicación Java.

# Tipos de datos primitivos enteros

Tenemos los tipos objetos y los primitivos.

Se escriben con letras minúsculas, entre los datos primitivos están:

- byte: 1 byte 
- short: 2 bytes
- int: 4 bytes
- long: 8 bytes

Para especificar un long, ***Agregar L*** al final del número. De lo contrario el compilador lo tomará como entero.

# Punto flotante

Son aquellos que permiten agregar puntos decimales.

- float: 4 bytes. Agregar ***F*** al final del número, porque el compilador lo tomaría como double.
- double: 8 bytes. 

- char: 2 bytes. Es único, solo tendrá un dato. Una letra en comillas simples siempre.

- boolean: 2 bytes. True o False.

# Naming en Java

Nombres en Java

Reglas:
- Java es sensible a mayúsculas y minúsculas
- Pueden comenzar con _ o $
- No pueden comenzar con números
- Las constantes se escriben en Mayúsculas
- LowerCamelCase para funciones y UpperCamelCase para clases.

# Cast de variables

Esto es para convertir un tipo de dato a otro.

Podemos castear datos primitivos y objetos.

Este es un cast:

```
double d = 86.45;
int i = (int) d;
```

El casteo es de menor a mayor es automático, en sentido inverso requiere un casteo.
