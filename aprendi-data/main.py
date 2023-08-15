"""
This script runs the application using a development server.
"""
from dotenv import load_dotenv
from models.tables import OrganizationTable, OrganizationDataTable
from models.seed import seed_all_data

if __name__ == '__main__':
    load_dotenv(verbose=True)

    if not OrganizationTable.exists():
        OrganizationTable.create_table(wait=True, read_capacity_units=5, write_capacity_units=5)

    if not OrganizationDataTable.exists():
        OrganizationDataTable.create_table(wait=True, read_capacity_units=100, write_capacity_units=100)

    seed_all_data()
