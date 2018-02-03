# Workshop: Configurando un entorno de trabajo para el curso Go

Con GoTest se pueden hacer prubeas unitarias y el framework de Revel hay pruebas unitarias.

Con Upper para interactuar con bases de datos.

Si se les hace más fácil con un framework vete por ese.

Con ***goose*** para hacer migraciones de datos.

Hay otros frameworks:
- Gorila
- Beggo
- Revel
- Martini

# Cómo personalizar la instalación de Revel en Curso de Go avanzado

Paquetes a utilizar:
- Revel: El framework
- Upper: Para administrar la base de datos
- Goose: Herramienta de migración de bases de datos

Por estándar con ***go get*** podemos obtener información de una url.

Con ***go env*** Podemos ver las variables de entorno de Go.

***go get -v -u paqueteDeGo***
***-v***: Información de la descarga
***-u***: Descargar o actualizar los más recientes
***-d***: Solo descargarlo sin instalarlo

Los paquetes se insttalan en ***/bin***

Dentro de ***~/go/src/*** Correr:
***revel new platzi/chat github.com/osmandi/platzi-chat***

Para correrlo en cualquier parte, mover la carpeta del proyecto a la carpeta de interés, en ***~go/src*** crear:
***ln -s /vagrant/platzi platzi***

Para instalar ***goose***, librería que ayuda mucho a las migraciones de bases de datos.

***go get -v bitbucket.org/liamstask/goose/cmd/goose*** 

Crear el archivo ***platzi/chat/db/dbconf.yml*** Donde colocar las configuraciones de la base de datos, para ello consultar la documentación de goose. Colocar en ese archivo el nombre de usuario, contraseña, host y sslmode=disable (este es una capa de seguridad)

[goose repo](https://bitbucket.org/liamstask/goose)

En el archivo dbconf.yml:
```
development:
    driver: postgres
    open: user=tito password=alkarismi_1 dbname=platzi host=127.0.0.1 sslmode=disable
```

Para ejecutar debe hacerse un directorio arriba de ***/db***

***goose status***: Para ver el estado.

Problemas que pueden ocurrir:
- Conección a la base de datos (Configuración de la IP del servidor de Postgres). Para el entorno de desarrollo: host all all 0.0.0.0/0 md5 en ***pg_hba.conf***. (Reiniciar el servicio con cada configuración). Otro problema es que debe escuchar la ip en ***postgresql.conf*** con ***listen_addresses='*'***.

La migración sirve para darle mentenimiento al software y poder compartirlo con alguien más.

***goose create createUserTable sql***

Esto crea un archivo en ***db/migrations/...***

***goose up***: Para subir o crear a la base de datos (Dentro del archivo)
***goose down***: Hacer un rolback a la base de datos (ejemplo DROP TABLE users;)

Table user (en goose up):
```
CREATE TABLE users
      (
      id SERIAL PRIMARY KEY,
      username VARCHAR(64),
      email VARCHAR(80),
      password VARCHAR(80),
      created_at TIMESTAMP DEFAULT now() NOT NULL,
      updated_at TIMESTAMP NOT NULL
      );
      CREATE UNIQUE INDEX unique_username ON users (username);
      CREATE UNIQUE INDEX unique_email ON users (email);
      CREATE INDEX ix_users_id ON users (id);
```

> Se recomienda probar la sentencia SQL antes de ingesar.

En la raíz del proyecto ***goose up*** para correr lo que está en la sección de ***goose up*** de la migración.

# Estructura para un chat server

Insertar la base de datos y registros, en el curso usan Postgres.

Una migración para crear la base de datos y otra para insertar registros.

Estructura del proyecto:
- app: Done estará la aplicación
  - Controllers: Lógica de la petición web a la lógica del negocio
  - init.go: Inicialización de variables
  - router: Definimos cómo serán mapeadas las rutas y cómo lo resolverá el navegador.
  - tmp: Archivos que utiliza revel para hacer un compilado interno.
  - views: Vistas de la aplicación, footer, errors, header... Con la intención de ahorrarnos código.
