package main

import (
	"io"
	"net/http"
)

// Esta aplicación es para iniciar un servidor

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8090", nil) // El nil es el manejador

}

// Función de respuesta cuando se conecte al servidor

func handler(w http.ResponseWriter, r *http.Request) { // El * es para dar una respuesta
	io.WriteString(w, "Hola Servidor Go!")
}
