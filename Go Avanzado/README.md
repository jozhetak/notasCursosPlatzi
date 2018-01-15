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

# Acceso a bases de datos

# Diseño de la vista de nuestra aplicación

# Notas importantes:
- [Recuperar la contraseña en postgres](https://alasombra.net/blog/2010/09/postgresql-recuperar-la-contrasena-de-postgres)
- El _ al importar un paquete, Ejemplo: '_ "upper.io/db/postgres"' Es para invocar el init de la librería y se inicie al inicializar.
- Status http [https://golang.org/net/http/status.co](https://golang.oeg/src/net/http/status.go)
