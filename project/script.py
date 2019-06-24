import json
import os
from PyInquirer import prompt

available_avtives_type = ["Criptocurrencies", "Treasure Securities", "Investment Funds", "Stocks", "DI"]

def load_actives(file_name):
    try: 
        with open(file_name, "r", encoding="utf-8") as infos:
            result = json.load(infos)
    except:
        result = {}
    return result

def list_select_active_type(all_actives):
    if not all_actives:
        print("There is no older information, please insert a active type to begin.")
        question = [
            {
                "type": "list",
                "name": "active_type",
                "message": "Which active do you want to check?",
                "choices": ["Add new active type","Quit"],
            }
        ]
        answer = prompt(question)
        return answer["active_type"]
    else:
        actives_list = list(all_actives.keys()) + ["Add new active type", "Delete existent active type", "Quit"]
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

def add_delete_active_type(all_actives, active_type):
    if active_type == "Add new active type":
        question = [
            {
                "type": "input",
                "name": "active_type",
                "message": "Input new active (" + ", ".join(available_avtives_type) + "):",
            }
        ]
        answer = prompt(question)
        all_actives[answer["active_type"]] = []
        with open("actives.json", "w", encoding="utf-8") as infos:
            json.dump(all_actives, infos)
        print("Active type added successfuly!")
    else:
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

def select_active(all_actives, active_type):
    options = all_actives[active_type] + ["Add new active", "Delet existent active", "Go back"]
    question = [
        {
            "type": "list",
            "name": "active",
            "message": "Which one from {} do tou want to check?".format(active_type),
            "choices": options,
        }
    ]
    answer = prompt(question)

    return answer["active"]

def main():
    os.system("clear")
    all_actives = load_actives("actives.json")
    active_type = list_select_active_type(all_actives)
    if active_type == "Add new active type" or active_type == "Delete existent active type":
        add_delete_active_type(all_actives,active_type)
        main()
    elif active_type == "Quit":
        return
    else:
        active = select_active(all_actives, active_type)

if __name__ == "__main__":
    main()