- conf: Configuración de toda la aplicación.
- db
- messages: Mensajes de los archivos
- public: Archivos estáticos
- test: Paquete de pruebas de funcionabilidad.

> route/routes.go: Es un código autogenerado. Para modificar dichos valores usar ***conf/routes***. Comentar /:controller/:action, quitar un Catch all para aquellas cosas que no estén predefinidas pero que nosotros agregamos como un controlador que a su vez tuviera una función interna podríamos invocarla son solo agregar el nombre del controller y el nombre de la acción, como generalmente lo que queremos es tener las cosas controladas lo comentamos.

Ambiente de desarrollo  en goose ***goose -env=dev status***

Así como lo hicimos con goose, en revel podemos generar más ambientes. Para ellos entramos en ***conf/app.conf***

- http.addr = Ip que estará escuchando, en blanco es que estará escuchando todas. Ideal para más seguridad o bien escalar.
- http.port: Puerto que va a usar
- http.ssl: Si va a usar un certificado
- http.sslcert y http.sslkey: Las llaves de ese certificado
- cookie.httpoly y cookie.prefix: Nombre de nuestra cookie y prefijjo
- cookie.domain: Para poner un dominio
- session.expires: Tiempo en que va a expirar la sesión
- result.chunked: Usar fecha UTC para que quede registrado con la fecha donde usuario hizo la petición siendo de otro país a donde está el srvidor. Es una buena práctica que pocas veces se lleva a cabo pero ayudará a ahorrar muchos dolores de cabeza.
- i18n.defeault_language: Configuración para localización
- log.trace.prefix ="TRACE": Todos los mensajes que son TRACE empezarán con esa palabra. De igual forma los otros
- [dev], [prod]: Módulo de pruebas.
  - log.trace.output, log.info.output: stderr, %(app.name)s_dev.log (para guardar ***chat.log***)

Para ejecutar en modo productivo: ***revel run platzi/chat prod***. Los log se guardan en la carpeta log.

> Nota: Con el modo de producción no aparace la pestaña de reporte del lado derecho.

> Nota: Con los enlaces simbólicos que hicimos al principio podemos ejecutar ***revel run platzi/chat*** desde donde queramos dentro de la carpeta ***revel/chat***.

Para traer de la base de datos al frontend, crear carpeta ***/app/modules*** y dentro de ella crear ***user.go**

> Go cuenta con templates que reemplaza el contenido entre {} de los html.

Aquí usaremos upper.io para interactuar la base de datos con el frontEnd. Se debe editar el archivo ***controllers/app.go***. Es importante dejar la "," al final de la variable en ***var user*** ya que ayuda a inicializarlas.

# Preguntas y respuestas
En este punto no se podía crear aplicaciones de escritorio gráficos con Go (según el profesor).

beego y gorilla tienen soporte de orm.

# Workshop: Unit Testing con Goblin

Las pruebas unitarias nos permiten evaluar una parte específica de nuestro código o bien un paquete, esto nos puede dar dos resultados. Uno positivo y otro negativo. El objetivo es evaluar estos resultados en función de lo que nosotros evaluamos. Es importante saber qué vamos a obtener.

> Las pruebas unitarias son del 2002.

Positivo: Ejecución normal
Negativo: Produce un error y un error esperado.

Ortogonalidad: Todos los pequeños elementos deben combinarse para crear software.

- go test: Ejecución de la prueba
- go test -v: Detalles de la ejecución
- go test -run=ExpReg: Ejecución de pruebas independientes

Convenciones:
- El paquete debe terminar *_test
- Importar el paquete "testing" y referenciar con testing.T
- El método a evaluar debe empezar por Test*

Estar pendiente de que se ejecute o no, hacer que falle para probar.

***go test -bench***: Hace lo mismo pero con la posibilidad de insertar una función para saber el tiempo de corrida de la prueba.

Frameworks para pruebas unitarias:
- ginkgo y gomega: Se usa el símbolo omega (???)
- gobblin: Es otra librería para Unit Testing


