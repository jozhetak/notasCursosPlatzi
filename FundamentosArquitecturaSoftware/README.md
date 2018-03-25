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

- Requerimientos del producto:
  - Negocio: Son las reglas del negocio del programa. Ej: El sistema permita tener varios usuarios.
  - Usuario: Cómo el usuaio se puede desenvolver usndo el sistema. Ejj: Identidades de personas, pago anticipado, seguridad del sistema.
  - Funcional: Se alimentan de los requerimientos anteriores para bajar a tierra, saber qué hay que hacer para implementar la funcionalidad.
- Requerimientos del proyecto: Son requerimientos que tienen que ver con el gestor del proyecto. Recursos, Licencias, Certificaciones, Capacitación, Plan de despliegue. **Por ejemplo, una beta de nuestra aplicación para una feria**.

- Requerimientos funcionales: Como usuario registrado quiere ingresar al sistema para tener una experiencia personalizada.

- Requerimientos no funcionales: Como usuario registrado quiero ingresar de forma segura al sistema para tener una experiencia personalizada.

# Riesgos

Serán muy importantes para atacarlos en un orden.

**Describir el riesgo** Usar escenarios de fracaso que sean medibles y accionables.

"En situaciones de carga pico, los clientes experimentan latencias mayores a cinco segundos".

"Un atacante podría obtener información confidencial por un ataque del medio"

- Riesgos de ingeniería: Relacionados con el análisis, diseño e implementación del producto.
- Riesgos de gestión del proyecto: Relacionados con la planificación, secuenciamiento de trabajo, entregas, tamaño de equipo, etc.

> Cuando más incertidumbre hay en algo que creemos importante, mayor es el riesgo.

**Tenemos que priorizar riesgos** Porque no podemos resolverlos todos. Priorizar aquellos riesgos que ponen en éxito o fracaso de la solución. Postergando los mismos según su prioridad.

# Restricciones

> "Una restricción limita las opciones de diseño o implementación disponibles al desarrollador". Wiegers

- Partes interesadas.
- Integración con otros sistemas.
- Ciclo de vida del producto.

# Panorama y definición

> Ningún patrón de arquitectura va a resolver todos los problemas. No hay bala de plata.

**¿Qué es un estilo de arquitectura?**

Es una colección de decisiones de diseño, aplicables en un contexto determinado, que restringen las decisiones arquitectóncas específicas en ese contexto y obtienen beneficios en cada sistema resultante. Taylor.

# LLamado y retorono

- Programa principal y subrutinas: Es el estilo más básico, ejemplo as funciones. Donde el código es secuencial y llamar a una función.
- Orientado a objetos: Jutamos el estado de la aplicación con los objetos que tienen comportamientos quienes no van a mostrarlo a menos que sean solicitados. Como por ejemplo las clases.
- Cliente - servidor: Un componente cliente se comunica con un servidor para obtener los datos del servidor.
- Multinivel: Cliente -> API -> Backend.

# Estilos: Flujo de datos

- Lote secuencial: Un código ejecuta un proceso y la salida de éste es la entrada de otro.
- Flujo de datos: Unión de aplicaciones que reciben un mismo texto como grep(filtra)->set(reemplaza)->wc(cuenta). Se utiliza mucho en scripting y programas preparados.

# Estilos: Centrados en datos

- Pizarrón: Diferentes componentes que van a interactuar con un componente central quien será el pizarrón. Cada componente hace una tarea y lo escribe en el pizarrón y cuando ya tiene los datos necesarios entrega una salida.
- Centrado en base de datos: Los componentes en vez de comunicarse entre sí lo hacen a través de una base de datos.
- Sistema experto - Basado en reglas: No se le ve muy seguido en aplicaciones modernas. Un componente de tipo cliente va a comunicarse con un componente que estará inferiendo si es una regla o una consulta y cuando tenga una consulta se comunica una base de datos. Es buena idea para esos casos en los que no conocemos los datos a usar.

# Estilos: Componentes independientementes

- Invocación implícita: Basados en eventos. Las aplicaciones pueden mandar mensajes entre sí, sin que una aplicación conozca exactamente a  quién le está hablando. 
- Invocación explícita: Cómo hacer para desarrollar componentes para cómo hacer que se comuniquen entre sí pero desarrollados independientementes.

# Comparando estilos ¿Cómo elijo?

- Estilos monolíticos: Es más fácil dar prioridad.
  - Eficiencia.
  - Curva de aprendizaje.
  - Capacidad de prueba.
  - Capacidad de modificiación.

- Estilos distribuidos:
  - Modularidad.
  - Disponibilidad: Es mayor que la monolítica, que esté disponible el módulo es más barato. Ya que puede escalar mucho más fácil y se aprovechan mejor los recursos.
  - Uso de recursos.
  - Adaptabilidad.

> En esencia la estructura monolícita es de mayor eficienia y facilidad de desarrollo. Mientras que la estructura por microservicios es más fácil de escalar.

# Proyecto: PlatziServicios

**Somos una startup que está empezando**

