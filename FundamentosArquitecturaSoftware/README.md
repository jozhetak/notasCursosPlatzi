# Introducción

Profesor: Guido Contreras Woda

# Etapas del proceso de desarrollo de software

Son etapas en cascada que indican el desarrollo de software:

- Análisis de requerimientos: Una idea, una necesidad, etc. Necesitamos saber qué vamos a descubrir.
- Diseño de la solución: Con el problema señalado se plantea la solución, con el conjunto de las herramientas a utilizar.
- Etapa de desarrollo y evaluación: Es cuando se programa la solución y se realizan los test. A su vez, se definen los fetures a aceptar.
- Despliegue: Hacer deploy para entregarlo al usuario final. Como servidores, balanceo de carga, DevOps, etc. O bien en el Play Store de Android apara que los usuarios la puedan descargar.
- Mantenimiento: Estamos pendiente de los errores y nuevas funciones hasta que detectemos que el software no es necesario.

# Dificultades en el desarrollo de software

* Problemas esenciales: Especificaciones, diseño y comprobación del concepto.
* Problemas Accidentales: Detalles de la implementación y producción actual. Plataforma, lenguajes, etc.

- Esenciales:
  - Complejidad: Cuando un conjunto de problemas a resolver es complejos por sí mismos.
  - Conformidad: En qué contexto se va a utilizar y cómo hacer los ajustes.
  - Tolerancia al cambio: Una vez que terminermos el software ¿va a sser fácil o difícil cambiarlo? No por el lenguaje sino los cambios del problema que estamos atacando. Como por ejemplo, impuestos, etc.
  - Invisibilidad: Trabajar con software es muy difícil porque no es tangible y por tal no entender su forma. Su forma está en código e infraestructura.

- Accidentales:
  - Lenguajes de alto nivel.
  - Multiprocesamiento: El problema del feedback, los resultados de rendimiento del software. Hay herramientas que ayudan acelerar esto.
  - Entornos de programación: Esto tiene que ver con las librerías, lenguaje que estemos utilizando. Que usemos APIs de sistemas externos, etc. Que nos facilita las ventajas de programar "No reinvestes la rueda".

> Las librerías resuelven dificultades accidentales.

### ¿Cómo resolver problemas esenciales?

- No desarrollar: Comprar. Cuando son muy difíciles es mejor comprarlos. O bien OpenSource. Y luego adaptarlo.
- Prototipado rápido: Metodología Agiles. Obtener feedback del usuario en cada paso. Es muy peligroso aquellas metodlogías en las que no obtienes feedback hasta muy tarde en el proceso.
- Grandes Diseñadores: No son solo personas que saben usar una tecnología. Sino que son ingenieros que pueden diseñar una solución elegante y que sea simple. Teniendo la mejor calidad en la parte que necsitan.
- Desarrollo evolutivo.

# Roles

Todo lo definido anteriormente es el desarrollo tradicional.

### Tradicional
1. Experto del dominio: Persona que resuelve las necesidades de los requerimientos.
2. Analista: Indaga en lo que hay que resolver. La persona responsable a definir el problema y a definir los requerimientos que darán solución del software.
3. Administrador del sistema (SysAdmin)
4. QA - Tester, Desarrollador, Arquitecto.
5. Gestor del proyecto.

### Agile
1. Partes interesadas (stakeholders)
2. Cliente - Dueño del producto define los requerimientos de la aplicación.
3. DevOps / SRE (Site reliability engineer). Operaciones y desarrollo. Ingeniero de la confianza del sitio. Las mejores empresas tienen al equipo de DevOps juntos con los del desarrollo.
4. Equipo de desarrollo.
5. Facilitador.

# ¿Qué es arquitectura de software?

> "La estructura del sistema, compuesta por elementos de softwre, sus propiedades visibles y sus relaciones." Software Architecture in practices.

> "El conjunto de decisiones principales de diseño tomadas para el sistema".

> "... la arquitectura se reduce a las cosas importantes, cualesquiera que sean" Fowler.

# La importancia de la comunicación - Ley de Conway

> "Una empresa o una organización va a poder generar estructuras que imiten la estructura de comunicación así como su organización".

Una aplicación distribuida requiere una organización distribuida,

# Objetivos del arquitecto

El arquitecto va a conectar los requerimientos de los stakeholder con el desarrollo.

**Necesidades de los Stakeholders**
- Cliente: Entrega a tiempo y dentro del presupuesto.
- Manager: A parte de los requerimientos del cliente. Permite equipos independientes (autogestionarse) y comunicación clara.
- Dev: Es fácil de implementar y mantener.
- Usuario: El sistema sea confiable, que no falle, y estará disponible cuando lo necesite.
- QA: Sea fácil de probar. Pudiendo responder de forma rápida y que esté modularizado que permita testear cada módulo.

# Arquitectura y metodología

**Metodologías tradicionales** (No tiene feedback hasta que la solución se implementan)
Definición del problema, Restricciones, Requerimientos, Riesgos -> Arguitecto -> Modelo de arquitectura y Documentación.

**Metodología Ágiles**

> No te adelantes a tomar una decisión que puede ser postergada a menos que ya tienes que tomar una decisión.

Se realizan métricas y alertas constantemente. El feedback es constante.

Podemos hacer esqueletos de soluciones. Es decir, plantear una prueba, "esta estructura va a ayudarnos a mejorar la flexibilidad". Hacer arquitectura iterativamente.

**Lo más importante es obtener feedback de lo que tenemos y saber cómo lo podemos mejorar**

# Entender el problema

- Espacio del problema: Idea, criterios de éxito e historias de usuarios. Entender el problem que va resolver y qué no va a resolver.
- Espacio de la solución: Diseño, desarrollo, evaluación, criterios de aceptacón y despliegue. Medir las métricas para obtener el feedback e implementar mejoras.

> La idea es tener claro qué vamos a resolver y qué no.

Problema: Problema definido a solucionar.
Solución: Implementación de tecnologías a utilizar para soluconar el problema.

# Requerimientos


