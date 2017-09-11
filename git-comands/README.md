# Comandos git para hacer deploy a github

git init                        -> Inicializa un repositorio local (Debe hacerse solo una vez).

git add .                       -> Agrega los cambios de todos los archivos al repositorio local.

git add -A archivoModificado    -> Agrega los cambios de un archivo en específico.

git clone url.git 		-> Clona un repositorio de la url indicada (Solo una vez).

git status			-> Muestra el estado del repositrio local (Ej: Cambios no guardados).

git commit --m "Mensaje" 	-> Paso final para guardar los cambios (obligatorio),
		            	  se recomienda dejar un mensaje con los cambios realizados.

git remote add origin url.git 	-> Establece un enlace entre el repositorio local y
			          el remoto (Debe hacerse solo una vez).

git push -u origin master 	-> Puja todo el contenido del repositorio local al remoto.

Nota: Se recomienda en gran medida usar conexiones por SSH en vez de usuario y contraseña. Para mayor seguridad.
Tutorial en: 
https://www.youtube.com/watch?v=G69dfwG2DJ4
http://github.com/guides/providing-your-ssh-key

