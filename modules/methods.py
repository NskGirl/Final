import requests
import os
from dotenv import load_dotenv
from faker import Faker
fake = Faker()

load_dotenv()
my_headers = {"Authorization": os.getenv("TOKEN")}

def create_goal(name):
    body = {
        "name": name
    }
    new_goal = requests.post(os.getenv("API_URL") + "/team/90151259069/goal", headers=my_headers, json=body)
    print(new_goal)
    return new_goal

def delete_goal(id):
    deleted_goal = requests.delete(os.getenv("API_URL") + "/goal/" + id, headers=my_headers)
    return deleted_goal

def create_not_valid_goal(name):
    body = {
        "name": name
    }
    not_valid_goal = requests.post(os.getenv("API_URL") + "/team/not_valid/goal", headers=my_headers, json=body)
    return not_valid_goal

def update_goal(name, id):
    body = {
        "name": name
    }
    update_goal = requests.put(os.getenv("API_URL") + "/goal/" + id, headers=my_headers, json=body)
    return update_goal