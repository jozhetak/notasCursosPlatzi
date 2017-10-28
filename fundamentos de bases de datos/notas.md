#Atomicidad: 1 transacción no se va a poder a dividir en más de una transacción.
Ejemplo:
Para transferir una saldo de una cuenta a otra: A -> B

Todo esto es una operación atómica, si en alguno de los pasos ocurre un error como que que se vaya la luz ocurre un roll back al estado inicial
********************************
* - Verificar que A tenga saldo*
* - B Esté activo              *
* - Transferencia de A -> B    *
********************************

Una vez finalizado los pasos, se hace un commit para informarle que la transacción fue exitosa.

#Consistencia: Pasar de un estado válido a otro estado válido. Ejemplo cambio de variables o alcance de límites de cada variable. Ejemplo que saquemos 40$ cuando no se puede tener saldo menor a 10$ y solo nos quede 40$.

# Aislamiento/Aislamiento:
Aislar un dato o una transacción hasta que se haya hecho un commit o completado una transacción, y ésta permanece ocupada para la siguiente transacción. Si fue comprada, se bloquea. Si se mantiene ocupada, no podrá ser accedida hasta que sea desocupada. Cuando hay varias conexiones al mismo tiempo al mismo dato, toma el primero y bloquea a los demás.

#Durabilidad:
Cuando la transacción haya sido válido, generar un commit y persistirlo en el tiempo. Las bases de datos en memoria, corren en memoria (la memoria es volátil). El almacenamiento de la base de datos en memoria al disco duro es más lento, se recomienda que sea sólido o FlashMemmory. Este respaldo es cada 5 minutos.

En las bases de datos tradicionales usan Logs que trabajan en memoria y al llenarse se bajan a los discos duros.

#Bases de Datos In-Memory(Cambio de árboles a columnar): La búsqueda en las bases de datos con estructura de árbol busca fila por fila empezando por la primera hasta finalizar la última.
En las bases de datos columnar, busca en forma de columnas.

# Otros tipos de Bases de Datos en la industria:
Bases de datos basados en grafos o en nodos. Ideal para e-commerce, fraude o de riesgo. Relaciones entre los eventos, ejemplo las recomendaciones entre de twitter y demás de redes sociales.
Facebook usa bases de datos distribuidos "Divide y vencerás". Las bases de datos en nodos o grafos corren muy bien en la nube.

#Bases de datos In-Memory con indexación de columnar
Profundizar esto, hacer aplicaciones y subiras a la discusión.

# Proyecto: Tienda de productos de Platzi
##Paso 1: Definición de las entidades. Debemos crear alertas para cuando nos estemos quedando sin inventario.
- Item: Un item es cada objeto que voy a vender en la tienda
- Cliente
- Método de compra
- Método de pago
- Proveedor
- Carrito

##Paso2: Cardinalidad de las relaciones. El gráfico para las relaciones en tre las entidades, se recomienda usar excel. Recuerda, la parte superior de la diagonal se un espejo de la parte inferior. 0 Significa que es opcinal.
-Cliente
-Item
-mCompra
-mPago
-Proveedor
-Carrito

##Paso3: Cololar las relaciones de manera gráfica

##Paso4: Definición del formato
Nombre de la tabla
******************************************
*Atributo*Tipo*Obligatorio*Llave Primaria*
******************************************
*        *    *           *              *
*        *    *           *              *
*        *    *           *              *
*        *    *           *              *
******************************************
Con char siempre se usará el espacio definido

Con varchar modificará la capacidad asignada en base al necesario ingresado

timestamp para fecha

**Cuando tengas tu aplicación recuerda dejar fecha y hora que pasó, no sabemos qué problemas pueden haber en un futuro con los usuarios.**

El registro de fecha nos ayudará a respaldarnos a solventar reclamos y análisis estadísticos con Data Science.

Con Data Science podemos analizar data para predecir comportamientos y posibles buenas ventas. Nunca piensen que un dato pueda parecer tonto, no hay datos que no sirvan simplemente son datos que en este momento no nos pueden dar información.

Si no especificamos la longitud puede que los motores usen el valor por defecto y puede ser muy grande.

##Paso4: Para los atributos nombreTabla_ID, nombreTabla_atributo.

