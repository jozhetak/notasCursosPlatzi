# Notas del curso de VueJS Profesional

# Introducción a VueJS

- Complejidad Inherente: Complejidad del funcionamiento y features de la aplicación.
- Complejidad Instrumental: El precio a pagar para realizar la aplicación, cuánto tiempo necesitamos aprender diversas herramientas.

> Ambas debe ir a la par, es una recomendación pagar el precio justo por la aplicación.

Con VueJS es progresivo, puedes algo básico y luego escalarlo o nunca hacerlo.

Caraterísticas:
- Está orientado a la vista
- Es reactivo: La vista se refresca y actualiza el código y viceversa.
- Es una librería chiquita pero es extensible.
- Su core son: Renderizado declarativo  y sistema de componentes.

Capas para agregar:
- Vuex: Manejar estados a gran escala.
- vue-router: Para el enrutamiento
- nuxt: Servir y compilando componentes del lado del servidor usando node.

***Renderizado delcarativo***
Cada vez que el estado mute ya sea en el código o en la vista (botones o input). Esto es reactividad, para que se enlacen y se sincronicen los datos.

Declaramos qué queremos mostrar y cómo queremos mostrarlo, VueJS se encarga del resto.

***Sistema de componentes***
Podemos construir las vistas a partir de pequeños elementos de componentes. Es como un árbol con componentes padres e hijos.

Al separar el código en diversos archivos, permite hacer una aplicación fácil de mantener.

Podemos cargar una aplicación con un componente e insertarlo en otra y debería funcionar de la misma manera.

En la instancia de VueJS, con ***el*** definimos cuál es elemento html al que vamos a montar la aplicación. En ***data()***, definimos todas las propiedades que tienen que ver con la reactividad, es decir, son todas las propiedades que están dentro de data son las que vamos a disponer dentro de la vista para visualizarlas utilizando las expresiones {{ variableEnData  }}

# Herramientas y experiencia de desarrollo

VueJS no corre sobre nodeJS pero muchas de sus herramientas corre sobre nodeJS

***Vue-devtools***

