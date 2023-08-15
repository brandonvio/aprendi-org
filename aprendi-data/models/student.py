"""
This module contains the Student model and repo
"""
import json
from typing import Optional
from uuid_extensions import uuid7str
from pydantic import BaseModel
from models.tables import OrganizationDataTable


class StudentModel(BaseModel):
    """
    This class represents the Student model
    """
    id: Optional[str] = None
    org_id: str
    first_name: str
    last_name: str
    dob: str


class StudentRepo():
    """
    This class represents the Student repo
    """

    @staticmethod
    def student_pk(org_id: str):
        """
        This method returns the pk for the Student
        """
        return f"ORG#{org_id}#STUDENT"

    @staticmethod
    def student_sk(student_id: str):
        """
        This method returns the sk for the Student
        """
        return f"STUDENT#{student_id}"

    @classmethod
    def save(cls, model: StudentModel) -> StudentModel:
        """
        This method saves the Student to the database
        """
        model.id = uuid7str()
        pk = cls.student_pk(org_id=model.org_id)
        sk = cls.student_sk(student_id=model.id)
        data = {
            "dob": model.dob
        }
        org = OrganizationDataTable(
            pk=pk,
            sk=sk,
            first_name=model.first_name,
            last_name=model.last_name,
            data=json.dumps(data))
        org.save()  # Saving to the database
        return model

    @classmethod
    def parse_student(cls, item) -> StudentModel:
        """
        This method takes a dynamodb item and returns a StudentModel
        """
        org_id = item.pk.split("#")[1]
        student_id = item.sk.split("#")[1]
        data = json.loads(item.data)
        return StudentModel(
            id=student_id,
            org_id=org_id,
            first_name=item.first_name,
            last_name=item.last_name,
            dob=data["dob"])

    @classmethod
    def get(cls, org_id: str, id: str) -> StudentModel:
        """
        This method gets the Student from the database
        """
        pk = cls.student_pk(org_id=org_id)
        sk = cls.student_sk(student_id=id)
        try:
            item = OrganizationDataTable.get(pk, sk)
            return cls.parse_student(item)
        except OrganizationDataTable.DoesNotExist:
            return None

    @classmethod
    def get_all(cls, org_id: str) -> list[StudentModel]:
        """
        This method gets all the Students from the database
        """
        pk = cls.student_pk(org_id=org_id)
        sk = cls.student_sk(student_id="")
        items = OrganizationDataTable.query(pk, OrganizationDataTable.sk.startswith(sk))
        return [cls.parse_student(item) for item in items]
