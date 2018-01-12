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

# Primeros pasos con MongoDB

MongoDB es una base de datos no relacional en C++ por el 2007. Es una base de datos documental (en documentos en formatos JSON).

***Conceptos claves***:
- Base de datos
- Tablas (Colecciones)
- Filas o registros (documentos -> BSON)
- Columnas o campos (campo)

> En un mismo campo se pueden guardar un número o bien un string.

# Modelado de datos en MongoDB relaciones uno a uno y uno a muchos.

El campo obligatorio en toda colección es "_id" que de no hacerlo se va autogenerar.

***Uno a uno***
La relación uno a uno trata de información de información que podrías guardar por separado y que básicamente una de las dos entidades que almacenes va a tener una referencia hacia la entidad que necesite.

Ejemplo
{
    _id: "platzi"
    name: "Platzi"
    address:(
     city: "Bogotá"
     country: "Colombia"
 )
}

Si fuera una base de datos SQL, el campo "addresss" se guardaría en otra tabla.

***Uno a muchos***

> En la actualidad es más barato pagar por la storage y no por CPU o RAM que es mucho más caro.

Ejemplo:
{
    title: "Curso de NoSQL y MongoDB",
    published_date: ISODate("2018-10-31"),
    languague:"Spanish",
    publisher:{
        name: "Platzi", location: "Colombia"
}
}


{
    title: "Curso de Programación en Go",
    published_date: ISODate("2018-10-31"),
    languague:"Spanish",
    publisher:{
        name: "Platzi", location: "Colombia"
}
}

Si la información cambia muy seguido, entonces utilizamos una referencia como que *publisher_id*

> "Redundar información en SQL es un pecado y por ello existe la normalización y diferentes técnicas para guardar la información necesaria". Pero en MongoDB es perfectamente válido redundar la información teniendo en cuenta que esto va a optimizar la consulta de dicha información.

# Modelado de datos tipo árbol

Empezamos un elemento y lo vamos desglosando así como en los organigramas. En MongoDB, los que están arriba son padres y los de abajo son hijos.

Hay dos tipos de referencia:

El resto de los campos quedan iguales.

- Referencia el padre <<parent: "Carrera de Bases de datos">>
- Referencia a los hijos <<children:["Curso de NoSQL y MongoDB"]>>

La forma en que se hacen es igual, la diferencia entre ambos es si recorres el árbol de arriba hacia abajo o inversa.

# Creando el modelo de datos de Cryptongo

