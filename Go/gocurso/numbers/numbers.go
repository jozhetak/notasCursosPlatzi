package numbers

import (
	"errors"
	"fmt"
)

func sum(a int, b int) int {
	return a + b
}

// SumManejoConErrores suma dos números y maneja errores
func SumManejoConErrores(a interface{}, b interface{}) (int, error) {
	switch a.(type) {
	case string:
		return 0, errors.New("Error")

	}
	switch b.(type) {
	case string:
		return 0, errors.New("El valor es string")

	}
	return a.(int) + b.(int), nil
}

func switchTest() {
	var number = 0
	fmt.Println("[Switch] Ingresa un número del 1 al 10: ")
	fmt.Scanf("%d", &number)
	switch number {
	case 1:
		fmt.Println("El número es 1")
	default:
		fmt.Println("El número no es 1")
	}

	switch {
	case number%2 == 0:
		fmt.Println("Es un número par")
	default:
		fmt.Println("Es un número impar")
	}

}
