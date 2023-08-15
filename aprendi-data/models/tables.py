"""
This module contains the AprendiTable class, which is a model for the Aprendi
"""
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


# class EntityTypeIndex(GlobalSecondaryIndex):
#     """
#     This class represents a global secondary index (GSI)
#     """
#     class Meta:
#         """
#         This class is a meta class for the GSI
#         """
#         # Name of the GSI
#         index_name = 'entity-type-index'
#         read_capacity_units = 100
#         write_capacity_units = 100
#         # We'll project all attributes for simplicity, but you can modify as per your needs
#         projection = AllProjection()

#     # Attributes for the GSI
#     entity_type = UnicodeAttribute(hash_key=True)
#     entity_id = UnicodeAttribute(range_key=True)

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

    pk = UnicodeAttribute(hash_key=True)
    sk = UnicodeAttribute(range_key=True)

    # entity_type = UnicodeAttribute(null=False)
    name = UnicodeAttribute(null=True)
    first_name = UnicodeAttribute(null=True)
    last_name = UnicodeAttribute(null=True)
    data = UnicodeAttribute(null=True)
