# Notas del curso de Docker 2018

# Contenedores: Qué son  y cómo encajan en DevOps

Profesor: Juan Julián Merelo

- El profesor señala que con Docker podemos aislar la aplicación.
- Con la ayuda de Dockerfile podemos crear una infraestructura que permitirá mantener toda la estructura necesaria.
- Docker implica DevOps, porque utiliza solamente lo que necesita repetitiva en Desarrollo, QA y Producción.
- Después de QA viene el despliegue.
- En todas las fases de infraestructura y despliegue de la aplicación internieve Docker.

# Reto 1: Herramientas necesarias para trabajar con Docker

- which <<paquete>> // Para saber dónde está ubicado el paquete instalado.
- Para el curso se utiliza Python, Git, Docker.
- El profesor tiene un libro de git en Amazon: **Aprende Git: ... y, de camino, GitHub)**.
- El profesor usa vagrant, para obtenerlo entramos en **github.com/JJ/platzi-docker-vm** luego **vagrant up** para instalar las herramientas que necesita.

# Reto 2: Sistemas de contenedoes: Historia, parecidos y diferencias.

Documentarte por internet la historia de:
- Virtualización.
- Aislamiento de recursos, memoria, ficheros, procesos.

Contarlo en un ensayo e incluir en el momento que entra Docker.

# Retos en la instalación de Docker en diferentes sistemas

- Docker es software libre.
- Tiene dos ediciones: Community y Enterprise.
- Sistemas operativos:
  - Linux: Ubuntu >14.x o Debian. Podemos trabajar con otras distribuciones, pero el profesor aún así recomienda usar ubuntu porque tiene facilidad para hacer loop.
  - Windows: 10.
  - MacOs: usable, pero poco aconsejable.
  - Docker en la nube: Solución nativa.
- Actualizar siempre: **apt-get update**.
- Instalar: **apt-get install apt-transport-httpls ca-certificates curl software-properties-common**
- Para verificar la clave gpg: **curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -**.
- Agregar la firma de paquetes: **apt-key fingerprint 0EBFCD88**.
- Agregar repo: **add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs) stable"**.
- Actualizar paquetes: **apt-get update**
- Instalar docker: **apt-get install docker-ce**.
- El comando **which docker** debe darnos alguna respuesta.

# Validación de post instalación de Docker

Prescindir de usar sudo al utilizar docker: 

```
sudo groupadd docker
sudo usermod -aG docker $USER
exit (salir de vagrant)
vagrant ssh (conectarse a vagrant)
```

# Uso básico de Docker: Imágenes, contenedores de Docker

¿Cómo conseguir imágenes?
- Hub: https:// hub.docker,com -> Abierto a todos.
- Store: https://store.docker.com -> Imágenes certificadas, comercial, por empresas.
- Propio: Para nuesto propios registros de imágenes.

Imágen: Es un archivo estático ejecutable.
Contenedor: Es funcionando o parado.

**Imagen adecuada**

"Buscar la imágen lo más oficial posible"

Dependerá de:
- Sistema operativo.
- Aplicación o lenguaje.
- Base usada para construirla.

**Descargar y correr una imagen con docker hub**
```
docker run -it fsharp
```

// Ver imágenes descargadas
docker images

// Ver contenedores corriendo
docker ps

// Ver contenedores
docker ps -a

// Borrar contenedor
docker rm <<nombre del contendor o id>>

// Instala el contendor y lo borra al salir
docker run --rm -it fsharp

# ¿Qué hay en un contenedor?

// Revisar los metadatos de una imagen, los dos puntos es el tag
docker inspect <<imagen>>:<<tag>>

> Utilizando jsonviewer.stack.hu -> Nos ayuda a organizar un JSON.

// Para mirar los contenedores
docker inspect <<id o nombre del contenedor>>

// Información de la construcción de la imagen. Nos ayuda a depurar.
docker history <<imagen>>

# Gestionando los contenedores instalados

> Recuerda que con **--rm** borra el contenedor una vez utilizado, **la imagen no la borra**

// Listar imágenes
docker images

// Borrar imagen
docker rmi <<imagen o id>>

// Listar todos los contenedores
docker ps -a

// Borrar contenedores
docker rm <<contenedor o id>>

> **Imágenes colgantes**: Imágenes que no tienen contenedor instanciado.

// Listar imágenes colgantes
docker images -q --no-trunc -f danling=true

