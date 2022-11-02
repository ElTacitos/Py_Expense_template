from PyInquirer import prompt
user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "New User - Name: ",
    },
]

def get_users():
    f = open("users.csv", "r")
    users = [user.replace("\n", "") for user in f.readlines()]
    return users
def add_user():
    infos = prompt(user_questions)
    # This function should create a new user, asking for its name
    f = open("users.csv", "a")
    f.write(f"{infos['name']}\n")
    f.close()
    return True