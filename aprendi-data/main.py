"""
This script runs the application using a development server.
"""
import os
from dotenv import load_dotenv
from models.seed_database import SeedDatabase


if __name__ == '__main__':
    load_dotenv(verbose=True)
    print("DYNAMODB_HOST:", os.environ.get('DYNAMODB_HOST'))
    seeder = SeedDatabase()
    seeder.run()
