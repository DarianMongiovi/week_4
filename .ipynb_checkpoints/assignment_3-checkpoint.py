'''

For this assignment please do the following:

- Read in the student_grades.csv file

- calculate the average grade for the class

- for each student record calculate the difference between the student's grade and the average grade

- write the output to a new file called student_grade_differences.csv
 

'''

with open('student_grades.csv','r') as f:

    lines = f.readlines()

    if len(lines) > 0:
        grades = []

        for line in lines[1:]:
            row = line.split(',')
            grades.append(int(row[3].replace('\n','')))

    avg = sum(grades) / len(grades)

    processed_grades = []

    for line in lines[1:]:
        row = line.split(',')
        processed_grades.append(f'{row[1]} {row[2]}, {avg}, {avg - int(row[3].replace('\n',''))}\n')

    print(processed_grades)

with open('processed_grades.csv', 'w') as f:
    f.write("Student, Average Grade, Difference\n")
    for i in range(len(processed_grades))
        f.write(processed_grades[i])