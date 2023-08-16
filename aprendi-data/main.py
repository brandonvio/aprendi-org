"""
This script runs the application using a development server.
"""
from dotenv import load_dotenv
from models.seed_database import SeedDatabase

if __name__ == '__main__':
    load_dotenv(verbose=True)
    seeder = SeedDatabase()
    seeder.run()