// Borrar imágenes colgantes
docker images -q --no-func -f dangling=true | xargs docker rmi

// Eliminar contenedores parados (cuando sale contenedores none)
docker rm $(docker ps -a -q)

# Plugins: Funcionalidad añadida y algún plugin interesante

Tipos:
- Autenticación: Sobre servicios o contenedores. Para la creación y acceso de contenedores.
- Red: Usar redes específicas.
- Filesystem: Volúmenes, almacenamiento de datos.

Métodos de instalación:
- Desde Docker Store.
- Desde fuentes del desarrollador.


> El tema de los plugin es más complicado. **Usar solo si es necesario**

Instalar el plugin de ejemplo del profesor, que es un servicio de almacenamiento.

```
docker plugin install store/hedving/hedving-volumme:v-1.0
```

Otro plugin interesante es para trabajar ficheros en forma local los almacenamiento de filesystem.

# Protocolo HTTP, órdenes y mensajes de estado

- HTTP funciona en el puerto 80.
- El cliente envía un URI (archivo) al servidor y éste devuelve una respuesta.
- Métodos HTTP:
  - GET: Conseguir un recurso.
  - PUT: Crear un recurso.
  - POST: Actualizar un recurso.
  - DELETE: Borrar un recurso.
- Símbolos de estado:
  - 404: Es una página que no se ha encontrado.
  - 200: Todo va bien.
  - 5xx: Error en el servidor.
  - 3xx: ?

# Qué es un API REST y buenas práctivas en su diseño

Hay otros modelos como GraphQL.

REST -> Representional, State, Transfer. Esto es que un estado en el servidor se le transfiere al cliente en una ruta URI.

Ejemplo: "/usuario/1"

Buenas prácticas:
- PUT: Crear el recurso.
- Delete: Eliminar el recurso.
- POST: Modificar el recurso.
- GET: Conseguir un recurso.

REST no es tanto un protocolo sino una convención. En todos volviendo código estados de HTTP Status Code.



Buenas prácticas:
- PUT: Crear el recurso.
- Delete: Eliminar el recurso.
- POST: Modificar el recurso.
- GET: Conseguir un recurso.

REST no es tanto un protocolo sino una convención. En todos volviendo código estados de HTTP Status Code.

# Implementando una API Rest en Python y ejecutándolo

Sericio: -> Datos: Fechas y nombre de hitos.
Microframework: -> Usaremos Hug.
Test: Serivcios web siempre deben probarse.

> Un servicio web que no es testeado es un servicio que no sirve.

Los puertos e IPs son los elementos más importantes en la configuración.

*Las clases parece no estar completa*

# Aislando microservicios en contenedores

Dockerfile: Definiendo infraestructura por software. Mini-lenguaje para creación sistemática imágenes de contenedores.

Las órdenes dependen del SO, se escriben en mayúsculas. Cada grupo crea capas, tener en cuenta que las imágenes deben ser lo más compacta posible.

Con **EXPOSE** podemos exponer un puerto al exterior. El resto está aislado.

1 Contenedor debe contener un solo proceso o servicio en particular.

- FROM: Definir la imagen a usar.
- WORKDIR: Definir el directorio del trabajo.
- ADD: Tomar los ficheros y copiarlos a la imagen terminando en "./"
- RUN: Correr un comando.
- CMD: Comando a ejecutar sin crear una capa.
- EXPOSE: Indicar el puerto a ejecutar.

> Con la opción de "-t" tendremos el output de la terminal.

# Puertos y cómo configurarlos

El puerto 80 es el puerto por defecto por el protocolo http para servir servicios web.

Para ello (Debemos hacer "EXPOSE 80"):
```
docker run --rm -it -p8000:80 -v $PWD/data:/src/data jjmerelo/platziws0
```

Para implementar variables de entorno en un Dockerfile

```
ENV PORT 80
EXPOSE $PORT
CMD hug -P $PORT -f main.py
```

Nota: Hug es la aplicación que se utiliza para servir servicios en el curso.

Para servir, en la terminal:
```
export PORT=3332
docker run --rm -it -p8000:$PORT -e PORT=$PORT -v $PWD/data:/src/data jjmerelo/platziws0
```

Podemos hacer que una API retorne un StatusCode 200 OK para demostrar una conección.

# Invocando contenedores

Con la opción "-d" es para instanciar el contenedor en una opción desplegada.

