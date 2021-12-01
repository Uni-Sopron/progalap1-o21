exams = "grades.json"
subjects = "subjects.txt"


def weighted_average_calculation():
    """Calculate and print the weighted average of grades.
    Grades are weighted with the number of credits for the subject.
    Only the last grade is considered, if any.
    If there are no grades registered for a subject, it counts as grade 1.
    """
    pass


def register_new_grade():
    """Register a new grade with date, subject name, and grade.
    Subject name should be from the list in `subjects.txt`.
    Grade should be 1-5.
    Date should be in yyyy.mm.dd format.
    """
    pass


if __name__ == "__main__":
    while True:
        selection = input(
            """ Mit szeretnel csinalni?
        1) Kiszamolni a kreditatlagomat.
        2) Uj vizsgaeredmenyt felvinni.
        3) Kilepni.
        """
        )
        if selection == "3":
            exit()
        elif selection == "1":
            weighted_average_calculation()
        elif selection == "2":
            register_new_grade()
        else:
            print("Hibas valasz.")
