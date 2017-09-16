### Instrucciones para correr este proyecto

1. Habiendo instalado ya NodeJS y Yarn, abre una terminal y navega hasta el directorio donde está este archivo.

2. Ejecuta el comando yarn install para instalar las dependencias

3. Ejecuta el comando node index.js para correr el Servidor

4. En el navegador, ve a la URL localhost:5678/graphiql para ver GraphiQL

### Instrucciones para crear la base de datos

1. Crea un archivo llamado db.sqlite dentro de la carpeta db

2. Desde el directorio raiz del proyecto ejecuta el comando yarn run db:migrate para generar la estructura en esa base de datos

3. Luego ejecuta el commando yarn run db:seed para generar datos en la base de datos