```
docker run --rm -dit -p8000:80 -v $PWD/data:/src/data jjmerelo/platziws0

// Para obtener el log
docker attach <<id del contenedor>>

// Ingresar dentro del contenedor
doker exec -it <<id del contenedor>> bash

// Parar el contenedor
docker stop <<id del contenedor>>

// Asignar nombre
docker run --rm -dit -p8000:80 -v $PWD/data:/src/data --name nombre-contenedor jjmerelo/platziws0

```

> Bash no necesariamente estará en todos los contenedores.

# ENTRYPOINT y CMD

Con **CMD** solo podemos ejecutar un solo comando.

Con **ENTRYPOINT** son todos los añadidos al comando.

```
// Correr contenedor en la red definido en el código ejecutado en python

// Dockerfile
FROM python:3

WORDIR /src

ADD status.py requeriments.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN rm requirements.txt

ENTRYPOINT ["./status.py"]


// Correr el contenedor
docker run --net=host --rm -it jjmerelo/platzistatus 2 (el 2 lo interpreta como un argumento de entrada al código con ENTRYPOINT)
```

# Trabajando con datos: Volúmenes

docker run --rm -v <<directorio-local>>:<<directrio-contenedor>> -p8000:8000 -it jjmerelo/platziws1

> Todo lo que corresponde a la izquierda de los dos puntos es nuestro host y todo a la derecha es el contenedor.

Con ese volumen instanciado podemos modificar el archivo, pero para que haga efecto debemos reiniciar el contenedor.

# Instalación de Docker Compose

> Al instalar Docker en Windows y MacOs ya tienen instalado docker-compose.

> Para conectarse a vagrant usar **vagrant ssh**

Para instalar:
```
sudo curl -L https://github.com/docker/compose/releases/download/1.19.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

// uname -s -> Dice el sistema operativo
// uname -m -> La arquitectura

En pocas palabras, va a bajar un fichero dependiendo del sistema operativo y la arquitectura que dispongamos.

// Dar permisos de ejecución
sudo chmod +x /usr/local/bin/docker-compose

// Ejecutar
docker-compose
```

# Componiendo servicios con docker-compose

Describe diferentes servicios y cómo se conectan entre ellos.

> No es tanto para llevar aplicaciones a producción, porque para ello existen herramientas como Docker swarm y para más complejas kubernetes.

Se utiliza para trabajar entornos de pruebas y entornos de desarrollo. No se utiliza para escalar ni para monitorizar.

Docker compose trabaja con servicios (usando Dockerfile) y también con volúmenes. Para que diferentes contenedores puedan compartir entre sí datos y volúmenes de datos.

También podemos conectar puertos unos con otros para desplegar conexciones más seguras.

Podemos hacer contenedores de datos, bases de datos, logs de aplicaciones que funcionen independientemente.

Tendremos dos contenedores, uno con los servicios y otro con los datos.

```
// Dockerfile que recibe datos
FROM busybox
WORKDIR /data
VOLUME /data
COPY hitos.json .

// Dockerfile que emite el srvicio
FROM python:3
WORKDIR /src
ADD main.py requirements.txt ./
RUN pip install --no-cache-dir -r <<...>>
RUN mkdir /src/Hitos
ADD Hitos/Hitos.py Hitos
RUN rm requirements.txt
EXPOSE 8000
CMD ["gunicorn", "--bind", <<...>>]
```

busybox -> Es una imagen de linux ligero pero con muchos ficheros.

docker-compose.yml
```
version: '2'

services:
  data:
    build: data
  web:
    build: .
    ports:
      - "8000" // 8000:8000
    volumenes_from: // Vamos a cargar un volumen que se llama **data** 
      - data:ro // ro es readoblet
```

docker-compose up // Para correr los contenedores
docker-compose ps // Ver los servicios corriendo con docker-compose

// Probar el servicio
curl http://localhost:32770/status

> Una vez que empiezas a usar docker-compose se te va hacer muy fácil para crear entornos de desarrollo y de pruebas sin necesidad de hacer escalado y despliegue en la nube.

# Usando docker stack deploy

Cuando estamos desplegando un swarm estamos obligados a usar la versión 3

```
version: '3'

services:
  data:
    image:jjmerelo/platzidata
    volumes:
      - data-vol:/data
  web:
    image:jjmirelo/platziws0
    ports:
      - "8001:80"
    volumes:
      - data-vol:/data

volumes:
  data-vol:
```

