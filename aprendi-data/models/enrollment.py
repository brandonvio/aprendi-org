"""
This module contains the Enrollment model and repo
"""
import json
from pydantic import BaseModel
from models.tables import OrganizationDataTable


class EnrollmentModel(BaseModel):
    """
    This class represents the Enrollment model
    """
    org_id: str
    student_id: str
    enrollment_id: str
    term_id: str
    course_name: str
    teacher_name: str
    period: str


class EnrollmentRepo():
    """
    This class represents the Enrollment repo
    """

    @staticmethod
    def enrollment_pk(org_id: str, student_id: str):
        """
        This method returns the pk for the Enrollment
        """
        return f"ORG#{org_id}#STUDENT#{student_id}#ENROLLMENT"

    @staticmethod
    def enrollment_sk(term_id: str, enrollment_id: str):
        """
        This method returns the sk for the Enrollment
        """
        return f"TERM#{term_id}#ENROLLMENT#{enrollment_id}"

    @classmethod
    def save(cls, model: EnrollmentModel) -> EnrollmentModel:
        """
        This method saves the Enrollment to the database
        """
        pk = cls.enrollment_pk(org_id=model.org_id, student_id=model.student_id)
        sk = cls.enrollment_sk(term_id=model.term_id, enrollment_id=model.enrollment_id)
        data = {
            "course_name": model.course_name,
            "teacher_name": model.teacher_name,
            "period": model.period
        }
        org = OrganizationDataTable(
            pk=pk,
            sk=sk,
            data=json.dumps(data))
        org.save()  # Saving to the database
        return model

    @classmethod
    def parse_enrollment(cls, item) -> EnrollmentModel:
        """
        This method takes a dynamodb item and returns a EnrollmentModel
        """
        print("#####item:", item)
        org_id = item.pk.split("#")[1]
        student_id = item.pk.split("#")[3]
        term_id = item.sk.split("#")[1]
        enrollment_id = item.sk.split("#")[3]
        data = json.loads(item.data)
        course_name = data["course_name"]
        teacher_name = data["teacher_name"]
        period = data["period"]
        return EnrollmentModel(
            org_id=org_id,
            student_id=student_id,
            enrollment_id=enrollment_id,
            term_id=term_id,
            course_name=course_name,
            teacher_name=teacher_name,
            period=period)

    @classmethod
    def get(cls, org_id: str, student_id: str, term_id: str, enrollment_id: str) -> EnrollmentModel:
        """
        This method gets the Enrollment from the database
        """
        pk = cls.enrollment_pk(org_id=org_id, student_id=student_id)
        sk = cls.enrollment_sk(term_id=term_id, enrollment_id=enrollment_id)
        try:
            item = OrganizationDataTable.get(pk, sk)
            return cls.parse_enrollment(item)
        except OrganizationDataTable.DoesNotExist:
            return None

    @classmethod
    def get_all(cls, org_id: str, student_id: str, term_id: str) -> list[EnrollmentModel]:
        """
        This method gets all the Enrollments from the database
        """
        pk = cls.enrollment_pk(org_id=org_id, student_id=student_id)
        sk = cls.enrollment_sk(term_id=term_id, enrollment_id="")
        items = OrganizationDataTable.query(pk, OrganizationDataTable.sk.startswith(sk))
        return [cls.parse_enrollment(item) for item in items]
