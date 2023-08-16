// exampleController.go
package controllers

import (
	"fmt"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

// @BasePath /api/v1
// PingExample godoc
// @Summary ping example
// @Schemes
// @Description do ping
// @Tags example
// @Accept json
// @Produce json
// @Success 200 {string} Helloworld
// @Router /example/helloworld [get]
func Helloworld(g *gin.Context) {
	g.JSON(http.StatusOK, fmt.Sprintf("hello world! it is %s", time.Now().Format(time.RFC3339)))
}

func SetupExampleRoutes(router *gin.RouterGroup) {
	eg := router.Group("/example")
	{
		eg.GET("/helloworld", Helloworld)
	}
}
