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
- Accept: Tipo de contenido que va a ser aceptado.

