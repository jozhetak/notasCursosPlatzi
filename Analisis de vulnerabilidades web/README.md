# Notas del curso de análisis de vulnerabilidades web

Profesor: Carlos Lozano

# Funcionamiento de aplicaciones web
## Funcionamiento de las aplicaciones web
Vamos a enfocarnos en seguridad web viendo los puntos de integración que tienen nuestras aplicaciones como posibles puntos de ventaja para obtener y explotar vulnerabilidades y llegar a resultados que el desarrollador no había tenido en cuenta el proceso del desarrollo del software.

Cuando empresas, como las bancas en línea, usan software de terceros para no tener que contratar desarrolladores deben comprar correcciones de fallos y a us vez realizar pruebas de pentesting.

> Nota: Features son características en inglés.

El usar frameworks de desarrollo web o bien orm no necesariamente nuestras aplicaciones son completamente seguras. Por lo que es recomendable realizar pruebas de pentesting para asegurarnos de la información de nuestras aplicaciones.

## Peticiones Http

La base fundamental de las aplicaciones web son las peticiones HTTP.

¿Qué es una petición HTTP? Es la forma en que se comunican clientes con servidores.

El cliente puede ser un computador, un navegador web, un celular, etc.

El servidor es el lugar donde se aloja nuestra aplicación web o un servicio.

El cliente solicita que el servidor le envíe información, y el servidor envía una respuesta.

La herramienta que estamos usando para capturar la petición HTTP se llama Burp Suite.

---

Hay muchos tipos de peticiones, los dos principales son GET y POST. Recibir y enviar peticiones HTTP.

> Nota: Hay diferentes versiones del protocolo http

***En BurpSuite***
- Host: Donde nos conectamos, puede ser dominio o IP.
- User-agent: Huella del cliente que estamos usando para conectarnos
- Accept: Tipo de contenido que vamos a poder obtener. Va a variar mucho entre las distintas aplicaciones.
- Cookie: Es una variable que va a guardar una información que la aplicación va a utilizar para lo que sea como por ejemplo la ubicación.


## Clientes Web y servidores

Hoy en día las aplicaciones web son muy ricas en contenido y en lo relacionado con la interactividad que tienen los usuarios.

Un cliente web es cualquier tipo de elemento que puede interactuar con una aplicación, por ejemplo los navegadores web, sistemas gps, un vehículo que obtiene información acerca de su ubicación etc.

Los servidores web son componentes de software que se encargan de mostrar, interpretar, interactuar y presentar contenido al cliente.

--- 

Los servidores web contienen la aplicación y la despliegan.

También hay servidores de solo base de datos.

Hoy en día para soportar múltiples conexiones, se utilizan muchos servidores y un balanceador de carga.

Los más conocido son Apache y iJS (???)

# Metodologías para revisión de aplicaciones web
## Metodologías para la revisión de aplicaciones web

Existen diferentes metodologías que se pueden aplicar para hacer diferentes tipos de revisiones de seguridad.

***Metodología clásica***: Simular un ataque como si fuéramos un usuario mal intencionado externo, en este tipo de metodología se requiere hacer una búsqueda inicial de vulnerabilidades que luego debemos explotar. Finalmente hacemos el ataque y borramos todas las pistan que nos vinculen con él. Muchas veces, el cliente nos va a pedir que no borremos las huellas.

***Metodología enfocada en revisión de aplicaciones***: Contextualización, tomar de las personas que diseñaron y desarrollaron la aplicación todo el contexto del software y luego hacemos un análisis estático, es decir hacer una revisión línea a línea del código que nos han proporcionado para detectar allí posibles vulnerabilidades. Finalmente se hace un análisis dinámico, en el que se monta la aplicación en un ambiente lo más parecido al ambiente de producción para estudiar su comportamiento. 

- Análisis estático: En él tenemos acceso al código fuente y allí verificar las fallas o código obsoleto.
- Análisis dinámico: Recreamos el sistema de producción.

***Metodología OWASP***: Es un proyecto abierto que busca generar documentación y herramientas para generar conocimiento relacionado a la seguridad web con diferentes variantes de tecnologías y plataformas.

Con OWASP tendremos una metodología que nos dirá que la aplicación es vulnerable o noCon OWASP tendremos una metodología que nos dirá que la aplicación es vulnerable o no.


***Metodología para Bug Bounty Hunting***: Son concursos abiertos para que sea atacado una aplicación y será recompensado.

Dependiendo del país, puede se pueden llamar "auditoría" o "pruebas de penetración"

## HTTP Proxy

