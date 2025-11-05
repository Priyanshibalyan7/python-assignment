# Name : Priyanshi
# Date : 5-11-25
# Title: Gradebook Analyzer

# Task 1 : Project setup and initiation

def menu():
    print("\n===== Gradebook Analyzer =====")
    print("1. Enter student data")
    print("2. View statistics")
    print("3. View grades summary")
    print("4. View pass/fail report")
    print("5. Display full results table")
    print("6. Exit")

    

# Task 2: Input & Data Collection
def student_data():
    s=int(input("Enter the number of students in class: "))
    marks={}
    for i in range(s):
        student_name=input(f"enter the students name {i + 1} : ")
        Marks=int(input(f"Enter the marks of {student_name}: "))
        marks[student_name] = Marks

# Task 3 : Statistical Analysis Functions
def average(marks):
    return (sum(marks.values()) / len(marks))

def median(marks):
    marks=list(marks.values())
    marks.sort()
    n=len(marks)
    if n==0:
        return None
    elif n%2 ==1 :
        median = marks[n//2]
    else:
        median=[marks(n//2)-1] + marks[n//2]/2
        return median
    
def max_score(marks):
    return (max(marks.values()))

def min_score(marks):
    return (min(marks.values()))

# Task 4 : assigning grades 


def assign_grades(marks):
    grades = {}
    for student_name, Marks in marks.items():
        if Marks >= 90:
            grades[student_name] = 'A'
        elif Marks >= 80:
            grades[student_name] = 'B'
        elif Marks >= 70:
            grades[student_name] = 'C'
        elif Marks >= 60:
            grades[student_name] = 'D'
        else:
            grades[student_name] = 'F'
    return( grades)

def count_grades(grades):
    summary = {}
    for grade in grades.values():
        summary[grade] = summary.get(grade, 0) + 1
    return (summary)

# Task 5 : pass and fail students
def pass_fail_lists(marks):
    passed_students = [student_name for student_name, m in marks.items() if m >= 40]
    failed_students = [student_name for student_name, m in marks.items() if m < 40]
    print (passed_students, failed_students)

#Task 6 : result table and user loop

def results_table(marks, grades):
    print("\n-----------------------------------")
    print(f"{'Name':<10} {'Marks':<10} {'Grade':<10}")
    print("-----------------------------------")
    for student_name in marks:
        print(f"{student_name:<10} {marks[student_name]:<10} {grades[student_name]:<10}")
    print("-----------------------------------")


def Main():
    print("Welcome to the Gradebook Analyzer!")
    marks = {}
    grades = {}


    while True:

         menu()
         choice = input("Enter your choice (1 – 6): ")

         if choice == '1':
            marks = student_data()
            print("Data entry complete.")
         elif choice == '2':
            if not marks:
                print("No data available.")
                continue
            print("\n--- Statistics ---")
            print(f"Average Marks: {average(marks):}")
            print(f"Median Marks: {median(marks):}")
            print(f"Highest Marks: {max_score(marks)}")
            print(f"Lowest Marks: {min_score(marks)}")

         elif choice == '3':
            if not marks:
                print("No data available.")
                continue
            grades = assign_grades(marks)
            grade_summary = count_grades(grades)
            print("\n--- Grade Distribution ---")
            for g, count in grade_summary.items():
                print(f"{g}: {count}")

         elif choice == '4':
            if not marks:
                print("No data available.")
                continue
            passed, failed = pass_fail_lists(marks)
            print("\n--- Pass/Fail Report ---")
            print(f"Passed ({len(passed)}): {passed}")
            print(f"Failed ({len(failed)}): {failed}")

         elif choice == '5':
            if not marks:
                print("No data available.")
                continue
            if not grades:
                grades = assign_grades(marks)
            results_table(marks, grades)

         elif choice == '6':
            print("Exiting program. Goodbye!")
            break

         else:
            print("Invalid choice. Try again.")


if __name__=="_Main_":
    Main()