package repos

import (
	"errors"

	"github.com/brandonvio/aprendi.org/cmd/aprendi-api/models"
	"github.com/guregu/dynamo"
)

// OrganizationDataRepo defines the interface for any repository operations related to models.OrganizationData.
type OrganizationDataRepo interface {
	// Save inserts or updates an item in the database.
	Save(data *models.OrganizationData) error

	// GetByPKSK retrieves an item based on its primary and sort keys.
	GetByPKSK(pk, sk string) (*models.OrganizationData, error)

	// Update modifies an existing item's attributes.
	Update(data *models.OrganizationData) error

	// Delete removes an item based on its primary and sort keys.
	Delete(pk, sk string) error

	// GetByPK retrieves all items with the given primary key.
	GetByPK(pk string) ([]models.OrganizationData, error)
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
func (repo *DynamoOrganizationDataRepo) Save(data *models.OrganizationData) error {
	return repo.dbTable.Put(data).Run()
}

// GetByPKSK retrieves an item based on its primary and sort keys.
func (repo *DynamoOrganizationDataRepo) GetByPKSK(pk, sk string) (*models.OrganizationData, error) {
	var data models.OrganizationData
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
func (repo *DynamoOrganizationDataRepo) Update(data *models.OrganizationData) error {
	return repo.Save(data)
}

// Delete removes an item based on its primary and sort keys.
func (repo *DynamoOrganizationDataRepo) Delete(pk, sk string) error {
	return repo.dbTable.Delete("pk", pk).Range("sk", sk).Run()
}

// GetByPK retrieves all items with the given primary key.
func (repo *DynamoOrganizationDataRepo) GetByPK(pk string) ([]models.OrganizationData, error) {
	var dataItems []models.OrganizationData
	err := repo.dbTable.Get("pk", pk).All(&dataItems)
	if err != nil {
		if errors.Is(err, dynamo.ErrNotFound) {
			return nil, nil
		}
		return nil, err
	}
	return dataItems, nil
}
