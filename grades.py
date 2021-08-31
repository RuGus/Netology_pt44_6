import mentors
import students


def avg_grade_calculate(person):
    if isinstance(person, (students.Student, mentors.Mentor)):
        if len(person.grades) == 0:
            return 0
        else:
            count_grades, sum_grades = 0, 0
            for value in person.grades.values():
                count_grades += len(value)
                sum_grades += sum(value)
            return round(sum_grades / count_grades, 2)
    else:
        return 'Ошибка'
