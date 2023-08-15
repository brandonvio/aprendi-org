# test_utils.py
import logging
import pytest
from models.tables import OrganizationDataTable

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.info('This is an info message')


@pytest.fixture(scope='session', autouse=True)
def dynamodb_local():
    """Fixture for setting up a local DynamoDB instance."""
    # Assuming you've set up pytest-dynamodb correctly, it should handle this.
    pass


@pytest.fixture(scope='session', autouse=True)
def setup_table():
    """Set up the table before tests and tear it down after."""
    log.warning("############## setting up table ####################")
    if not OrganizationDataTable.exists():
        OrganizationDataTable.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

    yield  # This is where the testing happens.

    OrganizationDataTable.delete_table()
