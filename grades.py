import mentors
import students


def avg_grade_calculate(person, course=''):
    if isinstance(person, (students.Student, mentors.Mentor)):
        if len(person.grades) == 0:
            return 0
        elif course != '':
            count_grades, sum_grades = 0, 0
            for value in person.grades[course]:
                count_grades += 1
                sum_grades += value
            return round(sum_grades / count_grades, 2)
        else:
            count_grades, sum_grades = 0, 0
            for value in person.grades.values():
                count_grades += len(value)
                sum_grades += sum(value)
            return round(sum_grades / count_grades, 2)
    else:
        return 'Ошибка'


def avg_grade_by_course(*persons, course=''):
    count_grades, sum_grades = 0, 0
    for person in persons:
        if isinstance(person, (students.Student, mentors.Lecturer)):
            if course in person.grades:
                sum_grades += avg_grade_calculate(person, course=course)
                count_grades += 1
        else:
            return 'Ошибка'
    return round(sum_grades / count_grades, 2)
