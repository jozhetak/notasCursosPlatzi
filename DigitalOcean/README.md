# Introducción al Curso de Digital Ocean

Este proveedor se caracteriza por tener precios bastante económicos y estar diseñado para desarrolladores. Es decir, todo lo que hacen y sus características lo hacen fácil para los usuarios que están orientados al desarrollo.

Block Storage: Nos permite almacenar nuestros archivos en un lugar aparte de nuestro droplet. Expandir el disco duro.

Object storage: Almacenar archivos los cuales podrán ser accedidos desde una interfaz http. Como dropbox para compartir a través de un enlace http

Teams work logether: Para crear múltiples usuarios que tendrán permisos de crear o no otros droples.

Load balancing as a service: Un endpoint donde podemos tener múltiples droplets detrás de ese load balancer sin necesidad de tener que configurar un HAproxy o un nginx o un apache para poder hacer esta funcionalidad.

Monitoring and alerting: Obtener métricas de CPU, RAM, red interna, etc. Y crear alertas que pueden ser enviadas a slack. Por ejemplo cuando la aplicación esté consumiendo más del 80% del cpu y tomar medidas como crear otro droplet o bien escalar este dropletservice: Un endpoint donde podemos tener múltiples droplets detrás de ese load balancer sin necesidad de tener que configurar un HAproxy o un nginx o un apache para poder hacer esta funcionalidad.

Monitoring and alerting: Obtener métricas de CPU, RAM, red interna, etc. Y crear alertas que pueden ser enviadas a slack. Por ejemplo cuando la aplicación esté consumiendo más del 80% del cpu y tomar medidas como crear otro droplet o bien escalar este droplet. Es muy importante estarlo monitoreando y crear alertas.

Lightning fast network: Una buena velocidad entre la red de los droplets.

La instancia más barata es la de $5 con 512MB de ram y 20GB de SSD. Con esa memoria es muy poca para correr wordpress con plugin pero podemos crear un swap y utilizar 1GB de SSD para agregarlo como ram, aunque no será tan rápida.

DigitalOcean cobra por horas, aunque tomes 15 minutos, igual te lo cobrará por una hora.

> No hay DataCenter en latinoamérica, pero en platzi lo montan en todos los DataCenter de norte américa.

# Registro en DigitalOcean

Acepta tarjeta de crédito y Paypal. Con Paypal es más sencillo porque ya estás prepagando una cantidad que será un saldo positivo.

# Servicios de DigitalOcean

Droplet es un nombre de mercadeo que quiere decir que es una máquina virtual o un instancia.

DigitalOcean no provee imágenes de windows.

> Recuerda que se puede desplegar un droplet desde la terminal con un API. Tiene ejemplos en Go.

***Features***
- Resize: Escalar el droplet
- Backup and snapshot: En caso de que nuestro droplet falle
- Snapshot transfer: Transferir snapshot entre cuentas, por ejemplo de si quieres pasar un droplet de tu cuenta personal al de una empresa.
- Monitoring: Nos lo ofrece ya por defecto.
- User data: Podemos pasar información del usuario para personalizarlo desde el inicio.
- Enterprise SSDs: Tener discos duros en estados sólidos con mucho más velocidad.
- 40GbE: Transferencia en la red interna.
- KVM: Hypervisors optimizado para nuestro droplet. Es un software que DigitalOcean instala en nuestro droplet para virtualizar de manera más optimizada.

Hay dos tipos de droplets:
- Los estándar: CPU virtualizado.
- Los que usan más CPU: CPU dedicado.
- Los que usan más RAM: CPU virtualizado.

# Servicios de DigitalOcean: Block Storage

Es para tener un SSD como externo a nuestro droplet.

- Highly available: En caso de que le pase algo a nuestro droplet, lo que hay dentro del volumen estará a salvo.
- Live resize: Escalar el SSD sin necesidad de reiniciar el droplet.

Todo esto se puede hacer desde el API de DigitalOcean.

Acá el precio se cobra por mes, lo estemos o no usando.

# Servicios de DigitalOcean: Spaces

Estos son los Object Storage

