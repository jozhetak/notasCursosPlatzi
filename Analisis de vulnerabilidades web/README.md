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

El método PUT se usa para subir archivos hacia una aplicación, como imágenes o archivos de escaneo.

El método DELETE se usa para eliminar información del servidor de archivos.

El método TRACE y el método TRACK se usan para hacer debug, no debe usarse en entornos de producción.
