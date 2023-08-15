"""
This module contains the AprendiTable class, which is a model for the Aprendi
"""
# from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class OrganizationTable(Model):
    """
    This class is a model for the Organization table
    """
    class Meta:
        """
        This class is a meta class for the Organization table
        """
        table_name = "aprendi_organization_table"
        region = 'us-west-2'
        host = "http://localhost:8000"

    pk = UnicodeAttribute(hash_key=True)
    sk = UnicodeAttribute(range_key=True)
    name = UnicodeAttribute(null=False)
    data = UnicodeAttribute(null=True)


class OrganizationDataTable(Model):
    """
    This class is a model for the Aprendi table
    """
    class Meta:
        """
        This class is a meta class for the Aprendi table
        """
        table_name = "aprendi_organization_data_table"
        region = 'us-west-2'
        host = "http://localhost:8000"

    # table keys
    pk = UnicodeAttribute(hash_key=True)
    sk = UnicodeAttribute(range_key=True)

    # student, teacher
    first_name = UnicodeAttribute(null=True)
    last_name = UnicodeAttribute(null=True)

    # course
    course_name = UnicodeAttribute(null=True)
    course_description = UnicodeAttribute(null=True)
    course_section = UnicodeAttribute(null=True)

    # other data
    data = UnicodeAttribute(null=True)
