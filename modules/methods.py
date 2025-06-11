import requests
import os
from dotenv import load_dotenv
from faker import Faker
fake = Faker()

load_dotenv()
my_headers = {"Authorization": os.getenv("TOKEN")}

def create_space(name):
    body = {
        "name": name
    }
    new_space = requests.post(os.getenv("API_URL") + "/team/90151259069/space", headers=my_headers, json=body)
    return new_space

def delete_space(id):
    deleted_space = requests.delete(os.getenv("API_URL") + "/space/" + id, headers=my_headers)
    return deleted_space

def create_not_valid_space(name):
    body = {
        "name": name
    }
    not_valid_space = requests.post(os.getenv("API_URL") + "/team/not_valid/space", headers=my_headers, json=body)
    return not_valid_space

def update_space(name, id):
    body = {
        "name": name
    }
    update_space = requests.put(os.getenv("API_URL") + "/space/" + id, headers=my_headers, json=body)
    return update_space