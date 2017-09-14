package main

import (
	"fmt"
	"time"
)

// Este es un pequeño juego del tipo ping pong

func main() {
	go pingPong()
	time.Sleep(10 * time.Second)
}

// pingPong Función que será invocada desde el main
func pingPong() {

	// Declaración de canales
	ball := make(chan int)
	action := make(chan string)
	go referi(action)
	go ping(ball, action)
	for {
		value := <-ball
		switch value {
		case 1:
			go pong(ball, action)
		case 2:
			go ping(ball, action)

		}

	}
}

// ping player ping
func ping(ball chan<- int, action chan<- string) {
	ball <- 1
	action <- "Player ping"
}

func pong(ball chan<- int, action chan<- string) {
	ball <- 2
	action <- "Player pong"
}

// Muestra el player en un ciclo iterativo
func referi(action <-chan string) {
	for {
		fmt.Println("Action: ", <-action)
	}
}
