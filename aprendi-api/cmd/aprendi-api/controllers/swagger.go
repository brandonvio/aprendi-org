// Package controllers contains all the controllers for the application
package controllers

import (
	"github.com/gin-gonic/gin"
	swaggerfiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"
)

// SetupSwaggerRoutes sets up the swagger routes
func SetupSwaggerRoutes(router *gin.Engine) {
	router.GET("/docs/*any", ginSwagger.WrapHandler(swaggerfiles.Handler))
}
