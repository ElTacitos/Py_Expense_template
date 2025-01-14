import csv

from PyInquirer import prompt

from user import get_users

expense_questions1 = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "list",
        "name": "spender",
        "message": "New Expense - Spender: ",
        "choices": []
    }
]
expense_questions2 = [
    {
        "type": "checkbox",
        "name": "participants",
        "message": "New Expense - Participants: ",
        "choices": []
    }
]




def get_checked_users(spender):
    return [{"name": user, "checked": user == spender} for user in get_users()]

def get_expense():
    # read expense_report.csv as csv file and return the content
    f = csv.reader(open("expense_report.csv", "r"))
    return [row for row in f]
def new_expense(*args):
    expense_questions1[2]["choices"] = get_users()
    infos = prompt(expense_questions1)
    expense_questions2[0]["choices"] = get_checked_users(infos["spender"])
    infos.update(prompt(expense_questions2))
    f = open("expense_report.csv", "a")
    f.write(f"{infos['amount']},{infos['label']},{infos['spender']},{';'.join(infos['participants'])}\n")
    f.close()
    print("Expense Added !")
    return True
