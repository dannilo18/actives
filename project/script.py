import json
import os
from PyInquirer import prompt
from prettytable import PrettyTable
import csv

available_avtives_type = ["Criptocurrencies", "Treasure Securities", "Investment Funds", "Stocks", "NUConta"]

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
        if answer["active_type"] not in available_avtives_type:
            input("Invalid active type. Press any key to return")
            add_delete_active_type(all_actives, active_type)
            return
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
    if not all_actives[active_type]:
        print("There is no older information, please insert a active to begin.")
        question = [
            {
                "type": "list",
                "name": "active",
                "message": "Which active do you want to check?",
                "choices": ["Add new active", "Quit"],
            }
        ]
        answer = prompt(question)
        return answer["active"]
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

def add_delete_active(all_actives, active_type, active):
    if active == "Add new active":
        question = [
            {
                "type": "input",
                "name": "active",
                "message": "Input new active: ",
            }
        ]
        answer = prompt(question)
        all_actives[active_type].append(answer["active"])
        with open("actives.json", "w", encoding="utf-8") as infos:
            json.dump(all_actives, infos)
        print("Active added successfuly!")
    else:
        question = [
            {
                "type": "list",
                "name": "active",
                "message": "Select which active do you want to delete",
                "choices": all_actives[active_type],
            }
        ]
        answer = prompt(question)
        del all_actives[active_type][answer["active"]]
        with open("actives.json", "w", encoding="utf-8") as infos:
            json.dump(all_actives, infos)
        print("Active deleted successfuly!")
    input("Press any key to continue...")

def create_file(active, active_type):
    if active_type == "Stocks":
        try:
            active_file = open(active + ".csv", 'x')
        except:
            return
        myFields = ["Date", "Volume", "Value", "Operation amount", "Total volume","Invested amount", "Updated amount", "Earnings", "Total Earnings"]
        writer = csv.DictWriter(active_file, fieldnames=myFields, delimiter=';')
        writer.writeheader()
        active_file.close()
    elif active_type == "Treasure Securities":
        try:
            active_file = open(active + ".csv", 'x')
        except:
            return
        myFields = ["Date", "Volume", "Value", "Operation amount", "Total volume", "Invested amount", "Updated amount"]
        writer = csv.DictWriter(active_file, fieldnames=myFields, delimiter=';')
        writer.writeheader()
        active_file.close()
    elif active_type == "Investment Funds":
        try:
            active_file = open(active + ".csv", 'x')
        except:
            return
        myFields = ["Date", "Value", "Invested amount", "Updated Amount"]
        writer = csv.DictWriter(active_file, fieldnames=myFields, delimiter=';')
        writer.writeheader()
        active_file.close()
    elif active_type == "Criptocurrencies":
        try:
            active_file = open(active + ".csv", 'x')
        except:
            return
        myFields = ["Date", "Volume", "Value", "Operation amount", "Total volume", "Invested amount", "Updated Amount"]
        writer = csv.DictWriter(active_file, fieldnames=myFields, delimiter=';')
        writer.writeheader()
        active_file.close()
    elif active_type == "NUConta":
        try:
            active_file = open(active + ".csv", 'x')
        except:
            return
        myFields = ["Date", "Value", "Invested amount", "Updated Amount"]
        writer = csv.DictWriter(active_file, fieldnames=myFields, delimiter=';')
        writer.writeheader()
        active_file.close()

def show_options(all_actives, active_type, active):
    create_file(active, active_type)
    ordinary_options = ["Update values", "Show info", "Show apport history", "Add apport"]
    if active_type == "Stocks":
        ordinary_options = ordinary_options + ["Add earnings"]
        question = [
            {
                "type": "list",
                "name": "option",
                "message": "What do you want to do?",
                "choices": ordinary_options + ["Go back"],
            }
        ]
        answer = prompt(question)
        return answer["option"]
    elif active_type == "Treasure Securities":
       question = [
           {
               "type": "list",
               "name": "option",
               "message": "What do you want to do?",
               "choices": ordinary_options + ["Go back"],
           }
       ]
       answer = prompt(question)
       return answer["option"]
    elif active_type == "Investment Funds":
        question = [
            {
                "type": "list",
                "name": "option",
                "message": "What do you want to do?",
                "choices": ordinary_options + ["Go back"],
            }
        ]
        answer = prompt(question)
        return answer["option"]
    elif active_type == "Criptocurrencies":
        question = [
            {
                "type": "list",
                "name": "option",
                "message": "What do you want to do?",
                "choices": ordinary_options + ["Go back"],
            }
        ]
        answer = prompt(question)
        return answer["option"]
    elif active_type == "NUConta":
        question = [
            {
                "type": "list",
                "name": "option",
                "message": "What do you want to do?",
                "choices": ordinary_options + ["Go back"],
            }
        ]
        answer = prompt(question)
        return answer["option"]


def update_values(active_type, active):
    print("chuchu")
