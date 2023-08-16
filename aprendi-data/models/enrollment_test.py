"""
Integration tests for EnrollmentRepo class.
"""
import logging
import pytest
from models.enrollment import EnrollmentModel, EnrollmentRepo

# Note: Always be cautious when running integration tests on live systems.
# The following tests assume that there is a live connection to a DynamoDB instance and that
# the table already exists. Please be sure to back up any important data.

# Sample data for tests
sample_enrollment1 = EnrollmentModel(
    enrollment_id="ENROLL1",
    org_id="ORG1",
    student_id="STUD1",
    course_id="COURSE1",
    term_id="TERM1",
    course_name="Math",
    teacher_name="Mr. Smith",
    period="1"
)

sample_enrollment2 = EnrollmentModel(
    enrollment_id="ENROLL2",
    org_id="ORG1",
    student_id="STUD1",
    course_id="COURSE2",
    term_id="TERM1",
    course_name="Science",
    teacher_name="Mrs. Brown",
    period="2"
)


def test_save_enrollment():
    """
    Test saving an enrollment to the database.
    """
    result = EnrollmentRepo.save(sample_enrollment1)
    assert result == sample_enrollment1


def test_get_enrollment():
    """
    Test retrieving a specific enrollment from the database using org_id, student_id, term_id, and course_id.
    """
    EnrollmentRepo.save(sample_enrollment1)
    result = EnrollmentRepo.get("ORG1", "STUD1", "TERM1", "COURSE1")
    assert result == sample_enrollment1


def test_get_by_enrollment_id():
    """
    Test retrieving a specific enrollment from the database using enrollment_id.
    """
    EnrollmentRepo.save(sample_enrollment1)
    result = EnrollmentRepo.get_by_enrollment_id("ORG1", "STUD1", "ENROLL1")
    assert result == sample_enrollment1


def test_get_all_enrollments():
    """
    Test retrieving all enrollments for a student in a term.
    """
    EnrollmentRepo.save(sample_enrollment1)
    EnrollmentRepo.save(sample_enrollment2)
    results = EnrollmentRepo.get_all("ORG1", "STUD1", "TERM1")
    assert len(results) == 2
    assert sample_enrollment1 in results
    assert sample_enrollment2 in results


# This is an example cleanup function to delete test data after tests are done.
# Commenting it out as it's recommended to be cautious with delete operations in a live environment.
# def teardown_module():
#     """
#     Clean up after tests.
#     """
#     table = OrganizationDataTable()
#     item1 = table.get("ORG#ORG1#STUDENT#STUD1#ENROLLMENT", "TERM#TERM1#COURSE#COURSE1#ENROLLMENT#ENROLL1")
#     item2 = table.get("ORG#ORG1#STUDENT#STUD1#ENROLLMENT", "TERM#TERM1#COURSE#COURSE2#ENROLLMENT#ENROLL2")
#     item1.delete()
#     item2.delete()