# Acceso a bases de datos
Una forma de accesar a la base de datos desde Go es con el siguiente código:
```
package main

import (
	"database/sql"
	"fmt"
	_ "github.com/lib/pq"
	"time"
)

const (
	USER     = "platzi"
	PASSWORD = "platzi"
	NAME     = "platzi_test"
)

func main() {
	dbinfo := fmt.Sprintf("user=%s password=%s dbname=%s sslmode=disable",
		USER, PASSWORD, NAME)
	db, err := sql.Open("postgres", dbinfo)
	checkErr(err)
	defer db.Close()

	fmt.Println("--- Insertando valores ---")

	var lastInsertId int
	err = db.QueryRow("INSERT INTO users(username,email,created_at) VALUES($1,$2,$3) returning id;", "platzi_user", "email@platzi.com", "2020-12-09").Scan(&lastInsertId)
	checkErr(err)
	fmt.Println("Último id =", lastInsertId)

	fmt.Println("--- Actualizando ---")
	stmt, err := db.Prepare("update users set username=$1 where id=$2")
	checkErr(err)

	res, err := stmt.Exec("platzi_update", lastInsertId)
	checkErr(err)

	affect, err := res.RowsAffected()
	checkErr(err)

	fmt.Println(affect, "Filas afectadas")

	fmt.Println("--- Consultando ---")
	rows, err := db.Query("SELECT * FROM users")
	checkErr(err)

	for rows.Next() {
		var id int
		var username string
		var email string
		var created time.Time
		err = rows.Scan(&id, &username, &email, &created)
		checkErr(err)
		fmt.Println("id | username | email | created_at ")
		fmt.Printf("%3v | %8v | %6v | %6v\n", id, username, email, created)
	}

	fmt.Println("# Deleting")
	stmt, err = db.Prepare("delete from users where id=$1")
	checkErr(err)

	res, err = stmt.Exec(lastInsertId)
	checkErr(err)

	affect, err = res.RowsAffected()
	checkErr(err)

	fmt.Println(affect, "rows changed")
}

func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}
```

Para crear una ruta, entrar en ***conf/routes**, recuerda colocar ***App.funcion*** y crear una función en ***app/controllers/app.go*** crear la función que resuelva la ruta.

Con ***revel.INFO.Printf("Texto a mostrar en consola cuando se acceda a esta url")***

# Diseño de la vista de nuestra aplicación

Aquí en revel también podemos hacer cambios en caliente a excepción de las rutas.

En producción debemos crear una vista para los errores y se vean mejor, ello lo accedemos con **views/errors**.

Por convención el nombre del controlador debe ser igual que el de la vista. Para el ejemplo de platzi ***app/views/App/platzi.html***.

Se debe usar ***c.Render()*** Para renderear la vista.

Los Flash son tanto para mensajes de éxito como de error.

# Mostrar en la vista lo que tenemos en la base de datos

> Por cada ruta se agrega un htlm y una función en el mismo u otro paquete. Ejemplo: App.Index, App.Platzi, Refresh.Index, Polling.Room. Tods configurados en routes.

# Workshop: Concurrencia, gorutinas y channels

***Concurrencia***: Es la composición de cálculos de ejecución de forma independiente. Es una manera de esructurar el software, en particuar como una forma de describir código limpio que interectuará bien con el mundo real. ***No es paralelismo***.

