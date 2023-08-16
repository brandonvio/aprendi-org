// Package repos provides the repository implementations for the aprendi-api.
package repos

import (
	"strings"

	"github.com/brandonvio/aprendi.org/cmd/aprendi-api/models"
)

// CourseModel represents the Course entity. It is used to transfer course data
// between the application and the database.
type CourseModel struct {
	ID          string `json:"id,omitempty"` // Unique identifier for the course
	OrgID       string `json:"org_id"`       // Identifier for the organization
	CourseName  string `json:"course_name"`  // Name of the course
	Description string `json:"description"`  // Description of the course content
	Section     string `json:"section"`      // Section or batch of the course
}

// ICourseRepo represents the operations associated with the Course entity.
type ICourseRepo interface {
	Save(model CourseModel) (CourseModel, error)     // Saves the given course model to the database
	Get(orgID, courseID string) (CourseModel, error) // Retrieves a course by its orgID and courseID
	GetAll(orgID string) ([]CourseModel, error)      // Retrieves all courses under a given orgID
}

// CourseRepo provides the DynamoDB implementation for the CourseRepo interface.
type CourseRepo struct {
	baseRepo OrganizationDataRepo // Base repository for operations on the OrganizationData table
}

// NewCourseRepo returns a new DynamoCourseRepo instance with the provided base repository.
func NewCourseRepo(baseRepo OrganizationDataRepo) ICourseRepo {
	return &CourseRepo{baseRepo: baseRepo}
}

// coursePK constructs the primary key (PK) for the course based on orgID.
func (repo *CourseRepo) coursePK(orgID string) string {
	return "ORG#" + orgID + "#COURSE"
}

// courseSK constructs the sort key (SK) for the course based on courseID.
func (repo *CourseRepo) courseSK(courseID string) string {
	return "COURSE#" + courseID
}

// parseCourse converts a retrieved OrganizationData item into a CourseModel.
func (repo *CourseRepo) parseCourse(item *models.OrganizationData) CourseModel {
	orgID := strings.Split(item.PK, "#")[1]
	courseID := strings.Split(item.SK, "#")[1]
	return CourseModel{
		ID:          courseID,
		OrgID:       orgID,
		CourseName:  *item.CourseName,
		Description: *item.CourseDescription,
		Section:     *item.CourseSection,
	}
}

// Save saves the given CourseModel to the DynamoDB table.
func (repo *CourseRepo) Save(model CourseModel) (CourseModel, error) {
	data := models.OrganizationData{
		PK:                repo.coursePK(model.OrgID),
		SK:                repo.courseSK(model.ID),
		CourseName:        &model.CourseName,
		CourseDescription: &model.Description,
		CourseSection:     &model.Section,
	}
	err := repo.baseRepo.Save(&data)
	return model, err
}

// Get retrieves a CourseModel from the DynamoDB table based on orgID and courseID.
func (repo *CourseRepo) Get(orgID, courseID string) (CourseModel, error) {
	item, err := repo.baseRepo.GetByPKSK(repo.coursePK(orgID), repo.courseSK(courseID))
	if err != nil || item == nil {
		return CourseModel{}, err
	}
	return repo.parseCourse(item), nil
}

// GetAll retrieves all courses under a specific orgID from the DynamoDB table.
func (repo *CourseRepo) GetAll(orgID string) ([]CourseModel, error) {
	items, err := repo.baseRepo.GetByPK(repo.coursePK(orgID))
	if err != nil {
		return nil, err
	}

	var courses []CourseModel
	for _, item := range items {
		courses = append(courses, repo.parseCourse(&item))
	}
	return courses, nil
}
