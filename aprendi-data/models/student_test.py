# test_student.py
from models.student import StudentModel, StudentRepo


def test_student_crud_operations():
    """
    This test will test the following:
    1. Save a student
    2. Retrieve a student
    3. Get all students for an organization
    """
    # 1. Save a student
    student = StudentModel(id="200", org_id="test_org_1", first_name="Jane",
                           last_name="Doe", dob="2002-02-02")
    saved_student = StudentRepo.save(student)

    assert saved_student.id is not None

    # 2. Retrieve a student
    fetched_student = StudentRepo.get(org_id="test_org_1", id=saved_student.id)
    assert fetched_student.first_name == "Jane"
    assert fetched_student.last_name == "Doe"
    assert fetched_student.dob == "2002-02-02"

    # 3. Get all students for an organization
    students = StudentRepo.get_all(org_id="test_org_1")
    assert len(students) == 1
    assert students[0].first_name == "Jane"
    assert students[0].last_name == "Doe"
    assert students[0].dob == "2002-02-02"
