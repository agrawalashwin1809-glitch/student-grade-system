#vidyarthi project for studet grade system 
#here we have cearte a empty dictonary so that user can store the name and grade acc to him
student_grades ={  }
#add a new studet in system
def add_student(name, grade):
    student_grades[name] = grade
    print("added student:", name, "with grade:", grade)
#if you want to upaste the studet grade in system    
def update_student(name,grade):
    if name in student_grades:
        student_grades[name] = grade
        print("updated student:", name, "with new grade:", grade)
    else:
        print("student not found:", name)
# if you want to delte the studet name in the system          
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(name, "has been deleted successfully")
    else:
        print("student not found:", name)
#you want to display the name and garde of all the studet in the system        
def display_all_students():
    if student_grades:
        print("Student Grades:")
        for name, grade in student_grades.items():
            print(name, ":", grade)
    else:
        print("No students found.")
# here is the main program where it will run the whole program & user will choose the option from the menu and it will perform        
def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Update Student Grade")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add_student(name, grade)
        elif choice == "2":
            name = input("Enter student name to update: ")
            grade = input("Enter new grade: ")
            update_student(name, grade)
        elif choice == "3":
            name = input("Enter student name to delete: ")
# delete functon here which is in bulit             
            delete_student(name)
        elif choice == "4":
            display_all_students()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()            


          
 