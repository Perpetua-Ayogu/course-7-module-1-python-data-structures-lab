# data_generator.py

def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily
    using a Python generator.
    """
    return (
        student
        for student in student_list
        if student[2] == major
    )