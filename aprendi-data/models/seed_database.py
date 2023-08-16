"""
Database Seeder

This module contains the logic to seed the database with a term schedule.
It sets up the necessary tables, populates them with domain data, and finally
creates term schedules using the populated data.
"""
import csv
import random
from typing import List
from collections import namedtuple
from models.tables import OrganizationDataTable, OrganizationTable
from models.course import CourseModel, CourseRepo
from models.student import StudentModel, StudentRepo
from models.teacher import TeacherModel, TeacherRepo
from models.term import TermModel, TermRepo
from models.term_schedule import TermScheduleModel, TermScheduleRepo
from models.organization import OrganizationModel, OrganizationRepo
from models.sentence import generate_random_sentence

Org = namedtuple('Org', ['id', 'name', 'teacher_num', 'student_num', 'course_num'])
Enrollment = namedtuple('Enrollment', ['org_id', 'term_id', 'student_id', 'courses'])
TermSchedule = namedtuple('TermSchedule', ['org_id', 'term_id', 'courses'])
Course = namedtuple('Course', ['id', 'course_name', 'section'])
Teacher = namedtuple('Teacher', ['id', 'last_name', 'first_name', 'dob', 'degree'])
Student = namedtuple('Student', ['id', 'last_name', 'first_name', 'dob'])
Term = namedtuple('Term', ['id', 'name'])


