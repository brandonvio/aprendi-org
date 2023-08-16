"""
This module contains the Course model and repo
"""
from pydantic import BaseModel
from models.tables import OrganizationDataTable


class CourseModel(BaseModel):
    """
    This class represents the Course model
    """
    id: str = None
    org_id: str
    course_name: str
    description: str
    section: str


class CourseRepo():
    """
    This class represents the Course repo
    """

    @staticmethod
    def course_pk(org_id: str):
        """
        This method returns the pk for the Course
        """
        return f"ORG#{org_id}#COURSE"

    @staticmethod
    def course_sk(course_id: str):
        """
        This method returns the sk for the Course
        """
        return f"COURSE#{course_id}"

    @classmethod
    def save(cls, model: CourseModel) -> CourseModel:
        """
        This method saves the Course to the database
        """
        pk = cls.course_pk(org_id=model.org_id)
        sk = cls.course_sk(course_id=model.id)
        org = OrganizationDataTable(
            pk=pk,
            sk=sk,
            course_name=model.course_name,
            course_description=model.description,
            course_section=model.section)
        org.save()  # Saving to the database
        return model

    @classmethod
    def parse_course(cls, item) -> CourseModel:
        """
        This method takes a dynamodb item and returns a CourseModel
        """
        org_id = item.pk.split("#")[1]
        course_id = item.sk.split("#")[1]
        return CourseModel(
            id=course_id,
            org_id=org_id,
            course_name=item.course_name,
            description=item.course_description,
            section=item.course_section)

    @classmethod
    def get(cls, org_id: str, id: str) -> CourseModel:
        """
        This method gets the Course from the database
        """
        pk = cls.course_pk(org_id=org_id)
        sk = cls.course_sk(course_id=id)
        try:
            item = OrganizationDataTable.get(pk, sk)
            return cls.parse_course(item)
        except OrganizationDataTable.DoesNotExist:
            return None

    @classmethod
    def get_all(cls, org_id: str) -> list[CourseModel]:
        """
        This method gets all the Courses from the database
        """
        pk = cls.course_pk(org_id=org_id)
        sk = cls.course_sk(course_id="")
        items = OrganizationDataTable.query(pk, OrganizationDataTable.sk.startswith(sk))
        return [cls.parse_course(item) for item in items]