Desde [coinmarketcap.com/api](https://coinmarketcap.com/api)

Capturamos el siguiente endpoint:

{
        "id": "bitcoin", 
        "name": "Bitcoin", 
        "symbol": "BTC", 
        "rank": "1", 
        "price_usd": "16868.0", 
        "price_btc": "1.0", 
        "market_info":{
            
            "24h_volume_usd": "20439700000.0", 
            "market_cap_usd": "283140124916", 
        },
        "available_supply": "16785637.0", 
        "total_supply": "16785637.0", 
        "max_supply": "21000000.0", 
        "last_updated": "1515246261",
        "hash_ticker": ""
    }

> Cada 5 minutos traeremos información del API, pero no queremos que la información se repita. El campo "last_updated" en formato unix nos dice la fecha de modificación.

> El campo "hash_ticker": Lo vamos a crear partiendo de los datos y de esta manera nos aseguramos que el hash va a ser único y no se repetirá el registro. 

Así estemos redundando, es preferible dejar todo en un mismo documento. Pero sí sería bueno que como reto hagas relaciones pertinentes uno a uno u uno a muchos de este mismo documento.

# Librerías de MongoDB

[enlace de librerías](https://docs.mongodb.com/manual/applications/drivers)

PyMongo: Librería que soporta MongoDB para Python.

# Ejecución de código JS en la shell de MongoDB

MongoDB tiene dos componentes, un componente servidor y un componente cliente.

***mongo*** -> Para ejecutar el cliente, de esta forma si lo tenemos en localhost.

***mongo --help*** -> Para ayuda

***show dbs*** -> Mostrar las bases de datos. *admin* y *local* son las bases de datos que se crean por defecto.

***use nombreBaseDeDatos*** -> Usar una base de datos

***db.curso.insert({"name": "platzi"})**

***show collections*** -> Ver las colecciones creadas

***db.createCollection("curso1")*** -> Creación de la collección de manera implícita.

> Podemos insertar código JS

function hello(){
    print("Hola")
}

hello()

for(i=0;i<10;i++){
    print(i)
}

Podemos implementar código javascript para implementarlo desde la consola.

Podemos insertar archivos de javascript

En un archivo:
function hello(){
    print("hola")
}

function getCol(){
    print(db.getCollectionsNames())
}

Para cargarlo, una vez usado la base de datos
***load("nombre-script.js")***

Podemos usar script en Javascript para crear cargas masivas de información que nos permitirán administrar el servidor de mongo de manera fácil.

# Insertar un documento con la consola de MongoDB

Podemos guardar variables, ejemplo

documento1={aquí lo que copiamos par el API }

***use cryptongo*** -> Base ded datos para nuestra aplicación.
***db.ticker.insert(documento1)*** -> Insertar nuestro documento.

Creamos otra variable, pero como documento2.

***db.ticker.insertOne(documento2)*** -> Insertar un documento en MongoDB, válido para v3 en adelante.

# Insertar múltiples documentos con la consola de Mongo

Crear dos o más variables "documento#" 

> Si no especificamos la base de datos creará las colecciones en test.

Para insertar múltiples documentos

***db.ticker.insertMany([documento1, documento2])***

Reto: Hacer una inserción de 10 documentos haciendo solo una operación en la shell de Mongo.

# Funciones find y findOne

***db.ticker.find()*** -> Primeros 20 documentos que encuentre

***db.ticker.findOne()*** -> Un document

***db.ticker.findOne()*** -> Un documento

# Operaciones avanzadas con find y findOne en la consola de MongoDB

***db.ticker.find({"last_updated":"1515246261", "available_supply":"16589962.0"}).pretty()*** -> Buscar con dos parámetros, la coma indica un "y"

***db.ticker.find().limit(1).pretty()*** -> Limita el número de colecciones y la función de pretty muestra en formato JSON, otra forma de hacer esto es con ***find.ticker.findOne()***.

***db.ticker.find({"last_updated": {$gt: "1506525557"} })*** -> Verificar que la información sea mayor a un número.

- $gt: Mayor que
- $lt: Menor que
- $lte: Menor o igual a
- $gte: Mayor o igual a

Después de ***{$gte: "1506525557"}}, {_id:0, price_btc:0, rank:0}).limit(4).pretty()*** -> Muestra todo a excepción de los campos marcados por 0.

# Modificación de documentos en la consola de MongoDB

Una forma es guardando un documento en una variable, hacer una modificación y guardando posteriormente ese documento.

***documento1 = db.ticker.findOne()***

***documento1.hash_ticker=1234***

***db.ticker.save(documento1)*** -> Si el documento existe lo modifica, si no existe lo crea.

Otra forma de modificar, podríamos perder información si utilizamos esta función ya que si solo insertamos la variable a usar eliminará el reste a excepción del id del documento.

***db.ticker.update({_id: ObjectId("todo un número")}, {hash_ticker: 123456})*** -> De esta manera se elimina el resto del documento. Para modificar solo un campo, colocar una variable entre los corchetes. Está también updateOne y updateMani

# Eliminar documentos en la consola de MongoDB

Hay dos formas, una con remove y drop.

- Remove: Para eliminar documentos según una query, un id, un campo, un rango...
- Drop: Elimina todos los documentos de una colección, aunque puedes hacerlo con remove, drop es más rápido.

***db.ticker.remove({_id: ObjetctId("12312312")})*** -> Para que elimine el documento de la base de datos.

***db.ticker.remove({"last_updated":{$gt: "123123213"}})*** -> Con esto eliminará los documentos mayores a dicho número.

