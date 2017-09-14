package struct2

import "fmt"

// PlatziCourse structura de un curso
type PlatziCourse struct {
	Name   string
	Slug   string
	Skills []string
}

// PlatziCareer carrerade Platzi
type PlatziCareer struct {
	PlatziCourse
}

// Platzi intrefaz
type Platzi interface {
	Suscribe(Name string)
}

// Suscribe define la suscripción
func (p PlatziCourse) Suscribe(name string) {
	fmt.Printf("La persona %s se ha registrado al curso %s.\n", name, p.Name)
}

// InterfaceTest interfaz
func InterfaceTest() {
	defer deferTest()
	platziCourse := PlatziCourse{Name: "Go genializado", Slug: "Go", Skills: []string{"Go es genial"}}
	platziCareer := new(PlatziCareer)
	platziCareer.Name = "Curso de Go"
	platziCareer.Slug = "Go"
	CallSuscribe(platziCareer)
	CallSuscribe(platziCourse)

}

func deferTest() {
	fmt.Println("Esta es la función defer que se ejecuta al terminar la función donde fue incodada")
	fmt.Println("No importa mucho el orden en que la coloques")
}

// CallSuscribe para suscribirse
func CallSuscribe(p Platzi) {
	p.Suscribe("Osmandi")
}
