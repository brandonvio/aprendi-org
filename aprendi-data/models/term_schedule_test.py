# test_term_schedule.py
from models.term_schedule import TermScheduleModel, TermScheduleRepo


def test_term_schedule_crud_operations():
    """
    This test will test the following:
    1. Save a term schedule
    2. Retrieve a term schedule by course_id
    3. Retrieve a term schedule by course_id and period
    4. Check if a teacher has been scheduled for a period
    """
    # 1. Save a term schedule
    term_schedule = TermScheduleModel(org_id="test_org_1",
                                      term_id="term_001",
                                      course_id="course_001",
                                      period="1",
                                      teacher_id="teacher_001",
                                      course_name="Math 101",
                                      teacher_name="John Doe")

    saved_term_schedule = TermScheduleRepo.save(term_schedule)

    assert saved_term_schedule.org_id == "test_org_1"
    assert saved_term_schedule.term_id == "term_001"
    assert saved_term_schedule.course_id == "course_001"
    assert saved_term_schedule.teacher_id == "teacher_001"

    # 2. Retrieve a term schedule by course_id
    fetched_term_schedule_by_course = TermScheduleRepo.get_by_course_id(org_id="test_org_1", term_id="term_001", course_id="course_001")
    assert len(fetched_term_schedule_by_course) == 1
    assert fetched_term_schedule_by_course[0].teacher_name == "John Doe"

    # 3. Retrieve a term schedule by course_id and period
    fetched_term_schedule_by_course_period = TermScheduleRepo.get_by_course_id_and_period(org_id="test_org_1", term_id="term_001", period="1", course_id="course_001")
    assert len(fetched_term_schedule_by_course_period) == 1
    assert fetched_term_schedule_by_course_period[0].teacher_name == "John Doe"

    # 4. Check if a teacher has been scheduled for a period
    teacher_schedule_by_period = TermScheduleRepo.get_by_teacher_id_and_period(org_id="test_org_1", term_id="term_001", period="1", teacher_id="teacher_001")
    print(teacher_schedule_by_period[0])
    assert len(teacher_schedule_by_period) == 1
    assert teacher_schedule_by_period[0].course_name == "Math 101"
