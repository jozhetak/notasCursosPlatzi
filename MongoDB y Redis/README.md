# Bienvenidos al curso de MongoDB y Redis

El profesor es [@yograterol][https://twitter.com/yograterol]

Las bases de datos NoSQL permiten almacenar gran cantidad de información manteniendo un rendimiento bastante óptimo para lo que require la aplicación.

# ¿Qué es NoSQL?

Not Only SQL (Que no se usa SQL)

Hay bases de datos que permiten consultas SQL y básicamente no son relacionales.

Cada base de datos resuelve un problema en concreto.

Ejemplo: MongoDB guarda documentos (el formato JSON) lo cual permite guardar gran cantidad de información.

Con Redis: Almacenamos algo rápido de leer y de escribir con información llave:valor.

# Ventajas y desventajas de NoSQL

***Ventajas***
- Escalabilidad: La forma en que la base de datos se expande para guardar la información y la velocidad en la que se puede crecer para recibir más consultas de la base de datos. Están diseñadas para escalar fácilmente de forma horizontal (una base de datos en otro servidor conectado como un cluster). Generando mayor velocidad y almacenamiento dentro de las bases de datos implicadas.
- ***Esquemas de datos flexibles***: No necesitas guardar la información de una manera fija todo el tiempo. Por ejemplo, en una base de datos relacional para agregar un nuevo campo debemos modificar todos los registros. En NoSQL se pueden guardar diferentes registros con diferentes campos.
- ***Velocidad***: Pueden ser muy rápidas con respecto a las bases de datos SQL. Pero tener cuidado de no forzar a una base de datos SQL se disminuirá el rendimiento. Mientras mantengas el uso correcto, mantendrás la velocidad y rendimiento de ese motor. 


***Desventajas***
- ***Transacciones***: No tienen, son un conjunto de instrucciones donde si ocurre un error durante una escritura no va hacer rollback (devolverse al estado anterior). Si tu aplicación necesita transacciones, NoSQL no sería tan ideal para lo que deseas hacer.
- ***Joins***: No los tiene porque no hay relaciones. Si simulamos relaciones con NoSQL entonces perderemos el uso de MongoDB.

> "No te preocupes por las desventajas que tengan las bases de datos NoSQL, más adelante te ayudaré a abordar para poder superar estas desventajas y convertirlas a ventajas para tus aplicaciones" Yohan.
