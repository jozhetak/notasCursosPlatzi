# Bases del lenguaje
## Bienvenida al curso

## Calcula el área de un triángulo. Creando funciones

***Usaremos las herramientas de desarrollador en el navegador***

***Ctrl+l para limpiar***

Para escribir y ejecutar la mayoría del código que vamos a escribir puedes usar la consola de desarrollo de tu navegador.
Para calcular el area de un cuadrado podemos ejecutar:

console.log("El área de un triángulo de base 5 y altura 7 es: " + 5 * 7 / 2)

Los ***String pueden ser comilla ",', `***

Con comilla invertida no necesitamos concatenar las variables para imprimirlas

console.log(`El área de un triángulo de base 5 y altura 7 es: ${5 * 7 / 2}`)


***¿Pero si queremos calcular el area de diferentes cuadrados?***

podemos automatizar esto utilizando una función
Una función encapsula una pieza de código que podemos ejecutar dependiendo de valores que les pasemos, para escribir nuestra funciones usamos el keyword function
Las funciones pueden tener un nombre, pero si no definimos este nombre son funciones anonimas, los valores que recibe se llaman parametros y devuelven un valor usando el keyword return

```
function triangleArea(base, height) {
  return base * height / 2
}

triangleArea(5,7)
```

Algo importante del lenguaje es que podemos asignar una función a una variable y usar un arrow function que nos hace la lectura del código más legible.

> Para declararlo como una constante usar ***const*** en vez de ***let***. Pero no cambiará el valor

Este es otra manera de poner las funciones de una forma más bonita. Se llama Arrow function

***No usar Chromium porque no ejecuta esta función***

let base = 5
let height = 7
let triangleArea = (base, height) => base * height / 2
console.log(`El área de un triángulo de base ${base} y altura ${height} es: ${triangleArea(base, height)}`)

A partir de aquí ejecutar
triangleArea(17,84)

Lo ejecuta

## ¿Quiénes pueden pasar a ver una película? Ejercicio con condicional

Las condiciones nos permiten decidir el código a ejecutar dependiendo de que sucede. Por ejemplo una persona puede pasar a ver una película o no.
Las condicionales se definen con el keyword if la estructura es

if (condición) {
  //código a ejecutar si se cumple la condición
} else {
  //código a ejecutar si no se cumple la condición
}

Algunas de las cosas que podemos evaluar son:

> es mayor
< es menor
>= es mayor e igual
<= es menor e igual
== es igual
!= es diferente
Si queremos concatenar varias condiciones lo podemos hacer usando el keyword else if

```
const startWars7 = 'Star Wars: El Despertar de la Fuerza'
const pgStartWars7 = 13

const nameSacha = 'Sacha'
const ageSacha = 26

const nameSanti = 'Santi'
const ageSanti = 12

function canWatchStart(name,age, isWithAdult=false){
    if (age >= pgStartWars7){
        alert(`${name} puede pasar a ver ${startWars7}`)
    }else if (isWithAdult) {
        alert(`${name} puede pasar a ver ${startWars7}. Aunque su edad es ${age}, se encuentra acomapañdo(a) por un adulto.`)
    }
    
    else{
        alert(`${name} no puede pasar a ver ${startWars7}. Tiene ${age} años y necesita tener ${pgStartWars7}`)
    }
}

canWatchStart(nameSacha, ageSacha)
canWatchStart(nameSanti, ageSanti, true)
```

***Crtl+r para reiniciar la consola***

Al declararse ***const*** no podemos cambiar su valor.

> Reto: Reescribir este código usando Arrow function.

## Inventar un idioma manipulando strings

***Aquí inventamos un idioma llamado Paltzon***

Reglas:
- Si la palabra termina con "ar" se le quitan esas letras
    Ejemplo: programar -> programa
- Si la palabra inicia con "Z", se le añade "pe" al final.
    Ejemplo: Zorro -> Zorrope
