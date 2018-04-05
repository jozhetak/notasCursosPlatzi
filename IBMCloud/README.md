# Notas del curso Fundamentos de IBM Cloud

Profesores: 
- Erika Chacón Vivas
- German Acosta
- Armando Castillo

IBM Cloud hay soluciones híbridas

# Te presento a IBM

IBM tiene tecnología de Inteligencia Artificial.

- Está cambiando totalmente su imagen empresarial.

Tienes internet de las cosas.

**Watson** Es una tecnología de IBM Cloud para inteligencia artificial.

# Recursosde IBM para diferentes perfiles

Programa de relacionamiento académico de IBM. Para un ambiente académico gratuito [enlace](https://onthehub.com/ibm)

Desarrolladores
http://developer.ibm.com

Arquitecturas
http://ibm.biz/ibmcloudgarage

Garage Method
http://ibm.biz/ibmcloudgarage

Global Entrepenuer Program (Programa para emprendedores)
https://developer.ibm.com/startup

# IBM Cloud, la nube empresarial

Se muestra el ejemplo de una tienda de e-commerce de TheNorthFace, quien usando ML interpreta el lenguaje de lo que uno quire y busca en su base de datos.

En dicho ejemplo se utiliza:
- Runtimes:
  - IBM Containers.
  - SDK for NodeJS.
- Watson:
  - Conversation.
- DevOps:
  - Auto-Scaling.
  - Monitoriting and Analytics.
- Bases de datos:
  - Compose for PostgreSQL.
- Weather:
  - Weather Company Data.
- Integration:
  - API Connect (Integrar datos importantes de forma segura).
  - Secure Gateway (Crear un túnel encriptado entre el BackEnd y la base de datos).

# Arquitectura para Discrupción

> Los datos son muy importantes para los clientes de las aplicaciones.

**Hay nubes que se quedan con tu información, es decir, tus datos.**

# Creación de tu cuenta IBM Cloud

Cuentas:
- IBM Cloud Lite: Gratuita limitada. Con los componentes más utilizados por desarrolloradores.
- Pago por uso.
- Subscripción: Para aplicaciones con millones de usuarios con ciertos descuentos.

**IBM Cloud Lite**
- Gratuito.
- Nunca Expira.
- 256 MB RAM.

[https://www.bluemix.net/](https://www.bluemix.net/)

Inicias con 45 servicios en la versión gratuita, cuando en la versión paga son cerca de 200.

No se necesita registrar ninguna tarjeta de crédito, solo en correo es suficiente.

# Navegando IBM Cloud, conociendo la plataforma

- IaaS
- PaaS

# Catálogos de componentes basados en OpenSource de IBM Cloud

CloudFoundry: Es una tecnología diferente a virtualización de máquinas (??). Es donde se utiliza aplicaciones en el lenguaje.

Desde esa opción, podemos instanciar PaaS con Go y otros lenguajes.

Cuando sale un círculo verde, es porque ya está deployado la aplicación.

# Git y GitHub

Podemos trabajar en local con Toolchain para conectarnos.

Para habilitar entramos en continuos delivery.

Dirección del Git donde aparecen los repositorios y las credenciales.
https://git.ng.bluemix.net

De esta forma cada vez que hacemos push queda reflejado en el repositorio local y en el de IBM Cloud.

# Crea tu primera aplicación en IBM Cloud

Pues aquí se muestra cómo crear aplicaciones jejeje

# Microservicios

# Tolchain o herramientas de Cloud Foundry

El corazón de la creación de aplicaciones es catalogo.

Las conexiones del Dashboard son las conexciones con las otras opciones del catálogo.

# DevOps en Cloud Foundry

Laboratorio DevOps: Es un servicio de CloundFoundry.

DevOps son las conexiones entre la producción y desarrollo.

Se puede usar Slack para la comunicación en el equipo.

El toolchain es el conjunto de herramientas que ayudan a DevOps.

Continuos Delivery: Así se llama el servicio para DevOps en IBM Cloud.

En Delivery pipeline se utiliza Jetkins.

# Delivery Pipeline

Podemos agregar otro stage (pilar) Podemos desplegar a otro espacion (desarrollo, producción, etc.)

Modificando el nombre para realizar un desplieque en desarrollo antes de llevar a producción.

Desde Delivery podemos modificar el script de despligue de "cf push".

Podemos agregar otras herramientas, oprimiendo "Add Tools". Son herrmientas de terceros, libres o bien propietarias.

# Docker y Kubernetes

> Contenedores: La siguiente frontera. Kubernetes es un orquestador de contenedores.

# Instalación de pre requisitos de un espacio en IBM Cloud

Prerequisitos:
- Tener cuenta IBM Cloud.
- Instalar Docker y kubernetes en nuestra máquina.
- Instalar CLI (bx).

Procedimientos:

```
bx login -u correo@gmail.com
  // Ingresar Password

bx plugin repo-plugins // Desplegar todos los plugins disponibes
bx plugin install IBM-Containers
bx plugin install container-registry
bx plugin install container-service

```

Container registry: Registro privado de los contenedores que pudieras estar desplegando sobre IBM Cloud.

En el Dashboard entramos en Containers in Kubernetes Clusters y Crear.

En la versión gratuita estaremos compartido. Con la versión de pago tenemos la opción de dedicado (hardware).

Tenemos 1 worker, 2 cpus y 4 GB de Ram.

# Configuración del ambiente de trabajo, instalación de Plugin

Tendremos IP pública e IP privada.

En la opción "Access" tendremos el tutorial de **bx cli** para kubernetes.

```
bx login -a https://api.ng.bluemix.net
-> Email
-> Password
-> Escoger un espacio de trabajo
bx target --cf
-> Organización
-> Espacio de trabajo
bx cs region-set us-south
bx cs cluster-config ibmcloudplatzi // Nombre de nuestro ambiente
// En este punto nos da una varaible de entorno que tenemos que seteaer en nuestra máquina.
kubectl get nodes // Conocer los nodos que se están ejecutando
kubectl proxy // Para inicializar un servidor de forma local las aplicaciones desplegadas en kubernetes.
```

# Ejecución de clusters en líneas de comando

> La ventaja de usar kubernetes es que se puede escalar de forma horizontal.

Desde el Docker Hub obtenemos una imagen de MongoDB

```
// Para desplegar MongoDB
kubectl run mongo --image=mongo --port=27017
kubectl expose deployment mongo --type=NodePort

// Para desplegar app web
kubectl run mytmp --image=kavisuresh/employee --port=80
kubectl expose deployment mytmp --type=NodePort --port=80 --target-port=8888

// Obtener los pod generado por la aplicación
kubectl get pod

// Inicializar el servicio de kubernetes, ingresando en el localhost podemos ver los datos del mismo.
kubectl proxy
```

# Despliegue de aplicaciones en el web cluster

> Un worker es una imagen virtual y dentro se pueden desplegar múltipes contenedores.

> Nota: Para acceder a las aplicaciones utilizamos la IP pública. Entramos en **console** para obtener dicha ip. Luego entramos en kubernetes de localhost para conocer los puertos.

Con la aplicación ejemplo, se muestra cómo desde la aplicación se guardan los datos en la base de datos.

# Réplicas de clusters

Esto es para escalar de forma horizontal las aplicaciones. Con HPA podemos escalar la aplicación. Podemos setear que cuando se consuma cierta cantidad de CPU haga una réplica y llegado a un punto eliminar las réplica.

```
kubectl run -i --tty load-generator7 --image=busybox /bin/sh

// Simula una carga masiva
while true;do wget -q -O- http://php-apache3.default.svc.cluster.local; done

Ver el comportamiento de los pod
kubectl get pods

// Ver la carga y réplicas
kubectl get hpa
```
**hpa** -> Horizontal Pod Autoscale

# Creación de un cluster de Kubernetes seguro en IBM Cloud

Las imágenes las podemos obtener desde Docker Hub

```
bx cr namespace-add ibmcloudplatzi
```

En console.bluemix.net

Entramos en Continuos Delivery incializándolo con un template.

El que vamos a usar es **Develop a Kubernetes app**. Para conectar con el espacio de trabajo debemos ingresar un API Key, para generarla debemos:

Entrar en Managmen -> Security -> Platform Api Key.

Se recomienda copiarlo y descargarlo.

**Image Registry Namespace** -> El que creamos: ibmcloudplatzi
**Bluemix APIKet**: El que generamos
**Cluster Name**: Si nos olvidamos el nombre de nuestro cluster, `bx cs clusters` que es ibmcloudplatzi.

La secuencia de pasos que va hacer es:
- Compilado.
- Análisis de vulnerabilidad y DevOps.
- Deploy.

# Entrega contínua IBM Cloud

Este es el mismo pipeline de los otros templates.

# Containers registry

Nos va a permitir construir y almacenar contenedores de Docker en IBM Cloud,

```
// Enlistar todos los namespace registrado en IBM Cloud
bx cr namespace-list

// Enlistar las imágenes en el container registry
bx cr image-list

// Obtener phpinfo de docker hub
docker pull cfortier/phpinfo

// Registrar la imagen en IBM Cloud
// Aquí cortaron el vídeo
docker push registry.eu-de.bluemix.net/ibmcloudplatzi/phpinfo:latest

// Ver las imágenes de docker
doker images

kubectl run phpinfo --image=registry.eu-de.bluemix.net/ibmcloudplatzi/info --port=80

// Ver status de los pod
kubectl get pods

// Deploy
kubectl expose deployment phpinfo --port=80 --type=NodePort

// Inicializar el Dashboard de kubernetes
kubectl proxy
```

Para acceder a la aplicación debemos entrar en worker para obtener la dirección ip pública, y el puerto lo obtenemos directamente del dashboard de kubernetes.

> Todo esto que vimos es para el despliegue de microservicios de con kubernetes.

En las opciones del dashboard de worker en registry aparecen los registros de las imágenes.

# Introducción a la economía de las APIs usando IBM Cloud API Connect

Una **API** es una forma de integración entre dos sistemas sin que importar el lenguaje en el que están construidos puede comunicarse en un mismo lenguaje. Es una forma en que servicios y productos se comunican entre sí a través de una interfaz documentada.

**Economía de APIs** Es la rentabilidad que puede aportar el dato de la API a través de la organización. Esto puede tener un costo. El proveedor de API puede garantizar la disponibilidad a consumidores.

Un marketplace es el portal del desarrollador. Donde la persona se suscribe a un plan para consumir el recurso.

> "Si hay alguna API que me parece muy intersante, fabulosa, responde a las necesidades que yo estoy planteando. Pues efectivamente yo pueda ratearla" Erika Chacón.

> 'Al menos el 80% de las organizaciones están en proceso de transformarse digitalmente y la agilidad des clave; el desarrollo de APIs es un medio importante en esa transformación'

**IBM API Connect**:
- Crear, depurar y desplegar APIs de alta escalabilidad y seguras.
- Crear y gestionar portales que permitan a desarrolladores descubrir y consumir APIs.
- Gestionar la seguridad y el gobierno de las APIs.
- Potenciar la economía de APIs ofreciendo catálogos con productos.

# Introducción a IBM Api Connect

Componentes de IBM Api Connect:
- Portal del Desarrollador.
- API Manager: Dashboard para el manejo de las APIs.
- API Gateway: Refuerza cualquier política de seguridad.
- Entorno de desarrollo: Developer Toolkit.

Conceptos claves:
- Catálogos: Son productos de API, para consultar las APIs, con la posibilidad de probarlos en línea.
- Productos: Con un cliendID y un clientSecret podemos consumir el producto.
- Planes: Si son planes ilimitados o limitados, por un pago mensual. Podemos tantos planes como sean necesarios para nuestros productos.
- Estándar: Swagger 2.0
- Mensajes: JSON/XML
- Protocolos: SOAP/REST

Para empezar entrar en https://console.bluemix.net/ y entrar en **API Connect** Para crear las APIS.

# Creación de APIS usando IBM API Connect

El servicio gratuito es hasta 50000 API CALLS/ mes. Pero si supera los 30 días sin actividad la API será borrada.

Los productos son los objetos donde nos podemos suscribir para poder consumir los recursos de api.

Approvalas: Gestionar las mismas de las soluciones en API que yo esté proveyendo.

Settings: Configuraciones del portal de desarrollo. Aquí se debe activar el portal del desarrollador. Es donde el proveedor muestra el servicio con una url. Este portal viene preconficurado y cada vez que desarrollo un API va aparecer acá.

Para crear una API entrar en **>>** y luego en draft. Podemos usar OAuth2, importar API a través de URL. También hay un ejemplo de OpenAPI para obtener un ejemplo que hace obtener el clima de tres días en adelante. Tenemos modo visual y por código.

# Continuando con la creación de APIs usando IBM API Connect

Change setup para cambiar el producto en el test.

Con el portal del desarrollador tenemos una manera de presentar nuestras APIs con la opción de ser valoradas y monetizadas.

# Habilitar la gestión de APIs en Aplicaciones Cloud Foundry

Con API Managment podemos gestionar las aplicaciones creadas. Podemos manejar authenticación y rate limit. Es decir, hace las funciones de API Gateway.

A su vez, podemos hacer que consuma la autenticación de alguna red social.

Todo esto es desde console.bluemix.net

Para correrlo en localhost debemos crear un archivo llamado vcap-loca.json

```
// En la sección de runtime tenemos los datos para interactuar con las credeciales
// Insertamos aquí
```

**npm i** // Para correr la aplicación
**node app** // Para correr la aplicación

Nota: Esta aplicación está hecha en node. Y la aplación ya está desplegada en CloudFoundry.

# Conociendo los elementos de despliegue de aplicaciones a IBM Cloud

¿Cómo podemos desarrollar apps en IBM Cloud?
1. Build-from-the-scratch: Construirla desde cero.
  - Runtimes: Diferentes lenguajes para construir aplicaciones, su acelerador es el hellow world de su respectiva aplicación con su respectiva url.
  - Boilerplates: Es un contenedor con su runtime y preconfigurados contenedores con servicios como bases de datos, watson, etc. Y otros servicios configurados.
2. Bring-your-own-app: Es una aplicación nativa en la nube. Utilizando CLI para publicar. Pudiendo publicar desde GitHub  con un archivo y un botón de despliegue. Que al darle clic se generará un runtime para correr la aplicación desde GitHub.

[Botón de despliegue](http://console.bluemix.net/docs/services/ContinuousDelivery/deploy_button.html#deploy-button)

# Conociendo los aceleradores boilerplates

Boilerpates en español: Contenedores de aplicación.

Podemos generar aplicaciones para móviles, usando Node.js podemos generar un starter de una base de datos no relacional.

Usando **bx login --sso** Podemos loguearnos con una contraseña generada por la página.

Con estos aceleradores tenemos ya las preconfiguraciones y empezar a editar desde allí.

# Desplegando aplicaciones cloud native

Esto es para desplegar aplicaciones que ya tenemos creadas.

Para ello crear un archivo llamado **manifest.yml**

```
declared-services:
  insights-wheather-weatherinsights:
    label: weatherinsights
    plan: Free-v2
applications:
- services:
  - insights-weather-weatherinsigths
  name: insights-weahter-prueba-platzi-2018
  host: insights-weather-prueba-plati-2018
  memory: 256M
```

weatherinsigths es un servicio de API que nos da el clima por ciudad.

En consola
```
bx cf create-service weatherinsights Free-v2 insights-weather-prueba-platzi-service
bx cf push <<x2, una para subir el manifest y el otro para desplegar la aplicació>>
```

Si queremos usar un repositorio existente desde GitHub, en la parte inferior podemos configurar ello.

Esto a su vez, levanta un servicio.

# Introducción a la computación cognitiva

Computación de cognitiva: Estamos hablando de redes neuronales artificiales. Esto ayuda para Machine Learning.

> "Cuando hablamos de contexto nos referimos al contexto de la persona en cómo interactuar para usarlo de la manera más adecuada".

La interacción con watson es a través de APIs. Con los Demos podemos tener un fork para el desarrollo inicial de la aplicación.

# Conociendo los servicios de Watson en IBM Cloud

- Conversation: Armado de conversaciones con contexto.
- Discovery: Descubrimiento de datos desde diferentes fuentes de información.
- Language Translator: Traductor de texto.
- Natural Language Classifier: Clasificador de lenguaje.
- Speech to Text: Tradutor de voz a texto.
- Tone Analizer: Tono con el que una persona nos está hablando.
- Personality Insights: Identificar personalidades.
- Visual recognition: Identificar objetos dentro de un contexto.
- Knowledge Studio (no lite): Poder hacer modelos personalizados para armar una propia API.

> Todos los servicios los consumimos a través de APIs.

Las APIs tienen una demo de la cual podemos hacer un fork. La respuesta es en formato JSON.