Esto es para guardar toda la información que queramos sin un límite establecido, estaremos pagando por la cantidad de GB que estemos consumiendo al mes. Lo mínimo es de $5 por mes.

No importa cuánto subamos sino lo que descarguemos de spaces.

***Tenemos un Try de 2 meses***

Es compatible con ***S3 de AWS*** Por lo que si cambiamos solo debemos cambiar el endpoint y pasar los archivos.

# Panel de control de DigitalOcean

El loadbalancer tenemos un precio adicional.

También se debe crear un firewall para Magento.

> Podemos ofrecer el servicio de deploy de DigitalOcean a través del API.

# Creación de un Droplet

Las imágenes que vienen con aplicaciones ya instalada, usan ubuntu.

> Hay una imagen de Machine Learning que viene con Jupyter, Python3, TensorFlow, Scikit y PyTorch. Para hacer ejercicios de Machine Learning.

Hay imágenes de Docker, Django, LAMP, MongoDB, MEAN, NodeJS, WordPress... con todas las aplicaciones ya instaladas desde el inicio.

Con *Private networking* para que entre los droplets hablen entre ellos sin usar internet, como por ejemplo que las bases de datos no tengan acceso a internet.

User data: La personalización de la hora por ejemplo durante la instalación.

Seleccionar *Monitoring* para contar con un monitoreo, si no se selecciona el monitoreo será muy básico.

Se debe crear una llave SSH y subir la llave pública.

Con ***Dokku*** es para crear un PaaS como el que usa heroku.

> Nota: Las gráficos del monitoreo no son en tiempo real, requieren de un tiempo para que sean ejecutadas.

# Panel de control de un droplet: Gráficas

Disk I/O: La cantidad de lectura y escritura que hace nuestra aplicación en el disco duro.

Cuando seleccionamos la opción tendremos, los gráficos de memoria, el uso de disco duro y una lista de las aplicaciones que consumen más CPU y RAM.

# Panel de control de un droplet: Accesos

Para acceder a una consola desde el navegador. (Se recomienda no usar y deshabilitar el acceso por usuario y contraseña)

> Solo usar Launch Console, si y solo sí hay una emergencia y no tengamos un computador con nuestro SSH

*Reset root password* Es para que por correo nos envíen una contraseña root de nuestro droplet. Se recomienda no usar frecuentemente porque deshabilita la conexión por ssh. Usarlo solo cuando perdamos la llave.

# Panel de control de un droplet: Power

Power of: Apagar el servidor, se recomienda hacerlo por ssh.

Power cycle: Hard reset de nuestro drople

# Panel de control de un droplet: Volumenes

Esto es para la creación de volúmenes.

Por ejemplo se puede tener bases de datos en volúmenes y crear un snapshot para llevarlo a otro droplet

# Panel de control de un droplet: Volumenes

Esto es para la creación de volúmenes.

Por ejemplo se puede tener bases de datos en volúmenes y crear un snapshot para llevarlo a otro droplet

# Panel de control de un droplet: Volumenes

Esto es para la creación de volúmenes.

Por ejemplo se puede tener bases de datos en volúmenes y crear un snapshot para llevarlo a otro droplet.

Desde el dashboard podemos asignar a qué droplet estará asignado el volumen.

# Panel de control de un droplet: Configurar volúmenes

El la sección de volúmenes entrar en "more-> config instruction" dese allí tendremos las instrucciones para configurar ese volumen en el droplet.

Recuerda que un volumen es un disco duro que estamos asignado a nuestro droplet.

Por seguridad hay un límite en la cantidad de droplet por cuenta. Para aumentar dicho límite se debe comunicar con soporte.

# Panel de control de un droplet: Escalar un droplet

Un escalamiento vertical, es para agregar más performance como RAM, CPU o el tipo de máquina. Se puede escalar cuando más se necesita y bajar cuando no se necesita.

CPU and RAM only: Es reversible
Disk,CPU and RAM: No es reversible

Para escalar debemos apagar nuestro droplet con poweroff (desde terminal ssh)

Entramos en el Dashboard y presionamos el botón *power on* para encender el droplet.

> El profesor usa ***htop*** para ver el consumo de cpu y ram.

