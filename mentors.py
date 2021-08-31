import students
import grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def attach_course(self, course_name):
        self.courses_attached.append(course_name)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return super().__str__() + f'Средняя оценка за лекции: {grades.avg_grade_calculate(self)}\n'

    def __lt__(self, other):
        return grades.avg_grade_calculate(self) < grades.avg_grade_calculate(other)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, students.Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
