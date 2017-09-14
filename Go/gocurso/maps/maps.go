package maps

func GetMap() map[string]int {
	mapTest := make(map[string]int)

	mapTest["Llave1"] = 1
	mapTest["Llave2"] = 2

	// Para borrar usar
	// delete(mapTest,"Llave1")

	return mapTest
}

func GetMap2() map[string]int {
	mapTest2 := map[string]int{
		"Juan":    18,
		"Yohan":   24,
		"Osmandi": 26,
	}

	return mapTest2
}
