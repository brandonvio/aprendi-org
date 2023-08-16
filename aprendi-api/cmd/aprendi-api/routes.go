package main

import (
	"github.com/brandonvio/aprendi.org/cmd/aprendi-api/controllers"
	"github.com/gin-gonic/gin"
)

func routes(g *gin.Engine) {
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

		// Setting up the OrganizationController and its route.
		organizationController := ProvideOrganizationController()
		v1.POST("/organizations", organizationController.Save)
		v1.GET("/organizations/:orgID", organizationController.Get)
		v1.GET("/organizations", organizationController.GetAll)
	}
	controllers.SetupSwaggerRoutes(g)
	controllers.InitGinLambda(g)
}