En este caso no se hace la construción a través de un Dockerfile, sino que tenemos que tener la imagen ya construida.

docker swarm init
docker stack deploy -c docker-compose.yml platzi-0 // Estamos usando una suborden de docker, en este caso lo estamos creando en swarm

docker stack ls // Mostrar los servicios desplegados. Es prácticamente la misma funcionalidad de docker-compose pero estamos haciendo algo mucho más potente. Estamos desplegando un swarm y éste puede estar funcionando en diferentes ordenadores, en la nube y en muchos sitios diferentes.

Con Docker podemos hacer despliegue de aplicaciones de forma fácil, eficiente y muy potentes.

# Creando paquetes de red

> Docker está creando una minired al gestionar todos los contenedores, podemos muy bien manipular esa red interna.

// Mostrar las redes que hay, sobre todo con Docker-compose
docker network ls

> Con la red **bridge** es la red en la que se comunican los contenedores.

// Para borrar redes
docker network rm platzi-net

// Crear una red
docker network create platzi-net

// Inspeccionar las redes
docker network inspect platzi-net

// Ejecutar un contenedor que esté dentro de la red
docker run -dit -p8000:80 -v $PWD/data:/src/data --name servicio_platzi_1 --network patzi-net jjmerelo/platziws0

Al ejecutar nuevamente **docker network inspect platzi-net** podemos ver el contenedor que se está ejecutando.

> Los contenedores alpine son muy ligeras.

// Instanciar otro contenedor en la misma red
docker run --rm --network platzi-net -it alpine

Allí dentro
```
ping servicio_platzi_1
wget -qO. http://servicio_platzi_1/status
```

// En otra terminal, inspecionamos la red y veremos los contenedores instanciados.
docker network inspect platzi-net

// Entrar en el servicio
docker exec -it servicio_platzi_1 bash

> Para hacer ping al otro contenedor, como no hemos puesto un nombre (y docker ha asignado un nombre aleatorio) podemos usar su ip el cual aparace en **docker network inspect platzi-net**

ping 172.18.0.3

# Instalación del cliente de Azure

> Cuando trabajamos con Python, es recomendable con virtualenv para el manejo de la versión Python a utilizar (2 o 3).

Instalamos el **azure-cli**. Para invocarlo con **az**.

> Con **az interactive** nos va a permitir un completado de comandos.

# Clientes de servicios cloud y como usarlos en nuestra aplicación

> Cuando utilizamos un servico cloud lo mejor es utilizar su cli.

> Las aplicaciones se crean en la nube: Y los contenedores necesitan una forma segura y eficiente de despliegue.

Anteriormente se utilizaba **docker-machine**, ahora usaremos **docker-cloud**.

Cuando vamos a trabajar en la nube lo hacemos con un registro que puede ser público o privado. Evidentemente cuando trabajamos en una empresa lo vamos hacer con un registro privado.

**¿Dónde podemos desplegar?**
Azure, AWS, Google Cloud Engine, OpenStack -> Todos tienen programas clientes, y permiten desplegar a partir de diferentes registros, incluyendo los públicos. También hay otros como DigitalOcean.

> Las imágenes que tengas en local de alguna forma hay que subirla a la nube para poder trabajar con ella.

**Grupos de recursos**
Reúnen recursos de un proyecto.

**Grupo de contenedores**
Permiten agrupar contenedores.

### Trabajando con azure

az interactive

// Crear grupo de recursos
group create -l brazilsouth -n platzi-curso 

> Debemos crear una instancia lo más cercano a nuestros clientes

// Crear el registro de los contenedores con los que vamos a trabajar
acr create --resource-group platzi-curso --name cursoplatzi2018 --sku Basic

> --sku Basic -> La persona que tiene acceso también va a tener acceso al registro.

> Las cosas cuado se escriben en la nube tienden a tardar un poco. De ser afirmativo retornará un JSON.

// Enviar un query para saber si se ha realizado un registro
acr list --resource-group platzi-curso --query "[].{acrLoginServer:loginServer}" --output table

> Se recomienda instalar el **azure-cli** con pip.

> Cuando se utiliza recursos no se debe implementar "-"

// El profesor tiene erroes con el CLI, crea el siguiente registro
az acr create --resource-group platzi-curso --name regplatzi --sku Basic

// Listar los registros
az acr list --resource-group platzi-curso --query "[].{acrLoginServer:loginServer}" --output table

