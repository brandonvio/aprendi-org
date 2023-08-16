// Package main provides ...
package main

import (
	"log"
	"os"

	"github.com/brandonvio/aprendi.org/cmd/aprendi-api/controllers"
	"github.com/brandonvio/aprendi.org/cmd/aprendi-api/docs"
	"github.com/gin-gonic/gin"
)

func main() {
	log.Println("starting up...")

	// swagger
	docs.SwaggerInfo.BasePath = "/api/v1"

	// gin
	g := gin.Default()
	routes(g)

	env := os.Getenv("GIN_MODE")
	if env == "release" {
		log.Println("starting up gin ##LAMBDA## for aprendi-api")
		controllers.RunLambda()
	} else {
		log.Println("starting up gin ##SERVER## for aprendi-api")
		g.Run(":8090")
	}
}
