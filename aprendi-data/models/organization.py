"""
This module contains the Organization model and repo
"""
from pydantic import BaseModel
from models.tables import OrganizationTable

METADATA = "ORGANIZATION"


class OrganizationModel(BaseModel):
    """
    This class represents the Organization model
    """
    id: str
    name: str


class OrganizationRepo():
    """
    This class represents the Organization repo
    """

    @staticmethod
    def org_pk(id):
        """
        This method returns the pk for the organization
        """
        return f"ORG#{id}"

    @staticmethod
    def org_sk():
        """
        This method returns the sk for the organization
        """
        return METADATA

    @classmethod
    def save(cls, model: OrganizationModel) -> OrganizationModel:
        """
        This method saves the organization to the database
        """
        pk = cls.org_pk(model.id)
        sk = cls.org_sk()
        org = OrganizationTable(pk=pk, sk=sk, name=model.name)
        org.save()  # Saving to the database
        return model

    @classmethod
    def get_all(cls) -> OrganizationModel:
        """
        This method gets the organization from the database
        """
        all_items = OrganizationTable.scan()
        if all_items:
            return [OrganizationModel(id=item.pk.split("#")[1], name=item.name) for item in all_items]
        return None

    @classmethod
    def get(cls, id: str) -> OrganizationModel:
        """
        This method gets the organization from the database
        """
        pk = cls.org_pk(id)
        sk = cls.org_sk()
        try:
            org = OrganizationTable.get(pk, sk)
            id = org.pk.split("#")[1]
            return OrganizationModel(id=id, name=org.name)
        except OrganizationTable.DoesNotExist:
            return None
