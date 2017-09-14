package main

import "fmt"

func main() {
	desafio2()
}

type cuadrado struct {
	Lado int
}

func desafio2() {
	ladoStruct := new(cuadrado)
	fmt.Println("Ingrese el valor de lado de un cuadrado")
	fmt.Scanf("%d", &ladoStruct.Lado)
	area, perimetro := AreaPerimetro(ladoStruct.Lado)
	fmt.Printf("El área es %d y \nel perímetro es %d\n", area, perimetro)
}

// AreaPerimetro determina área y perímetro de un cuadrado
func AreaPerimetro(lado int) (int, int) {
	return lado * lado, lado * 4
}

// Solución de Diego
/*
package main

import"fmt"

// Definimos la estructura
type Rectangle struct {
	base   int
	height int
}

// Función para recibir la información del usuario, retorna una instancia de Rectangle
func getInfo() *Rectangle {
	// Creamos una instancia de la struct
	rectangle := new(Rectangle)

	fmt.Println("Calcular el area de un rectangulo")
	fmt.Println("Ingrese el valor de la Base")
	// Recibimos el valor y lo almacenamos en la struct
	fmt.Scanf("%d", &rectangle.base)
	fmt.Println("Ingrese el valor de la Altura")
	// Recibimos el valor y lo almacenamos en la struct
	fmt.Scanf("%d", &rectangle.height)

	return rectangle
}

// Definimos el metodo del struct para calcular el area
func (r Rectangle) getArea() {
	area := r.base * r.height
	fmt.Printf("El área del cuadrado de base %d y altura %d es: %d\n", r.base, r.height, area)
}

// Definimos el metodo del struct para calcular el perímetro
func (r Rectangle) getPerimeter() {
	perimeter := 2 * (r.base + r.height)
	fmt.Printf("El perímetro del cuadrado de base %d y altura %d es: %d\n", r.base, r.height, perimeter)
}

func main() {
	// Almacenamos en r la struct que retorna get info
	r := getInfo()
	// Llamamos a los metodos de la struct
	r.getArea()
	r.getPerimeter()
}
*/
