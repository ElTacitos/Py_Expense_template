from user import get_users
from expense import get_expense

#WIP
def equilibrate_debts(debts):
    users_status = {user: 0 for user in get_users()}
    # iterate over each user of debts
    print(users_status)
    for user in debts:
        debt = debts[user]
        for user2 in debt:
            users_status[user] -= debt[user2]
            users_status[user2] += debt[user2]

    sorted_users_status = sorted(users_status.items(), key=lambda x: x[1])
    print(sorted_users_status)

def compute_status():
    users = get_users()
    expense = get_expense()
    debts = {user: {user: 0 for user in users} for user in users}

    for transaction in expense:
        spender = transaction[2]
        participants = transaction[3].split(";")
        for user in participants:
            if user == spender:
                debts[spender][spender] += float(transaction[0]) / len(participants)
            else:
                debts[spender][user] += float(transaction[0]) / len(participants)

    return debts


def display_status():
    status = compute_status()
    for user in status:
        to_print = f"{user} owes:\n"
        for user2 in status[user]:
            if status[user][user2] != 0:
                to_print += f"\t{status[user][user2]} to {user2}\n"

        if to_print == f"{user} owes:\n":
            print(f"{user} owes Nothing")
        else:
            print(to_print)