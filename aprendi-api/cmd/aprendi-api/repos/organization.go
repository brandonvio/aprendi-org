// Package repos provides the repository implementations for the aprendi-api.
package repos

import (
	"strings"

	"github.com/guregu/dynamo"
)

// METADATA represents the metadata value for the sort key.
const METADATA = "ORGANIZATION"

// Organization represents the Organization entity in the DynamoDB table.
type Organization struct {
	PK   string  `dynamo:"pk,hash"`        // Primary Key
	SK   string  `dynamo:"sk,range"`       // Sort Key
	Name string  `dynamo:"name"`           // Organization's name
	Data *string `dynamo:"data,omitempty"` // Optional data
}

// OrganizationModel represents the data structure to interact with the repo.
type OrganizationModel struct {
	ID   string
	Name string
}

// OrganizationRepo provides methods for CRUD operations on the Organization entity.
type OrganizationRepo struct {
	db  *dynamo.DB
	tab string // Name of the DynamoDB table
}

// NewOrganizationRepo initializes a new instance of OrganizationRepo.
func NewOrganizationRepo(db *dynamo.DB, tableName string) *OrganizationRepo {
	return &OrganizationRepo{db: db, tab: tableName}
}

// orgPK constructs the primary key for the organization based on its ID.
func (repo *OrganizationRepo) orgPK(id string) string {
	return "ORG#" + id
}

// orgSK constructs the sort key for the organization.
func (repo *OrganizationRepo) orgSK() string {
	return METADATA
}

// Save saves the given OrganizationModel to the DynamoDB table.
func (repo *OrganizationRepo) Save(model OrganizationModel) (OrganizationModel, error) {
	org := Organization{
		PK:   repo.orgPK(model.ID),
		SK:   repo.orgSK(),
		Name: model.Name,
	}
	err := repo.db.Table(repo.tab).Put(org).Run()
	return model, err
}

// GetAll retrieves all organizations from the DynamoDB table.
func (repo *OrganizationRepo) GetAll() ([]OrganizationModel, error) {
	var orgs []Organization
	err := repo.db.Table(repo.tab).Scan().All(&orgs)
	if err != nil {
		return nil, err
	}

	var models []OrganizationModel
	for _, org := range orgs {
		models = append(models, OrganizationModel{
			ID:   strings.Split(org.PK, "#")[1],
			Name: org.Name,
		})
	}
	return models, nil
}

// Get retrieves an organization by its ID from the DynamoDB table.
func (repo *OrganizationRepo) Get(id string) (*OrganizationModel, error) {
	org := new(Organization)
	err := repo.db.Table(repo.tab).Get("pk", repo.orgPK(id)).Range("sk", dynamo.Equal, repo.orgSK()).One(org)
	if err != nil {
		if err == dynamo.ErrNotFound {
			return nil, nil
		}
		return nil, err
	}

	model := &OrganizationModel{
		ID:   strings.Split(org.PK, "#")[1],
		Name: org.Name,
	}
	return model, nil
}
