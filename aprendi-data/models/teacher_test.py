# test_teacher.py
from models.teacher import TeacherModel, TeacherRepo


def test_teacher_crud_operations():
    """
    This test will test the following:
    1. Save a teacher
    2. Retrieve a teacher
    3. Get all teachers for an organization
    """
    # 1. Save a teacher
    teacher = TeacherModel(org_id="test_org_1", first_name="John", last_name="Doe", degree="Masters", dob="1990-01-01")
    saved_teacher = TeacherRepo.save(teacher)

    assert saved_teacher.id is not None

    # 2. Retrieve a teacher
    fetched_teacher = TeacherRepo.get(org_id="test_org_1", id=saved_teacher.id)
    assert fetched_teacher.first_name == "John"
    assert fetched_teacher.last_name == "Doe"
    assert fetched_teacher.degree == "Masters"
    assert fetched_teacher.dob == "1990-01-01"

    # 3. Get all teachers for an organization
    teachers = TeacherRepo.get_all(org_id="test_org_1")
    assert len(teachers) == 1
    assert teachers[0].first_name == "John"
    assert teachers[0].last_name == "Doe"
    assert teachers[0].degree == "Masters"
    assert teachers[0].dob == "1990-01-01"
