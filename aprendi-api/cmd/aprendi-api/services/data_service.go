// Package services contains the business logic for interacting with the database.
package services

// Import statements, including those from the previous example
import (
	"github.com/brandonvio/aprendi.org/cmd/aprendi-api/repos"
)

// OrganizationDataService is an interface defining methods a service should implement
// for interacting with OrganizationData.
type OrganizationDataService interface {
	Create(data *repos.OrganizationData) error
	Fetch(pk, sk string) (*repos.OrganizationData, error)
	Modify(data *repos.OrganizationData) error
	Remove(pk, sk string) error
}

// OrganizationDataServiceImpl is a concrete implementation of OrganizationDataService.
type OrganizationDataServiceImpl struct {
	repo repos.OrganizationDataRepo
}

// NewOrganizationDataService creates a new instance of OrganizationDataServiceImpl.
func NewOrganizationDataService(repo repos.OrganizationDataRepo) OrganizationDataService {
	return &OrganizationDataServiceImpl{
		repo: repo,
	}
}

// Create stores the given OrganizationData into the database.
func (s *OrganizationDataServiceImpl) Create(data *repos.OrganizationData) error {
	// Add any business validation or logic here

	// Persist data
	return s.repo.Save(data)
}

// Fetch retrieves an OrganizationData based on its primary and sort keys.
func (s *OrganizationDataServiceImpl) Fetch(pk, sk string) (*repos.OrganizationData, error) {
	// Add any pre-fetch logic here if needed

	return s.repo.GetByPKSK(pk, sk)
}

// Modify updates an existing OrganizationData's attributes.
func (s *OrganizationDataServiceImpl) Modify(data *repos.OrganizationData) error {
	// Add any business validation or logic here

	// Persist changes
	return s.repo.Update(data)
}

// Remove deletes an OrganizationData based on its primary and sort keys.
func (s *OrganizationDataServiceImpl) Remove(pk, sk string) error {
	// Add any pre-delete logic or validation here

	return s.repo.Delete(pk, sk)
}
