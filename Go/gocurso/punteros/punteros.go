package punteros

import "fmt"

// Los punteros son aquellos donde se accede a la dirección de memoria donde
// apunta una variable en la ram

// PointerTest muestra los punteros
func PointerTest() {
	a := 100
	var b *int        // Lo que va a recibir es un espacio de memoria
	b = &a            // b recibe el espacio de memoria de a
	fmt.Println(a, b) // a=100; b=0x2131232d12312
	*b = 10           // Modifica el valor de b y a en 10
	fmt.Println("Después de modificar", a, b)
	fmt.Println("Después de modificar", a, *b)

	// Nota importante
	// b -> Espacio de memoria
	// *b -> Valor de la variable
}
