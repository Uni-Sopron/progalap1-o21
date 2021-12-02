import json
from typing import List

unscheduled_file_name = "to_be_scheduled.json"
scheduled_file_name = "scheduled.json"


def dayname_to_int(dayname: str) -> int:
    if dayname in ["hetfo", "Hetfo", "H", "1"]:
        return 0
    elif dayname in ["kedd", "Kedd", "K", "2"]:
        return 1
    # todo tobbi nap
    else:
        return 2


def fetch_subjects(filename:str) -> List[dict]:
    with open(filename) as file:
        return json.load(file)


def persist_subjects(data: List[dict], filename:str) -> None:
    with open(filename, "w") as file:
        json.dump(data, file)
    
def append_new_subject(subject:dict, filename:str) -> None:
    data = fetch_subjects(filename)
    data.append(subject)
    persist_subjects(data, filename)



def input_unscheduled_subject() -> dict:
    name = input("Mi a targy neve? ")
    students = input("Kiknek van a targy? ")
    teacher = input("Ki fogja tartani a targyat? ")
    duration = int(input("Hany oras? "))
    return {
        "subject": name,
        "students": students,
        "teacher": teacher,
        "duration": duration
    }


def register_unscheduled_subject():
    new_subject = input_unscheduled_subject()
    append_new_subject(new_subject,unscheduled_file_name)


def schedule_unscheduled_subject():
    data = fetch_subjects(unscheduled_file_name)
    # 2 kivalasztani melyikett akarjuk utemezni
    print("Melyik targyat szeretned beutemezni?")
    formatstring = "  {}.: {} ({}/{}) - {}h"
    for idx, subject in enumerate(data):
        print(formatstring.format(
            idx+1,
            subject["subject"],
            subject["students"],
            subject["teacher"],
            subject["duration"]
        ))
    selection = int(input("Add meg a sorszamat: ")) -1 
    selected_subject = data[selection]
    # 3 bekerni hogy mikor legyen
    day = dayname_to_int(input("Melyik nap legyen?"))
    start = int(input("Hany oratol kezdodjon?"))
    # 4 leellenorizni, hog yutkozik-e
    #todo
    # 5 ha nem, akkor kimenteni a scheduled-ba
    del data[selection]
    persist_subjects(data,unscheduled_file_name)
    selected_subject["day"] = day
    selected_subject["start"] = start
    append_new_subject(selected_subject,scheduled_file_name)


if __name__ == "__main__":
    while True:
        selection = input("""Mit szeretnel csinalni?
        1) Felvinni egy uj utemezetlen targyat.
        2) Beutemezni egy targyat.
        3) Orarendet megjeleniteni
        4) Kilepes
        """)
        if selection == "4":
            exit()
        elif selection == "1":
            register_unscheduled_subject()
        elif selection == "2":
            schedule_unscheduled_subject()
        else:
            print("Rossz / nem implementalt opcio.")
