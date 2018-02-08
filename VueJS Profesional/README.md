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