La herramienta que vamos a usar para hacer el análisis de nuestras aplicaciones es un HTTP Proxy, es una herramienta de software que intercepta todas las solicitudes y respuestas de clientes y servidores. Los hay orientados a desarrollo y otros a seguridad.

Para crear un proxy en firefox:
Preferencias-> Avanzadas -> Settings (network)

Con un proxy toda la información de nuestra computadora a internet pasa por allí que en este caso será interpretada por un software instalado en nuestra computadora.

En el caso de empresas, todo el interne pasa por un proxy para de esa forma controlar el tráfico de red de las mismas.

> Nota: Todos los proxy usan le puerto http 8080

!()[proxy-1.png]

!()[proxy-2.png]

El más sencillo se llama Paros Proxy

Desde Paros podemos interactuar directamente con el BackEnd de la aplicación sin limitarse por las limitaciones impuestas en el FrontEnd.

Al darle click contrario en el historial y luego en Resend podemos interactuar directamente con la aplicación desde el programa. De esta forma podemos saltarnos limitantes de seguridad del FrontEnd hecho por Javascript.

## Entorno de desarrollo y herramientas a usar durante el curso.

Ya es hora de que empecemos a practicar todos los conceptos que hemos revisado hasta este momento. Para esto hemos preparado dos aplicaciones que están en dos máquinas virtuales usando la herramienta VMWare.

Una de ellas es una aplicación vulnerable, una vez realizado. Se dejará un reto. 

## Instalación y configuración de las máquinas virtuales en Windows

