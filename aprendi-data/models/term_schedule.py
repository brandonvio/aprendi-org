"""
This module contains the TermSchedule model and repo
"""
import json
from pydantic import BaseModel
from models.tables import OrganizationDataTable


class TermScheduleModel(BaseModel):
    """
    This class represents the TermSchedule model
    """
    org_id: str
    term_id: str
    course_id: str
    period: str
    teacher_id: str
    # data
    course_name: str
    teacher_name: str


class TermScheduleRepo():
    """
    This class represents the TermSchedule repo
    """

    @staticmethod
    def term_pk(org_id: str, term_id: str):
        """
        This method returns the pk for the TermSchedule
        """
        return f"ORG#{org_id}#TERM#{term_id}#SCHEDULE"

    @staticmethod
    def term_sk(course_id: str, period_number: str, teacher_id: str):
        """
        This method returns the sk for the TermSchedule
        """
        return f"COURSE#{course_id}#PERIOD#{period_number}#TEACHER#{teacher_id}"

    @staticmethod
    def teacher_period_sk(teacher_id: str, period_number: str):
        """
        This method returns the sk for the TermSchedule
        """
        return f"TEACHER#{teacher_id}#PERIOD#{period_number}"

    @staticmethod
    def teacher_sk(teacher_id: str):
        """
        This method returns the sk for the TermSchedule
        """
        return f"TEACHER#{teacher_id}"

    @staticmethod
    def period_course_sk(period_number: str, course_id: str):
        """
        This method returns the sk for the TermSchedule
        """
        return f"COURSE#{course_id}#PERIOD#{period_number}"

    @staticmethod
    def course_sk(course_id: str):
        """
        This method returns the sk for the TermSchedule
        """
        return f"COURSE#{course_id}"

    @classmethod
    def save(cls, model: TermScheduleModel) -> TermScheduleModel:
        """
        This method saves the TermSchedule to the database
        """
        pk = cls.term_pk(org_id=model.org_id, term_id=model.term_id)
        sk = cls.term_sk(course_id=model.course_id, period_number=model.period, teacher_id=model.teacher_id)
        data = {
            "course_name": model.course_name,
            "teacher_name": model.teacher_name
        }
        org = OrganizationDataTable(
            pk=pk,
            sk=sk,
            lsi_sk1=cls.teacher_period_sk(period_number=model.period, teacher_id=model.teacher_id),
            data=json.dumps(data)
        )
        org.save()  # Saving to the database
        return model

    @classmethod
    def parse_term(cls, item) -> TermScheduleModel:
        """
        This method takes a dynamodb item and returns a TermScheduleModel
        """
        pk_split = item.pk.split("#")
        sk_split = item.sk.split("#")
        org_id, term_id = pk_split[1], pk_split[3]
        course_id, period_number, teacher_id = sk_split[1], sk_split[3], sk_split[5]
        data = json.loads(item.data)

        return TermScheduleModel(
            org_id=org_id,
            term_id=term_id,
            course_id=course_id,
            period=period_number,
            teacher_id=teacher_id,
            course_name=data["course_name"],
            teacher_name=data["teacher_name"]
        )

    @classmethod
    def get_by_course_id(cls, org_id: str, term_id: str, course_id: str) -> TermScheduleModel:
        """
        This will get all the periods available for a course.
        """
        pk = cls.term_pk(org_id=org_id, term_id=term_id)
        sk = cls.course_sk(course_id=course_id)
        items = OrganizationDataTable.query(pk, OrganizationDataTable.sk.startswith(sk))
        return [cls.parse_term(item) for item in items]

    @classmethod
    def get_by_course_id_and_period(cls, org_id: str, term_id: str, period: str, course_id: str) -> TermScheduleModel:
        """
        This will get the availablity by course and period.
        """
        pk = cls.term_pk(org_id=org_id, term_id=term_id)
        sk = cls.period_course_sk(period_number=period, course_id=course_id)
        items = OrganizationDataTable.query(pk, OrganizationDataTable.sk.startswith(sk))
        return [cls.parse_term(item) for item in items]

    @classmethod
    def get_by_teacher_id_and_period(cls, org_id: str, term_id: str, period: str, teacher_id: str) -> TermScheduleModel:
        """
        This will tell us if a teacher has already been scheduled for a period.
        """
        pk = cls.term_pk(org_id=org_id, term_id=term_id)
        sk = cls.teacher_period_sk(period_number=period, teacher_id=teacher_id)
        items = OrganizationDataTable.local_secondary_index1.query(pk, OrganizationDataTable.lsi_sk1 == sk)
        return [cls.parse_term(item) for item in items]

    @classmethod
    def get_by_teacher_id(cls, org_id: str, term_id: str, teacher_id: str) -> TermScheduleModel:
        """
        This will tell us if a teacher has already been scheduled for a period.
        """
        pk = cls.term_pk(org_id=org_id, term_id=term_id)
        sk = cls.teacher_sk(teacher_id=teacher_id)
        items = OrganizationDataTable.local_secondary_index1.query(pk, OrganizationDataTable.lsi_sk1.startswith(sk))
        return [cls.parse_term(item) for item in items]
