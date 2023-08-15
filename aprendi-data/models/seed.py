"""
This script runs the application using a development server.
"""
import csv
from models.teacher import TeacherRepo, TeacherModel
from models.student import StudentRepo, StudentModel
from models.tables import OrganizationTable, OrganizationDataTable
from models.organization import OrganizationRepo, OrganizationModel
from models.course import CourseRepo, CourseModel
from models.term import TermRepo, TermModel
from models.sentence import generate_random_sentence


def get_reader(csv_filename):
    """
    This function gets the csv reader
    """
    with open('data/' + csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


def empty_data_table():
    """
    This function empties the table
    """
    for item in OrganizationDataTable.scan():
        item.delete()

# Organization


def get_all_organizations():
    """
    This function gets all the organizations
    """
    for item in OrganizationTable.scan():
        print(item)


def seed_organization(org: OrganizationModel):
    """
    This seeds the organization data
    """
    org = OrganizationRepo.save(org)
    org = OrganizationRepo.get(id="FLA")
    print(org)


# Teachers

def seed_teachers(org_id: str):
    """
    This seeds the teacher data
    """
    reader = get_reader("teachers.csv")
    for row in reader:
        id, last, first, dob, degree = row
        item = TeacherModel(
            org_id=org_id,
            first_name=first,
            last_name=last,
            degree=degree,
            dob=dob
        )
        item = TeacherRepo.save(item)
        item = TeacherRepo.get(org_id=item.org_id, id=item.id)
        print(item)


def get_all_teachers(org_id: str):
    """
    This gets all the teachers
    """
    for item in TeacherRepo.get_all(org_id=org_id):
        print(item)


# Students

def seed_students(org_id: str):
    """
    This seeds the teacher data
    """
    reader = get_reader("students.csv")
    for row in reader:
        id, last, first, dob = row
        item = StudentModel(
            org_id=org_id,
            first_name=first,
            last_name=last,
            dob=dob
        )
        item = StudentRepo.save(item)
        item = StudentRepo.get(org_id=item.org_id, id=item.id)
        print(item)


def get_all_students(org_id: str):
    """
    This gets all the teachers
    """
    for item in StudentRepo.get_all(org_id=org_id):
        print(item)

# Courses


def seed_courses(org_id: str):
    """
    This seeds the teacher data
    """
    reader = get_reader("courses.csv")
    for row in reader:
        id, name, section = row
        item = CourseModel(
            org_id=org_id,
            name=name,
            section=section,
            description=generate_random_sentence()
        )
        item = CourseRepo.save(item)
        item = CourseRepo.get(org_id=item.org_id, id=item.id)
        print(item)


def get_all_courses(org_id: str):
    """
    This gets all the teachers
    """
    for item in CourseRepo.get_all(org_id=org_id):
        print(item)


def seed_terms(org_id: str):
    """
    This function seeds the course schedule
    """
    terms = [("202303", "Fall 2023"), ("202304", "Winter 2023"), ("202401", "Spring 2024"), ("202402", "Summer 2024")]
    for term in terms:
        item = TermModel(
            org_id=org_id,
            term_id=term[0],
            term_name=term[1]
        )
        item = TermRepo.save(item)
        item = TermRepo.get(org_id=item.org_id, id=item.term_id)
        print(item)


def get_all_terms(org_id: str):
    """
    This gets all the teachers
    """
    for item in TermRepo.get_all(org_id=org_id):
        print(item)

# All data


def seed_all_data():
    """
    This seeds all the data
    """
    # empty_data_table()

    # # organization
    # _org = OrganizationModel(id="FLA", name="Florentia Academy")
    # seed_organization(org=_org)
    # get_all_organizations()

    # # teachers
    # seed_teachers(org_id=_org.id)
    # get_all_teachers(org_id=_org.id)

    # # students
    # seed_students(org_id=_org.id)
    # get_all_students(org_id=_org.id)

    # # courses
    # seed_courses(org_id=_org.id)
    # get_all_courses(org_id=_org.id)
    seed_terms(org_id="FLA")
    get_all_terms(org_id="FLA")
