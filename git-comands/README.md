# Comandos git para hacer deploy a github

Inicializa un repositorio local

```
git init
```       

Agrega los cambios de todos los archivos al repositorio local.

```
git add .
```

Agrega los cambios de un archivo en específico
```
git add -A archivoModificado.extension
```

Clona un repositorio de la url indicada
```
git clone url.git
```

Muestra el estado del repositorio local (Ej: Cambios no guardados)
```
git status
```

Paso final para guardar los cambios (obligatorio), se recomienda dejar un mensaje de los cambios realizados
```
git commit --m "Mensaje"
```

Establece un enlace entre el repositorio local t el remoto (Debe hacerse solo una vez)
```
git remote add origin url.git
```

Puja todo el contenido del repositorio local al remoto
```
git push -u origin master
```

Nota: Se recomienda en gran medida usar conexiones por SSH en vez de usuario y contraseña, para mayor seguridad.
Una vez habilitada la conexión SSH del repositorio y subida la llave pública, en nuestro terminal
```
eval"$(ssh-agent -s)"
ssh-add pathDelSSH
```


[Tutorial 1](https://www.youtube.com/watch?v=G69dfwG2DJ4)
[Tutorial 2](http://github.com/guides/providing-your-ssh-key)

