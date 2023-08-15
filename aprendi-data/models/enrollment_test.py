"""
Integration tests for EnrollmentRepo
"""

import pytest
from models.enrollment import EnrollmentModel, EnrollmentRepo


@pytest.fixture
def sample_enrollment():
    """
    Sample enrollment data
    """
    return EnrollmentModel(
        org_id="ORG1",
        student_id="STUDENT1",
        enrollment_id="ENROLLMENT1",
        term_id="TERM1",
        course_name="Math",
        teacher_name="John Doe",
        period="1"
    )


def setup_function():
    """
    Setup function for each test case to ensure a clean slate.
    """
    # Remove existing data if exists for the test cases. Handle this appropriately.
    # Note: This is just a placeholder. Ideally, you should remove data based on your primary and sort key.
    pass


def teardown_function():
    """
    Cleanup function after each test.
    """
    # Clean up any data created during the test to ensure no side-effects.
    # Note: This is just a placeholder. Ideally, you should remove data based on your primary and sort key.
    pass


def test_save_enrollment(sample_enrollment):
    """
    Test saving an enrollment
    """
    saved_enrollment = EnrollmentRepo.save(sample_enrollment)
    assert saved_enrollment == sample_enrollment


def test_get_enrollment(sample_enrollment):
    """
    Test getting an enrollment
    """
    EnrollmentRepo.save(sample_enrollment)
    fetched_enrollment = EnrollmentRepo.get(
        org_id=sample_enrollment.org_id,
        student_id=sample_enrollment.student_id,
        term_id=sample_enrollment.term_id,
        enrollment_id=sample_enrollment.enrollment_id
    )
    assert fetched_enrollment == sample_enrollment


def test_get_all_enrollments(sample_enrollment):
    """
    Test getting all enrollments for a student in a term
    """
    EnrollmentRepo.save(sample_enrollment)
    fetched_enrollments = EnrollmentRepo.get_all(
        org_id=sample_enrollment.org_id,
        student_id=sample_enrollment.student_id,
        term_id=sample_enrollment.term_id
    )
    assert len(fetched_enrollments) == 1
    assert fetched_enrollments[0] == sample_enrollment


def test_get_non_existent_enrollment(sample_enrollment):
    """
    Test getting an enrollment that does not exist
    """
    fetched_enrollment = EnrollmentRepo.get(
        org_id=sample_enrollment.org_id,
        student_id="NON_EXISTENT",
        term_id=sample_enrollment.term_id,
        enrollment_id=sample_enrollment.enrollment_id
    )
    assert fetched_enrollment is None
