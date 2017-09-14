package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

func main() {
	var client = http.Client{Timeout: 10 * time.Second} // Establece el tiempo de respuesta
	url := "https://jsonplaceholder.typicode.com/posts"

	resp, err := client.Get(url)
	if err != nil {
		panic(err.Error())

	}

	var post []Post

	err = json.NewDecoder(resp.Body).Decode(&post)

	if err != nil {
		panic(err.Error())
	}

	fmt.Println(post)
}

type Post struct {
	// Si fuera sql:"variable" o xmln:"variable"
	UserId int    `json:"userId"`
	ID     int    `json:"id"`
	Tittle string `json:"title"`
	Body   string `json:"body"`
}