# Panel de control de un droplet: Backups y Snapshots

Los Backups son de manera automática si lo tienes habilitado.

Cada semana crea un snapshot de un droplet, el automático pero tiene un costo de 1 dólar por mes.

Pero puedes hacer un snapshots manualmente cuando vas hacer un cambio que crees que pueda dañar el droplet.

# Panel de control de un droplet: Networking y Firewall

Esto es para administrar la red de nuestro droplet. Podemos administrar la red pública o privada con otros droplets. Esto es para crear un cluster, es decir varios droplets conectados en una red interna, un droplet de bases de datos que no tendrá conexión a internet.

> Recuerda que la tendencia actual es separar la bases de datos, backend y frontend.

Una medida es conectar por ssh con IPv4 y servir el puerto 80 con IPv6

También podemos crear IPv6

De igual forma, podemos administrar nuestro firewall. Por seguridad eliminar elimina el protocolo ICMP, esto es para deshabilitar el ping

Esto es para la configuración con Magento, es bueno repasar el curso de Seguridad informática para establecer un buen firewall y evitar ataques o bien minimizarlos.
En Inbound Rules: SSH(22), HTTP(40), HTTPS(443) [Los últimos dos no usar]

En Outbound Rules: All TCP y all UDP 

# Panel de control de un droplet: Kernel

En droplet como centos podemos cambiar la versión del kernel. Es importante para aquellos software que requieren un kernel en específico ara que funcione. En Ubuntu 16.04 no se puede cambiar.

Recovery: Para instalar un kernel en modo de recuperación. Y cuando vuelva a iniciar el droplet se abre en modo de recuperación y desde ***access*** acceder al droplet para repara el sistema.

# Panel de control de un droplet: History, Destroy y Tags

History: Desde aquí tenemos aquí un acceso a los logs del dashboard.

Destroy: Destruir un droplet completamente o reconstruir con otra imagen. (Se perderá toda la información en el droplet pero no la del volumen, recuerda que esto es un block storage)

> Si apagas el droplet, siguen cobrando porque mantienen tus archivos. Para que no te facture debes destruirlo.

Tags: Agrupar droplets según una etiqueta específica y hacer acciones en base en ese grupo, por ejemplo los de producción y desarrollo.

# Instalación de nginx

Nginx es un servidor web que nos permite servir html, css y archivos estáticos y también nos permite hacer un reverse proxy para conectar conexiones dinámicas, load balancer, poder escribir url.

Es muy raro que falle y tiene muy bien soporte para linux.

Pasos para instalación:
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install nginx

> Nota: Ubuntu inicia los servicios que se instalan de forma automática.

systemctl status nginx

En este punto al acceder desde la ip en un navegador al puerto 80 (recuerda tener habilitado el Inbound rules el puerto 80). Posiblemente haya que refrescar la configuración (revidar curso de AWS)

Los archivos de configuración están en /etc/nginx

La configuración base está en nginx.conf

Para una configuración más local, en sites-available/default para poder configurar el sitio que están disponibles para desplegarlas en nginx. Ejemplo: Todas las peticiones que van a este droplet var a servir el index de /var/www/html.

En la carpeta ***sites-available*** están los sitios que están disponibles pero en ***sites-enabled*** están los sitios que están habilitados pero aquí están son archivos simbólicos de ***sites-available***

# Instalación de MySQL

> Recuerda que puedes muy bien usar ***MariaDB***

apt-get install mysql-server mysql-client
mysql -U root -p

mysql_secure_installation (Para las configuraciones que harán segura)
- [Seguridad password]si -> 0 (Para producción seleccionar strong)
- [Remover usuarios anónimos]: yes
- [Deshabilitar ususario root remoto]: yes
- [Eliminar bases de datos de prueba]: yes

> Aquí no habilitaremos el puerto de MySQL para que no tenga internet. Si se hace un MySQL en otro droplet usar una red privada.

mysql> CREATE USER 'MAGENTO'@'localhost' (El usuario disponible solo desde localhost, sino especificar la ip) IDENTIFIED BY 'contraseña'

