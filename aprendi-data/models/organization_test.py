"""
Integration tests for the OrganizationModel and OrganizationRepo classes.
"""

import pytest
from models.organization import OrganizationModel, OrganizationRepo
from models.tables import OrganizationTable


@pytest.fixture
def dynamodb():
    """
    Mocked DynamoDB setup - assuming the pytest-dynamodb plugin is correctly set up.
    """
    # The pytest-dynamodb plugin would automatically handle this for you.
    # This is just a placeholder to give you an idea.
    pass


def test_organization_model():
    """
    Test to verify the creation of an OrganizationModel instance.
    """
    org = OrganizationModel(id="123", name="OpenAI")
    assert org.id == "123"
    assert org.name == "OpenAI"


def test_save_org(dynamodb):
    """
    Test to save an organization and ensure it gets saved correctly.
    """
    org_model = OrganizationModel(id="1", name="OpenAI")
    saved_org = OrganizationRepo.save(org_model)
    assert saved_org == org_model


def test_get_org(dynamodb):
    """
    Test to retrieve an organization and verify its correctness.
    """
    org_id = "1"
    org_name = "OpenAI"
    org_model = OrganizationModel(id=org_id, name=org_name)
    OrganizationRepo.save(org_model)

    fetched_org = OrganizationRepo.get(org_id)
    assert fetched_org.id == org_id
    assert fetched_org.name == org_name


def test_get_all_orgs(dynamodb):
    """
    Test to retrieve all organizations and ensure they're correctly fetched.
    """
    org1 = OrganizationModel(id="1", name="OpenAI")
    org2 = OrganizationModel(id="2", name="Tesla")

    OrganizationRepo.save(org1)
    OrganizationRepo.save(org2)

    all_orgs = OrganizationRepo.get_all()
    assert len(all_orgs) == 2
    org_ids = {org.id for org in all_orgs}
    assert "1" in org_ids
    assert "2" in org_ids


def test_get_nonexistent_org(dynamodb):
    """
    Test to fetch an organization that does not exist in the database.
    """
    org = OrganizationRepo.get("999")
    assert org is None


def test_save_and_update_org(dynamodb):
    """
    Test to save an organization and then update its attributes.
    """
    org_model = OrganizationModel(id="1", name="OpenAI")
    saved_org = OrganizationRepo.save(org_model)
    assert saved_org.name == "OpenAI"

    # Update the organization's name
    org_model.name = "New Name"
    updated_org = OrganizationRepo.save(org_model)
    assert updated_org.name == "New Name"
    assert updated_org.id == saved_org.id
