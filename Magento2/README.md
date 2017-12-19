# Introducción a Magento2

## Qué es un E-commerce
Con la llegada del e-commerce el mundo de las ventas cambió radicalmente, hoy en día on un poco de esfuerzo una persona pude estar vendiendo on-line muy fácil y rápidamente.

Veamos cuáles son las distintas características de las diferentes plataformas de E-commerce existentes.

***Plataformas***
- PaaS: La plataforma se encarga completamente de la infraestructura y nosotros los clientes solo programamos

- Hosted: Nos ocupamos de la infraestructura para manejar nuestra tienda. En este subgrupo para manejar nuestra tienda.

***Verticales***
- B2B: Empresas a otras empresas
- B2C: Empresas a consumidores
- H2H: De humano a humano para un trato más cercano sin tanto tecnicismo de por medio.

***Características***
- Alcance global: A cualquier usuario de internet
- Internacionalización: Idioma para cada país para que tenga una experiencia acorde con el lenguaje
- Experiencia Omnichannel: Utilizar la misma experiencia tanto online como ofline (misma experiencia tanto física como online)
- Personalización de la compra: Medir su comportamiento pasado para predecir su comportamiento futuro y así mejorar su experiencia de compra
- Accessibilidad: Adaptarse a las diferentes capacidades de los usuarios
- Pago online: Tarjeta de crédito y también pago preferido dependiendo de la ubicación del cliente

***Integraciones***
- Pasarelas de pago dependiendo del lugar
- Pasarelas de envío dependiendo del lugar
- ERP: Manejo de stock y distribución interno
- Business Intelligence: Nos deja utilizar las operaciones u órdenes anteriores de nuestros clientes para predecir su futuro comportamiento y de esta manera brindarle una experiencia mucho más cómoda

***Margento*** es una plataform de código abierto escrita en PHP que tiene la mayoría de estas funciones.

# Preparando el entorno de instalación
## Preparando nuestro entorno, estructura de carpetas y móduos y test pre instalación
Vamos a realizar la configuración del entorno requerido para el funcionamiento de nuestra plataforma de ventas en línea Magento

Algunos de los requerimientos que tenemos son:
- Tener al menos 2 GB de memoria RAM
- Composer
- Web server, puede ser Apache o nginx
- Base de datos, puede ser MySQL 5.6
- Versión de PHP superior a 7.0

Algunas recomendaciones adicionales no obligatorias son:

Utilizar caché y un certificado para todo el sitio.

---

***Estructura***
- app: Donde está la mayor parte de nuestra aplicación
- vendor: Donde está la mayor parte de nuestro código y de terceros. Margento usa PCR para levantar las dependendicas. La idea es usar compose para esta función.
- pub: Donde se servirán los recursos, que de internet es a lo único que se tiene acceso.
- var: logs, caché  creados por Margento


## Configuración del servidor Web y la Bse de datos
Aquí configuramos todo lo necesario para iniciar Margento con MySQL desde la configuración del servidor apache.

# Instalación de la plataforma a producción
Para deployar el proyecto:
- FTP: No es la opción recomendable
- Composer: Es la recomendable
- GitHub: Ideal para trabajo colaborativo donde forkean el proyecto y de allí instalar.


--- Agregar el paso a paso para la instalación

***Descargar composer***
```
curl -sS https://getcomposer.org/installer | php

Para usar:
php composer.phar ...

Para una instalación global:
sudo mv composer.phar /usr/local/bin/composer
```

***Instalación de Magento2 con composer***

