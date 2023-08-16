package repos

import (
	"fmt"
	"strings"
)

// EnrollmentRequest represents the Enrollment request model in Go
type EnrollmentRequest struct {
	OrgID     string          `json:"org_id"`
	StudentID string          `json:"student_id"`
	TermID    string          `json:"term_id"`
	Courses   []CourseRequest `json:"courses"`
}

// CourseRequest represents the Course request model in Go
type CourseRequest struct {
	CourseID string `json:"course_id"`
	Prioty   int    `json:"priority"`
}

// Enrollment represents the Enrollment model in Go
type Enrollment struct {
	EnrollmentID string `json:"enrollment_id,omitempty"`
	OrgID        string `json:"org_id"`
	StudentID    string `json:"student_id"`
	CourseID     string `json:"course_id"`
	TermID       string `json:"term_id"`
	CourseName   string `json:"course_name"`
	TeacherName  string `json:"teacher_name"`
	Period       string `json:"period"`
}

// EnrollmentRepo defines the repository operations for the Enrollment model
type EnrollmentRepo struct {
	baseRepo OrganizationDataRepo
}

// NewEnrollmentRepo initializes a new Enrollment repository
func NewEnrollmentRepo(base OrganizationDataRepo) *EnrollmentRepo {
	return &EnrollmentRepo{
		baseRepo: base,
	}
}

// enrollmentPK generates the primary key for the Enrollment
func (er *EnrollmentRepo) enrollmentPK(orgID, studentID string) string {
	return fmt.Sprintf("ORG#%s#STUDENT#%s#ENROLLMENT", orgID, studentID)
}

// enrollmentSK generates the sort key for the Enrollment
func (er *EnrollmentRepo) enrollmentSK(termID, courseID, enrollmentID string) string {
	return fmt.Sprintf("TERM#%s#COURSE#%s#ENROLLMENT#%s", termID, courseID, enrollmentID)
}

// enrollmentCourseSK generates the course sort key for the Enrollment
func (er *EnrollmentRepo) enrollmentCourseSK(termID, courseID string) string {
	return fmt.Sprintf("TERM#%s#COURSE#%s", termID, courseID)
}

// enrollmentTermSK generates the term sort key for the Enrollment
func (er *EnrollmentRepo) enrollmentTermSK(termID string) string {
	return fmt.Sprintf("TERM#%s", termID)
}

// Save inserts or updates an Enrollment in the database
func (er *EnrollmentRepo) Save(enrollment *Enrollment) error {
	dataMap := make(map[string]string)
	dataMap["course_name"] = enrollment.CourseName
	dataMap["teacher_name"] = enrollment.TeacherName
	dataMap["period"] = enrollment.Period
	data := &OrganizationData{
		PK:     er.enrollmentPK(enrollment.OrgID, enrollment.StudentID),
		SK:     er.enrollmentSK(enrollment.TermID, enrollment.CourseID, enrollment.EnrollmentID),
		LSISK1: &enrollment.EnrollmentID,
		Data:   dataMap,
	}
	return er.baseRepo.Save(data)
}

// ParseEnrollment translates a OrganizationData to an Enrollment
func (er *EnrollmentRepo) ParseEnrollment(data *OrganizationData) (*Enrollment, error) {
	orgID := strings.Split(data.PK, "#")[1]
	studentID := strings.Split(data.PK, "#")[3]
	termID := strings.Split(data.SK, "#")[1]
	courseID := strings.Split(data.SK, "#")[3]
	enrollmentID := data.LSISK1
	return &Enrollment{
		EnrollmentID: *enrollmentID,
		OrgID:        orgID,
		StudentID:    studentID,
		TermID:       termID,
		CourseID:     courseID,
		CourseName:   data.Data["course_name"],
		TeacherName:  data.Data["teacher_name"],
		Period:       data.Data["period"],
	}, nil
}

// Get retrieves an Enrollment based on orgID, studentID, termID, and courseID
func (er *EnrollmentRepo) Get(orgID, studentID, termID, courseID string) (*Enrollment, error) {
	data, err := er.baseRepo.GetByPKSK(er.enrollmentPK(orgID, studentID), er.enrollmentCourseSK(termID, courseID))
	if err != nil || data == nil {
		return nil, err
	}
	return er.ParseEnrollment(data)
}

// GetByEnrollmentID retrieves an Enrollment using the enrollment ID
func (er *EnrollmentRepo) GetByEnrollmentID(orgID, studentID, enrollmentID string) (*Enrollment, error) {
	dataItems, err := er.baseRepo.GetByPK(er.enrollmentPK(orgID, studentID))
	if err != nil {
		return nil, err
	}
	for _, item := range dataItems {
		if item.LSISK1 == &enrollmentID {
			return er.ParseEnrollment(&item)
		}
	}
	return nil, nil
}

// GetAll retrieves all Enrollments for a given orgID, studentID, and termID
func (er *EnrollmentRepo) GetAll(orgID, studentID, termID string) ([]Enrollment, error) {
	dataItems, err := er.baseRepo.GetByPK(er.enrollmentPK(orgID, studentID))
	if err != nil {
		return nil, err
	}

	var enrollments []Enrollment
	for _, item := range dataItems {
		if strings.HasPrefix(item.SK, er.enrollmentTermSK(termID)) {
			enrollment, err := er.ParseEnrollment(&item)
			if err == nil {
				enrollments = append(enrollments, *enrollment)
			}
		}
	}
	return enrollments, nil
}
