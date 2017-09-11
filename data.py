import csv
import string
import random


def bubble_sort(myList):
    for i in range(0, len(myList) - 1):
        for j in range(0, len(myList) - 1 - i):
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
    return myList


"""
This module should use random module to generate_id
"""


def import_data_from_file(filename='class_data.txt'):
    """
    Import data from file to list. Expected returned data format:
        [['M9@p', 'Ela', 'Opak', '1988', 'A', '60', '69'],
        ['E4)i', 'Barbara', 'Loremska', '1991', 'B', '76', '61'],
        ...]

    :param str filename: optional, name of file to be imported

    :returns: list of lists representing students' data
    :rtype: list
    """
    students_data = []
    with open(filename, "r") as data_file:
        for line in data_file:
            students_data.append(list(line.strip("\n").split(",")))
    return students_data


def export_to_file(data, filename='class_data.txt', mode='a'):
    """
    Export data from list to file. If called with mode 'w' it should overwritte
    data in file. If called with mode 'a' it should append data at the end.

    :param list data: students' data
    :param str filename: optional, name of file to export data to
    :param str mode: optional, file open mode with the same meaning as\
    file open modes used in Python. Possible values: only 'w' or 'a'

    :raises ValueError: if mode other than 'w' or 'a' was given. Error message:
        'Wrong write mode'
    """
    if mode == "a":
        mode = "a"
    elif mode == "w":
        mode = "w"
    else:
        raise ValueError("Wrong write mode")

    with open(filename, mode) as data_file:
        data_txt_file = csv.writer(data_file, delimiter=",")
        for line in data:
            data_txt_file.writerow(line)


def get_student_by_id(uid, students):
    """
    Get student by unique id

    :param str uid: student unique id
    :param list students: students' data

    :raises ValueError: if student's uid not found in class data.
        Error message: 'Student does not exist'

    :returns: specific student's data
    :rtype: list
    """
    id_column = 0
    for student_data in students:
        if student_data[id_column] == uid:
            return student_data
    else:
        raise ValueError("Student does not exist!")


def get_students_of_class(students, class_name):
    """
    Get all students from given class

    :param list students: list of nested list imported from file
    :param str class_name: string representing class name that student\
        attends to

    :returns: students from given class only
    :rtype: list
    """
    class_column = 4
    students_from_given_class = []
    for student_data in students:
        if student_data[class_column] == class_name:
            students_from_given_class.append(student_data)
    return students_from_given_class


def get_youngest_student(students):
    """
    Get youngest student from all classes

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data

    :returns: youngest student
    :rtype: list
    """
    birth_year_column = 3
    youngest_student_birth_year = students[0][birth_year_column]
    youngest_student = students[0]
    for student_data in students:
        if student_data[birth_year_column] > youngest_student_birth_year:
            youngest_student_birth_year = student_data[birth_year_column]
            youngest_student = student_data

    return youngest_student


def get_youngest_student_of_class(students, class_name):
    """
    Get youngest student from given class

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data
    :param str class_name: string representing class name that student\
        attends to

    :returns: youngest student from given class
    :rtype: list
    """
    students_from_given_class = get_students_of_class(students, class_name)
    return get_youngest_student(students_from_given_class)


def get_oldest_student(students):
    """
    Get oldest student from all classes

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data

    :returns: oldest student
    :rtype: list
    """
    birth_year_column = 3
    oldest_student_birth_year = students[0][birth_year_column]
    oldest_student = students[0]
    for student_data in students:
        if student_data[birth_year_column] < oldest_student_birth_year:
            oldest_student_birth_year = student_data[birth_year_column]
            oldest_student = student_data

    return oldest_student


def get_oldest_student_of_class(students, class_name):
    """
    Get oldest student from given class

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data
    :param str class_name: string representing class name that student\
        attends to

    :returns: oldest student
    :rtype: list
    """
    students_from_given_class = get_students_of_class(students, class_name)
    return get_oldest_student(students_from_given_class)