Encontrarlo en [enlace](https://vuejs/vue-devtools) que nos permite debuguear, es muy útil para un plugin en crhome.

***vue-cli*** 
[enlace](https://github.com/vuejs/vue-cli)
Es para interactuar con proyectos vue. Instalar con ***npm install -g vue-cli*** y correr con ***vue init <template-name> <project name>***.

# CLI - Hello world

Tendremos diferentes templates con diferentes herramientas que nos ayudará a la configuración inicial. Los nombres aparecen en el repositorio.

Los archivos .vue contendrá la lógica, el diseño y el estilo.

Creación de Hello world
```
vue init webpacl-simple platzi-music
cd platzi-music
npm install o npm i
npm run dev
```

Usaremos sass, que es un preprocesador de CSS que nos ayudará en el flujo de trabajo.

Partes del proyecto:
- .babelrc: El archivo de configuración de babel, que es un traspilador de código.
- .gitignore: Definir qué cosas no queremos en el repositorio de git
- index.html: Nuestro único html de la aplicación, no tendremos otro.
- package.json: Contiene toda la metadata del proyecto y las dependencias que el proyecto va a utilizar. Para crear compatibilidad en cualquier ambiente de desarrollo.
- README.md: Nuestra carta de presentación y contiene unas instrucciones útiles de nuestro proyecto.
- webpack.config.js: Es un vundle, un archivo que se genera a partir de muchos archivos. Toma muchos archivos pero generan pocos archivos para producción. 
- src: Donde estará todo el código de nuestra aplicación.
  - main.js: Donde se va a instanciar la aplicación a través de vuejs, no debemos configurar nada aquí.
  - App.vue: Componente principal, aquí está el html, lógica y el estilo para que el componente funcione.
  - assets: Donde podemos poner archivos estáticos como imágenes, música, vídeos, etc.

# webpack

El comando "dev" es para correr nuestra aplicación en localhost y con "build" para compilar nuestra aplicación con webpack que se va a llevar a producción.

Babel es un transpilador de código de ecmascript que transforma el código javascript con las últimas funcionalidades a navegadores que no la soporten. Usando babel nos olvidaremos de los problemas de compatibilidad.

En el webpack, propiedad devServer{noinfo} cambiarla a false, para tener algo más de información en la consola de lo que está pasando. En performance, podemos activar las sugerencias para activar las notificaciones de malas prácticas que puede estar afectando el rendimiento de nuestro código.

Al final verifica si vamos a correr en modo de producción, para realizar algunas optimizaciones.

# Babel
EcmaScript a partir del 2015 empezó a lanzar funcionalidades en javascript que nos permiten a los desarrolladores aumentar la productividad pudiendo no ser compatible con ciertos navegadores.

Para ello está babel, que es un traspilador de código javascript a código compatible con navegadores que no soportan las funcionalidades nuevas.

En ***.babelrc*** podemos usar los presets que queramos pero es recomendable usar env.

Esto no tiene nada que ver con Vue, pero puede aplicarse a cualquier otra aplicación en javascript.

# Eslint

Es un linter de código, nos permite definir ciertas reglas para que los desarrolladores que trabajen en el proyecto cumplan con dichas reglas por ejemplo los punto y comas, llaves, etc. Es custmizable.

Otra opción, son reglas predefinidas que se llama standarJS. [https://standarjs.com](https://standarjs.com). Para instalarlo, entramos al repositorio: [feros/eslint-config-standard](https://github.com/feros/eslint-config-standard). Para instalarlo:

***npm i -D eslint***

Copiar las dependencias de las dependencias contenidas en el repositorio y las instrucciones.

Instalarlo en el editor de texto que estemos usando para codear.

Para sobreescribir las reglas, en .eslintrc:

```
{
    "extends": "standar",
    "rules: {
        "no-new": 0
    },
    "plugins": ["html"]
}
```

Debemos chequear la documentación para consultar los parámetros correctos.

Para integrarlo en webpack, en webpackconfig:
Instalar: ***npm i -D eslint-loader *** // El -D es para indicar que solo se va a usar en el entorno de desarrollo.

Instalar: ***npm i -D eslint-plugin-html***

Para hacer que solo funcione en el entorno de desarrollo y lintee solo el contenido de src.

```
rules:[
    {
        test: /\.(js|vue)$/,
        loader: 'eslint-loader',
        enforce: 'pre', 
        include: [path.resolve(_dirname, './src')]
    }
]
```

# Sass y Bulma

Sass es un preprocesador de css el cual nos permite optmizar el código reutilizándolo inclusive usar variables y funciones.

La mayoría de los estilos van a estar dentro de sus componentes.

Bulma es un framework de css, es muy sencillo de utilizar. No necesitamos dependendicas como jQuery y por otro lado nos permite usar sistemas de grilla responsivos pudiendo adaptarse a los diferentes tamaños de pantalla.

***npm i -S bulma***// -S es una dependencia que se va a usar en producción

# Pug

Es un preprocesador de html, que nos permite crear html con mucho menos código y luego con webpack recompilarlo para que funcione en el browser.

*** npm i -D pug pug-loader***

***En pug es importante la identacón***.

Pug, anteriormente se llamaba Jade pero por razones de derechos se tuvo que cambiar el nombre.

# Expresiones
Con {{  }} podemos manejar variables, operaciones artiméticas,

Hay muchas otras directivas en VueJS, pero todas comienzan con ***v***.

# Data binding

Implica que podamos enlazar parámetros desde la vista a nuestro código y del código a la vista. Esto quiere decir que cuando algo se cambie en el código aparecerá en la vista pero también cada vez que el usuario agregue un texto en la vista o interactúe con otros sitios a través de eventos también podemos reflejarlo en elcódigo.

 concatenar métodos y mucho más.

No podemos usar for, if ,etc. Pero podemos hacer expresiones ternarias con:
```
p {{ 1+1 }}
p {{ 'Hola'  + 'Mundo' }}
p {{ person.name }} // definido en data:{person:{name : 'Juan'}}
p {{ person.name.toUpperCase() }}
p {{ JSON.stringify(person) }}
p {{ true ? 'true' : 'false' }}
```

# Directivas

Es una de las expresiones que vienen de Angular 1.

Son marcadores o atributos que podemos agregar a nuestros elementos html que nos sirven para aplicar transformaciones en esos mismos elementos:

```
p (v-show="showValue") {{ value  }} // Muestra el valor si es true
p (v-if="showValue") {{ value }} // De ser falsa ni siquiera va a existir en el DOM (tarda más en comparación a v-show)
p (v-else) {{ 'algo más' }}
p (v-else-if="true") {{'algo más'}}
p (v-else){{ 'lo último' }}

// Para un for
ul (v-for="i in items") {{ i  }} // Items es un array en Data
```

> ***v-show*** lo oculta, ***v-if*** lo elimina.

Hay muchas otras directivas en VueJS, pero todas comienzan con ***v***.

# Data binding

Implica que podamos enlazar parámetros desde la vista a nuestro código y del código a la vista. Esto quiere decir que cuando algo se cambie en el código aparecerá en la vista pero también cada vez que el usuario agregue un texto en la vista o interactúe con otros sitios a través de eventos también podemos reflejarlo en el
código.

```
#app
    input(v-model="name")
    p {{name}}

data():
...
    name: ''
```

Con ***v-bind*** que nos permite enlazar cualquier atributo de un elemento html con cualquier de las propiedades de nuestro ***v-model***

```
#app
    a(v-bind:href="url") Link

data():
...
    
    url: 'https://platzi.com'
```

Podemos escribir ***:*** que equivale a ***v-bind***.

> ***v-model*** Nos permite enlazar propiedades dentro de nuestro v-model con elementos con input de nuestro html. Esto nos permite que el usuario pueda ingresar información y que esta información se refresque automáticamente en nuestro código.

> ***v-bind*** Nos sirve para enlazar cualquier propiedad de nuestro ***v-model*** en cualquier tipo de atributo html.

# Computed properties

Propiedades computadas.

Son calculadas a partir de los valores de otras propiedades, es decir, podemos crear propiedades dinámicas que van a ser regeneradas a la vez que otras propiedades cambien su valor.

Ejemplo:
```
#app
    input(v-model="nam")
    input(v-model="lastName")

data():
...
    name:'',
    lastName: ''

}, // data
 
computed: {
    fullName(){
        return `${this.name} ${this.lastName}`
}
}

```

Tener en cuenta que las propiedades se acceden con ***this***. Un posible uso es calcular la edad de una persona a partir de la fecha de nacimiento. De esta forma, cada vez que la fecha cambie, la edad de la persona se recalcularía inmediatamente.

> "Recuerden que las propiedades computadas nos sirven para generar valores o variables en base a otros valores o propiedades que ya tenemos en el v-model".

Las computed properties son funciones que devuelven un valor y estas funciones pueden utilizar propiedades ya existentes.

Te reto que a que a través de la fecha de nacimiento y una propiedad computada calcules la edad de una persona.

# Watchers

Nos permite ejecutar código a partir de que una propiedad de nuestro v-model cambia. Pero, no devuelven valores, no son propiedades y no pueden ser utilizadas en expresiones.

Los watches, se enlazan directamente con las variables del v-model (las contenida en data) por lo que si queremos usarlas debemos usar el mismo nombre.

Ejemplo:
```
}, // data o computed

watch: {
    // Imprime el valor nuevo y el valor viejo de la propiedad.
    name(newVal, oldVal) {
        console.log(newVal, oldval)
}
}
```

Un uso común de watch es desencadenar peticiones http cuando un input esté modificándose, como por ejemplo el de google y cada vez que se tecle sobre el input reforzar la búsqueda.

# Eventos

Los eventos así como los inputs son la manera de cómo los usuarios pueden interactuar con nuestra aplicación.

Los eventos se crean dentro de un objetos y éstos dentro de ***methods*** que no siempre van a estar ligados a un evento.

```
    name: '',
    formattedName:''
}, // Data
methods: {
    format() {
        this.formattedName = this.name.split(' ').join('-')// Separar por espacio y guardarlo por un guión.
    }
}

#app
    input(v-model="name")
    input(v-model="lastName")
    p {{ fullName }}
    button(v-on:click="format") Format // Tipo de evento y la función a ejecutar.
    p {{ formattedName }}
```

> Los eventos no son solamente para usarlo en botones y eventos click, también pueden usarse en eventos "submit" de formularios. Pueden utilizarse en eventos ***float*** de imágenes y básicamente pueden usarse con cualquier evento soportado por el navegador y por javascript. Podemos reemplazar ***v-on:click*** con ***@click***.

# Integración a PlatziMusic

Recuerda que estamos usando bulma como framework de estilos css.

section.section -> El primero es el id y el segundo la clase

button.is-info y button.is-danger, el is info y is-danger son estilos de botones de bulma.

is-large: Ocupa lo largo de la pantalla
&times; : Para dibujar una cruz chiquitita

Es igual .container que div.container

Bulma usa flex por defecto para el responsive.

La información ficticia o harkcodeada la hacemos fuera de la instanciación de VueJS.

# Servicios

Para interactuar con API podemos hacerlo muy bien con vainilla Javascript. Pero ten en cuenta que las API key serán vistas desde el front.

> Sintaxis kibba: Nombrar los archivos con palabras minusculas separadas por guiones.

Para usar una API, crearemos una carpeta llamada servicios y en ella config.js y platzi-music.js

Para los componentes usaremos pascal-key donde cada palabra tendrá la primera letra en mayúsuculas y no se utilizan espacios para separarse.

# Fetch API & Trae

Fetch nos ayudará a realizar peticiones http y Trae que hará un rapper con Fetch a navegadores que no lo tengan soportado.

***La -S es para guardarla como dependencia para producción***

```
npm i -S trae
```

Cuando no especificas el path de la librería, webpack lo incluirá de npm

Aquí hay un reto de API

# Componentes

Hay dos maneras de crear componentes, una es global que puede ser reutilizado en cualquier aplicación. La otra es la manera local donde especificar dónde usar componentes hijos.

Siempre deben tener un único componente padre. El de los div y esas cosas.

***Esto es global***

src/ChildComponet.vue:
```
<template lang="pug">
  h1 Este es un componente
</template>
```

Se debe importar en main.js

```
...
import ChildCompomnet from './ChildComponet.vue'

vue.component('child', ChildComponent)
```

En App.vue:
```
#app
  ...
  child
```

***Esto es local***

src/LocalComponent.vue
```
<template lang="pug">
  h1 Este es un local component
</template>
```

> Los componentes podemos usarlo en cualquier parte, tanto en App, como Child.

En ChildComponent.vue
```
<template>
  div
    h1 Este es un componente hijo
    local-component <!-- es LocalComponent pero pascal-case lo convierte automáticamente -->
...</template>

<script>
import LocalComponent from './LocalComponent.vue'

export default {
  components: { LocalComponent }
}
</script>
```

# Creación de componentes para PlatziMusic

Es buena práctica colocar todos los componentes dentro de una carpeta componets y dejar App.vue fuera de esta carpeta.

Para el footer se creará una instalación local y no tenga acceso desde otros componentes. Recuerda que al instalar localmente vue lo convierte a pascal case, es decir de PmFooter a pm-footer para el pug.

Revisar la documentación de Bulma y Pug para conocer las propiedades y cómo hacer las cosas. 

La creación de componentes, por buena práctica, empiezan por ***Pm***

# Reactividad

Es una de las cualidades más importante del framework, la reactividad es lo que hace al buscar los cambios realizados y los propague  las vistas de manera dinámica. Para ello Vue agrega Getters y Setters. La función watcher chequea la data y lo renderea ante cualquier cambio para así mostrarlo a las vistas y luego al ***VirtualDom***, para hacer más óptimo el código con las mutaciones cuando que tenemos renderizar y actualizar la vista.

Pero la reactividad tiene un límite. Hay dos maneras:
- Poner en data el objeto a retornar.
- Cuando se inicializa la aplicación y quieres agregar una propiedad nueva:

> Las funciones internas de Vue comienzan por ***$*** 

```
...
  data() {
    return {
      person: {
          name: 'Osmandi'
      }
    }
  },

  methods: {
    addProp() {
      //this.person.lastName = 'Gomez'
      //this.$set(this.person, 'lastName', 'Gomez')
      //Para agregar más de una propiedad y además agregarle una reactividad:

      this.person = Object.assing({}, this.person, {a:1,b:2})
    }
  }
```

# Ciclo de vida de los componentes

Cada componente de Vue tiene un ciclo de vida desde que se crea hasta que se destruye. Todo está en la documentación de VueJS. Hay métodos procedurales y otros que son cíclicos mientras el componente exista.

Se escriben como funciones con el nombre del mismo.

Algunos casos de usos como el ***created*** para cargar en memoria una solicitud a una API.

# Comunicación entre componentes padres e hijos

La comunicación de un padre a un hijo funciona a traves de propiedades, es decir, que envía información a través de propiedades así como las definimos en los html. En cambio, la comunicación de un hijo hacia un padre, la comunicación funciona orientado a eventos, es decir, que    un hijo emite eventos que un padre puede escuchar.

Para quitar el path al especificiar, en webpack:

```
...
resolve:{
  alias: {
    ...
    '@': path.resolve(__dirname, './src')
  }
}
```

Cada vez que vayamos a pasar valores entre componentes debemos bindearlo.

Es buena práctica definir a las variables booleanas con verbos: is, has...

Si algo se va a estar ocultando y prendiendo, es más performante usar v-show.

# Comunicación desde el hijo al padre

Esto es para que cada vez que se le de click a un botón de una de las canciones envíe un evento para que se comunique con el padre. Esto lo haremos con ***v-on*** o @seletct

# Utilización de Slots

Es una funcionalidad que nos permite integrar desde el componente padre html, con elementos dentro de los componentes hijos.

Lo podemos usar para personalizar modals o ventanas emergentes.

Los watch deben llamarse igual que la propiedad que se quiere usar, en este caso showNotification que lo uso como isShowNotification. Lo que se quiere hacer aquí es ocultar la notificación por tres segundos luego de hacer iniciado.

El propósito de los slots es para no sobrecarcargar componentes con mucha lógica. Porque nos permite inyectar html de manera dinámica de padre a hijo.

# Comunicación entre componentes genéricos

Para ello crearemos un plugin en /src/plugins/event-bus.js

Un plugin permite extender métodos y funcionalidades a Vue model con componentes que no están relacionados.

Esto se hace para que el componente Track que no tiene relación con el componente Player se comuniquen.

El evento emit, emite el evento y el on lo escucha.

El caso mostrado en el proyecto es de uso común, un caso muy común del profesor es crear plugin en cosas que usa mucho, por ejemplo un componente que tiene funcionalidad de guardar en el localstorage, en lugar de importar ese archivo en cada uno de esos componentes de manera manual lo que hace es crear un plugin, registrarlo e instalarlo para tal forma que dicha funcionalidad quede en cada uno de los componentes y así usar this.$storage para guardar la información en lugar de hacer un import manual.

# Introducción a VueRouter

Lo que hasta ahora hemos visto es el Core de VueJS. VueRouter es un enrutador del lado del cliente, esto quiere decir que en lugar de ir a otra url y refrescar la página completa, solo refrescará una parte. Ejemplo, en vez de cargar un Header y un Footer en todas las páginas solo carguemos el contenido. De esta forma podemos crear mejor experiencia de usuario.

Con VueRouter cada ruta será un componentes, también hacer animaciones, navegar en el historial del navegador.

# Instalar vue router y configurar router view

***npm i -S vue-router***

> Cuando trabajemos con Pug y bulma, separar los atributos por coma.

# Crear y navegar rutas en router-link

Con $route.params podemos obtener los parámetros que viajan en la url.

El layout con pug se maneja con columns y column.

Para navegar de una ruta a un código, usamos push porque usa el historial de navegación html 5 y porque necesitamos que la ruta sea dinámica (cambio de id).

$route: Información de la ruta específica, es decir parámetros, url, etc.
$router: Navegar programáticamente y para accedera a funcionalidad del router.

El historial de navegación no está por defecto en VueJS, activándolo se elminará el "#" de la url.

En router de main.js

```
const router = new VuewRouter({
  routes,
  mode: `history`
})
```

Tener en cuenta que debemos tener un servidor que soporte el rooteo para que no dañe el cliente.

# Modifiers

Son algunos atributos que podemos agregar sobre directivas que nos permite extender el uso de las directivas, por ejemplo, cuando trabajamos con eventos. Ejemplo presionar enter sobre la barra de navegación.

***@keyup.enter="search"*** Con los modifiers evitamos tener que colocar las teclas.

# Filtros

Permiten mostrar o modificar un valor sin modificar el contenido real. Porque muchos valores en la vista lo mostramos de una manera pero en el código de otra. Por ejemplo convertir milisegundos a minutos.

> Recuerda que los filtros se aplican con |

# Directivas personalizadas

Las directivas son un concepto y una funcionalidad que ya viene por defecto en el framework que ayudan mucho a manipular el DOM.

Al igual que los plugins podemos instalarla global (si la vamos a usar en muchos componentes) y local (uno o dos componentes).

Vamos a crear una directiva que nos detecte si una canción no contiene un preview.

```
function setBlur(elementoHtml, informacionAtributos, referenciaeNuevaAlDom, referenciaAntiguoDom)
```

> Las etiquetas ***a*** no tiene la opción a deshabilitar pero las buton sí.

# Mixins

Nos permiten reutilizar funcionalidades de los componentes, parecido a una herencia pero en realidad los combina.

Cualquier cosa que funcione en un componente la puede colocar en un Mixin.

> Lo que es html no se puede mejorar con un mixin porque para eso están los componentes.

# Vue transitons y animaciones de CSS

Vamos a usar CSS 3.

Cuando movemos en el eje X es por fuera de la pantalla.

En la documentación es Transition Effects -> Transition Classes. 

Editamos el archio src/scss/main.scss

```
.move-enter-active
```

move: Es el name, enter y active son los estados.

Para profundizar de animaciones más sofisticadas está el curso. Hay otro transition.

# Estado centralizado, Flux y Vuex

El profesor recomienda usarlo para aplicaciones de mediana o gran escala.

La principal ventaja es que nos va a permitir ordenar el flujo de información para que nuestros componentes puedan compartir información y comunicarse entre ellos de manera más sencilla.

Todos los componentes se van a conectar a una única fuente de información, esto quiere decir que cada vez que se actualice este store de almacenamiento van a renderizar o recomponener lo visual en los componentes.

La información siempre será en un sentido desde el estado a la vista.

Un buen caso de uso es cuando tenemos mucha interaccíón entre componentes padres e hijos y los que no tienen relaciones. Al ser una aplicación grande va a ser difícil de mantener los eventos que permiten la comunicación entre los componentes.

> No tenemos que preocuparnos de cuándo la tenemos que utilizar, "las librerías Flux son como los anteojos, cuando as vamos a necesitar nos vamos a dar cuenta." @dan_abramov

# State

Instalar con:
***npm i -S vuex***

Con mapState podemos mapear los métodos y así facilitar los estados.

Instalar un preset más avanzado de babel

***npm i -D  babel-preset-stage-2***

Instalar en el .babelrc

```
...
    ["stage-2"]
```

***let {x,y,...z} = {x:1, y:2, a:3, b:4};***

# Mutations

Son las que permiten actualizar la función del estado. Funcionan similares a los eventos, de tal forma que el componente debe actualizar el estado.

En el ejemplo, el componente modifica el estado que actualiza los valores y después es el estado quien propaga los valores en los componentes.

Con VueTool en la pestaña de Vuex podemos ver los valores en cada cambio.

En esta clase se muestra la opción para escribir una función con valores por defecto.

# Getters

Actúan como utilidad para acceder a propiedades del estado de manera customizada.

# Actions

Existen porque las Mutations son operaciones sincrónicas, quiere decir que no podemos ejecutar peticiones http dentro de una mutation porque la petición se va a terminar antes de que Vuex actualice el store de los componentes.

Las acciones nos permiten escribir código asincrónico, para poder ejecutar una mutación cuando el código haya ejecutado.
