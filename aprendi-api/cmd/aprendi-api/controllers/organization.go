// Package controllers manages HTTP endpoints for different entities.
package controllers

import (
	"net/http"

	"github.com/brandonvio/aprendi.org/cmd/aprendi-api/repos"
	"github.com/gin-gonic/gin"
)

// OrganizationController provides HTTP handlers for the Organization entity.
type OrganizationController struct {
	OrgRepo *repos.OrganizationRepo
}

// NewOrganizationController initializes a new instance of OrganizationController.
func NewOrganizationController(repo *repos.OrganizationRepo) *OrganizationController {
	return &OrganizationController{
		OrgRepo: repo,
	}
}

// @Summary Create an organization
// @Description Save a new organization
// @Tags organizations
// @Accept  json
// @Produce  json
// @Param organization body repos.OrganizationModel true "Organization Model"
// @Success 201 {object} repos.OrganizationModel
// @Failure 400 {object} map[string]string
// @Router /organizations [post]
func (o *OrganizationController) Save(ctx *gin.Context) {
	var org repos.OrganizationModel
	if err := ctx.ShouldBindJSON(&org); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	savedOrg, err := o.OrgRepo.Save(org)
	if err != nil {
		ctx.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	ctx.JSON(http.StatusCreated, savedOrg)
}

// @Summary Get all organizations
// @Description Retrieve all organizations
// @Tags organizations
// @Accept  json
// @Produce  json
// @Success 200 {array} repos.OrganizationModel
// @Failure 404 {object} map[string]string
// @Router /organizations [get]
func (o *OrganizationController) GetAll(ctx *gin.Context) {
	orgs, err := o.OrgRepo.GetAll()
	if err != nil {
		ctx.JSON(http.StatusNotFound, gin.H{"error": "Organizations not found"})
		return
	}

	ctx.JSON(http.StatusOK, orgs)
}

// @Summary Get an organization by its ID
// @Description Retrieve organization details
// @Tags organizations
// @Accept  json
// @Produce  json
// @Param orgID path string true "Organization ID"
// @Success 200 {object} repos.OrganizationModel
// @Failure 404 {object} map[string]string
// @Router /organizations/{orgID} [get]
func (o *OrganizationController) Get(ctx *gin.Context) {
	orgID := ctx.Param("orgID")

	org, err := o.OrgRepo.Get(orgID)
	if err != nil || org == nil {
		ctx.JSON(http.StatusNotFound, gin.H{"error": "Organization not found"})
		return
	}

	ctx.JSON(http.StatusOK, org)
}
