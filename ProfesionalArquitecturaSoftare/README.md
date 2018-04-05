# Notas del curso profesional de arquitectura de software

# Defición

**Atributos de calidad**
"Los atributos de calidad son expectativas de usuario, en general implícitas, de cuán bien funcionará un producto". Por ejemplo, rendimiento y seguridad de la aplicación.

# Atributos: Idoneidad funcional

Es lo que conecta al usuario de las necesidades del usuario con las funcionabilidades de la aplicación.

- Completitud funcional: De cuán está completa las funciones respecto a lo que se espera del sistema. Requerimietos funcionales vs funcionales implementadas.
  - Por ejemplo que necesitemos implementar login de redes sociales, podríamos hacerlo incrementalmente.
- Exactitud funcional: Lo preciso de la implementación funcional. Resultado esperado vs resultado obtenido.
  - De esto saber si se ha tenido un éxito o un fracaso.
- Pertinencia funcional: Cuán alineado está lo que se implementó con lo que se necesita. Objetivos cumplidos vs objetivos esperados.
  - Las aplicaciones suelen ser muy buenas al principio. Pero en la medida que avance la aplicación esto será segmentado.

# Atributos: Eficiencia de ejecución

Trata de cuán bueno es la aplicación al momento de responder lo que el usuario necesita. Y saber cómo aprovecha los recursos disponibles.

- Tiempo a comportamiento: Tiempo transcurrido entre pedido y respuesta vs tiempo esperado o tiempo máximo tolerado.
- Uso de recursos: Consumo de recursos vs consumo esperado o tolerado de recursos. Ejemplo: RAM, CPU.
- Capacidad: Límite de tolerancia detectado y límite de tolerancia esperado. Esto es la cantidad de tiempo en responder. En esto se utilizan las métricas! Debemos estar preparado para esos momentos en que el sistema va a estar exigido.

# Atributos: Compatibilidad

Trata de cuán el sistema es compatible con otro. Es decir en vivir en un contexto más grande.

- Interoperabilidad: Cuán fácil es comunicarse con este sistema.
  - Implementación de estándares y disponibilidad de esquemmas: HATEOAS (analizar una API de un sistema), SOAP, Open API, JSON Schema. Todo esto trata de cómo comunicarse con el sistema de forma programática.
- Coexistencia: Cuánto el sistema soporta o no estar en un contexto con otro sistema. Es decir en otro servidor.
  - Cantidad de fallos por razones externas en un tiempo dado. En un contexto dado, que una aplicación externa hace que falle nuestra aplicación. Ejemplo API públicas. Ejemplo transacciones.

# Atributos: Usabilidad

- Reconocimiento de idoneidad: Cuánto nos damos cuenta es lo que nosostros necesitamos usar para resolveer un problema. Relación entre conceptos de dominio y acciones de sistema. Ejemplo: Compra, carrito de compra para asociar la acción a una compra.
- Curva de aprendizaje: Cuán fácil o difícil es aprender a usar el sistema. Cuanto más intuitivo  sea el sistema más fácil será usarlo.
- Operabilidad: Cantidad de pasos hasta lograr los objetivos. Métricas de conversión.
- Protección a errores: Cantidad de intentos fallidos e intentos totales de interacción: Esto viene del feedback de los usuarios.
- Estética de interfaz: Es muy abstracto, podemos hacer encuesta de apreciación de estética de nuestros usuarios.
- Accesibilidad: Adhesión a estándares, para ser usado por personas con discapacidades.

Ejemplos:
- Reconocimiento de idoneidad: Cuando estamos haciendo uso de un sistema que no está hecho para tal. Ejemplo los CM como WordPress que está hecho para hacer blogs pero tiende a ser complicado agregar funcionabilidades para que haga lo que queramos que haga. El dominio de la aplicación originalmente se distanción mucho del uso actual.
- Curva de aprendizaje: Aprovechar diseños ya establecidos para que intuitivamente el usuario tenga una curva de aprendizaje ligera.
- Operabilidad: Intentar ahorar pasos.
- Protección a errores: Maneras rápidas de decirle a usuario que se equivocó y cómo corregirlo. Como por ejemplo que no se haya ejecutado un pago. De la forma más amable posible porque nos interesa que complete ese paso.
- Estética de la interfaz: Esto trata de UX y UI. Todo dependerá del usuario final.aa
- Accesibilidad: Por ejemplo imágenes con texto, para ello usar **alt** de las imágenes. Puede ser con los usuarios con discapacidades visuales, o bien no usar html semántico.
- Estética de interfaz: 
