package repos

import (
	"errors"

	"github.com/guregu/dynamo"
)

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

// OrganizationDataRepo defines the interface for any repository operations related to OrganizationData.
type OrganizationDataRepo interface {
	// Save inserts or updates an item in the database.
	Save(data *OrganizationData) error

	// GetByPKSK retrieves an item based on its primary and sort keys.
	GetByPKSK(pk, sk string) (*OrganizationData, error)

	// Update modifies an existing item's attributes.
	Update(data *OrganizationData) error

	// Delete removes an item based on its primary and sort keys.
	Delete(pk, sk string) error

	// GetByPK retrieves all items with the given primary key.
	GetByPK(pk string) ([]OrganizationData, error)
}

// DynamoOrganizationDataRepo is an implementation of the OrganizationDataRepo for DynamoDB.
type DynamoOrganizationDataRepo struct {
	dbTable dynamo.Table
}

// NewOrganizationDataRepo initializes a new DynamoDB repository.
func NewOrganizationDataRepo(db dynamo.DB, tableName string) OrganizationDataRepo {
	return &DynamoOrganizationDataRepo{
		dbTable: db.Table(tableName),
	}
}

// Save inserts or updates an item in the database.
func (repo *DynamoOrganizationDataRepo) Save(data *OrganizationData) error {
	return repo.dbTable.Put(data).Run()
}

// GetByPKSK retrieves an item based on its primary and sort keys.
func (repo *DynamoOrganizationDataRepo) GetByPKSK(pk, sk string) (*OrganizationData, error) {
	var data OrganizationData
	err := repo.dbTable.Get("pk", pk).Range("sk", dynamo.Equal, sk).One(&data)
	if err != nil {
		if errors.Is(err, dynamo.ErrNotFound) {
			return nil, nil
		}
		return nil, err
	}
	return &data, nil
}

// Update modifies an existing item's attributes.
// In DynamoDB, an update is essentially a put operation with the same primary and sort keys.
func (repo *DynamoOrganizationDataRepo) Update(data *OrganizationData) error {
	return repo.Save(data)
}

// Delete removes an item based on its primary and sort keys.
func (repo *DynamoOrganizationDataRepo) Delete(pk, sk string) error {
	return repo.dbTable.Delete("pk", pk).Range("sk", sk).Run()
}

// GetByPK retrieves all items with the given primary key.
func (repo *DynamoOrganizationDataRepo) GetByPK(pk string) ([]OrganizationData, error) {
	var dataItems []OrganizationData
	err := repo.dbTable.Get("pk", pk).All(&dataItems)
	if err != nil {
		if errors.Is(err, dynamo.ErrNotFound) {
			return nil, nil
		}
		return nil, err
	}
	return dataItems, nil
}
