
import json
import os

db_file = "sponsors.json"

def load_sponsors():
    if not os.path.exists(db_file):
        save_sponsors([])
    with open(db_file, "r") as f:
        return json.load(f)

def save_sponsors(sponsors):
    with open(db_file, "w") as f:
        json.dump(sponsors, f, indent=4)

def get_all_users():
    if not os.path.exists("users.json"):
        with open("users.json", "w") as f:
            json.dump([], f)
    with open("users.json", "r") as f:
        return json.load(f)

def save_user(user_id):
    users = get_all_users()
    if user_id not in users:
        users.append(user_id)
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)