***db.ticker.drop()*** Elimina toda la colección ticker.

# Indices en MongoDB

Ayudan a ordenar para poder extraer la información mucho más rápido.

Para crear índices usar este enlace [https://docs.mongodb.com/v3.4/reference/method/db.collection.createIndex/](https://docs.mongodb.com/v3.4/reference/method/db.collection.createIndex/)

# Estructura del proyecto Cryptongo

Tendrá dos componentes, el que interaptuarán con coinmarketcap y guardará en la bas de datos y el que será una api que mostrará resultados en el navegador.

El endpoint ticker donde nos mostrará la información de coinmarketcap y top20 quien mostrará las primeras 20 monedas de toda la información de la base de datos.

Todo hecho completamente en python.

En el agente necesitamos que la información no se duplique.

# Cómo funciona el agente que consulta CoinmarketCap

Nota: El profesor usa pycharm

Cada vez que se utiliza un API, debemos chequear la conección con un status code 200.

raise: Palabra reservada en python para producir un error.

cryptongo se actualiza cada 5 minutos.

# Calcular el hash a partir de a información del ticker en Cryptongo


# Guardar la información obtenida por el agente

Correr el programa con ***python3 main.py***

# Crear API que consulta la base de datos get_documents()

Para ello se utilizará Flask que es un microframework para construir apis res con Python.




# Primeros pasos con Redis

Redis es una base de datos NoSQL del tipo llave-valor. Almacena mayormente en memoria pero si uno lo desea puede guardar al disco duro.

La velocidad de escritura y lectura en ram es muy superior a cualquier otra que necesite buscar en disco duro.

Usos:
- Full Page Cache: Hacer que todo el sitio web se renderee una sola veez y se almacene ese resultado html en una key de redis y cuando el visitante vuelva a visitar la página traiga esa información de la base de datos y se lo muestras en pantalla. De esta manera no tienes que hacer consultas a la base de datos para hacer render en esa vista.

En la forma como uno trabaja con un framework se hace render del html una y otra vez. Pero con Redis podemos hacerlos acelerar el tiempo de carga al ser leído desde la memoria ram. Y de esta manera tener mejor rendimiento de la aplicación.

PubNub: Permitir Pub/Sub, es una técnica para poder crear emisión de datos donde existe un Publisher quien emite la información y hay unos Subcribe quien recibe la información. Algo como si fuera un canal. Ejemplo: Socket.io. Ideal para websocket, una cola de procesamiento.

# Consola interactiva de Redis

Para entrar solo colocar ***redis-cli***

***redis-cli --help***

Podemos asignar una ip, usuario y contraseña.

> Nota: No se recomienda ingresar directamente la contraseña porque esto queda almacenado en el historial de log de la terminal.

En redis las bases de datos no tienen nombre, sino que se identifican por números. Máximo va a tener 16 bases de datos, pero esto se puede configurar para cambiar el valor permitido. Recuerda que el límite lo va a dar la ram de tu servidor.

El puerto de redis es ***6379***

Para seleccionar la base de datos ***SELECT 1***

***INFO*** Para obtener información de redis.

Redis es fácilmente escalable.

# Full page cache con Redis

Guardaremos los html de platzi.com/precios. Recuerda que según la ciudad se muestra un valor.

En ***Python***

```
import redis
r=redis.StrictRedis()
r
r = redis.StrictRedis(db=8)

# Pegar en esta variable el contenido de html de platzi.com/precios
content = """
... #Pegar
"""
# Almacenar el html en una variable
r.set('pricing_co', content)

# Para almacenar el resto de los sitios por país, usar una función

```
Con ***r.setex(name='pricing_mx', value=content, time=3600)*** Podemos especificar el tiempo que estará esa base de datos. Es útil para cuando no necesitamos guardar la información por días.



La compresión del html es minificado

# Cierre del curso

Ya en este punto puedes implementar MongoDB y Redis en tus aplicaciones sin ningún tipo de problemas.