Para hacer las pruebas de las diferentes herramientas que usaremos en el curso para la detección y explotación de vulnerabilidades vas a necesitar descargar e instalar VMWare Workstation player en tu equipo. Puedes hacerlo desde (aqui)[https://www.vmware.com/products/workstation-player.html]

(Máquinas virtuales del curso)[https://www.dropbox.com/sh/wxop0zn2s6o0pzk/AAB4692pgB6JCTjXpFGpYb11a?dl=0]

(Maquina 1)[https://drive.google.com/file/d/1qIBQFnFLLxc15XvaYIvW2cmwWJ9NCniB/view]

(Maquina 2)[https://drive.google.com/file/d/1cjhAD0MS7riStIBab8XDRim1Pbdcae-i/view]

User: platzi
Password: platzi

Una vez instalado, iniciar en el navegador (el mismo usado en el curso de Pentesting) ip/dvwa
User: admin
Password: password

## Conceptos fundamentales de protocols y tecnologías

Protocolo HTTP - Como habíamos visto es el protocolo mediante el cual funciona toda la tecnología web. Todos los navegadores tienen un protocolo, es decir las instrucciones, elementos y estructura que debe tener cada petición y respuesta HTTP para que cualquier navegador sea capaz de interpretarlo.

Vamos a ir a la aplicación web que ya tenemos en nuestra maquina virtual, y usando un proxy HTTP vamos a empezar a interceptar peticiones para analizarlas.

> Un protocolo es la forma cómo se comporta una tecnología.

En BurpSuite hay una variable llamada security que dice el nivel de seguridad de las aplicación web. También nos dice si usa servidor único o un balanceador de carga también la versión la distribución de linux del servidor.


## Metodos HTTP

En esta clase vamos a ver los métodos principales de se usan en el protocolo HTTP.

El método GET es para obtener un recurso

El método POST normalmente lo vamos a encontrar en formularios que nos permiten hacer ingreso de datos, como formularios de registro o de inicio de sesión. El método POST es un método que nos permite enviar información hacia una aplicación.

El método PUT se usa para subir archivos hacia una aplicación, como imágenes o archivos de escaneo. Esto es de forma binaria, ejemplo imágenes o diversos archivos.

El método DELETE se usa para eliminar información del servidor de archivos.

El método TRACE y el método TRACK se usan para hacer debug, no debe usarse en entornos de producción. Si por error se deja activo, podemos tener inforación de las versiones de tecnologías. 

> Las aplicaciones en PHP tienen a ser más sencillas de vulnerar a otros.

El método CONNECT sirve para la autenticación de usuarios por un puerto.

Con BurpSuite podemos saber con qué metodos y el nombre de las variables que se envía.

Usando **user_token** podemos evita que se hagan múltiples ataques de fuerza bruta por cliente a usuario y contraseña. Sirve como id de usuario.

> Los que hacen las aplicaciones para conectarse con los servidores es a través de puentes (que tienden a ser más seguros) pero éstos son vulnerables.

### Repaso de uso

Para el uso, utilizamos metasploitable usuario:"user", password:"user".

Una vez entrado, buscamos la ip y nos conectamos a ella. Dentro de la misma podemos tener acceso a las configuraciones de distintas vulnerabilidades dispuestas a ser explotadas.

> Un proxy es para que todas las solicitudes se envíen hacia un equipo y de allí se envíen hacia internet. Lo que hacemos con **BurpSuite** es enviar toda la información a ese software y luego de allí pasarlo a internet.

En BurpSuite, entrar en la configuración de firefox configurar manualmente el proxy usamos el localhost:8080 (que es el que usan todos los httproxy) marcar **Use this proxy server for all protocols** Porque hay aplicaciones que utilizan protocolos https.

> En BurpSuite el user-agent es la información del navegador. En la cookie estará la variable de dificultad y la de id de sesión de usuario.

En **HTTP history** tendremos el historial de peticiones http. En la opción de Response, el apartado de **Server** nos va a decir si el servicor que nos respondió es un equipo, uno virtualizado o bien un balanceador. El elemento **Expires** es la fecha de expiración de la cookie.

> Sabiendo la versión del servidor de respuesta podemos estar al tanto de los fallos de seguridad.

> Debemos ocultar completamente las tecnologías y versiones para que no se haga uso indebido de ellos. (Desactivar TRACE y TRACK).

# Código de error HTTP

- 200: OK.
- 300: Informarción del servidor.
- 400: Error en la aplicación cliente.
- 500: Error en el servidor.

> Si intentamos una autenticación incorrecta seremos redireccionados a la página de authenticación.

# Proxy HTTP

> Es importante saber usar distintas herramientas porque siempre nos vamos a encontrar con compartiamientos distintos.

- Burp Suite: Pensada para análisis de seguridad, pero a diferenia de ZAP es de pago. Cuando se cancela aparace la pestaña **Scanner** quien automatiza ciertas funciones, pero éstas se pueden hacer manualmente. En la versión gratuita no se pueden guardar sesiones. La parte más importante es la de Intruder, donde podemos ingresar carateres aleatorios o a través de diferentes listas para saber el comportamiento de las aplicaciones de forma automatizada que nos ahorrará mucho tiempo durante el análisis. Su principal característica es que está orientado a experimentos, donde podemos hacer nuestras propias extensiones o bien descargarlas.
- Fiddler: No está orientado a seguridad sino al desarrollo web, para hacer debug. Está orientado a tecnologías .NET. Va a interpretar información que viaja en binario, como las de skype. Podemos hacer simulaciones para detectar fallas.
- ZAP Proxy: Desarrollado por OWASP. Parte de la base de paros pero enfocado a seguridad. Lo primero que preguntará es si queremos guardar la información de la sesión. Hay análisis que duran semanas. Podemos definir que cada que carguemos un formulario ingrese datos de forma automática. Nos permite generar reportes. Explorar a profundidad sitios web. Está la opción de **Fuzz** para ingresar ciertas cadenas.
- Paroz Proxy: Es el más sencillo de todos. Es útil cuando analizamos tecnologías como flash. Ya que la información no será modificada y se mantendrá binaria. Toda la información de la sesión de trabajo se elimina.
- Charlse Proxy: Es de pago, pero nos va a ayudar mucho a revisar aplicaciones móviles. Tiene precargado User-Agent para que haga solicitudes de un client distinto al que estamos utilizando. Ejemplo que nuestra aplicaciones use aplicaciones para móviles, tablets o navegadores. Muy bien una entidad bancaria puede tener vulnerabilidades en un navegador en particular.

# Explorando una aplicación con NMAP

> Hay una opción de NMAP en entorno gráfico pero por terminal hay más opciones. Los puertos son como puertas de acceso de los usuarios al servidor.

- Puerto 80 -> HTTP (Información en texto claro)
- Puerto 443 -> HTTPS (Información cifrada)

nmap -> Puedes ayudarnos a detectar vulnerabilidades.

npmap -A 192.168.1.23
-A -> Todas las opciones controladas.
Dirección -> Es la dirección ip de la aplicación, puede ser también un dominio.

Con el comando anterior podemos ver los puertos abiertos y las vulnerabiliades que existen.

Resultados del análisis:
- Tiene habilitado el puerto 80 -> El cual nos indica que podemos hacer solicitudes HTTP.
  - Nos da información del servidor que ejecuta la aplicación. No siempre esta información es correcta porque es un banner. Algunos desarrolladores modifican este banner para confundir a los atacantes.
- Mediante un análisis probabilísticos define el SO.