Primero crear una cuenta en [https://marketplace.magento.com/](https://marketplace.magento.com/)
 - Seguir con esto [http://devdocs.magento.com/guides/v2.0/install-gde/prereq/connect-auth.html](http://devdocs.magento.com/guides/v2.0/install-gde/prereq/connect-auth.html)
 - La llave pública es usuario y la privada la contraseña

El comando de instalación es:
```
composer create-project --repository-url=https://repo.magento.com/ magento/project-community-edition .
```

Creado el proyecto, sería localhost/magento2

Correr el check para iniciar, recuerda tener una base de datos preconfigurada.

Desde allí se configuran las bases de datos

La url de admin customizarla para que el atacante primero debo encontrar la url, no es algo tan complejo pero es una capa más.

Para las configuraciones usar $USD y Inglés, luego se personaliza a español

Luego crear un Admin.

Hay dos zonas diferentes, un frontend donde los usuarios compran y venden y un administrador donde administraremos nuestra tienda.

## Parámetros de instalación
Ya con la plataforma instalada, vamos a hablar de los diferentes parámetros de instalación. Otra forma de instalar Magento es a través de la consola de comandos.

Vamos a demostrar una instalación por comandos.

Para esto, por la terminal:
```
magento setup:install --base-url=http://127.0.0.1/magento2/ \
--db-host=localhost --db-name=magento --db-user=magento --db-password=magento \
--admin-firstname=Magento --admin-lastname=User --admin-email=user@example.com \
--admin-user=admin --admin-password=admin123 --language=en_US \
--currency=USD --timezone=America/Chicago --use-rewrites=1
```

Instala tu propia versión de Magento y deja todos tus comentarios en el sistema de discusiones.

En la documentación hay otros comandos de instalación, ideal para la instalación por servidor.

## Instalación el cronjob
Un problema recurente y muy fácil de manejar, es la configuración del cronjob.

Para configurarlo vamos a ir a la consola y escribir el sigueinte comando
`crontab -e`

Esto es para ingresar a editar el cronjob, una vez dentro del archivo vamos a ingresar el siguiente comando:
```
#~ MAGENTO START
     /usr/bin/php /var/www/html/magento2/bin/magento cron:run 2>&1 | grep -v Ran jobs by schedule >>/var/www/html/magento2/var/log/magento.cron.log
     /usr/bin/php /var/www/html/magento2/update/cron.php >> /var/www/html/magento2/var/log/update.cron.log
    * /usr/bin/php /var/www/html/magento2/bin/magento setup:cron:run >> /var/www/html/magento2/var/log/setup.cron.log
#~ MAGENTO END
```

Se debe configurar el cronjob porque si no se hace habrán errores y esto es un problema recurrente en las instalciones de Magento.

La configuración está en [enlace](http://devdocs.magento.com/guides/v2.2/config-guide/cli/config-cli-subcommands-cron.html)

## Troubleshooting de instalación
Hay algunos casos en los que nos hemos encontrado con algunos inconvenientes.

1 La instalación se detiene en el 70%: Se debe a que el servidor no tiene los suficientes recursos y el tiempo de ejecución de PHP es muy bajo

Solución: Aumentar el tiempo de ejecución de PHP para que se termine de ejecutar la instalción por completo:
- Localiza el php.ini usando l archivo phpinfo.php
- Abre el archivo php.ini en un editor de texto, esto debe hacerse como usuario con permisos root.
- Localiza el parámetro max_execution_time
- Cambia el valor a 18000
- Guarda los cambios en el php.ini y cierra el editor de texto
- Reinicia Apache

CentOS: service httpd restart
Ubuntu: service apache2 restart

Instrucciones adicionles [enlace](http://devdocs.magento.com/guides/v2.2/install-gde/trouble/php/tshoot_70pct.html)

2 La instalación no se completa, usando nginx: Se debe a que el redirect no está  funcionando.

Solución: Ponerle /setup a la url que estamos usando

3 Error fatal de PDO durante la instalación: Se debe a que no se encuentran instaladas todas las extensiones requeridas para el funcionamiento de Magento 2.

4 Problemas con las sesiones: Se debe a que tenemos configurado PHP para que guarde las sesiones en un lugar distinto a los archivos

Solución: Cambiar el lugar de guardado de sesiones a archivos

5 Problemas con compose: Se debe a que la versión de composr no es compatible

Solución: usar una versión más baja de Composer

Magento es una plataforma en constante desarrollo y con una comunidad muy activa, si alguna vez encuentras otros erros no dudes en registralos en el github del proyecto [https://github.com/magento](https://github.com/magento)

## Areas de Magento 2
Magento se divide en dos áreas distintas, una área de frontend y un área de administración.

***FrontEnd***: Donde los clientes navegan para hacer sus compras

***Administración***: Donde se hace la administración de la tienda.

Demos un recorrido por el admin de Magento 2.2

---

Una vez instalado dirá success

Ambos modos están en dos url distintas, para la url de admin se necesita usuario y contraseña.

Recorrido de Admin:
- Dashboard: Pantalla de control principal, ventas totales, cosas que más busca la gente, etc.
- Sales: Reportes de ventas
- Catalogo: Todo lo referido a la administración del catálogo.
- Custumers: Todos nuestros clientes, verlos y saber qué están haciendo.
- Marketing: Conexiones a facebook, marketing y todo lo que sea seo de nuestra tienda.
- Content: Contenido estático.
- Reports: Reportes necesarios.
- Stores: Envío o pago de nuestras ventas.
- System: Configuraciones avanzadas y módulos.
- Extensiones: Marketplace de las extenciones de Margento

## El admin de Magento
Lo primero que vamos a aprender es a hacer un flush de cache, cómo sabes que necesitas hacerlo? Cuando haces cambios pero en tu sitio no se ven reflejados, necesitas limpiar el cache. Por ejemplo cuando hacemos cambios en el CSS y los cambios no se reflejan.

Para ello en ***Sytem*** -> tildar la lista Refresh  luego en Flush Magento Cache.

***Flush Magento Cache***: Se encarga de la caché de Magento.

***Flush Cache Storage***: Warning, build cache, caché te tercera parte.

Luego en ***System*** -> Index Management -> Seleccionar Rebuild design config grd index -> Update by Schedule para que se reindexe cada cierta cantidad de tiempo. Si el cron no estuviese configurado esto no funcionaría.

En ***Customers*** -> All Customers Agregamos un nuevo Customers. Agregamos nuestro usuario, sale toda la información de los clientes.

> Nota: ***Billing Agreements*** es cuando por ejemplo te suscribes a una revista a través de Magento y todos los meses te cobraría la suscripción.

En ***Wish list***: Son los artículo que el usuario agrega as su wish list para luego aplicar Data Science y predecir su comportamiento futuro.

## Crear tu propio usuario admin

Una opción muy útil es la opción de crear usuarios administradores sin necesidad de ingresar al administrador de Magento. Esto porque muchas veces un cliente te solicita cambios en la tienda pero no tiene acceso administrativo, esto lo puedes resolver de la siguiente manera.

Pare esto vamos a la consola de comandos y digitamos el siguiente comando:
```
magento admin:user:create [--<parameter_name>=<value>, ...]
```

Los posibles parámetros para la configuración son:

Nombre del usuario administrador que estas creando, este parámetro es requerido.
-admin-firstname

Magento administrador user's last name, este parámetro es requerido
-admin-lastname

Dirección de correo electrónico del usuario que estás creando, este parámetro es requerido
-admin-email

UserName del usuario que estás creando, este parámetro es requerido
-admin-user

Contraseña del usuario que estás creando, este parámetro es requerido
-admin-password

La contraseña debe tener por lo menos 7 caracteres e largo, y necesita incluir por lo menos una letra y por lo menos un número.

---

Esto es para crear usuarios administradores sin entrar a la página. Ideal para cuando se nos olvida la contraseña

```
php bin/magento admin:user:create --paremetro='valor'
```

Para cambiar la contraseña del usuario, es ingresar los mismos parámetros pero con la otra contraseña.

> Cuando necesitemos entrar al admin de Magento o crear un nuevo usuario, no necesariamente tenemos que tener el password del admin... Muchas veces los clientes olvidan sus contraseñas o bien nuestros clientes piensan que cuando les pedimos su contraseña admin les vamos a quitar algo (jejeje)

# Manejo de contenido Magento 2
## Manejo de contenido estático, páginas estáticas

Vamos a trabajar con algunas páginas estáticas, veamos cómo se hace la administración de widgets y blogs para incrementar las funcionalidades de nuestra tienda.

En la pestaña de ***Content*** -> Pages para editar las páginas. 

Hay editores para la edición sin necesidad de usa HTML. Pero es recomendable tener nociones básicas ya que no siembre el editor funciona.

Con ***Search Engine Optimization*** Como las urls de acceso, Meta keywords, Meta title.

En ***Page in websites*** podemos configurar los estilos.

También se pueden crear páginas para que se muestren en un período de tiempo, por ejemplo fechas feriadas.
