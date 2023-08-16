package main

import (
	"log"
	"os"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/brandonvio/aprendi.org/cmd/aprendi-api/controllers"
	"github.com/brandonvio/aprendi.org/cmd/aprendi-api/repos"
	"github.com/guregu/dynamo"
)

// ProvideDynamoDb provides a DynamoDB instance
func ProvideDynamoDb() *dynamo.DB {
	endpoint := os.Getenv("DYNAMODB_ENDPOINT")
	session := session.Must(session.NewSession())
	dynamoDb := dynamo.New(session, &aws.Config{
		Region:   aws.String("us-west-2"),
		Endpoint: aws.String(endpoint),
	})
	log.Printf("#dynamodb# endpoint: %s", endpoint)
	return dynamoDb
}

// ProvideDataRepo provides an OrganizationDataRepo
func ProvideDataRepo() repos.OrganizationDataRepo {
	dynamoDb := ProvideDynamoDb()
	dataRepo := repos.NewOrganizationDataRepo(*dynamoDb, "aprendi_organization_data_table")
	return dataRepo
}

// ProvideEnrollmentController provides an EnrollmentController
func ProvideEnrollmentController() *controllers.EnrollmentController {
	enrollmentRepo := repos.NewEnrollmentRepo(ProvideDataRepo())
	enrollmentController := controllers.NewEnrollmentController(*enrollmentRepo)
	return enrollmentController
}

// ProvideCourseController provides a CourseController
func ProvideCourseController() *controllers.CourseController {
	courseRepo := repos.NewCourseRepo(ProvideDataRepo())
	return controllers.NewCourseController(courseRepo)
}

// ProvideOrganizationController provides an OrganizationController
func ProvideOrganizationController() *controllers.OrganizationController {
	dynamoDb := ProvideDynamoDb()
	organizationRepo := repos.NewOrganizationRepo(dynamoDb, "aprendi_organization_table")
	return controllers.NewOrganizationController(organizationRepo)
}
