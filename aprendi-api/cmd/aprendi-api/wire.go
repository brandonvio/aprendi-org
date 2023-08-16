package main

import (
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/brandonvio/aprendi.org/cmd/aprendi-api/controllers"
	"github.com/brandonvio/aprendi.org/cmd/aprendi-api/repos"
	"github.com/guregu/dynamo"
)

// ProvideEnrollmentController provides an EnrollmentController
func ProvideEnrollmentController() *controllers.EnrollmentController {
	session := session.Must(session.NewSession())
	dynamoDb := dynamo.New(session, &aws.Config{Region: aws.String("us-west-2")})
	dataRepo := repos.NewOrganizationDataRepo(*dynamoDb, "aprendi_organization_data_table")
	enrollmentRepo := repos.NewEnrollmentRepo(dataRepo)
	enrollmentController := controllers.NewEnrollmentController(*enrollmentRepo)
	return enrollmentController
}
