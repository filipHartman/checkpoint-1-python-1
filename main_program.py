import data
import display
import os
"""
The main program should use functions from data and display modules
"""


def add_new_student(students, new_student):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Creates id for new student, adds it at the beginning of new student data,
    adds new student to students list and appends it to data file.

    :param list students: currently existing students
    :param list new_student: new student data without id. Format:
        name,surname,year of birth,class,average grade,average presence

    :returns: updated students list
    :rtype: list
    """


def delete_student_by_id(students, uid):
    """
    Deletes student from list by given unique id and updates data file

    :param list students: currently existing students
    :param str uid: unique id of student to be deleted

    :returns: updated students list
    :rtype: list
    """
    id_column = 0
    updated_students = []
    for student_data in students:
        if student_data[id_column] != uid:
            updated_students.append(student_data)
    return updated_students



def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should have main loop of program that will end only
    when user choose an option from menu to close the program. It should repeat
    displaying menu and asking for input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    menu_options = [
                    "Print all students",
                    "Print student data from ID",
                    "Delete student",
                    "Print data of the youngest student",
                    "Print data of the oldest student",
                    "Exit"
                    ]

    print("Hello to JERZYBOT. Please select your option")

    while True:
        try:
            display.print_program_menu(menu_options)
            choice = int(input("Choose: "))
            os.system("clear")

            students = data.import_data_from_file()
            if choice == 0:
                display.print_students_list(students)
                input("Enter any key ")
                os.system("clear")

            elif choice == 1:
                uid = input("Enter ID of student to display his/her data: ")
                student_data = data.get_student_by_id(uid, students)
                display.print_student_info(student_data)
                print("\n")
                input("Enter any key ")
                os.system("clear")

            elif choice == 2:
                uid = input("Enter ID of student to remove his/her data from the list: ")
                new_list = delete_student_by_id(students, uid)
                data.export_to_file(new_list, mode="w")
                print("Data of student with given ID have been removed.")
                input("Enter any key ")
                os.system("clear")

            elif choice == 3:
                youngest_student_data = data.get_youngest_student(students)
                display.print_student_info(youngest_student_data)
                print("\n")
                input("Enter any key ")
                os.system("clear")

            elif choice == 4:
                oldest_student_data = data.get_oldest_student(students)
                display.print_student_info(oldest_student_data)
                print("\n")
                input("Enter any key ")
                os.system("clear")

            elif choice == 5:
                exit()

            else:
                pass

        except ValueError:
            print("Invalid input!")


if __name__ == '__main__':
    main()
