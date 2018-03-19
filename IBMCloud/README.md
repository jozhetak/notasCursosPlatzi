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
