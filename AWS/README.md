# Introducción a Amazon Web Services
## Introducción a Cloud Computing

Vamos a aprender la capa de infraestructura como servicio (IaaS), aquí podemos dejar de preocuparnos por el hardware en nuestros proyectos y podemos utilizar alguno provisto por un tercer, en el caso de este curso por AWS, además existe PaaS, dónde tu puedes utilizar una plataforma en la cual brindar tus servicios y también SaaS directamente utilizando servicios de terceros podrías utilizar softwares terminados para tu comodidad, por ejemplo Gmail.

- IaaS: Infraestructure as a service. Se puede acceder al sistema operativo.
- SaaS: Software as a Service. Como Gmail, solo podemos usar la aplicación ya creada.
- PaaS: Platform as a Service. Para hacer deploy de una aplicación hecha en Java, PHP, Go, etc.

> Se recomienda tener un plan b por cualquier problema, en caso de que debas migrar a otro proveedor de Cloud Computing.

Computaciones de confianza:
- AWS (lo usan en platzi)
- Azure (lo usan en platzi)
- DigitalOcean (lo usan en platzi, recientemente usado para pequeños servicios)
- Google Cloud Platform
- Openshift

---

Con AWS se puede integrar una nube pública (cloud computing) y una nube privada (servidor dentro de la empresa).

En AWS hay servicios que se pueden contratar por horas y por días.

Tener en cuenta la seguridad de datos. De qué tan seguro pueden ser tu proveedor.

# Introducción a Amazon Web Service
Amazon ofrece diferentes tipos de servicios siendo el más grande del grupo computación, aquí dentro tenemos EC2 y este servicio que vamos a aprender a utilizar.

---

Amazon fue el primero de computación en la nube

Computación:
- EC2: Instancias de servidores
- Route 53: Administrar dominios DNS
- VPC: Crear redes internas para conectar instancias EC2

Almacenamiento:
- CloudFront: CDN para archivos estáticos o backup
- Glacier: Barato para guardar backup, bases de datos de nóminas por años.
- S3: Guardar archivos sin importar el tipo, imágenes, vídeos, etc. 

En S3 hay disponibilidad inmediata en Glacier hay que esperar un tiempo.

Bases de datos: (Todo el mantenimiento lo va hacer Amazon)
- DynamoDB:
- RDS: Oracle, MySQL, PostgreSQL.
- ElastiCache

Despliegue de aplicaciones:
- CloudFormation: Con plantillas con script, creación de instancia y servicios. (Como lo visto en el curso de DevOps)
- CloudWatch: Monitoreos de las instancias, bases de datos, CDN, etc.
- IAM: Todo el tema de seguridad de nuestra cuenta
- OpsWorks:

Análisis de datos: (Big Data)
- MapReduce
- Kinesis 

Servicios adicionales:
- Cloud Search: Creación de buscador con baja latencia para nuestras aplicaciones.
- Transcoder: Procesamiento de vídeo
- SQS: Colas de procesamiento como pagos, o API
- SES: Servicio de correos y SMTP desde AWS

Todos estos productos puedes muy bien crearlo desde EC2, pero lo mejor es minimizar los costos sin necesidad de inventar la rueda.

# EC2 Compute
EC2 Compute, nos permite crear instancias o máquinas virtuales en las que podemos elegir la capacidad de disco duro, ram y cpu.

Tenemos diversas opciones como Ubuntu 16,4 y de ahí instanciarla tantas veces como quiera.

Los volúmenes son los espacios de almacenamiento expandible que podemos agregar, de hecho  el volumen de una instancia no es lo ideal para guardar información, por eso podemos utilizar un EVS donde podremos persistir la información importante de nuestra aplicación.

Instancia: Es un entorno con sistema operativo virtualizado.
Amazon Machine Images: Plantilla preconfigurada para su instancia, esta plantilla contiene el sistema operativo y los paquetes adicionales.

Volumen de almacenamiento de la instancia: Es una unidad de almacenamiento temporal. Para cuando el disco duro principal de la aplicación falle, esto es como un respaldo.

Virtual Private Network: Red local privada. La privada para crear un clouster.

# RDS Database
Es un servicio de base de datos relacional llamada aurora (de amazon), pero también tiene MariaDB, PostgreSQL...

Hay dos precios:
on-demand: Pagas lo que consumes
Reserved: Se paga todo el contrato desde un principio.

Por lo general, los más usados son los de EE.UU

# Dashboard de Amazon Web Services AWS

Si estás buscando un producto que no aparezca en el dashboard escribe a soporte para que lo habiliten.

Toda la documentación de AWS está en inglés.

# EC2 Dashboard

(status.aws.amazon.com)[https://status.aws.amazon.com] Para revisar el estatus de los datacenter.


Los ***Spot*** son instancias subastadas de recursos sobrantes muy baratas pero no aseguran disponibilidad por más de una hora.

***Reserved Instances*** Son las instancia que uno renta por un tiempo definido.

***Dedicated Host*** Son servidores dedicados, ideal para cuando queremos más recursos.

En Images:
- AIMs: Definir qué necesitamos o queremos para nuestra instancia. Hay un market place donde podremos encontrar software libre o comercial.

En Elastic Block Store: 
- Volumenes: Discos duros disponibles de otras instancias
- Snapshots: Captura de los volúmenes

En Network & Security
- Security Groups: Son por instancia, para habilitar puertos. Es importante no compartir los security groups con otras instancias.
- Elastic IPs: Genera ip pública y las asigna a una instancia o a una interfaz de red.
- Key Pairs: Para las llaves SSH para conectarse a las instancias.

