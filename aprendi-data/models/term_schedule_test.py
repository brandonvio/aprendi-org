"""
This module contains unit tests for the TermSchedule model and its associated operations.

The tests are designed to cover the following scenarios:
1. Handling multiple courses in a schedule.
2. Scenarios where a teacher is teaching more than one class.
3. Scenarios where the database has to retrieve more than one class for a specific query.
"""
import json
from collections import namedtuple
from uuid_extensions import uuid7str
import pytest
from models.term_schedule import TermScheduleRepo, TermScheduleModel


# Constants for testing
ORG_ID = "test_org"
TERM_ID = "test_term"

# Extended courses and details
COURSE_DETAILS = [
    {"course_id": "course_101", "period": "period_1", "teacher_id": "teacher_1",
     "course_name": "Mathematics", "teacher_name": "Mr. Smith"},
    {"course_id": "course_102", "period": "period_2", "teacher_id": "teacher_1",
     "course_name": "Science", "teacher_name": "Mr. Smith"},
    {"course_id": "course_103", "period": "period_3", "teacher_id": "teacher_3",
     "course_name": "History", "teacher_name": "Mr. White"}
]

MockedItem = namedtuple('MockedItem', ['pk', 'sk', 'lsi_sk2', 'data'])


@pytest.fixture
def clean_database():
    """
    Set up the database to its initial state before each test. 
    """
    # Mocked cleanup of the database.
    # In a real-world scenario, you'd interact with your database to clean it.
    pass


@pytest.fixture
def models_for_testing():
    """
    Create and return a list of TermScheduleModel for testing.
    """
    return [TermScheduleModel(org_id=ORG_ID, term_id=TERM_ID, **course_detail) for course_detail in COURSE_DETAILS]


@pytest.mark.usefixtures("clean_database")
def test_zero_courses():
    """
    Test scenario where no courses are present in the system.
    """
    for detail in COURSE_DETAILS:
        retrieved = TermScheduleRepo.get_by_course_id(ORG_ID, TERM_ID, detail['course_id'])
        assert len(retrieved) == 0


@pytest.mark.usefixtures("clean_database")
def test_one_course(models_for_testing):
    """
    Test scenario with a single course.
    """
    TermScheduleRepo.save(models_for_testing[0])

    # Check retrieval for first course
    detail = COURSE_DETAILS[0]
    retrieved = TermScheduleRepo.get_by_course_id(ORG_ID, TERM_ID, detail['course_id'])
    assert len(retrieved) == 1
    # assert retrieved[0] == models_for_testing[0]


@pytest.mark.usefixtures("clean_database")
def test_two_courses(models_for_testing):
    """
    Test scenario with two courses, with one teacher teaching both.
    """
    for model in models_for_testing[:2]:
        TermScheduleRepo.save(model)

    for i in range(2):
        detail = COURSE_DETAILS[i]
        retrieved = TermScheduleRepo.get_by_course_id(ORG_ID, TERM_ID, detail['course_id'])
        assert len(retrieved) == 1
        # assert retrieved[0] == models_for_testing[i]


@pytest.mark.usefixtures("clean_database")
def test_three_courses(models_for_testing):
    """
    Test scenario with three courses.
    """
    for model in models_for_testing:
        TermScheduleRepo.save(model)

    for i, detail in enumerate(COURSE_DETAILS):
        retrieved = TermScheduleRepo.get_by_course_id(ORG_ID, TERM_ID, detail['course_id'])
        assert len(retrieved) == 1
        # assert retrieved[0] == models_for_testing[i]


@pytest.mark.usefixtures("clean_database")
def test_courses_by_teacher(models_for_testing):
    """
    Test retrieval of courses by teacher_id.
    """
    # Save all models
    for model in models_for_testing:
        TermScheduleRepo.save(model)

    # Retrieve courses taught by Mr. Smith (teacher_1)
    retrieved = TermScheduleRepo.get_by_teacher_id(ORG_ID, TERM_ID, "teacher_1")
    assert len(retrieved) == 2


@pytest.mark.usefixtures("clean_database")
def test_parse_term():
    """
    Test the parse_term functionality for each course detail.
    """
    for detail in COURSE_DETAILS:
        item_mock = MockedItem(
            pk=f"ORG#{ORG_ID}#TERM#{TERM_ID}#SCHEDULE",
            sk=f"COURSE#{detail['course_id']}#PERIOD#{detail['period']}#TEACHER#{detail['teacher_id']}",
            lsi_sk2=uuid7str(),
            data={"course_name": detail["course_name"],
                  "teacher_name": detail["teacher_name"]}
        )

        parsed_model = TermScheduleRepo.parse_term(item_mock)
        assert parsed_model.org_id == ORG_ID
        assert parsed_model.term_id == TERM_ID
        assert parsed_model.course_id == detail["course_id"]
        assert parsed_model.period == detail["period"]
        assert parsed_model.teacher_id == detail["teacher_id"]
        assert parsed_model.course_name == detail["course_name"]
        assert parsed_model.teacher_name == detail["teacher_name"]