> Con **--query** es para hacer una petición al JSON, aplicando un filtro sobre el JSON retornado.

**azurecr** -> Azure container registry.

# Creación de contenedores en la nube

// Para subir una imagen debemos hacer un tag
docker tag jjmerelo/platziws0 regplatzi.azurecr.io/platzi:v0

// Hacer autenticación dentro del registro
az acr login --name regplatzi

// Hacemos un push
docker push regplatzi.azurecr.io/platzi:v0

> En este punto hemos subido nuestra imagen al registro en la nube.

// Vamos a actualizar el registro para que se pueda administrar
az acr update -n regplatzi --admin-enabled true

// Crearemos una variable de entorno donde almacenaremos nuestra clave sin que quede registrada en nuestro sistema de ficheros del terminal
export AZ_CR_KEY=$(az acr credential show --name regplatzi --query "passwords[0].value" --out tsv)

> La forma segura de administrar contraseñas en la nube es utilziando variables de entorno.

// Crear el contenedor en azure
az container create -g curso-platzi --name hitosv1 --image regplatzi.azurecr.io/platzi:v0 --registry-password $AZ_CR_KEY

// Manejar el contenedor
az interactive

// Listar contenedores instanciados
az container list

// Despliegue de microservicios

> Es muy importante que tengas en cuenta la seguridad desde el principio, esto es realmente importante al trabajar en la nube. Cualquier fallo de seguridad va a costar dinero.

> "Ten en cuenta que hay gente buscando contínuamente por todos los repositorios abiertos a ver si hay una clave disponible de lo que sea... sobre todo de máquinas virtuales en la nube van... a minar bitcoin o monero."

### Seguridad desde el principio

Desde el comienzo del despliegue hasta el final:

> Si puedes evitar que aparezcan tus claves en el sistemas de ficheros mejor.

- **Claves**: Usar gestor -> Que no aparezcan en la historia del shell. Esto es tan seguro como pueda ser tu cuenta. Con ello implica tus contenedores y los de tus clientes. Los gestores, te piden una clave maestra.
- **Variables de entorno**: Por shell, manera más segura de almacenarlas si tu usuario es seguro. Son más seguro que los ficheros porque se quedarán en local, en cambio un fichero por un descuido puedes terminar publicando tus claves allí.

> Siempre que puedas usa variables de entorno. En todo caso de que uses un fichero asegúrate de agregarlo al **.gitignore**.

**Los despliegues seguros son reproducibes** -> Trabaja en línea de órdenes no en la web.

**Regenera claves** -> Siempre que sea posible. Y elimina ficheros de tus pruebas porque éstos están consumiendo recursos.
**Gestionar acceso** -> Usa solo los permisos necesarios. Ejemplo: Si quieres que la persona solo suba imágenes al servicio, solo debes darle ese acceso.
**Asegura las aplicaciones** -> Mínimos puertos (levante solo los puertos necesarios, ssh, base de datos, etc.), redes segura (solamente 1 contenedor que va a ser el que esté respondiendo necesita ip pública) el resto usa red interna (pero si se compromete el primer nodo se comprometerán el resto), trabajar contendores seguros (asegurándolos lo más que se pueda).

**Los pasos para el despliegue de contenedoes en Cloud**
1. Crear un registro.
2. Subir la imagen al registro.
3. Instanciar la imagen del contenedor.

# Integrando contenedores en aplicaciones en la nube

**Docker cloud**: Sistema gestionado de Docker. Es una interfaz común a todos los servicios cloud ya sea de modo normal o docker swarm.

**Servicios**: Son grupos de contenedores con la misma imagen y etiqueta.
**Prerequisito: Alta en servicio**: Si te das de alta en Docker Cloud tendrás cupones gratuitos para una serie de servicios.

> DigitalOcean aconseja el profesor.

**Despliega nodos desde docker-cloud**: Primero provisionar nodos previo al despliegue.

**Los despliegues seguros son reproducibles**: Todas las veces que quieras con diferentes funcionalidades.

**cloud-stack**: Es la descripción de servicios y su conexión. Se parece mucho a docker-compose en su versión 3. Se utiliza para desplegarlo fácilmente en la nube.

# Instalando Docker Cloud

Docker cloud solo funciona con la versión 2 de python. Para ello usar gestor de versiones como **pyenv**.

