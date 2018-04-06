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

docker network ls 
