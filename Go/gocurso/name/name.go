package name

import "fmt"

// GetName esta función devuelve el nombre
func GetName() string {
	var name string
	fmt.Print("Hi, what is yout name?: ")
	fmt.Scanf("%s", &name)
	return name
}
