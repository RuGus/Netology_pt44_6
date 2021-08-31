import mentors
import students
import grades

# Создаем персоналии
lecturer_1 = mentors.Lecturer('Ivan', 'Petrov')
lecturer_2 = mentors.Lecturer('Semen', 'Veselko')
rewiever_1 = mentors.Reviewer('Petr', 'Ponomarenko')
rewiever_2 = mentors.Reviewer('Elena', 'Teremok')
student_1 = students.Student('Stanislav', 'Mudko', 'male')
student_2 = students.Student('Ekaterina', 'Chudko', 'female')

# Назначаем курсы
lecturer_1.attach_course('Python')
lecturer_2.attach_course('OOP')
rewiever_1.attach_course('Python')
rewiever_2.attach_course('OOP')

student_1.add_courses_in_progress('Python')
student_1.add_courses_in_progress('OOP')
student_2.add_courses_in_progress('Python')
student_2.add_courses_in_progress('OOP')

# Проставляем оценки
rewiever_1.rate_hw(student_1, 'Python', 5)
rewiever_1.rate_hw(student_2, 'Python', 5)
rewiever_1.rate_hw(student_1, 'Python', 3)
rewiever_1.rate_hw(student_2, 'Python', 5)
rewiever_2.rate_hw(student_1, 'OOP', 3)
rewiever_2.rate_hw(student_2, 'OOP', 2)
rewiever_2.rate_hw(student_1, 'OOP', 4)
rewiever_2.rate_hw(student_2, 'OOP', 5)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Python', 7)
student_2.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_2, 'OOP', 8)
student_2.rate_lecturer(lecturer_2, 'OOP', 7)
student_1.rate_lecturer(lecturer_2, 'OOP', 9)
student_2.rate_lecturer(lecturer_2, 'OOP', 8)

# Выводим результаты
print('-------------Our Lecturers------------')
print(lecturer_1)
print(lecturer_2)
print('-------------Our Reviewers------------')
print(rewiever_1)
print(rewiever_2)
print('-------------Our Students------------')
print(student_1)
print(student_2)
print('-----------------')
print(f'Средняя оценка наших студентов за курс "Python": '
      f'{grades.avg_grade_by_course(student_1, student_2, course="Python")}')
print(f'Средняя оценка наших студентов за курс "OOP": '
      f'{grades.avg_grade_by_course(student_1, student_2, course="OOP")}')
print(f'Средняя оценка наших лекторов за курс "Python": '
      f'{grades.avg_grade_by_course(lecturer_1, lecturer_2, course="Python")}')
print(f'Средняя оценка наших лекторов за курс "OOP": '
      f'{grades.avg_grade_by_course(lecturer_1, lecturer_2, course="OOP")}')
print(f'---Лучший студент---\n{max(student_1,student_2)}')
print(f'---Лучший лектор---\n{max(lecturer_1,lecturer_2)}')
