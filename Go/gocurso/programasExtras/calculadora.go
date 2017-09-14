/*
	Este es un ejercicio de crear
	una calculadora con Go
*/

package main

import "fmt"

/*
func main() {
	welcome()
	result()
	goodBye()
}
*/
func welcome() {
	fmt.Println("          /*************************************\\")
	fmt.Println("********** Bienvenido a calulator v0.1 by Platzi **********")
	fmt.Println("          \\*************************************/")
}

func getNumbers() (int, int) {
	var numbert1 int
	var numbert2 int
	fmt.Println("Ingresa dos números ENTEROS separados por un espacio.\nEl 0 es el valor por defecto.")
	fmt.Scanf("%d %d", &numbert1, &numbert2)

	return numbert1, numbert2
}
func result() {
	numbert1, numbert2 := getNumbers()
	fmt.Printf("Número %d y Número %d\n", numbert1, numbert2)
	fmt.Printf("Sumatoria = %d\n", sum(numbert1, numbert2))
	fmt.Printf("Resta = %d\n", sust(numbert1, numbert2))
}
func goodBye() {
	fmt.Println("¡Gracias por usar! :D Go es divertido!")
	fmt.Println("***********************************************************")
}

func sum(a int, b int) int {
	return a + b
}
func sust(a int, b int) int {
	return a - b
}
