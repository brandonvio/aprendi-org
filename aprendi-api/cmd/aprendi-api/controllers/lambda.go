// lambda_controller.go

package controllers

import (
	"context"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
	ginadapter "github.com/awslabs/aws-lambda-go-api-proxy/gin"
	"github.com/gin-gonic/gin"
)

var ginLambda *ginadapter.GinLambda

func InitGinLambda(g *gin.Engine) {
	ginLambda = ginadapter.New(g)
}

// LambdaHandler is the entrypoint for AWS Lambda
func LambdaHandler(ctx context.Context, request events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
	return ginLambda.ProxyWithContext(ctx, request)
}

// RunLambda starts the Lambda server
func RunLambda() {
	lambda.Start(LambdaHandler)
}
