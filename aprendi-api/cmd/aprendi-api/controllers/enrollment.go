// Package controllers ...
package controllers

import (
	"fmt"
	"net/http"

	"github.com/brandonvio/aprendi.org/cmd/aprendi-api/repos"
	"github.com/gin-gonic/gin"
)

// EnrollmentController ...
type EnrollmentController struct {
	EnrollmentRepo repos.EnrollmentRepo
}

// NewEnrollmentController ...
func NewEnrollmentController(repo repos.EnrollmentRepo) *EnrollmentController {
	return &EnrollmentController{
		EnrollmentRepo: repo,
	}
}

// @Summary Enroll a student
// @Description enroll a student to a course
// @Tags students
// @Accept  json
// @Produce  json
// @Param enrollment body repos.EnrollmentRequest true "Enrollment Request"
// @Success 200 {string} Post
// @Router /enroll [post]
func (c *EnrollmentController) Post(ctx *gin.Context) {
	var enrollmentRequest repos.EnrollmentRequest
	if err := ctx.ShouldBindJSON(&enrollmentRequest); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	// You can process the enrollment request here, for now it just prints it.
	fmt.Printf("Enrollment request: %+v\n", enrollmentRequest)

	// Response, adjust as necessary.
	ctx.JSON(http.StatusOK, gin.H{"message": "Enrollment processed"})
}