// Setear la versión de python a usar
pyenv global 2.7.14

// Instalar Docker Cloud
pip install -U docker-cloud

// Verificar la instalación
docker-cloud --version

# Iniciación del API de Docker Cloud

> Con **bpython** es una interfaz de líneas de órdenes de Python así como **ipython**. Pero tiene un completado muy bueno.

bpython
```
import dockercloud
regions = dockercloud.Region.list() // Enlistar los nodos disponibles
regions // Ver las regiones descargadas
regions[3].name // Muestra el nombre
```

> Docker-cloud usa el mismo login de docker.

// Script en python para ver el nombre, proveedor y el tipo de nodo (no todos los tipos de nodos están disponibles en la misma localización ni proveedor)
```
#!/usr/bin/env python

import dockercloud
import sys

if len(sys.argv)>1:
  provider = sys.argv[1]
else:
  provider = 'digitalocean'

for r in dockercloud.Region.list():
  if r.provider.find(provicer)> 0:
    print (r.name, "|",r.label,"=>", r.node_types)
```

// Ejecutar programa (tener en cuenta que puede haber problemas de red)
./get-regions.py

// Una mejor presentación
./get-regions.py | less

> "La biblioteca tiene una versión en Go. Go es un lenguaje muy interesante que recomiendo que aprendas en un momento determinado" :D

> Con esta librería podemos crear aplicaciones muy complejas usando docker cloud.

# Usando cloud docker

> La idea principal de Docker es hacer infraestructura como código y éste puede ser como de la líneas de órdenes como código.

Docker cloud integra tu id de docker hub, por lo que todas las imágenes que hayas subido a docker hub estarán allí.

> Una de las cosas que podemos hacer es la creación de nodos aunque es algo que podemos hacer por cli. Los cupones gratuitos se pueden crear 1 solo nodo.

Todo lo que tengas ejecutándose va a incurrir en costos de la suscripción. Una recomendación al haber realizado tus pruebas es que apagues los nodos. Pero si lo está pagando la empresa, adelante :)

En esta parte, desplegamos un nodo con docker instalado.

Los endpoints nos va a servir para conectarnos con ello.

# Uso de Docker Cloud, cómo desplegar un servicio en un contenedor

// Desplegando desde la línea de órdenes
docker-cloud nodecluster create -t 1 --tag platzi platzi-big digitalocean ffra1 2gb

// Listar nodos disponibles y en qué estado están
docker-cloud nodecluster ls

> Con Docker cloud free podemos desplegar solo 1 nodo. Una manera que hicieron las personas de Docker para monetizar es creando docker ee.

Esto lo podemos ver también desde cloud.docker.com

> Si tarda mucho, podría usarse otra región.

// Instanciar el contenedor, la imagen que despleguemos debe estar desplegado en docker hub. Esto aparecerá en services.
docker-cloud service run -p 80 --name platziws1 jjmerelo/platzi-servicio-web

> El despliegue de contenedores en docker hub es bastante rápida.

// Con el endpoint podemos ver las rutas de dominio público
// Para Interactuar con el servicio desplegado
curl http://platziws1-1.03ea0fea.cont.dockerapp.io:32769/status

> Cuando acabes las pruebas, vayas a Nodes y termina el nodo para que no gastes dinero. Por economía y por seguridad, y ahorrar el cupón, termina el nodo una vez terminado de usar.

# Cómo desplegar un stack

**Stack**: Nuestra aplicación su serie de servicios. En vez de una base de datos vamos a usar un **log**. Los logs son muy importante en la arquitectura de hoy en día.

Usaremos **logstash** que está escrito en Java. Ver cuellos de botella, cómo lo están usando los usuarios, el coste... La imagen de logstash en docker hub está obsoleta. Conviene usar la indicada en el archivo docker-cloud.yml

docker-cloud.yml
```
logstash:
  image: docker.elastic.co/logstash/logstash-oss:6.2.1
  expose:
    - "5959"
  command: -e 'input { tcp { port => 5959 codec => json } } output { stdout {} }'
web:
  image: jjmerelo/platzi-servicio-web
  ports:
    - "80:80"
  links:
    - logstash
```

> **docker stack != docker cloud stack**: El primero es servicios locales y el segundo es un servicio que está gestionado con docker cloud.

**Cuando estés en producción reemplazar 'stdout {} ' por la base de datos**.

// Levantar el stack en docker cloud
docker-cloud stack create -f docker-cloud.yml

