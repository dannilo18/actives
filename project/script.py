import json
import os
from PyInquirer import prompt

def list_applications(file_name):
    try: 
        with open(file_name, "r", encoding="utf-8") as infos:
            result = json.load(infos)
    except:
        result = {}
    return result

def select_active_type(all_actives):
    if not all_actives:
        question = [
            {
                "type": "list",
                "name": "active_type",
                "message": "Which active do you want to check?",
                "choices": ["Add new one","Quit"],
            }
        ]
        answer = prompt(question)
        return answer["active_type"]
    else:
        actives_list = list(all_actives.keys()) + ["Add new one", "Delet existent one", "Quit"]
        question = [
            {
                "type": "list",
                "name": "active_type",
                "message": "Which active do you want to check?",
                "choices": actives_list,
            }
        ]
        answer = prompt(question)

        return answer["active_type"]

def add_active_type(all_actives):
    question = [
        {
            "type": "input",
            "name": "active_type",
            "message": "Input new active:",
        }
    ]
    answer = prompt(question)
    all_actives[answer["active_type"]] = []
    with open("actives.json", "w", encoding="utf-8") as infos:
        json.dump(all_actives, infos)
    print("Active type added successfuly!")
    input("Press any key to continue...")

def delet_active_type(all_actives):
    question = [
        {
            "type": "list",
            "name": "active_type",
            "message": "Select which active type do tou want to delete",
            "choices": list(all_actives.keys()),
        }
    ]
    answer = prompt(question)
    del all_actives[answer["active_type"]]
    with open("actives.json", "w", encoding="utf-8") as infos:
        json.dump(all_actives, infos)
    print("Active type deleted successfuly!")
    input("Press any key to continue...")

def main():
    os.system("clear")
    all_actives = list_applications("actives.json")
    active_type = select_active_type(all_actives)

if __name__ == "__main__":
    main()
