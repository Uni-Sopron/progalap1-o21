# Készítsd el az alábbi 2 függvény implementációját!
# A megoldáshoz készíthetsz további segédfüggvényeket is.

"""Ebben a szöveges fájlban vannak a felvett tárgyak, soronként 1.
    Minden sor elején a tárgy kreditértéke van, majd pontosvessző után a neve."""
subjects = "subjects.csv"

"""Ebben a fájlban vannak a vizsgaeredmények egy JSON listában.
    A lista minden eleme egy dictionary, 3 kulcs-érték párral.
    A "subject" a tárgy neve, ahogy a subjects.csv-ben is szerepel.
    A "date" a vizsga dátuma yyyy.mm.dd formátumban.
    (Egy tárgyból egy napon csak 1 vizsga lehet.)
    A "grade" a vizsgajegy 1-5 között."""
exams = "grades.json"


"""Számítsa ki és írja ki a féléves súlyozott átlagot.
    A tárgyak a kreditértékükkel legyenek súlyozva.
    Minden tárgyból a legutolsó vizsga eredménye számít.
    Ha egy tárgyból nincs vizsgaeredmény, az 1-es eredménynek számít."""
def weighted_average_calculation():
    """Calculate and print the weighted average of grades.
        Grades are weighted with the number of credits for the subject.
        Only the latest grade is considered, if any.
        If there are no grades registered for a subject, it counts as grade 1.
        """
    pass


"""Olvasson be egy új vizsgaeredményt, és fűzze hozzá a JSON fájlhoz.
    Listázza ki a felvett tárgyakat, és kérje be a kívánt tárgy indexét.
    Hibás index esetén ismételje meg a bekérést.
    Kérje be az eredményt. Ha nem 1-5 közti egész szám, kérje be újra.
    Kérje be a dátumot. Ha nem 3 db, ponttal elválasztott egész számot adnak
    meg, kérje be újra."""
def register_new_grade():
    """Read and register a new grade with date, subject name, and grade.
        Print subject list and read index of the chosen subject.
        Grade should be 1-5.
        Date should be in yyyy.mm.dd format.
        """
    pass


def main():
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

if __name__ == "__main__":
    main()
