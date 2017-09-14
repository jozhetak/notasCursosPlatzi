// El desafío 3 consiste en leer un archivo en el disco
// e imprimir este valor en pantalla
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func main() {

	desafio3()

}

func desafio3() {
	archivote := "archivote.txt" // Establecer nombre del archivo

	if fileExits(archivote) { // Verifica que el archivo exista

		readFile(archivote) // Lee el archivo y lo muestra en consola

	} else { // En caso de no encontrar el archivo

		createFile(archivote) // Lo crea y lo lee

	}
}

// Verifica que el archivo exista
func fileExits(nameFile string) bool {
	_, err := os.Stat("./" + nameFile)
	return err == nil
}

// Crea el archivo, si no existe
func createFile(nameFile string) {
	// Nombre del archivo, contenido casteado en byte y permisos del archivo
	err := ioutil.WriteFile(nameFile, []byte("¡Hola! Estoy aprendiendo Go en Platzi :D "), 0644)
	if err != nil {
		log.Fatal(err)
	}

	readFile(nameFile)
}

// Leer el archivo
func readFile(nameFile string) {
	// Cargar el archivo en memoria
	content, err := ioutil.ReadFile(nameFile)
	if err != nil {
		panic(err)
	}
	// Los ... es para decirle a Go que escriba byte por byte, de esa froma evitar hacer un ciclo for
	content = append(content, []byte("Go!")...)

	err2 := ioutil.WriteFile(nameFile, content, 0644)
	if err2 != nil {
		log.Fatal(err2)
	}

	fmt.Println(string(content) + "\n") // Castear los bytes en string
}
