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

# Creación de una instancia

Una instancia es una máquina virtual para AWS.

En AWS Marketplace se tiene un buscador de imágenes.

> Nota: Ciertas imágenes no son compatibles con ciertas instancias.

Una subnet es una red privada interna.

La que la IP pública no cambie hay que usar una elastic ip. Porque cuando se reinicia el servidor se pueden cambiar la IP.

Con "Protect against accidental termination" es para tener que hacer un doble paso para terminar el servidor y así evitar hacerlo accidentalmente a las 3:00 am

Los security group son para la apertura de puerto, aquí se abre el puerto 22. Lo ideal es asignar una IP o un rango de IPs de la cual accederemos.

No colocar como nombre de Security Group que comience por "sg*"

Si se tiene una IP dinámica hay que cambiar el SG cada vez que cambie.

# Modificación de un Security Group

Para habilitar el puerto 80 y el 443

Inbound, conexiones entrantes
- HTTP (80) Para todo el mundo
- HTTPS (443) Para todo el mundo
- Se abren para IPV4 y IPV6
Outbound, conexiones de salida
- Cualquier puerto puedan lanzar información

> Nunca está de más verificar dos veces los puertos abiertos.

# RDS Dashboard

Para ello hay que entrar en el servicio RDS para crear una instancia de base de datos, AWS hará todo y nos otorgará un endpoint.

Podemos tener un clusters, snapshops no de la base de datos si no de la instancia de la base de datos aunque esto se puede programar.

En Platzi se hacen respaldos diarios y cada uno se almacena por 30 días. Cada aplicación puede tener un respaldo cada cierto tiempo pero se recomienda diario si es una aplicación grande.

- Paremeter groups: Conjunto de parámetros que definen una bases de datos específica.

# Aurora

Es una base de datos creada por Amazon que promete compatibilidad con MySQL y PostgreSQL.

Te promete hasta 5 veces más rendimiento que una base de datos MySQL tradicional y hasta 3 veces más que una base de PostgreSQL a un precio más barato. Dependiendo de la instancia, a veces MySQL puede ser más barata.

> Cluster: Bases de datos distribuidas.

Al crear la instancia de aurora debemos escoger con cuál motor de base de datos va a ser compatible.

# Creando de una instancia de bases de datos en RDS

Para bases de datos relacionales hay:
- Aurora
- MySQL
- MariaDB
- PostgreSQL
- Oracle
- SQL Server

También las version (5.6), el tiempo de Backup para retener (a más días más cobran), hay monitoreo, AWS actualiza la versión en el tercer nivel.

# Instalación de Nginx

Descargado la imagen, editar los permisos para que solo pueda ser usado por los usuarios

chmod 0600 curso-aws.pem

Nos conectamos

ssh -i curso-aws.pem usuario@ip del servidor

Actualizar repositorios

sudo apt-get update

sudo apt-get upgrade (para actualizar)

> Es importante siempre tener actualizado el sistema por temas de seguridad

sudo apt-get install nginx

sudo systemctl status nginx (para verficar que el demonio funciona)

Si ingresamos en el puerto 80 (colocar la IP pública), ngnix debe salir con una página estática.

cd /var/www/html -> aquí debe estar el archivo

cd /etc/nginx -> Los archivos de configuración

> Dentro de ésta, la carpeta ***sites-enabled*** muestra las páginas que están habilitadas donde sus archivos son un enlace simbólico a la carpeta ***sites-available***

Dentro de la carpeta /etc/nginx/sites-available está el archivo ***default** Que es el archivo de configuración donde podemos habilitar PHP, Proxy reverse o el puerto 443 que nos permite tener certificado SSL.
# Instalación de PHP
Para tener en cuenta: La dependencia que uno instala en un servidor cuando se está utilizando computación en la nube, depende mucho el tipo de aplicación que uno necesite.

No es lo mismo instalar las dependencias de WordPress que las de Magento.

Para ver que la ejecución de PHP se está realizando correctamente:
sudo systemctl status php7.0-fpm

Para configurar de que Ngnix renderice un php.index

cd /etc/ngnix/sites-available
sudo vim default

En la línea donde dice index, al lado poner index.php

Para verificar la configuración

sudo nginx -t

En /var/www/html crear phpinfo.php

```
<?php
phpinfo();
?>
```

sudo systemctl reload nginx

ip-de-AWS/phpinfo.php Debería salir toda las librerías y configuración de php.

# Instalación y despliegue de Wordpress

Para iniciar sesión en AWS
ssh -i curso-aws.pem usuario@ipPublica

Configurar nginx para que ejecute wordpress

--- Colocar imagen

Para instalar wordpress se hace en la carpeta /var/www/html con wget

Para descomprimir `tar xvf archivo.tar.gz`

Crear un usuario para que no tenga privilegios root o acceso desde afuera
`sudo adduser --disabled-password --disabled-login wordpress`

esa es la carpeta de wordpress

Verificar el usuario con *cat /etc/passwd*

Agregar la carpeta el usuario

sudo chown -R wordpress:www-data wordpress/

Asignamos la carpeta raíz de nginx en */etc/nginx/sites-available/*

root /var/www/html/wordpress;

sudo systemctl reload nginx

En el navegador entrar dentro de la carpeta raíz y accederemos a wordpress.

Para la base de datos entramos en la instancia de RDS y de allí tenemos el endpoint (ruta de la base de datos) y el usuario, podemos muy bien usar ese nombre de usuario.

Al crear la instancia RDS creamos nuestra contraseña.

En EC2 agregar en el Security Group el puerto de MySQL, usaremos la ip privada para que pueda editar el archivo que worpress necesita en su base de datos.

# Terminando la instalación de WordPress

Para solucionar el error de que WordPress no puede editar un archivo:

`sudo find /var/www/html/wordpress -type d -exec chmod g+w {} \;`

WordPress hizo casi todo, el blog ya quedó hecho.

***Nota***: Ver el curso de WordPress.