> Logstash tarda un rato en desplegarse.

// Ver los stacks
docker-cloud stack ls

> Cuando son dos servicios que dependen uno del otro. Primero arranca logstash y luego el web.

Cuando estés haciendo las pruebas, es bueno que revises la página para ver los logs y el estado de la aplicación.

Todo el stack estará desplegado en un subdominio.

Podemos desplegar los servicios de forma independiente.

# Conceptos principales en la orquestación de servicios

**Necesitas orquestación si**:
- Tienes gran cantidad de servicios.
- Quieres integrar nubes (AWS, Azure, DigitalOcean...).
- Quieres monitorización y niveles de servicio.

**Nodos**: Ejecutan servidores Docker.
**Tareas**: Contenedores docker ejecutándose.
**Cluster**: Conjunto de nodos gestionados por uno solo (el manager).

La manera oficial de Docker es usando **el modo swarm**. Que realiza orquestación de Docker incluida en la edición community.

Hay otras opciones como kubernetes.

**Seguridad por defecto**:
- Todos los nodos van a ser seguros, todos los puertos van a estar cerrados.
- Descubrimiento de servicio: Se hace automáticamente la conexión de servicios.
- Equilibrado de carga automáticamente.
- Configuración distribuida: Creará un sistema de configuración distribuida.

# Instalación de docker machine y uso básico

docker machine: Es una utilidad que permite instalar docker en diferentes máquinas virtuales.

Lo que va hacer docker machine es crear máquinas virtuales con una imagen por defecto que una vez que arranca tendrá docker instalado.

// Listar máquinas
docker-machine ls

// Crear una máquina virtual
docker-machine create -d virtualbox platzi-00

> Estamos creando una máquina virtual con Docker dentro.

// Instanciar la máquina virtual
docker-machine env platzi-00

// Entrar en la máquina virtual
docker-machine ssh platzi-00

// Borrar máquinas
docker-machine rm <<name>>

> Docker machine nos va a servir cuando estemos trabajando con docker swarm, para las pruebas en local. Pero en cloud no tanto.

# Docker swarm

Vamos a trabajar con Docker swarm, es decir con un conjunto de nodos.

> Docker Swarm en muchas partes están en beta.

Cuando haces un docker swarm creas un nodo manager que gestiona el resto.

// Crear Docker Swarm. La dirección sale de **docker-machine env platzi-00**. Sino podemos enlistar los puertos netstat.
docker swarm init --advertise-addr 192.168.99.103:2376

> Cada Swarm está ligado a un token. Ten cuidado con este token porque alguien podría añadir contenedores con dicho token.

// Unirse al swarm (dentro de docker machine)
docker swarm join --token <<token>> 192.168.103:2377

// Irnos del swarm
docker swarm leave

> Si hay un error, es probable que sea el puerto. Usar el puerto siguiente.

// Enlistar los nodos donde instanciamos el swarm
docker node ls

// Nodo worker (donde nos unimos al swarm). Para saber si está activo.
docker info | grep Swarm

Docker Swarm va a ser muy útil para aplicaciones complejas. Uno de los trucos, es utilizar el puerto 2377 al instanciar docker swarm y evitar problemas.

# A dónde ir desde aquí

> El ecosistema de Docker es bastante complejo.

Investigar:
- Kubernetes: Es un sistema de orquestación bastante más maduro. Que permite orquestar cantidades masivas. Es complicado empezar a trabajar con él pero una vez lo hagas es muy rico en conocimiento.
- CoreOS: Es un sistema operativo para trabajar con contenedores. Crea un entorno muy favorable con ETS. Sacaron un sistema alternativo RKT, tiene ciertas ventajas con respecto a Docker. Permite cifrar contenedores y de esta forma evitar que la plataforma cloud tenga acceso al contenedor.
- OCI: Open Container Iniciative. Crear con cualquier herramienta de creación de contenedores, un contenedor o una imagen. Y esa imagen se pueda ejecutar en cualquier infraeetructura. Creando estándares, uno de ellos es moby. Moby es una generalización de Docker. El cual utiliza un API.
- Mesos: Es de apache que entra competeción con kubernetes y docker swarm.

> Para mantenerse al tanto hay que seguir una serie de canales, cuentas de twitter, páginas de medium, el blog de Docker, thePracticalDev.

Las cuentas del profesor es jjmerelo o jj.