class SeedDatabase:
    """
    This class contains methods to set up the database, seed domain data, 
    and create term schedules.
    """

    def __init__(self):
        """
        Initializes the SeedDatabase class and sets up the database tables.
        """
        self.org_data: List[Org] = []
        self.teacher_data: List[Teacher] = []
        self.student_data: List[Student] = []
        self.course_data: List[Course] = []
        self.term_data: List[Term] = []
        self.setup()

    def setup(self):
        """
        Sets up the database tables if they don't exist, 
        and deletes existing data from these tables.
        """
        # if not OrganizationTable.exists():
        #     OrganizationTable.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
        #     OrganizationDataTable.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

        # if OrganizationTable.exists():
        #     OrganizationTable.delete_table()
        #     OrganizationDataTable.delete_table()

        # OrganizationTable.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
        # OrganizationDataTable.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

        for item in OrganizationDataTable.scan():
            item.delete()

        for item in OrganizationTable.scan():
            item.delete()

        reader = self.get_reader("teachers.csv")
        for row in reader:
            self.teacher_data.append(Teacher(*row))

        reader = self.get_reader("students.csv")
        for row in reader:
            self.student_data.append(Student(*row))

        reader = self.get_reader("courses.csv")
        for row in reader:
            self.course_data.append(Course(*row))

        reader = self.get_reader("orgs.csv")
        for row in reader:
            self.org_data.append(Org(*row))

        terms = [("202303", "Fall 2023"), ("202304", "Winter 2023"), ("202401", "Spring 2024"), ("202402", "Summer 2024")]
        for item in terms:
            self.term_data.append(Term(*item))

    def run(self):
        """
        Executes the database seeding process.
        It seeds domain data and then creates a term schedule.
        """
        print("OrganizationDataTable.Meta.host:", OrganizationDataTable.Meta.host)
        self.seed_orgs()
        for org in self.org_data:
            self.seed_teachers(org.id, int(org.teacher_num))
            self.seed_students(org.id, int(org.student_num))
            self.seed_courses(org.id, int(org.course_num))
            self.seed_terms(org.id)
            self.seed_term_schedule(org.id)
            # print("teachers:", TeacherRepo.get_all(org_id=org.id))
            # print("students:", StudentRepo.get_all(org_id=org.id))

    def seed_orgs(self):
        """
        Seeds the organization data into the database.
        """
        for item in self.org_data:
            item = OrganizationModel(
                id=item.id,
                name=item.name
            )
            item = OrganizationRepo.save(item)

    def seed_teachers(self, org_id: str, num: int):
        """
        Seeds the teacher data into the database.
        """
        selected_indices = random.sample(range(len(self.teacher_data)), num)
        # print("teachers#", selected_indices)
        for i in selected_indices:
            item = self.teacher_data[i]
            item = TeacherModel(
                org_id=org_id,
                id=item.id,
                first_name=item.first_name,
                last_name=item.last_name,
                degree=item.degree,
                dob=item.dob
            )
            item = TeacherRepo.save(item)

    def seed_students(self, org_id: str, num: int):
        """
        Seeds the teacher data into the database.
        """
        selected_indices = random.sample(range(len(self.student_data)), num)
        # print("students#", selected_indices)
        for i in selected_indices:
            item = self.student_data[i]
            item = StudentModel(
                org_id=org_id,
                id=item.id,
                first_name=item.first_name,
                last_name=item.last_name,
                dob=item.dob
            )
            item = StudentRepo.save(item)

    def seed_courses(self, org_id: str, num: int):
        """
        Seeds the teacher data into the database.
        """
        selected_indices = random.sample(range(len(self.course_data)), num)
        for i in selected_indices:
            item = self.course_data[i]
            item = CourseModel(
                org_id=org_id,
                id=item.id,
                course_name=item.course_name,
                section=item.section,
                description=generate_random_sentence()
            )
            item = CourseRepo.save(item)

    def seed_terms(self, org_id: str):
        """
        Seeds the domain data such as organizations, teachers, students, 
        courses, and terms into the database.
        """
        for item in self.term_data:
            TermRepo.save(TermModel(term_id=item.id, term_name=item.name, org_id=org_id))

    def is_teacher_available(self, org_id, teacher_id: str, term_id: str, period: str):
        """
        Checks if the teacher is available for the given term and period.
        """
        result = TermScheduleRepo.get_by_teacher_id_and_period(
            org_id=org_id,
            teacher_id=teacher_id,
            term_id=term_id,
            period=period)
        return len(result) == 0

    def get_teacher(self, teachers: List[TeacherModel], org_id: str, term_id: str, period: str):
        """
        Gets a teacher for the given term and period.
        """
        teacher = None
        while True:
            teacher = random.choice(teachers)
            if self.is_teacher_available(org_id, teacher.id, term_id, period):
                break
        return teacher

    def seed_term_schedule(self, org_id: str):
        """
        This method creates a term schedule for the given organization and term.
        """
        periods = ["1", "2", "3", "4", "5", "6", "7", "8"]
        terms = TermRepo.get_all(org_id=org_id)
        courses = CourseRepo.get_all(org_id=org_id)
        teachers = TeacherRepo.get_all(org_id=org_id)
        students = StudentRepo.get_all(org_id=org_id)
        print(str.format("orgid:{3}terms#:{0}, courses#:{1}, teachers#:{2}, students#:{4}", len(terms), len(courses), len(teachers), org_id, len(students)))
        for term in terms:
            print("term:", term)
            for _ in range(len(courses)):
                for period in periods:
                    _course = courses[random.randint(0, len(courses) - 1)]
                    teacher = self.get_teacher(teachers, org_id=org_id, term_id=term.term_id, period=period)
                    item = TermScheduleModel(
                        org_id=org_id,
                        term_id=term.term_id,
                        period=period,
                        course_id=_course.id,
                        teacher_id=teacher.id,
                        course_name=_course.course_name,
                        teacher_name=teacher.first_name + " " + teacher.last_name
                    )
                    item = TermScheduleRepo.save(item)

        for term in terms:
            schedule = TermScheduleRepo.get(org_id=org_id, term_id=term.term_id)
            print("Getting schedule for term:", org_id, term, len(schedule))
            for row in schedule:
                print(row)

    def get_reader(self, csv_filename):
        """
        This function gets the csv reader
        """
        with open('data/' + csv_filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            return list(reader)