def show_info(active_type, active):
    if active_type == "Stocks":
        with open(active + ".csv", newline="") as myFile:
            reader = csv.reader(myFile)
            table = PrettyTable(["Total volume", "Invested amount", "Updated amount", "Total Earnings"])
            count = 0
            for row in reader:
                row = row[0].split(";")
                if not count:
                    indexes = [row.index("Total volume"), row.index("Invested amount"), row.index("Updated amount"), row.index("Total Earnings")]
                else:
                    new_row = []
                    for index in indexes:
                        new_row.append(row[index])
                    table.add_row(new_row)
                count = count+1
                if count == 2:
                    break
    elif active_type == "Treasure Securities":
        with open(active + ".csv", newline="") as myFile:
            reader = csv.reader(myFile)
            table = PrettyTable(["Invested amount", "Updated amount"])
            count = 0
            for row in reader:
                row = row[0].split(";")
                if not count:
                    indexes = [row.index("Invested amount"), row.index("Updated amount")]
                else:
                    new_row = []
                    for index in indexes:
                        new_row.append(row[index])
                    table.add_row(new_row)
                count = count+1
                if count == 2:
                    break
    elif active_type == "Investment Funds":
        with open(active + ".csv", newline="") as myFile:
            reader = csv.reader(myFile)
            table = PrettyTable(["Invested amount", "Updated amount"])
            count = 0
            for row in reader:
                row = row[0].split(";")
                if not count:
                    indexes = [row.index("Invested amount"), row.index("Updated amount")]
                else:
                    new_row = []
                    for index in indexes:
                        new_row.append(row[index])
                    table.add_row(new_row)
                count = count+1
                if count == 2:
                    break
    elif active_type == "NUConta":
        with open(active + ".csv", newline="") as myFile:
            reader = csv.reader(myFile)
            table = PrettyTable(["Invested amount", "Updated amount"])
            count = 0
            for row in reader:
                row = row[0].split(";")
                if not count:
                    indexes = [row.index("Invested amount"),
                               row.index("Updated amount")]
                else:
                    new_row = []
                    for index in indexes:
                        new_row.append(row[index])
                    table.add_row(new_row)
                count = count+1
                if count == 2:
                    break
    if active_type == "Criptocurrencies":
        with open(active + ".csv", newline="") as myFile:
            reader = csv.reader(myFile)
            table = PrettyTable(["Total volume", "Invested amount", "Updated amount"])
            count = 0
            for row in reader:
                row = row[0].split(";")
                if not count:
                    indexes = [row.index("Total volume"), row.index("Invested amount"), row.index("Updated amount")]
                else:
                    new_row = []
                    for index in indexes:
                        new_row.append(row[index])
                    table.add_row(new_row)
                count = count+1
                if count == 2:
                    break
    print(table)

def show_apport_history(active_type, active):
    create_file(active, active_type)
    with open(active + ".csv", newline="") as myFile:
        reader = csv.reader(myFile)
        count = 0
        for row in reader:
            row = row[0].split(";")
            if not count:
                table = PrettyTable(row)
                total_len = len(row)
            else:
                if len(row) < total_len:
                    while len(row) < total_len:
                        row = row + [""]
                table.add_row(row)
            count = 1
    print(table)

def add_apport(active_type, active):
    print("Chipa")
    if active_type == "Stocks":
        with open(active + ".csv", "r", newline="") as myFile:
            old_info = csv.DictReader(myFile)
            for row in old_info:
                print(row)
        date = input("Input apport date (dd/mm/yyyy): ")
        volume = input("Input apport volume: ")
        value = input("Input apport value: ")
        operation_amount = volume * value

        with open(active + ".csv", "a", newline="") as myFile:
            myFields = ["Date", "Volume", "Value", "Operation amount", "Total volume", "Invested amount", "Updated amount", "Earnings", "Total Earnings"]
            writer = csv.DictWriter(myFile, fieldnames=myFields, delimiter=';')
            writer.writerow({"Date": date, "Volume": volume, "Value": value})

def main():
    os.system("clear")
    all_actives = load_actives("actives.json")
    active_type = list_select_active_type(all_actives)
    if active_type == "Add new active type" or active_type == "Delete existent active type":
        add_delete_active_type(all_actives,active_type)
        main()
        return
    elif active_type == "Quit":
        return
    else:
        active = select_active(all_actives, active_type)
        if active == "Add new active" or active == "Delete existent active":
            add_delete_active(all_actives, active_type, active)
            main()
            return
        elif active_type == "Go back":
            main()
            return
        else:
            desire = show_options(all_actives, active_type, active)
            if desire == "Update values":
                update_values(active_type, active)
            elif desire == "Show info":
                show_info(active_type, active)
            elif desire == "Show apport history":
                show_apport_history(active_type, active)
            elif desire == "Add apport":
                add_apport(active_type, active)
            elif desire == "Add earnings":
                add_earnings(active_type, active)
            elif desire == "Go back":
                select_active(all_actives,active_type)


if __name__ == "__main__":
    main()
