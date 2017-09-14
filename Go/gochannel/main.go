package main

import "fmt"

// Los canales en go es la manera cómo podemos hacer que los goroutines se comuniquen

func main() {
	ch := make(chan string) // Así se declara un canal solo para string

	go func() { // Función anónima, con go es para crear goroutines
		ch <- "Hola channel" // Recibir valores a la pila del canal
		defer close(ch)      // Cerrar el canal

	}() // Ejecutar la función anónima

	fmt.Println(<-ch) // Sacar el goroutine del canal

	ch1 := make(chan int) // Canal de solo goroutines int
	go func() {
		defer close(ch1) // Para que cierre en canal al terminar esta función
		ch1 <- 1
		ch1 <- 2
		ch1 <- 3
		ch1 <- 4
		ch1 <- 5
	}()

	// Nota cada Println saca un goroutine del canal
	for n := range ch1 {
		fmt.Printf("%d\n", n)
	}

	ch2 := make(chan int, 2) // El número es para limitar el número de goroutine en el canal
	ch2 <- 1
	ch2 <- 2
	// ch2 <- 3 // Dará error porque el canal está lleno
	// Cada Print saca un goroutine del canal
	fmt.Println(<-ch2)
	ch2 <- 3 // Se agregará porque con cada Print se saca un goroutine del canal
	fmt.Println(<-ch2)
	fmt.Println(<-ch2)

}
