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
	log.Println("starting up ##GIN## __aprendi-api__")
	g := gin.Default()
	docs.SwaggerInfo.BasePath = "/api/v1"

	v1 := g.Group("/api/v1")
	{
		controllers.SetupExampleRoutes(v1)

		// Setting up the EnrollmentController and its route.
		enrollmentController := ProvideEnrollmentController()
		v1.POST("/enroll", enrollmentController.Post)

		// Setting up the CourseController and its route.
		courseController := ProvideCourseController()
		v1.POST("/courses", courseController.Save)
		v1.GET("/courses/:orgID/:courseID", courseController.Get)
		v1.GET("/courses/:orgID", courseController.GetAll)
	}

	controllers.SetupSwaggerRoutes(g)
	controllers.InitGinLambda(g)

	env := os.Getenv("GIN_MODE")
	if env == "release" {
		log.Println("starting up gin ##LAMBDA## for aprendi-api")
		controllers.RunLambda()
	} else {
		log.Println("starting up gin ##SERVER## for aprendi-api")
		g.Run(":8090")
	}
}
