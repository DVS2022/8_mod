import sqlite3

conn = sqlite3.connect('data_base.sqlite')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE Students (id int, name Varchar(32), surname Varchar(32), age int, city Varchar(32))''')

cursor.execute('''CREATE TABLE Courses (id int, name Varchar(32), time_start Varchar(32), time_end Varchar(32))''')

cursor.execute('''CREATE TABLE Student_courses (course_id int, student_id int)''')


cursor.executemany('''INSERT INTO Students VALUES (?, ?, ?, ?, ?)''',
[
(1, 'Max', 'Brooks', 24, 'Spb'),
(2, 'John', 'Stones', 15, 'Spb'),
(3, 'Andy', 'Wings', 45, 'Manchester'),
(4, 'Kate', 'Brooks', 34, 'Spb'),
(5, 'Vadim', 'Demochkin', 33, 'Pattaya')
])

cursor.executemany('''INSERT INTO Courses VALUES (?, ?, ?, ?)''',
[
(1, 'python', '21.07.21', '21.08.21'),
(2, 'java', '13.07.21', '16.08.21')
])

cursor.executemany('''INSERT INTO Student_courses VALUES (?, ?)''',
[(1, 1), (1, 2), (1, 3), (2, 4), (1, 5)])


conn.commit()

cursor.execute("SELECT * FROM Students WHERE age>30;")
old_students = cursor.fetchall()
print('Студентам больше 30 лет:', old_students)

cursor.execute("""SELECT Students.surname FROM Student_courses JOIN Students ON Student_courses.student_id = Students.id WHERE course_id=1;""")
python_students = cursor.fetchall()
print('Студенты курсов Python:', python_students)

cursor.execute("""SELECT Students.surname FROM Student_courses JOIN Students ON Student_courses.student_id = Students.id WHERE Students.city = 'Spb' AND course_id = 1;""")
spb_python_students = cursor.fetchall()
print('Студенты курсов Python в СПБ:', spb_python_students)

conn.close()