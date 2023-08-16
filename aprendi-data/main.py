"""
This script seeds the database with the data from the data folder.
"""
import os
from dotenv import load_dotenv
from models.seed_database import SeedDatabase


if __name__ == '__main__':
    load_dotenv(verbose=True)
    print("DYNAMODB_ENDPOINT:", os.environ.get('DYNAMODB_ENDPOINT'))
    seeder = SeedDatabase()
    seeder.run()
