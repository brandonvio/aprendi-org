"""
Database Seeder

This module contains the logic to seed the database with a term schedule.
It sets up the necessary tables, populates them with domain data, and finally
creates term schedules using the populated data.
"""

from collections import namedtuple
from models.tables import OrganizationDataTable, OrganizationTable
from models.course import CourseModel, CourseRepo
from models.student import StudentModel, StudentRepo
from models.teacher import TeacherModel, TeacherRepo
from models.term import TermModel, TermRepo
from models.term_schedule import TermScheduleModel, TermScheduleRepo
from models.organization import OrganizationModel, OrganizationRepo
from models.sentence import generate_random_sentence

Enrollment = namedtuple('Enrollment', ['org_id', 'term_id', 'student_id', 'courses'])
Course = namedtuple('Course', ['period', 'course_id', 'teacher_id'])
TermSchedule = namedtuple('TermSchedule', ['org_id', 'term_id', 'courses'])


class SeedDatabase:
    """
    This class contains methods to set up the database, seed domain data, 
    and create term schedules.
    """

    def __init__(self):
        """
        Initializes the SeedDatabase class and sets up the database tables.
        """
        self.setup()

    def setup(self):
        """
        Sets up the database tables if they don't exist, 
        and deletes existing data from these tables.
        """
        if not OrganizationTable.exists():
            OrganizationTable.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
            OrganizationDataTable.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

        for item in OrganizationDataTable.scan():
            item.delete()

        for item in OrganizationTable.scan():
            item.delete()

    def seed_domain_data(self):
        """
        Seeds the domain data such as organizations, teachers, students, 
        courses, and terms into the database.
        """
        org_data = {"id": "UCSD", "name": "University of California San Diego"}

        teacher_data = [
            "100,Williams,Liam,1985-09-15,Masters of Science in Computer Science",
            "101,Johnson,Olivia,1994-07-21,PhD in Linguistics",
            "102,Smith,Noah,1988-03-10,Masters of Business Administration",
            "103,Brown,Emma,1979-12-05,Masters of Science in Electrical Engineering",
            "104,Jones,Lucas,1998-11-18,PhD in Psychology",
            "105,Garcia,Ava,1982-06-25,Masters of Arts in History",
            "106,Miller,Mia,1996-02-09,Masters of Science in Biology",
            "107,Davis,Ethan,1989-10-31,PhD in Economics",
            "108,Rodriguez,Isabella,1977-08-14,Masters of Fine Arts in Creative Writing"
        ]

        student_data = [
            "100,Williams,Liam,1985-09-15",
            "101,Johnson,Olivia,1994-07-21",
            "102,Smith,Noah,1988-03-10",
            "103,Brown,Emma,1979-12-05",
            "104,Jones,Lucas,1998-11-18",
            "105,Garcia,Ava,1982-06-25",
            "106,Miller,Mia,1996-02-09",
            "107,Davis,Ethan,1989-10-31",
            "108,Rodriguez,Isabella,1977-08-14"
        ]

        course_data = [
            "100,Creative Writing,101",
            "101,Biology,201",
            "102,Chemistry,103",
            "103,Physics,301",
            "104,Mathematics,401",
            "105,Computer Science,101",
            "106,History,201",
            "107,Geography,103",
            "108,English Literature,301"
        ]

        term_data = [("202303", "Fall 2023"), ("202304", "Winter 2023"), ("202401", "Spring 2024"), ("202402", "Summer 2024")]

        org = OrganizationModel(id=org_data["id"], name=org_data["name"])
        org = OrganizationRepo.save(org)

        for item in teacher_data:
            id, first, last, dob, degree = item.split(",")
            TeacherRepo.save(TeacherModel(id=id, first_name=first, last_name=last, dob=dob, degree=degree, org_id=org.id))

        for item in student_data:
            id, first, last, dob = item.split(",")
            StudentRepo.save(StudentModel(id=id, first_name=first, last_name=last, dob=dob, org_id=org.id))

        for item in course_data:
            id, course_name, section = item.split(",")
            CourseRepo.save(CourseModel(id=id, course_name=course_name, section=section, description=generate_random_sentence(), org_id=org.id))

        for item in term_data:
            term_id, term_name = item
            TermRepo.save(TermModel(term_id=term_id, term_name=term_name, org_id=org.id))

    def create_term_schedule(self, schedule: TermSchedule):
        """
        Creates a term schedule using the provided schedule information.

        Args:
        - schedule (TermSchedule): A namedtuple containing the organization, term, and courses info.
        """
        for course_t in schedule.courses:
            course_m = CourseRepo.get(org_id=schedule.org_id, id=course_t.course_id)
            teacher_m = TeacherRepo.get(org_id=schedule.org_id, id=course_t.teacher_id)
            term_schedule_model = TermScheduleModel(
                org_id=schedule.org_id,
                term_id=schedule.term_id,
                course_id=course_t.course_id,
                teacher_id=course_t.teacher_id,
                period=course_t.period,
                course_name=course_m.course_name,
                teacher_name=f"{teacher_m.first_name} {teacher_m.last_name}")
            TermScheduleRepo.save(term_schedule_model)

    def run(self):
        """
        Executes the database seeding process.
        It seeds domain data and then creates a term schedule.
        """
        print("OrganizationDataTable.Meta.host:", OrganizationDataTable.Meta.host)

        self.seed_domain_data()

        term_schedule_data = {
            "org_id": "UCSD",
            "term_id": "202303",
            "courses": [
                {"period": "1", "course_id": "100", "teacher_id": "100"},
                {"period": "1", "course_id": "101", "teacher_id": "101"},
                {"period": "1", "course_id": "102", "teacher_id": "102"},
                {"period": "1", "course_id": "103", "teacher_id": "103"},
                {"period": "1", "course_id": "104", "teacher_id": "104"},
                {"period": "2", "course_id": "100", "teacher_id": "100"},
                {"period": "2", "course_id": "101", "teacher_id": "101"},
                {"period": "2", "course_id": "102", "teacher_id": "102"},
                {"period": "2", "course_id": "103", "teacher_id": "103"},
                {"period": "2", "course_id": "104", "teacher_id": "104"},
                {"period": "3", "course_id": "100", "teacher_id": "100"},
                {"period": "3", "course_id": "101", "teacher_id": "101"},
                {"period": "3", "course_id": "102", "teacher_id": "102"},
                {"period": "3", "course_id": "103", "teacher_id": "103"},
                {"period": "3", "course_id": "104", "teacher_id": "104"},
                {"period": "4", "course_id": "100", "teacher_id": "100"},
                {"period": "4", "course_id": "101", "teacher_id": "101"},
                {"period": "4", "course_id": "102", "teacher_id": "102"},
                {"period": "4", "course_id": "103", "teacher_id": "103"},
                {"period": "4", "course_id": "104", "teacher_id": "104"},
                {"period": "5", "course_id": "105", "teacher_id": "105"},
                {"period": "5", "course_id": "106", "teacher_id": "106"},
                {"period": "5", "course_id": "107", "teacher_id": "107"},
                {"period": "5", "course_id": "108", "teacher_id": "108"},
                {"period": "6", "course_id": "105", "teacher_id": "105"},
                {"period": "6", "course_id": "106", "teacher_id": "106"},
                {"period": "6", "course_id": "107", "teacher_id": "107"},
                {"period": "6", "course_id": "108", "teacher_id": "108"},
                {"period": "7", "course_id": "105", "teacher_id": "105"},
                {"period": "7", "course_id": "106", "teacher_id": "106"},
                {"period": "7", "course_id": "107", "teacher_id": "107"},
                {"period": "7", "course_id": "108", "teacher_id": "108"}
            ]
        }

        courses = [Course(**course_data) for course_data in term_schedule_data['courses']]
        term_schedule_namedtuple = TermSchedule(org_id=term_schedule_data['org_id'], term_id=term_schedule_data['term_id'], courses=courses)
        self.create_term_schedule(term_schedule_namedtuple)

        schedule = TermScheduleRepo.get(org_id="UCSD", term_id="202303")
        for row in schedule:
            print(row)
