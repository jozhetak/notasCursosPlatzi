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

# Diferencias con SQL

***Lenguajes de programación***

En ***SQL*** Es un lenguaje de programación que se usa en todas las bases de datos relacionales. El motor de la base de datos no implementa el lenguaje SQL.

En ***NoSQL*** cada motor tiene su propio lenguaje para interactuar con él.

***Base de datos distribuidas***

Para escalar las bases de datos relacionales se hace de manera vertical (aumentando la performance del servidor donde está la base de datos).

Para NoSQL, estas bases de datos están hechas para ser distribuidas desde un comienzo. De esta forma se puede tener n cantidad de servidores conectados entre sí y cada uno puede almacenar cada información específica o toda la información general.

En el caso de MongoDB, tenemos un motor que permite distribuir la información con el modelo de sharing donde cada servidor guarda una porción de la base de datos. Por ejemplo, en una guardar las ventas, en otra los clientes, contabilidad, etc. Entonces si se daña un servidor en otro está respaldado. Entonces si por ejemplo queremos escalar la bases de datos de ventas solamente insertamos más servidores en esa base de datos. Esto en SQL es muy difícil de hacer y es muy propenso a cometer errores fácilmente.

Las ventajas no hace menos o más SQL o NoSQL.

En platzi usan Postgre, MySQL, Redis y MongoDB. Para todas estas bases de datos usan aplicaciones diferentes.

Estudiantes, usuarios, texto, vídeos, discusiones lo guardan en bases de datos SQL donde necesitan tener relaciones, tener JOINS y transacciones.

"Por otro lado, necesitamos darle velocidad al sitio. Por lo que guardamos las consultas en Redis".

Todas las discusiones que se generan en realtime en las clases en vivo se guardan en MongoDB. (Chat)

> "A la hora de elegir un motor no los pondría a competir con un SQL vs NoSQL a ver quién gana, no. Simplemente empiezas con la base de datos que creas que resuelva tu problema general y a medida que pasa el tiempo ve colocando el motor de la base de datos que resuelvan el problema en específico como información que pueda ser borrada en cierto tiempo (información volátil) o una gran cantidad de información que se requiera guardar en poco tiempo como un chat, MongoDB es una gran opción para resolver este problema de ser en tiempo real y gran cantidad de información. 

# Introducción a Cryptongo

Es un software escrito en python para guardar un market cap, la información de las criptomonedas para tener un historial de los precios de las criptomonedas.

La página es [coinmarketcap.com](https://coinmarketcap.com) tienen información que se actualiza cada 5 minutos. Donde muestra el precio de cada criptomoneda. También tiene API para obtener información de las monedas. Aproximadamente hay 1100 monedas dentro coinmarketcap. Entonces vamos a guardar 1100 registros cada 5 minutos.

El reto acá es poder traer la información y hacer conversión de datos y almacenarlas en el motor de MongoDB y crear luego un API Rest para poder consultar esa información sin necesidad de pasar por coinmarketcap sino directamente a la base de datos de MongoDB.

Usar una librería para acceder a MongoDB con Python.