def get_average_grade_of_students(students):
    """
    Calculate average grade of all students

    IMPORTANT:
        Implement this function without built-in functions like sum()
        or similar

    :param list students:  students' data

    :returns: average grade of students value
    :rtype: float
    """
    grade_column = 5
    sum_of_grades = 0
    number_of_students = 0

    for student_data in students:
        sum_of_grades += int(student_data[grade_column])
        number_of_students += 1
    average_grade = sum_of_grades / number_of_students

    return average_grade


def get_average_presence_of_students(students):
    """
    Returns rounded average presence of all students. For instance,
    if average presence is 35.4912, returned value should be 35,
    if average presence is 41.5, returned value should be 42,

    IMPORTANT:
        Implement this function without built-in functions like sum(), round()
        or similar

    :param list students:  students' data

    :returns: average presence of students rounded to int
    :rtype: int
    """
    presence_column = 6
    sum_of_presence = 0
    number_of_students = 0
    for student_data in students:
        sum_of_presence += int(student_data[presence_column])
        number_of_students += 1
    average_presence = str(sum_of_presence / number_of_students)
    result = int(average_presence.split(".")[0])
    if average_presence.split(".")[1][0] >= "5":
        result += 1

    return result


def generate_id(current_ids):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Generate unique id. It should be unique in all existing students list. If
    generated id was already used, function should regenerate it untill it is
    totaly new. Newly generated unique id should be added to current_ids

    REQUIREMENTS:
        - All ids must be 4-characters long
        - Characters should appear in given order:
            1. Upper letter
            2. Digit from 0 to 9
            3. Special character from this list: !@#$%^&*()_+
            4. Lower letter

            Example ids:
                W1&p
                M9@p
                P1!n

    :param list current_ids: list of all ids. It's used to check if
            generated id is unique or not. If new id is unique, current_ids
            should be extended to include this new id.

    :returns: unique id
    :rtype: str
    """
    while True:
        up_letter = random.choice(string.ascii_uppercase)
        digit = str(random.randint(0, 9))
        symbol = random.choice(string.punctuation)
        low_letter = random.choice(string.ascii_lowercase)
        new_id = up_letter + digit + symbol + low_letter

        if new_id not in current_ids:
            return new_id


def get_all_by_gender(students, gender):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Get all students with given gender. As someone forgot to ask students about
    it, the only way JERZYBOT can find out if someone is female is her name.
    Treat all students with name ending with 'a' as female (Maria, Anna, etc).
    (we're sorry Miriam, we'll update JERZYBOT as soon as possible)

    :param list students:  students' data
    :param str gender: gender to filter by. 'female' will return female
        students, 'male' will return list of male students

    :raises ValueError: if gender other than 'female' or 'male' was given.
        Error message: 'Wrong gender'

    :returns: list of students filtered by given gender
    :rtype: list
    """
    name_column = 1
    choosen_gender_student = []
    if gender == "female":
        for student_data in students:
            if student_data[name_column][-1] == "a":
                choosen_gender_student.append(student_data)
    elif gender == "male":
        for student_data in students:
            if student_data[name_column][-1] != "a":
                choosen_gender_student.append(student_data)
    else:
        raise ValueError("Wrong gender")

    return choosen_gender_student


def sort_students_by_age(students, order=None):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Sorts student list by age. User can choose sorting order by passing
    'desc' for descending order or 'asc' for ascening order.
    If order is None returns empty list

    IMPORTANT:
        Implement this function without using sorted() or similar built-in
        functions

    :param list students:  students' data
    :param str order: optional, sorting order

    :raises ValueError: if order other than 'asc', 'desc' or None
        was given

    :returns: sorted students or empty list
    :rtype: list
    """
    sorted_students_list = []
    if order == None:
        return sorted_students_list
    elif order == "asc":
        pass
    elif order == "desc":
        pass