Concurrencia no es paralelismo: [enlance](https://golang.org/s/concurrency-is-not-parallelis).

Características de la concurrencia como en Java o C:
- Un solo código, múltiples instancias ejecutándose.
- Un hilo por instancia (generalmente)
- Desarrollador describe explícitamente qué pasa y cuándo

Concurrencia en Go:
- Un solo código
- Una instancia en ejecución (sí, solo una)
- Memoria compartida (en el mismo programa compartirla con otra goroutina)
- Desarrolladores describen qué pasa al mismo tiempo.
- Go decide en tiempo de ejecución cómo pasa

Elementos principales concurrencia en Go:
- Goroutines: Describe las unidades que lo ejecutan independientemente
- Channels: Comunicación entre goroutines
- Select: Elige entre los channels

El paquete ***sync*** provee las primitivas de sincronización más avanzadas (sync.Mutex, sync.WaitGroup) para profundizar en las goroutinas a bajo nivel.

# Refactorizando el BackEnd


Goroutines:
- Es la ejecución independiente de una función
- Es muy barato. Puedes tener practicamente miles o hasta cientos de miles de goroutines
- ***No es un hilo***

Channels:
- Es un canal que provee una conexión entre dos goroutines, permitiendo la comunicación.

Resumen de las goroutines:
- Múltiples entradas
- Múltiples salidas
- Timeouts
- Fallas
- Son divertidas (mmm sí lo son)

Select: Es la manera de cómo podemos manejar los canales de forma que nosotros mismos definimos de tal forma en que estamos manejando el canal que queremos. Terminar la ejecución, terminar canales, etc. Evaluar el contenido del canal y dependiendo de lo que tiene ejecutará un código.

Función anónima: Es una función que no tiene nombre y se define en plena línea de código. Ejemplo:

```
go func(){
    // Toda la función
}("Variable input")
```

Para tener un orden, podemos usar el paquete ***container/list*** que usaremos en el websocket del chat.

***Tres elementos principales***:
- Goroutines (go keyword) describe las unidades que lo ejecutan independientemente.
- Channels (chan type) comunicación entre goroutines
- Select elige entre los channels. Es una manera para elegir qué correr según el contenido de los canales.

***WaitGroup*** Controlar tiempo de espera a un grupo de funciones en goroutinas.

Elementos el chat:
- Usuario
- Evento
- Chatroom
  - Suscripción
  - Publicación
  - Descripción

Tipos de actualización de mensaje:
- Refresh
- Polling
- WebSocket

En Revel podemos ejecutar pruebas unitarias por terminal o bien agregando en la ruta ***@test***

# El uso de goroutines

Es buena práctica limitar la capacidad de los canales para tener un control. 

# WebSockets en Go
Para poner alias en la importación: *** import alias "librería"***

Para la creación de API con Go, beego tiene la ventaja de crear un proecto. Otras opciones son: Martini, echo (Este es el que recomienda la gente de GygaCode)

# Conclusiones
- Es buena práctica limitar la capacidad de los canales
- En vez de reescribir las aplicaciones hechas, usan a Go como microservicios
- Las presentaciones del profesor se hacen con [Presents](http://halyph.com/blog/2015/05/18/golang-presentation-tool.html). El cual se escribe en Markdown

# Notas importantes:
- [Recuperar la contraseña en postgres](https://alasombra.net/blog/2010/09/postgresql-recuperar-la-contrasena-de-postgres)
- El _ al importar un paquete, Ejemplo: '_ "upper.io/db/postgres"' Es para invocar el init de la librería y se inicie al inicializar.
- Status http [https://golang.org/net/http/status.co](https://golang.oeg/src/net/http/status.go)
- Enlace del repositorio [gopro-chat](https://github.com/platzi/gopro-chat)
- Bootsrap lo desarrolló twitter, el profesor usa este framework.
- Es buena práctica crear un paquete por cada estructura ya que de esta forma nos ayudará a localizar errores.

> Siempre es bueno saber las causas de nuestros errores. El error del snipper en la clase "Mostrar en la vista lo que tenemos en la base de datos" para el html.
- Haciendo ***// TODO: Mensaje*** Podemos en un directorio más arriba agregar ***grep -rn "TODO" .*** y de esta forma nos aparecerá en la consola el mensaje. Ideal para pendientes. Algo del framework en el ***var HeaderFilter*** para evitar XSS. Que está por defecto.
- Cuando retornamos un nil no va a buscar la vistas
- Hay momentos en que Revel compila internamente, esto dura un poco. Pero no debería durar mucho tiempo, en ese caso revisar las rutas o cambios.
- Para llevar una variable a otro controlador: ***var user = "Ivan"*** y ***eturn c.Render(user)*** para usar en el html ***{{.user}}
- Para recibir y retornar el tipo de variables en una función con un canal. Se hace ***func Inpunt(input <-chan string) <-chan string{}***
