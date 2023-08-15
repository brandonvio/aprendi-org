"""
This module contains the Term model and repo
"""
from pydantic import BaseModel
from models.tables import OrganizationDataTable


class TermModel(BaseModel):
    """
    This class represents the Term model
    """
    org_id: str
    term_id: str
    term_name: str


class TermRepo():
    """
    This class represents the Term repo
    """

    @staticmethod
    def term_pk(org_id: str):
        """
        This method returns the pk for the Term
        """
        return f"ORG#{org_id}#TERM"

    @staticmethod
    def term_sk(term_id: str):
        """
        This method returns the sk for the Term
        """
        return f"TERM#{term_id}"

    @classmethod
    def save(cls, model: TermModel) -> TermModel:
        """
        This method saves the Term to the database
        """
        pk = cls.term_pk(org_id=model.org_id)
        sk = cls.term_sk(term_id=model.term_id)
        org = OrganizationDataTable(
            pk=pk,
            sk=sk,
            term_name=model.term_name)
        org.save()  # Saving to the database
        return model

    @classmethod
    def parse_term(cls, item) -> TermModel:
        """
        This method takes a dynamodb item and returns a TermModel
        """
        org_id = item.pk.split("#")[1]
        term_id = item.sk.split("#")[1]
        term = TermModel(
            org_id=org_id,
            term_id=term_id,
            term_name=item.term_name)
        return term

    @classmethod
    def get(cls, org_id: str, id: str) -> TermModel:
        """
        This method gets the Term from the database
        """
        pk = cls.term_pk(org_id=org_id)
        sk = cls.term_sk(term_id=id)
        try:
            item = OrganizationDataTable.get(pk, sk)
            return cls.parse_term(item)
        except OrganizationDataTable.DoesNotExist:
            return None

    @classmethod
    def get_all(cls, org_id: str) -> list[TermModel]:
        """
        This method gets all the Terms from the database
        """
        pk = cls.term_pk(org_id=org_id)
        sk = cls.term_sk(term_id="")
        items = OrganizationDataTable.query(pk, OrganizationDataTable.sk.startswith(sk))
        terms = [cls.parse_term(item) for item in items]
        return terms