- Si la palabra traducida tiene 10 o más letras, se debe partir en dos por la mitad y unir con un guión medio
    Ejemplo: abecedario -> abece-diario
- Si la palabra original es un palíntromo (se leen igual de atrás hacia adelante y viceversa), ninguna regla anterior cuenta y se devuelve la misma palabra pero intercalando letras mayúsculas y minúsculas
    Ejemplo: sometemos ->SoMeTemoS



Los strings son cadenas de texto como palabras, frases, etc.
cuando ejecutamos métodos sobre un string estos no se modifican, debemos asignarlo a otra variable.
Cada letra del texto tiene un indice y este indice comienza en 0, por ejemplo
“platzi” seria
0 = P
1 = l
2 = a
3 = t
4 = z
5 = i
También podemos comenzar a contar su indice desde el final,
-6 = P
-5 = l
-4 = a
-3 = t
-2 = z
-1 = i
Concatenar
Podemos unir dos string utilizando el operador +, por ejemplo:
const palabra = \'Pla\' + \'tzi\' 

palabra == \'Platzi\'
Convertir a arrays
Podemos convertir los arrays a caracteres con el metodo split diciéndole por cual carácter dividirlo, por ejemplo
let str = \'hola\'

str.split(\'\') == [\'h\',\'o\',\'l\',\'a\']
También podemos unir un array y convertirlo en un array usando el metodo join
let arr = [\'h\',\'o\',\'l\',\'a\']

arr.join(\'\') == \'hola\'
Metodos utiles.
str.toUpperCase() // convierte el texto a mayúscula
str.toLowerCase() // convierte el texto en minúsculas
str.endsWith(\'\') // evalúa si el string termina con un texto
str.startsWith(\'\') // evalúa si un string comienza con un texto
str.slice(inicio, final) // partir un carácter
str.length // cuantos caracteres tiene el string

Código
```
function platzom(str){
    let translation = str
    
    // Si la primera palabra termina en "ar", se le quitan esos dos carateres
    
    // Esto no modifica el String sino que actúa sobre él
    
    if(str.toLowerCase().endsWith('ar')){
        translation = str.slice(0,-2)
    }
    
    // Si la palabra inicia con Z, se le añade "pe" al final
    
    if (str.toLowerCase().startsWith('z')){
        translation += 'pe'
    }
    
    // Si la palabra traducida tiene 10 o mas letras se depe partir a la mitad y unir con un guión del medio
    const length = translation.length
    if(length >=10){
        const firstHalf = translation.slice(0,Math.round(length/2))
        
        const secondHalf = translation.slice(Math.round(length/2))
        
        translation = `${firstHalf}-${secondHalf}`
        
    }
    
    /*
    Si la palabra original es un políndromo
    Ninguna regla anterior cuenta y se devuelve
    la misma palabra intercalando mayúsuclas y minúsculas
    */
    
    //split -> Corta en caracteres
    // reverse -> Revierte el orden
    // Join -> Une los caracteres
    const reverse = (str) => str.split('').reverse().join('')
    
    function minMay(str){
        const length = str.length
        let translation = ''
        let capitalize = true
        for (let i = 0; i<length;i++){
            const char = str.charAt(i)
            translation += capitalize ? char.toUpperCase():char.toLowerCase()
            capitalize = !capitalize
        }
        return translation
    }
    
    if (str==reverse(str)){
        return minMay(str)
    }
    
    return translation
}

console.log (platzom("programar"))
console.log(platzom("Zorro"))
console.log(platzom("Zarpar"))
console.log(platzom("abecedario"))
console.log(platzom("sometemos"))
```

## ¿Cuántos km corre una persona promedio? Entendiendo el ciclo for

JavaScript nos permite ejecutar cierto código una cantidad de veces definida, por ejemplo podemos recorrer un array con un ciclo:
const dias = [\'lunes\',\'martes\',\'miércoles\',\'jueves\',\'sábado\',\'domingo\']

for (let i=0; i < dias.length; i++) {
  console.log(\'dia: \', dias[i])
}

La construcción de for tiene tres valores
El iterador
La condición
Cómo cambia el iterador

Math.floor permite redondear para abajo
Matt.raund redondear correctamente

```
const nombre = "Sacha"
const dias =[
    "lunes",
    "martes",
    "miércoles",
    "jueves",
    "viernes",
    "sábado",
    "domingo"
]

function correr(){
    const min = 5
    const max = 15
    return Math.round(Math.random()* (max-min))+min
}

let totalKm = 0
const length = dias.length
for (let i=0;i<length;i++){
    const km = correr()
    totalKm += km
    console.log(`El día ${dias[i]} ${nombre} corrió ${km} km`)
}
const promedioKm = (totalKm/dias.length).toFixed(2)
console.log(`Èn promedio, ${nombre} corrió ${promedioKm} km`)
```

## ¿Quién gana en una pelea: Gokú o Superman? Resolviendo este problema con ciclos while

```
let vidaGoku = 100
let vidaSuperman = 100

const MIN_POWER = 15
const MAX_POWER = 12

function ambosSiguenVivos2(){
    return vidaGoku > 0 && vidaSuperman > 0
}

const ambosSiguenVivos = () => vidaGoku > 0 && vidaSuperman > 0

let round = 0

const gokuSigueVivo = () => vidaGoku>0

const calcularGolpe = () => Math.round(Math.random()*(MAX_POWER - MIN_POWER) + MIN_POWER)

while(ambosSiguenVivos()){
    round++
    console.log(`Round ${round}`)
    
    const golpeGoku = calcularGolpe()
    const golpeSuperman = calcularGolpe()
    
    if(golpeGoku > golpeSuperman){
        // Ataca Goku
        console.log(`Goku ataca a Superman con un golpe de ${golpeGoku}`)
        vidaSuperman -= golpeGoku
        console.log(`Superman queda en ${vidaSuperman} de vida`)
    }else{
        // Ataca Superman
        console.log(`Super ataca a Goku con un golpe de ${golpeSuperman}`)
        vidaGoku -= golpeSuperman
        console.log(`Goku queda en ${vidaGoku} de vida`)
    }
}

if (gokuSigueVivo()){
    console.log(`Goku ganó la pelea.Su vida es de: ${vidaGoku}`)
}else{
    console.log(`Superman ganó la apelea. Su vida es de ${vidaSuperman}`)
}
```

## ¿Cuánto tiempo pasó desde tu fecha de nacimiento
¿Cómo calcularías cuanto tiempo pasó desde la fecha de tu nacimiento?

Primero debemos crear la fecha de nacimiento, en JavaScript podemos ejecutar new Date() y puede recibir una fecha con un año, mes (restandole 1), dia.

Segundo debemos crear la fecha actual, para esto ejeutamos new Date(), esto nos devuelve la fecha actual

Tercero, podemos restar estas dos fechas

De esta forma podemos calcular cuanto tiempo ha pasado desde nuestra fecha de nacimiento en milisegundos.

```
// 12 agosto 1990, cumpleaños de Sacha
const nacimiento = new Date(1990,8-1,12)
nacimiento // Para imprimirlas
const hoy =new Date()
hoy // Imprimir la fecha de hoy
const tiempo = hoy - nacimiento
tiempo // tiempo en milisegundos
const tiempoSegundos = tiempo/1000
const tiempoMin = tiempoSegundo/60
const tiempoHoras = tiempoMin/60
const proximo = new Date(hoy.getFullYear(),nacimiento.getMonth(), nacimiento.getDate())
const diasSemana =[
"domingo",
"lunes",
"martes",
"miercoles",
"jueves",
"viernes",
"sabado"
]
diasSemana[0] // Acceder al domingo
console.log(diasSemana[proximo.getDay()])
```





