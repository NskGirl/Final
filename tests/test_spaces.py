import time

import requests
from faker import Faker
fake = Faker()
from pytest_steps import (test_steps)
import os
from dotenv import load_dotenv

from modules.methods import create_space, delete_space, create_not_valid_space, update_space

load_dotenv()

my_headers = {"Authorization": os.getenv("TOKEN")}
name1=fake.first_name_male()
name2=fake.first_name_female()


@test_steps("Create new space1", "create new space2", "Get space list", "Delete space1", "Delete space2")
def test_get_spaces():
    res1 = create_space(name1)
    assert res1.status_code == 200
    id1 = res1.json()["id"]
    yield
    res2 = create_space(name2)
    assert res2.status_code == 200
    id2 = res2.json()["id"]
    yield
    time.sleep(4)
    spaces_list = requests.get(os.getenv("API_URL") + "/team/90151259069/space", headers=my_headers)
    assert spaces_list.status_code == 200
    assert spaces_list.json()["spaces"][0]["name"] == name1
    assert spaces_list.json()["spaces"][1]["name"] == name2
    yield
    res3 = delete_space(id1)
    assert res3.status_code == 200
    yield
    res4 = delete_space(id2)
    assert res4.status_code == 200
    yield


@test_steps("Create new space1", "Create space with not valid team id", "delete space")
def test_create_spaces():
    res1 = create_space(name1)
    assert res1.status_code == 200
    id1 = res1.json()["id"]
    yield
    res2 = create_not_valid_space(name2)
    assert res2.status_code == 400
    yield
    res3 = delete_space(id1)
    assert res3.status_code == 200
    yield

@test_steps("Create new space1", "Get space", "delete space")
def test_get_one_space():
    res1 = create_space(name1)
    assert res1.status_code == 200
    id1 = res1.json()["id"]
    yield
    time.sleep(1)
    space = requests.get(os.getenv("API_URL") + "/space/" + id1, headers=my_headers)
    assert space.status_code == 200
    assert space.json()["name"] == name1
    yield
    res3 = delete_space(id1)
    assert res3.status_code == 200
    yield

@test_steps("Create new space1", "Update space", "delete space")
def test_update_space():
    res1 = create_space(name1)
    assert res1.status_code == 200
    id1 = res1.json()["id"]
    yield
    time.sleep(1)
    random_name_for_upd = fake.color_name()
    res2 = update_space(random_name_for_upd, id1)
    assert res2.status_code == 200
    assert res2.json()["name"] == random_name_for_upd
    yield
    res3 = delete_space(id1)
    assert res3.status_code == 200
    yield

@test_steps("Create new space1", "Delete space with not valid id", "delete space")
def test_delete_space():
    res1 = create_space(name1)
    assert res1.status_code == 200
    id1 = res1.json()["id"]
    yield
    res2 = delete_space("not_valid")
    assert res2.status_code == 400
    yield
    res3 = delete_space(id1)
    assert res3.status_code == 200
    yield