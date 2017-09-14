package main

import (
	"fmt"
	"math/rand"
	"strings"
)

// Te reto a crear una función que reciba un string, cambie una letra y retorne el cambio

func main() {
	string()
}

func string() {
	variable := ""
	fmt.Println("Ingresa una palabra")
	fmt.Scanf("%s", &variable)
	fmt.Printf("Palabra que ingresate: %s\n", variable)
	variableModificada := strings.Split(variable, "")
	numeroAleatorio := random(len(variableModificada))
	letraModifcar := variableModificada[numeroAleatorio]
	fmt.Printf("Letra a modificar: %s\n", letraModifcar)
	fmt.Println("Resultado: " + strings.Replace(variable, letraModifcar, "Z", 1))
}

func random(a int) int {
	return rand.Intn(a)
}