number(#):Número
timestamp:Fecha
varchar(#):Letras
Serial: Autoincremental
OLE: Archivos, no es recomendable en BD

##Paso5: Diagramar conceptualmente la Base de Datos con su cardinalidad

Se recomienda draw.io (Software), colocar los tipos de datos y atributos por tablas.

No usar tildes ni caracteres especiales.

Buscar otras herramientas para modelar Bases de Datos.

# -> Llave primaria
* -> Obligatorio
o -> Opcional

##Paso6: Modelo lógico -> Establecer las entidades fuertes y débiles (tablas intermedias) en ella se pondrán las llaves foráneas.

##Paso7: Disponer de las tablas intermedias con su respectivo ID, no deben ser seriales. tabla1_tabla2. Para romper las relaciones Muchos a Muchos.

##Paso8: Modelo físico. Terminación en cabeza de flecha que especifica de llave foránea a llave primaria. Transfomar los datos a los que se van a usar en el motor de base de datos seleccionado.
En este punto las entidades ya no se llaman así, se llaman tablas.

##Paso9: Llevando nuestro proyecto a SQL.

Cuando vamos a generar las tablas, correr:
drop table if exits CARRITO; -> Para eliminar las tablas en caso de que las tengamos en nuestra Base de Datos. (No usar en ambientes productivos)

- Metodología de diseño, primero crear las tablas y luego crear las llaves foráneas.
 
Los comentarios se hacen con <<comment 'Comentario'>>

Para agregar las llaves foráneas
<<alter table CARRITO add constraint FK_Carrito_Cliente foreign key (CLIENTE_ID, CLIENTE_CUENTAPLATZI) references (CLIENTE_ID, CLIENTE_CUENTAPLATZI) on delete restrict on update restrict>>

Lo último es para restringir que no se pueda eliminar la llave foránea.

#Propiedades de dependencias funcionales
- Propiedad funcional reflexiva: Llegar de un dato a otro porque están en misma tabla

- Propuedad funcional extensiva: No entendí :(

- Propiedad funcional transitiva: Eliminar relaciones entre tabla para evitar círculos y redundancia de datos.

# Normalización: Llevando el proyecto hasta la tercera forma normal. Hay 5, pero eran 3 inicialmente, es la tradicional. De 4 a 5 es cuando vamos a necesitar mucho más detalle, después de miles de registros más de la 3era forma normal se vuelve inmanejable

Las formas normales 

###Primera forma normal: Está relacionado con la Atomicidad.
Dividir lo más posibles el contenido de los registros en nuevos atributos. Ejemplo, separar nombres en segundo  nombre, y apellidos. Debemos tener obligatoriamente una llave primaria.

###Segunda forma normal: Cuando los atributos no están estrictamente relacionado entre sí, ejemplo ciudad y país de origen. Para aplicar la 2da forma normal, dos tablas. Una con ID-Ciudad-IDPais y la otra ID-País.

###Tercera forma normal: Cada uno de los atributos que no sean claves dentro de la tabla pueden llegar a ser claves que determinen a uno no clave. Ejemplo separar ciudad de origen y país. La idea es que en vez de poner el campo repetido usar una tabla a parte con ide. Hasta aquí se trabaja en producción.

###Cuarta forma normal: Obligatoriamente no podemos repetir datos en una misma tabla, ejemplo tallas y color de ropa. Crea combinaciones únicas.

###Quinta forma normal: Es importantísimo tener 4ta forma normal. Cada dependencia de unión entre tablas (join) va a estar hecho por claves candidatas y no por condiciones que no se vayan a cumplir.

Hasta aquí es la normalización. En producción con la tercera forma normal es suficiente, para ello debe aplicarse tanto la primera como la segunda.

##Tener en cuenta en el FileSystem:
- Redundancia
- Concurrencia
- Aislamiento
- Integridad
- Inconsistencia
- Seguridad
- Acceso (Rol de administrador y usuarios)
- Atomicidad

##DDL: Data defination language
- Create y drop: 
    table: Tabla
    view: Porciones de la data (muesta)
    procedure: Procedimiento en la base de datos, triggerst. Cada cierto tiempo se dispara un evento)
    index
    schema (Conjunto de tablas que tienen algo en común)

- Alter:
    table
    view
    procedure










