# CIS129_ReeceEnfield_Lab11_ClassAverageFiles.py
# Reece Enfield
# April 15, 2024
# This program defines and executes three functions. One that writes grades to a text file (grades.txt), one that reads grades from the grades.txt text file, and one that writes records of students' exam grades to a CSV file.

# Exercise 9.1 (Class Average: Writing Grades to a Plain Text File)
def write_grades_txt_file():
    with open('grades.txt', 'w') as file: # Create and open grades.txt in write mode
        print("""Please enter grades (enter "end" to end the entry process)""")
        while True:
            grade = input("Enter a grade: ") # get grades from user
            if grade.lower() == "end": # create end entry condition
                break
            file.write(grade + "\n") # enter grades to grades.txt file


# Exercise 9.2 (Class Average: Reading Grades from a Plain Text File)
def read_grades_txt_file():
    with open('grades.txt', 'r') as file: # Open grades.txt in read mode
        grades_list = [] #Initialize empty grade list
        for grade_line in file.readlines():
            try:
                add_grade = int(grade_line.strip()) #converts grades to integers and strips whitespace from lines
                grades_list.append(add_grade) #adds grade to grades_list
            except ValueError: #omits invalid grades
                print(f"Invalid grade, '{grade_line.strip()}' omitted")

    # Calculate total, count, and average values
    total = sum(grades_list)
    count = len(grades_list)
    average = total / count if count > 0 else 0

    # Display individual grades, total, count, and average
    print("Individual grades:", grades_list)
    print("Total sum of grades:", total)
    print("Number of grades:", count)
    print("Grade average:", average)

# Exercise 9.3 (Class Average: Writing Student Records to a CSV File)
def write_student_record_csv():
    import csv #import csv module
    with open('grades.csv', 'w', newline='') as csvfile: # Create and open grades.csv in write mode
        writer = csv.writer(csvfile)
        while True: # Loop entry process for each student until user enters "end"
            firstname = input("""Enter the student's first name (enter "end" to end the entry process): """)
            if firstname.lower() == "end":
                break
            lastname = input("Enter the student's last name: ")
            exam1grade = int(input("Enter the grade for Exam 1: "))
            exam2grade = int(input("Enter the grade for Exam 2: "))
            exam3grade = int(input("Enter the grade for Exam 3: "))

            writer.writerow([firstname,lastname,exam1grade,exam2grade,exam3grade]) # Writes the names and grade entries as a record to the CSV file


# Call each function
write_grades_txt_file()
read_grades_txt_file()
write_student_record_csv()