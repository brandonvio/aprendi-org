// Code generated by swaggo/swag. DO NOT EDIT.

package docs

import "github.com/swaggo/swag"

const docTemplate = `{
    "schemes": {{ marshal .Schemes }},
    "swagger": "2.0",
    "info": {
        "description": "{{escape .Description}}",
        "title": "{{.Title}}",
        "contact": {},
        "version": "{{.Version}}"
    },
    "host": "{{.Host}}",
    "basePath": "{{.BasePath}}",
    "paths": {
        "/courses": {
            "post": {
                "description": "Save a new course",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "courses"
                ],
                "summary": "Create a course",
                "parameters": [
                    {
                        "description": "Course Model",
                        "name": "course",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/repos.CourseModel"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Created",
                        "schema": {
                            "$ref": "#/definitions/repos.CourseModel"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "type": "object",
                            "additionalProperties": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        },
        "/courses/{orgID}": {
            "get": {
                "description": "Retrieve all courses. Try \"UCSD\" as orgID.",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "courses"
                ],
                "summary": "Get all courses under an orgID",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Organization ID",
                        "name": "orgID",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/repos.CourseModel"
                            }
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "type": "object",
                            "additionalProperties": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        },
        "/courses/{orgID}/{courseID}": {
            "get": {
                "description": "Retrieve course details",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "courses"
                ],
                "summary": "Get a course by orgID and courseID",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Organization ID",
                        "name": "orgID",
                        "in": "path",
                        "required": true
                    },
                    {
                        "type": "string",
                        "description": "Course ID",
                        "name": "courseID",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/repos.CourseModel"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "type": "object",
                            "additionalProperties": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        },
        "/enroll": {
            "post": {
                "description": "enroll a student to a course",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "students"
                ],
                "summary": "Enroll a student",
                "parameters": [
                    {
                        "description": "Enrollment Request",
                        "name": "enrollment",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/repos.EnrollmentRequest"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "/example/helloworld": {
            "get": {
                "description": "do ping",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "example"
                ],
                "summary": "ping example",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "/organizations": {
            "get": {
                "description": "Retrieve all organizations",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "organizations"
                ],
                "summary": "Get all organizations",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/repos.OrganizationModel"
                            }
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "type": "object",
                            "additionalProperties": {
                                "type": "string"
                            }
                        }
                    }
                }
            },
            "post": {
                "description": "Save a new organization",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "organizations"
                ],
                "summary": "Create an organization",
                "parameters": [
                    {
                        "description": "Organization Model",
                        "name": "organization",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/repos.OrganizationModel"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Created",
                        "schema": {
                            "$ref": "#/definitions/repos.OrganizationModel"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "type": "object",
                            "additionalProperties": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        },
        "/organizations/{orgID}": {
            "get": {
                "description": "Retrieve organization details",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "organizations"
                ],
                "summary": "Get an organization by its ID",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Organization ID",
                        "name": "orgID",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/repos.OrganizationModel"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "type": "object",
                            "additionalProperties": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        }
    },
    "definitions": {
        "repos.CourseModel": {
            "type": "object",
            "properties": {
                "course_name": {
                    "description": "Name of the course",
                    "type": "string"
                },
                "description": {
                    "description": "Description of the course content",
                    "type": "string"
                },
                "id": {
                    "description": "Unique identifier for the course",
                    "type": "string"
                },
                "org_id": {
                    "description": "Identifier for the organization",
                    "type": "string"
                },
                "section": {
                    "description": "Section or batch of the course",
                    "type": "string"
                }
            }
        },
        "repos.CourseRequest": {
            "type": "object",
            "properties": {
                "course_id": {
                    "type": "string"
                },
                "priority": {
                    "type": "integer"
                }
            }
        },
        "repos.EnrollmentRequest": {
            "type": "object",
            "properties": {
                "courses": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/repos.CourseRequest"
                    }
                },
                "org_id": {
                    "type": "string"
                },
                "student_id": {
                    "type": "string"
                },
                "term_id": {
                    "type": "string"
                }
            }
        },
        "repos.OrganizationModel": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                }
            }
        }
    }
}`

// SwaggerInfo holds exported Swagger Info so clients can modify it
var SwaggerInfo = &swag.Spec{
	Version:          "",
	Host:             "",
	BasePath:         "",
	Schemes:          []string{},
	Title:            "",
	Description:      "",
	InfoInstanceName: "swagger",
	SwaggerTemplate:  docTemplate,
	LeftDelim:        "{{",
	RightDelim:       "}}",
}

func init() {
	swag.Register(SwaggerInfo.InstanceName(), SwaggerInfo)
}
