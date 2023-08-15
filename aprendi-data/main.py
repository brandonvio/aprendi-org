"""
This script runs the application using a development server.
"""
import csv
from dotenv import load_dotenv
from models.teacher import TeacherRepo, TeacherModel
from models.tables import OrganizationTable, OrganizationDataTable
from models.organization import OrganizationRepo, OrganizationModel


load_dotenv(verbose=True)

if not OrganizationTable.exists():
    OrganizationTable.create_table(wait=True, read_capacity_units=5, write_capacity_units=5)

if not OrganizationDataTable.exists():
    OrganizationDataTable.create_table(wait=True, read_capacity_units=100, write_capacity_units=100)


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


if __name__ == '__main__':
    empty_data_table()
    _org = OrganizationModel(id="FLA", name="Florentia Academy")
    seed_organization(org=_org)
    get_all_organizations()
    seed_teachers(org_id=_org.id)
    get_all_teachers(org_id=_org.id)
