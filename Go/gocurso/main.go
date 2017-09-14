package main

import (
	"fmt"
	"strings"
)

const hello string = "¡Hola!"

func main() {
	/*
		firstName := name.GetName()
		lastname := ""
		var edad int = 26
		a, b, c := getVariables()

		fmt.Print("And lastname?: ")
		fmt.Scanf("%s", &lastname)
		//fmt.Printf("Hola %s, felicidades por tu hola mundo en go.\n", name)
		fmt.Println("Hola de nuevo :D.")

		fmt.Printf(hello+" %s %s. Tienes %d años. a=%d, b=%d y c=%d\n", firstName, lastname, edad, a, b, c)
		fmt.Println(edad, a, b, c, sum(500, 12321))

		strings2()
		switchTest()
	*/
	//fmt.Println(maps.GetMap())
	//fmt.Println(maps.GetMap2())
	//platziCourse2 := struct2.PlatziCourse{Name: "GO", Slug: "Mucho go", Skills: []string{"1", "Dos"}}
	//fmt.Println(platziCourse2)

	// Goroutines
	//go forGo(100)
	//go forGo(200)
	// Si no se pone, los gouroutines morirán cuando el hilo del main termine
	///time.Sleep(10000 + time.Millisecond)

	//struct2.InterfaceTest()
	/*
		number, error := numbers.SumManejoConErrores(50, 50)
		fmt.Println(number, error)

		number2, error2 := numbers.SumManejoConErrores(50, "100")

		// Para hacer un panic (Cerrar completamente el programa)
		if error2 != nil { // Da nil cuando la operación se ejecuta, así fue programado en numbers.numbers.go
			panic(error2)
		}
		fmt.Println(number2, error2)
	*/
	// punteros
	//punteros.PointerTest()

} // Aquí termina el main

func helloGo(index int) {
	fmt.Println("Hola soy un Println en la Go runtimne #", index)
}

func forGo(n int) {
	for i := 0; i < n; i++ {
		go helloGo(i)
	}
}

func getVariables() (int, int, int) {
	return 1, 2, 3
}

func strings2() {
	var text = "Hello world, Hello Platzi, Hello Go"
	fmt.Println(strings.ToUpper(text))                      // Todo a mayúsculas
	fmt.Println(strings.ToLower(text))                      // Todo a minúsculas
	fmt.Println(strings.Replace(text, "Hello", "Hola", -1)) // Reemplaza un caracter por otro, con -1 todos, con 1,2,3,n secuencia de caracteres siguientes
	fmt.Println(strings.Split(text, ","))                   //Se obtiene una Array esparado por cada ","
	fmt.Println(strings.Split(text, ",")[0])                //Imprime el 1er elemento
}
