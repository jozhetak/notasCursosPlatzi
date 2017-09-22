# Curso SQL y MySQL

## Profesores
* Gustavo Angulo [@woakas](https://twitter.com/woakas)
* Alberto Alcoque [@beco](https://twitter.com/beco)

## Recursos
* [MySQL](dev.mysql.com)

## Notas
SQL (Structured Query Language): Es un lenguaje declarativo de acceso a base de datos relacionales.

***Operaciones SQL***

* Create: Crea tabla
* Alter: Altera la tabla (Columnas, restricciones, etc).
* Drop: Elimina columnas de la tabla, se puede eliminar una tabla completa con `drop table` dentro de la tabla de datos.
* Delete: Elimina registros de la base de datos.
* Truncate: Casi nunca se utiliza, elimina la tabla o la base de datos (más rápido que Drop) porque no analiza integridad de datos.
* Select: Muestra y filtra la información.
* Insert: Adiciona, inserta registros.
* Update: Cambiar datos en los registros.

### Motores SQL
* `MySQL`
* `SQLite`
* `PostgreSQL`
* `Oracle`
* `Microsoft SQL Server`
* DB2
* Firebird
* HSQL
* Iformix
* Interbase
* MariaDB
* Posgress
* PervasiveSQL
* Sybase ASE

> "Cada vez que cambias algo en la base de datos,si agrego una columna es obligatorio que todos los datos estén allí (registros) tienen que tener un dato esa columna puede ser null o cualquier valor pero siempre debe tener algo... Tener mucho cuidado cuando hay millones de registros".

> "Siempre sacar un BackUp antes de modificar o ejecutar cualquier ejecución en la base de datos".

> "Cada base de datos tiene una forma de crear réplicas".

> `Integridad refrencial` Relación que existen entre las tablas.

> "El ID debe ser independiente de los otros campos"

> "Si el motor de la base de datos no maneja integridad de datos, elimilará los registros almacenados en otras tablas".

> "Hay partes en que MariaDB y MySQL ya no son compatibles".

> MariaDB es un fork de MySQL, el primero es creado por la comunidad y el segundo fue comprado a Sun por Oracle.

***Ventajas de BD SQL***
* Son Transaccionales("O todo se hace o nada se ejecuta" - Palabras de Anahí Salgado :blush:) y no se perderá ningún dato.
* Existe álgebra y cálculo referencial.
* Estándares SQL.
* Fundamentos relacionales.
* Procedimientos almacenados en diferentes lenguajes.

***Desventajas de BD SQL***
* Realizar cambios a una tabla muy grande (30X10^6) puede ser un dolor de cabeza.
* Pueden tener problemas de performance dependiendo de discos duros y otras operaciones ID.
* No todas tienen integridad referencial (Si un registro depende de otro no se eliminará sin avisar). 
* No son compatibles entre otras bases de datos.

### Motores NoSQL

Cualquier motor que no usa SQL.

> "Antiguamente las base de datos NoSQL no garantizaban la escritura de datos (99.99%).

* Documentales
  * `MongoDB`
  * CouchDB
  * CouchBase
  * RavenDB
  * Djondb

> "Las base de datos documentales pueden tener restricciones, no nacieron para relacionar los documentos, sí se pueden relacionar pero no es natural.

> "Todos los documentos tienen un ID único para diferenciarlo de otros documentos".

> Tiene Geolocalización (latitud y longitud).

* Documentales en Grafos
  * `Neo4j`
  * `OrientDB`
  * Infinite Graph
  * Info Grid
  * Hyper GraphDB

> "Las base de datos en Grafos, las relaciones entre entidades se crean atributos". Los dos primeros fueron escritos en Java y son usadas en Big Data.

* Llave-Valor
  * `Redis`
  * Cassandra
  * Big Table
  * Dynamid
  * Rick

> "Compuesta por una llave única en toda la bse de datos y su valor. Son muy usadas para almacenar en caché con inicio de sesión en cookies, sistemas de autorización, se almacena en memoria ram, es más rápida.

> "Deben cambiar el paradigma que tienen ustede. Estamos acostrumbrados a llevarlo todo a tablas y pensar en tablas. Y así no es el mundo".

> "La documentación de Redis es muy buena".

* Orientadas a objetos
  * ObjectDB
  * zofe ObjectDatiles


***Ventajas de NoSQL***
* Cada una resuelve un problema diferente de performance.
* Son relativamente nuevas (no más de 15 años).
* Dependiendo del tipo es muy fácil hacer cambios en la structura de datos (agregar o cambiar tablas).

***Desventajas de NoSQL***
* En ocasiones son más lentas que SQL.

> "Normalmente usar una de cada una en un mismo sistema, ***BigData*** Cassandra; ***Caché en ram*** Redis; ***Sistemas bancarios*** Postgress o SQL.

> Preferencias de Gustavo Angulo: ***Transaccional*** Postgress; ***NoSQL*** CouchBase, MongoDB y Redis.

> "Lean la documentación, hay profesionales que llevan 15 años en esto".

### MySQL en código

> La pronunciación de MySQL es "mai esquel" (Por ahí va la broma).

> Para conectarse a la base de datos usar, insertar la contraseña luego de ingresar en la terminal
```
mysql -h localhost nombreUsuario -p
```

> Toda la metadata y select insertados en MySQL se encuentra en `information_schema`, mucho cuidado con esa base de datos.

> Begint se almacena como un string pero se comporta como un int.

> Cuando se usan referencias_id de las tablas, usar el mismo nombre en todas las tablas.

> Tipos de tablas: ***catálogo*** solo se almacena datos y ya. ***operación*** entrada y salida de datos muy frecuente (hay desarrolladores que lo hacen en otra base de datos).

> "Evitar tener phpmyadmin con acceso público.

*Seremos una librería que vende y presta libros*

> desc nombreTabla; Describe los campos de la tabla

Creación de la base de datos

```
show databases;
create database platzi;
use platzi;

create table books (
	book_id integer unsigned primary key autoincrement,
	publisher_id integer unsigned not null default 0, --unsigned para que no guarde el signo
	author varchar (100) not null,
	title varchar(50) not null,	
	description TEXT, -- Permite mucho más espacio que varchar, se puedeb guardar libros enteros
	price decimal (5,2), -- 5 parte entera y 2 parte decimal
	copies int not null default 0
	);

create table publishers (
	publisher_id integer unsigned primary key auto_increment;
	name varchar (100) not null,
	country varchar (20)
	);


create table users (
	user_id integer unsigned primary key auto_increment;
	name varchar (100) not null,
	email varchar (100) not null unique
	);

create table actions (
	action_id integer unsigned primary key auto_increment,
	book_id integer unsigned not null,
	user_id integer unsigned not null,
	action_type enum ('venta', 'prestamo', 'devolución') not null, -- default 'venta'
	created_at timestamp not null default current_timestamp -- Evitar usar timestamp porque se usará hasta el 2038
	);

```

LLenado de registros de la base de datos:
```
INSERT INTO users(name, email) VALUES
    ('Ricardo', 'ricardo@hola.com'),
    ('Laura', 'laura@hola.com'),
    ('Jose', 'jose@hola.com'),
    ('Sofia', 'sofia@hola.com'),
    ('Fernanda', 'fernanda@hola.com'),
    ('Jose Guillermo', 'memo@hola.com'),
    ('Maria', 'maria@hola.com'),
    ('Susana', 'susana@hola.com'),
    ('Jorge', 'jorge@hola.com');

INSERT INTO publishers(publisher_id, name, country) VALUES
	(1, 'OReilly', 'USA'),
	(2, 'Santillana', 'Mexico'),
	(3, 'MIT Edu', 'USA'),
	(4, 'UTPC', 'Colombia'),
	(5, 'Platzi', 'USA');

INSERT INTO books(publisher_id, title, author, description, price, copies) VALUES
    (1, 'Mastering MySQL', 'John Goodman', 'Clases de bases de datos usando MySQL', 10.50, 4),
    (2, 'Trigonometria avanzada', 'Pi Tagoras', 'Trigonometria desde sus origenes', 7.30, 2),
    (3, 'Advanced Statistics', 'Carl Gauss', 'De curvas y otras graficas', 23.60, 1),
    (4, 'Redes Avanzadas', 'Tim Bernes-Lee', 'Lo que viene siendo el Internet', 13.50, 4),
    (2, 'Curvas Parabolicas', 'Napoleon TNT', 'Historia de la parabola', 6.99, 10),
    (1, 'Ruby On (the) Road', 'A Miner', 'Un nuevo acercamiento a la programacion', 18.75, 4),
    (1, 'Estudios basicos de estudios', 'John Goodman', 'Clases de datos usando MySQL', 10.50 , 4),
    (4, 'Donde esta Y?', 'John Goodman', 'Clases de datos usando MySQL', 10.50, 4),
    (3, 'Quimica Avanzada', 'John White', 'Profitable studies on chemistry', 45.35, 1),
    (4, 'Graficas Matematicas', 'Rene Descartes', 'De donde viene el plano', 13.99, 7),
    (4, 'Numeros Importantes', 'Leonard Euler', 'De numeros que a veces nos sirven', 10, 3),
    (3, 'Modelado de conocimiento', 'Jack Friedman', 'Una vez adquirido, como se guarda el conocimiento', 29.99, 2),
    (3, 'Teoria de juegos', 'John Nash', 'A o B?', 12.55, 3),
    (1, 'Calculo de variables', 'Brian Kernhigan', 'Programacion mega basica', 9.50, 3),
    (5, 'Produccion de streaming', 'Juan Pablo Rojas', 'De la oficina ala pan', 23.49, 9),
    (5, 'ELearning', 'JFD & DvdH', 'Diseno y ejecucion de educacion online', 23.55, 4),
    (5, 'Pet Caring for Geeks', 'KC', 'Que tu perro aprenda a programar', 18.79, 3 ),
    (1, 'Algebra basica', 'Al Juarismi', 'Esto de encontrar X o Y, dependiendo', 13.50, 8);

insert into actions (book_id, user_id, action_type)values
  (3, 2, 'venta'),
  (6, 1, 'devolucion'),
  (7, 7, 'devolucion'),
  (2, 5, 'venta'),
  (10, 9, 'venta'),
  (18, 8, 'devolucion'),
  (12, 4, 'venta'),
  (1, 3, 'venta'),
  (4, 5, 'devolucion'),
  (5, 2, 'venta');

```


Con `\G` al final de un select muestra el result en tarjetas. Ejemplo:
```
select * from books \G
```

> show tables: Muestra las tablas dentro de la base de datos.

> show databases: Muestra las bases de datos. Usar `use nombreBaseDeDatos` para utilizar.

> actions es la tabla pivote que relaciona las otras tablas.

> Alias ayudan a aligerar el query. Ejemplo `nombreTabla as bt`.

> Tabla satélite es un JOIN.

> "No hay cosa más peligrosa en una aplicación que mostrar información equivocada. Acaba la aplicación".

Requisitos de UNION (Concatena result de dos o más query)
* Misma cantidad de columnas.
* Mismo tipo de dato por columna

*Queremos representar la columna price en 0 si no es venta*

Usando UNION:

```
select a.action_id as aid
	b.title,
	a.action_type,
	u.name,
	0 as price

from actions as a
left join books as b
	on b.book_id = a.book_id
left join users as u
	on a.user_id = u.user_id
where a.action_type != 'venta'

union

select a.action_id as aid,
	b.title,
	a.action_type,
	u.name,
	b.price as price
from actions as a
left join books as b
	on b.book_id = a.book_id
left join users as u
	on a.user_id = u.user_id
where a.action_type = 'venta'

order by aid -- Ordenar por el id
```

*La mejor forma de hacerlo es:*

```
select a.action_id as iad,
	b.title,
	a.action_type,
	u.name,
	if(a.action_type = 'venta', -- Condición
		b.price,	    -- Si es verdadera
		0), as price,       -- Si es falsa
from actions as a
left join books as b
	on b.book_id = a.book_id
left join users as u
	on a.user_id = u.user_id
```

> ***Operación atómica*** Operación que devuelve un valor, ya sea un número o un string. La suma es una operación atómica.

Agregando el descuentos de libros:
```
if (b.book_id in (1,2,4,6,8),
	b.price * 0.9,
	b.price) as dcto
```

> Se pueden hacer operaciones matemáticas y subquerys en MySQL (algo avanzado).

> La redundancia de código en programación si no está penado con la muertestá muy mal visto.

> ***Redundancia de datos*** Ejemplo: El nombre de la persona a la que le prestaste el libro esté almacenada en dos lugares diferentes. El problema de ello es cuando vayas a cambiar los registros y debes hacerlo en múltiples tablas.

> El motor ***MyISAM*** no es transaccional y por tal no emplea llaves foráneas, es más rápido que ***InoDB***, éste se puede usar llaves foráneas, es transaccional y se pueden recuperar datos aunque se vaya la luz. Ideal para sistemas bancarios.

> ***Llaves foráneas físicas*** Las que se declaran.

> ***Llaves foráneas lógicas*** Aquellas que se saben que existen por la convención de nombres.

> ***Normalización*** "Si yo tengo 500 tablas en una base de datos y todas ellas tienen que ver con usuarios, una buena normalización significa que el nombre del usuario esté escrito en una y solo una tabla, eso significa que en todas las tablas donde se haga referencia en una u otra forma, una buena base de datos normalizada hará referencia a un id de usuario".

> ***MyISAM*** y ***InoDB*** son las formas en cómo MySQL almacena la información.

quellas que se saben que existen por la convención de nombres.

> ***Normalización*** "Si yo tengo 500 tablas en una base de datos y todas ellas tienen que ver con usuarios, una buena normalización significa que el nombre del usuario esté escrito en una y solo una tabla, eso significa que en todas las tablas donde se haga referencia en una u otra forma, una buena base de datos normalizada hará referencia a un id de usuario".

> ***MyISAM*** y ***InoDB*** son las formas en cómo MySQL almacena la información.

***¿Cuáles editoriales hay en existencia?***
```
select p.name,
	b.title,
	b.price,
	b.copies
from books as b
left join publishers as p
	on b.publisher_id = p.publisher_id
```

***Saber cuánto costo total de libro por copia hay por librería***
```
select p.publisher_id as pid,
	p.name,
	sum(b.price * b.copies)
from books as b
left join publihsers as p
	on b.publiher_id = p.publisher_id
group by pid
```

***Conseguimos un multimillonario que compró todos los libros inferiores a 15 y nos pide que los regalemos***

Igual que el anterior pero agregar
```
sum (if(b.price < 15, 0, b.price*b.copies)) as total
```


***¿Cuántos títulos por editorial estoy guardando***
```
select p.publisher_id as pid,
	p.name,
	count(b.book_id) as libros
from books as b
left join publishers as p
	on p.publisher_id = b.publisher_id
group by pid
```
Se pueden aplicar las siguientes columnas:
```
select 
	p.publisher_id as pid,
	p.name,
	sum (if(b.price>=15,1,0)) as libros_mios
	sum (if(b.price<15,0,b.price*b.copies)) as total
	sum (if(b.price>15,0,1) as libros_por_vender
	count(b.book_id) as libros
from books as b
join publishers as p
	on b.publisher_id = p.publisher_id
group by pid.
```

***Agregar columna active en la tabla users***
```
alter table users add column active tinyinit(1) not null default 1

update users set active = 0 where user_id = 16
```

***Insertar una tupla con una columna UNIQUE duplicada***
```
insert into users (name, email) values ('rocio','sofia@gmail.com')
	on duplicate key update active = 1, name = concat(name, ' - nuevo')
```

***Al actualizar una tupla marcar un límite de filas afectables***
```
update users set name='juan' where user_id=5 limit 1
```

***Usando replace***
Hace la misma función de UPDATE, con la diferencia de que si al hacer un insert está duplicado, borra la tupla y la vuelve a insertar pero con otra key (si esta es autoincrementable.

Hay dos maneras de usar REPLACE:
```
replace into users (name, email, active,) values ('lorena', 'lorena@gmail.com',1)

replace into users set name = 'juan', email='juan@hotmail.com'
```

### Sensión de preguntas
***¿Cómo hacer más seguras las bases de datos?***
* Crear 3 usuarios:
  * Completo acceso de lectura y escritura
  * Solo que pueda leer información
  * Solo pueda leer cierta información
* Cifrar los registros

***¿Cómo puedo capturar los errores de la base de datos para que la validación no se haga en la App sino en la base de datos?***
> "MySQL más que estructuras de control no tiene nada smilar al try catch, hay varios eventos que se pueden catchar y está en la documentación.

***Los modelos de cubos para hacer análisis de negocios, montar modelos financieros, supermecados, etc. ¿Ese tipo de cosas es posible en MySQL?***
>"No, pero hay maneras de exportar para hacer esos cubos"

***¿Por qué hay que usar replace y en qué casos usar?***
> "Uno de los casos donde yo más uso replaces es cuando hago logs grandes a bases  de datos y no a archivos. No quiero tener un problema de que si existe un alif de mi sistema que haya mostrado algún error, simplemente quiero mostrar el último, quiero garantizar que eso utilice el menor tiempo de CPU posible y la lógica no me interesa, quiero que se ejecute sí o sí. Si dominan el ON DUPLICATE KEY UPDATE puedeb obviar completamente el REPLACE"

> Los cubos normalmente se refieren al tema financiero en el que se tienen productos, ciudades y tiempo, es una forma de entender en múltiples variables ***qué producto se vende más en cada mercado***.

***¿Cómo guardo el registro de la fecha y la zona horaria en que se registra una tupla automáticamente?***
> No se debe usar TIMESTAMP porque dan errores al registrar una fecha que no ha pasado y porque la variable tendrá vigencia hasta el 2038. En su caso, usar DEAPTIME (lo siento, no sé cómo se escribe) quien permite un registro desde el año 0000 hasta 9999.

***¿Está bien usar la sentencia like para búsquedas?***
> "Like es una sentencia válida para búsquedas siempre y cuando lo hafas contra algo que conozcas, si vas contra un TEXT (Se pueden almacenar libros enteros aquí)  vas a tardar siglos en encontrar. Una buena práctica es que el ¿wile shark? esté a la derecha del caracter, si está a la izquierda se duplica el tiempo en encontrar el match (resultado)"
> Nota: Usar varchar pequeños.

***Si haces un ALTER TABLE y agregas un campo como índice ¿se indexan todos los datos ya ingresados en ese campo?***
> "Si".

> No todos los select llevan FROM

> "Juan Pablo tenía que cuando usaba una consulta a punta de ORM (mapeador de bases de datos como Hibernate y JPA en Java) se demoraba 17 segundos y cuando saltó el ORM e hizo la consulta con SQL tardó 0.9 segundos".

> "La mayoría de los ORM van a la base de datos, traen la estructura de la base de datos, crean un objeto con la estructura de la base de datos pero crean un objeto con toda la estructura de la base de datos para modificar un dato y regresar a la base de datos haciendo un insert recorriendo todas y cada una de las columnas para insertar a la base de datos".

***¿Cuál es la diferencia entre una vista y una tabla temporal?***
> Las vistas vienen de un query. Beco prefiere usar tablas temporales.

> ***"Lo que yo les enseñé es menos del 2% de lo que es MySQL... Lo que más me gustaría es que tuvieran esa curiosidad de saber más. ir a romper bases de datos (en su computadora), ir a romper y perder información, repararlas, hacer querys complejísimos, no lleguen a un query de más de 200k porque estarían haciendo algo mal".***

### Notas finales personales
* Se recomienda usar 0 y 1 (tinyint) como booleanos ya que facilita la exportación de datos a otros sistemas.
* La función TO_DAYS(x) devuelve la cantidad de días desde el año 0.
* Las tablas temporales ayudan a agilizar la consultas pesadas, una vez creadas estas se eliminan cuando se cierra la conexión del usuario con la base de datos.
* NUMERIC(x,y) y DECIMAL(x,y)
  * x: Número total de enteros y decimales
  * y: Número máximo de decimales
* Eliminar datos y esquema se usa DROP
* Elimnar solo datos se puede usar DELETE y TRUNCATE
* El orden de los query son:
  SELECT - FROM - JOIN - WHERE - GROUP - ORDER 
