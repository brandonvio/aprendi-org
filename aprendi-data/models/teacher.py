"""
This module contains the Teacher model and repo
"""
import json
from typing import Optional
from uuid_extensions import uuid7str
from pydantic import BaseModel
from models.tables import OrganizationDataTable


class TeacherModel(BaseModel):
    """
    This class represents the Teacher model
    """
    id: Optional[str] = None
    org_id: str
    first_name: str
    last_name: str
    degree: str
    dob: str


class TeacherRepo():
    """
    This class represents the Teacher repo
    """

    @staticmethod
    def teacher_pk(org_id: str):
        """
        This method returns the pk for the Teacher
        """
        return f"ORG#{org_id}#TEACHER"

    @staticmethod
    def teacher_sk(teacher_id: str):
        """
        This method returns the sk for the Teacher
        """
        return f"TEACHER#{teacher_id}"

    @classmethod
    def save(cls, model: TeacherModel) -> TeacherModel:
        """
        This method saves the Teacher to the database
        """
        model.id = uuid7str()
        pk = cls.teacher_pk(org_id=model.org_id)
        sk = cls.teacher_sk(teacher_id=model.id)
        data = {
            "degree": model.degree,
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
    def parse_teacher(cls, item) -> TeacherModel:
        """
        This method takes a dynamodb item and returns a TeacherModel
        """
        org_id = item.pk.split("#")[1]
        teacher_id = item.sk.split("#")[1]
        data = json.loads(item.data)
        return TeacherModel(
            id=teacher_id,
            org_id=org_id,
            first_name=item.first_name,
            last_name=item.last_name,
            degree=data["degree"],
            dob=data["dob"])

    @classmethod
    def get(cls, org_id: str, id: str) -> TeacherModel:
        """
        This method gets the Teacher from the database
        """
        pk = cls.teacher_pk(org_id=org_id)
        sk = cls.teacher_sk(teacher_id=id)
        try:
            item = OrganizationDataTable.get(pk, sk)
            return cls.parse_teacher(item)
        except OrganizationDataTable.DoesNotExist:
            return None

    @classmethod
    def get_all(cls, org_id: str) -> list[TeacherModel]:
        """
        This method gets all the Teachers from the database
        """
        pk = cls.teacher_pk(org_id=org_id)
        sk = cls.teacher_sk(teacher_id="")
        items = OrganizationDataTable.query(pk, OrganizationDataTable.sk.startswith(sk))
        return [cls.parse_teacher(item) for item in items]
