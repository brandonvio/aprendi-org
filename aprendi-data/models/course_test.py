# test_course.py
from models.course import CourseModel, CourseRepo


def test_course_crud_operations():
    """
    This test will test the following:
    1. Save a course
    2. Retrieve a course
    3. Get all courses for an organization
    """
    # 1. Save a course
    course = CourseModel(id="100", org_id="test_org_1", name="Mathematics", description="Introduction to Algebra", section="101A")
    saved_course = CourseRepo.save(course)

    assert saved_course.id is not None

    # 2. Retrieve a course
    fetched_course = CourseRepo.get(org_id="test_org_1", id=saved_course.id)
    assert fetched_course.name == "Mathematics"
    assert fetched_course.description == "Introduction to Algebra"
    assert fetched_course.section == "101A"

    # 3. Get all courses for an organization
    courses = CourseRepo.get_all(org_id="test_org_1")
    assert len(courses) == 1
    assert courses[0].name == "Mathematics"
    assert courses[0].description == "Introduction to Algebra"
    assert courses[0].section == "101A"
