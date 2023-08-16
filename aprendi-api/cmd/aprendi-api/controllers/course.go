// Package controllers ...
package controllers

import (
	"net/http"

	"github.com/brandonvio/aprendi.org/cmd/aprendi-api/repos"
	"github.com/gin-gonic/gin"
)

// CourseController ...
type CourseController struct {
	CourseRepo repos.ICourseRepo
}

// NewCourseController ...
func NewCourseController(repo repos.ICourseRepo) *CourseController {
	return &CourseController{
		CourseRepo: repo,
	}
}

// @Summary Create a course
// @Description Save a new course
// @Tags courses
// @Accept  json
// @Produce  json
// @Param course body repos.CourseModel true "Course Model"
// @Success 201 {object} repos.CourseModel
// @Failure 400 {object} map[string]string
// @Router /courses [post]
func (c *CourseController) Save(ctx *gin.Context) {
	var course repos.CourseModel
	if err := ctx.ShouldBindJSON(&course); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	savedCourse, err := c.CourseRepo.Save(course)
	if err != nil {
		ctx.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	ctx.JSON(http.StatusCreated, savedCourse)
}

// @Summary Get a course by orgID and courseID
// @Description Retrieve course details
// @Tags courses
// @Accept  json
// @Produce  json
// @Param orgID path string true "Organization ID"
// @Param courseID path string true "Course ID"
// @Success 200 {object} repos.CourseModel
// @Failure 404 {object} map[string]string
// @Router /courses/{orgID}/{courseID} [get]
func (c *CourseController) Get(ctx *gin.Context) {
	orgID := ctx.Param("orgID")
	courseID := ctx.Param("courseID")

	course, err := c.CourseRepo.Get(orgID, courseID)
	if err != nil {
		ctx.JSON(http.StatusNotFound, gin.H{"error": "Course not found"})
		return
	}

	ctx.JSON(http.StatusOK, course)
}

// @Summary Get all courses under an orgID
// @Description Retrieve all courses. Try "LBU, SDU or OU" as orgID.
// @Tags courses
// @Accept  json
// @Produce  json
// @Param orgID path string true "Organization ID"
// @Success 200 {array} repos.CourseModel
// @Failure 404 {object} map[string]string
// @Router /courses/{orgID} [get]
func (c *CourseController) GetAll(ctx *gin.Context) {
	orgID := ctx.Param("orgID")

	courses, err := c.CourseRepo.GetAll(orgID)
	if err != nil {
		ctx.JSON(http.StatusNotFound, gin.H{"error": "Courses not found"})
		return
	}

	ctx.JSON(http.StatusOK, courses)
}
