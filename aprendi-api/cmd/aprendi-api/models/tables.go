// Package models contains the models used in the Aprendi application
package models

// Organization represents the structure of the "aprendi_organization_table" in DynamoDB
type Organization struct {
	PK   string  `dynamo:"pk,hash"`        // Primary Key
	SK   string  `dynamo:"sk,range"`       // Sort Key
	Name string  `dynamo:"name"`           // Organization's name
	Data *string `dynamo:"data,omitempty"` // Optional data
}

// OrganizationData represents the structure of the "aprendi_organization_data_table" in DynamoDB
type OrganizationData struct {
	PK                string  `dynamo:"pk,hash"`                      // Primary Key
	SK                string  `dynamo:"sk,range"`                     // Sort Key
	FirstName         *string `dynamo:"first_name,omitempty"`         // Student/Teacher's first name
	LastName          *string `dynamo:"last_name,omitempty"`          // Student/Teacher's last name
	CourseName        *string `dynamo:"course_name,omitempty"`        // Course name
	CourseDescription *string `dynamo:"course_description,omitempty"` // Course description
	CourseSection     *string `dynamo:"course_section,omitempty"`     // Course section
	TermName          *string `dynamo:"term_name,omitempty"`          // Term name
	Data              *string `dynamo:"data,omitempty"`               // Other optional data
	LSISK1            *string `dynamo:"lsi_sk1,omitempty"`            // Local Secondary Index 1
	LSISK2            *string `dynamo:"lsi_sk2,omitempty"`            // Local Secondary Index 2
}