mysql> GRANT ALL PRIVILEGIES ON *.* To 'magento'@'localhost'; (Con esta instrucción tiene casi todos los permisos, pero recuerda que hay permisos específicos)

mysql> FLUSH PRIVILEGIES; (Para actualizar los privilegios)

> Es importante que cuando instalamos un software no usar root sino usuarios por base de datos y tener un control sobre ellos.

mysql -u magento -p
mysql>CREATE DATABASE magento;
mysql> USE magento;

# Instalación de fmp-php

FPM: FastCGI Process Manager

Instalar todas las librerías para usar magento

No es el comando exacto pero va a funcionar
```
sudoapt-getinstallphp7.0-mysqlphp7.0-fpmphp7.0-mcryptphp7.0-curlphp7.0-cliphp7.0-gdphp7.0-xslphp7.0-jsonphp7.0-intlphp-pearphp7.0-devphp7.0-commonphp7.0-mbstringphp7.0-zipphp-soapphp7.0-xmlrpclibcurl3curl
```

Para verificar que funciona

***systemctl status php7.0-fpm***

cd /etc/php/7.0
cd fpm
vim php.ini (Aquí está toda la configuración de PHP)

Buscamos ***memory_limit*** subirlo a 256M (nuestro droplet tiene 500MB)

Buscamos ***max_execution_time*** ponerla en 1800

Buscamos ***zlib.output_compression*** ponerla en on. Para conectar esa librería a Magento.

systemctl restart php7.0-fpm (Para que se habiliten los cambios)

En ../cli/php.ini
- memory_limit: -1
- max_execution_time: 1800
- zlib.output_compresion:on

systemctl restart php7.0-fpm

Configurar nginx para que habilite php.

cd /etc/nginx/sites-avalaible

vim default
Agregar index.php
En location / comentar ***#try_files $uri $uri/ =404***

Más abajo está la location de / php.

cd /var/www/html
crear ***info.php*** para probar la instalación
<?php
phpinfo();
?>

systemctl reload nginx (cambio en caliente)

ip/info.php (Debería salir todas las librerías de php)

# Instalación de magento

ssh root@ip (Conectarse al droplet)

Crear el swap porque composer consume mucha memoria

df -h (ver discos duros)

fallocate -l 4G /swap (en root)
ls -lh
chmod 0600 swap (Para que el solo dueño del archivo pueda hacer modificaciones)
mkswap swap (crear el espacio swap)
swapon swap (subir la swap)
htop (para ver la swap)

Instalar composer (herramienta de php para el manejo de dependencias, como npm, pip y gem)

curl -sS https://getcomposer.org/installer | php

mv composer.phar ~/

mv composer.phar /user/bin/composer

La instalación de magento debe ser con un usuario creado, porque en caso de instalar un plugin con código malicioso no tendrá permisos root.
adduser --disabled-password --disable-login magento

cat /etc/passwd

Buscar el enlace de magento2 en github
wget https://github.com/magento/magento2/archive/2.1.9.tar.gz

tar xvf 2.1.9.tar.gz

> El profesor borra los archivos comprimidos

mv magento2-2.1.9 /var/www/html/magento

chown -R magento:www-data (usuario magento y grupo de nginx) magento

# Conclusiones del curso

su - magento
whoami (para ver el usuario)
cd /var/www/html/magento

composer install (se descargan las dependencias composer.json)

vim nginx.conf.sample (un archivo importante para nosotros de la configuración de nginx)
pwd (copiamos esta dirección)
cd /etc/nginx/sites-available (quitar toda la configuración de php)
exit (para logearse como root)
Comentamos location, index

encima de ***server***
upstream fastcgi_backend{
    server unix:/run/php/php7.0-fpm.sock;
}

Debajo de server_name _;
set $MAGE_ROOT /var/www/html/magento;
include /var/www/html/magento/nginx.conf.sample;
nginx -t (verificar que la configuración funciona)
systemctl reload nginx

Si accedemos a la ip, podemos ir accediendo al setup de magento.

La dirección de administrador es aleatoria.

Check use apache web ser rewrites (en nginx puede estar habilitado sin problema)

Salen varios españoles.

Ya a partir de aquí podemos subir nuestros productos a la tienda.
composer -v
