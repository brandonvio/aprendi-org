import random


def generate_course_schedule(org_id, num_teachers, num_courses):
    teachers = fetch_entities(Teacher, org_id, num_teachers, "TEACHER")
    courses = fetch_entities(Course, org_id, num_courses, "COURSE")

    schedule = {}
    teacher_period_assignments = {}  # To keep track of which teachers are assigned in each period

    for period in range(1, 9):  # 8 periods
        available_teachers = teachers[:]
        for course in random.sample(courses, len(courses)):  # Randomly pick courses
            if available_teachers:
                teacher = random.choice(available_teachers)

                # Make sure the teacher isn't already assigned in this period
                while teacher.sort_key in teacher_period_assignments.get(period, []) and available_teachers:
                    available_teachers.remove(teacher)
                    if available_teachers:
                        teacher = random.choice(available_teachers)

                if period not in schedule:
                    schedule[period] = []
                schedule[period].append({
                    'course_id': course.sort_key.split("#")[-1],
                    'teacher_id': teacher.sort_key.split("#")[-1]
                })

                # Update the teacher's assignment for this period
                if period not in teacher_period_assignments:
                    teacher_period_assignments[period] = []
                teacher_period_assignments[period].append(teacher.sort_key)

                available_teachers.remove(teacher)

    return schedule


class Schedule(Model):
    class Meta:
        table_name = 'your_table_name'
    partition_key = UnicodeAttribute(hash_key=True)
    sort_key = UnicodeAttribute(range_key=True)
    data = UnicodeAttribute()


def store_schedule(org_id, schedule):
    partition_key_val = f"ORG#{org_id}#SCHEDULE"
    sort_key_val = "SCHEDULE#TESTING"  # You can use a more appropriate value
    schedule_str = str(schedule)  # Convert dict to str for storing
    Schedule(partition_key=partition_key_val, sort_key=sort_key_val, data=schedule_str).save()