- Disparador: ¿Cómo encontrar un plomero de confianza?
- Análisis de requerimientos:
  - Criterios de éxito:
    1. Conectar rápidamente a un cliente con un profesional de confianza.
    2. Garantizar el aumento del volúmen de trabajo al profesional.
  - Historias de usuario: (Se debe ser genérico y no dar la solución)
    - Como cliente necesito contactar un profesional en el monento para reparar un problema en mi hogar.
    - Como cliente necesito conocer la experiencia del profesional para decidir a cuál contacto.
    - Como profesional neceesito cobrar mi trabajo realizado para continuar prestando el servicio.
    - Como proesional necesito ampliar mi cartera de clientes para tener más flujo de trabajo.
  - Requerimientos:
    - Ciclo de prestación de servicio: Solicitar, aceptar y finalizar una prestación de servicio de forma segura.
    - Comunicación: Capacidad de búsqueda y comunicación rápida entre clientes y profesionales disponibles.
    - Evaluación: Capacidad de evaluar profesionales y clientes para referencia futura.
  - Riesgos:
    - Un cliente utiliza un servicio y no completa el pago en un tiempo determinado.
    - Un profesional llegó a la puerta de mi casa y no puedo confirmar que sea quien dice que es.
    - El proyecto no está terminado para la feria de Profesionales Independientes de agosto 2018.
  - Restricciones:
    - Recursos disponibles para el desarrollo.
    - Registo de impuestos del profesional.
    - Garantía de profesionales sin antecedentes penales.
- Estilo arquitectónico: Cliente-Servidor montada en la web para aprovechar la infraestructura del internet.

# Desarrollo del proyecto: PlatziServicios fase producto en crecimiento

**Somos una startup en crecimiento**

- Análisis de requerimientos
  - Criterios de éxito:
    1. Brindar a las empresas cliente estabilidad y control de costos de las prestaciones de servicios que necesiten.
    2. Brinar a las empresas prestadoras una visión de crecimiento de sus servicios.
  - Historias de usuario:
    - Como empresa cliente necesito reporte de gastos en servicios para controlar y entender mis finanzas.
    - Como empresa cliente necesito generar listas de profesionales prefridos para nunca perder la disponibilidad del servicio.
    - Como empresa prestadora necesito medir el rendimiento de mis profesionales para comprender mi propio crecimiento.
    - Como empresa prestadora necesito posicionarme como la mejor empresa del mercado para obtener más clientes.
  - Requerimientos:
    - Reportes: Reportes de gasgos por período y por tipo de servicio contratado. Reporte de ingresos y horas trabajadas por profesional por período y tipo de servicio prestado.
    - Autorización: Gestión de usuarios, roles y permisos asociados a acciones del sistema.
    - Posicionamiento y comunicación: Ranking de prestadores por evaluación. Lista priorizada de prestadores por tipo de prestación.
  - Riesgos:
    - Las empresas clientes no pueden extraer la información del sistema para integrar en sus aplicaciones.
    - Los indicadores de la empresa prestadora no son indicativos del trabajo realizado.
    - El proyecto podría recibir juicios de fraude por cobros injustificados.
  - Restricciones:
    - Conformar a estándares de auditoría profesional.
    - Garantizar la privacidad de los datos de consumo.
  - Estilo arquitectónico: Cliente-servidor, pasar base de datos transaccional a otra base de datos de reportes para evitar perder rendimiento de lectura.

# Desarrollo del proyecto: PlatziServicios fase escala global

**Somos ya una startup de gran escala**

**Análisis de crecimiento:**
- Criterios de éxito:  
  - Conectar a empresas locales y lobales con los mejores prestadores de servicios.
  - Facilitar el crecimiento y la globalización de las empresas prestadoras.

- Historias de usuario:
  - Como cliente necesito entender el sistema en mi idioma para poder garantizar el buen uso del mismo.
  - Como cliente necesito acceder a servicios locales y globales para estandarizar los prestadores en mis diferentes localidades.
  - Como usuario necesito acceder a los servicios en cualquier momento para no tener problemas dependientes del huso horario.
  - Como empresa prestadora necesito brindar mis servicios de forma global para ampliar mi alcance al mercado internacional.

- Requerimientos_
  - Internacionalización:
    - Traducciones de contenido.
    - Registro de prestadores globales y capacidad de búsqueda local o global.
  - Disponibilidad de datos:
    - Cálculo de reportes en tiempo real.

- Riesgos:
  - El crecimiento de la compañía hace difícil la transmisión de conocimiento y la productividad de nuestros equipos de desarrollo.
  - Pérdida parcial o total de datos por fallas no previstas.
  - Un mercado específico no es accesible por diferencias de idioma.

- Restricciones:
  - Evitar procesos acoplados a un huso horario específico.
  - Empresas que no permiten que sus datos salgan del país de origen.

- Estilo arquitectónico: Cliente-servidor, con un servidor local y otro global -> Microservicios. Los repotes y el servidor local se comunican con un bus de eventos. Hay una base de datos de reportes y base de datos local.
