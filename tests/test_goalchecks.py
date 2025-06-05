import requests
from faker import Faker
fake = Faker()
from pytest_steps import (test_steps)
import os
from dotenv import load_dotenv

from modules.methods import create_goal, delete_goal, create_not_valid_goal, update_goal

load_dotenv()

my_headers = {"Authorization": os.getenv("TOKEN")}
name1=fake.first_name_male()
name2=fake.first_name_female()


@test_steps("Create new goal1", "create new goal2", "Get goals list", "Delete goal1", "Delete goal2")
def test_get_goals():
    res1 = create_goal(name1)
    assert res1.status_code == 200
    id1 = res1.json()["goal"]["id"]
    yield
    res2 = create_goal(name2)
    assert res2.status_code == 200
    id2 = res2.json()["goal"]["id"]
    yield
    goals_list = requests.get(os.getenv("API_URL") + "/team/90151259069/goal", headers=my_headers)
    assert goals_list.status_code == 200
    assert goals_list.json()["goals"][0]["name"] == name1
    assert goals_list.json()["goals"][1]["name"] == name2
    yield
    res3 = delete_goal(id1)
    assert res3.status_code == 200
    yield
    res4 = delete_goal(id2)
    assert res4.status_code == 200
    yield


@test_steps("Create new goal1", "Create goal with not valid space id", "delete goal")
def test_create_goals():
    res1 = create_goal(name1)
    assert res1.status_code == 200
    id1 = res1.json()["goal"]["id"]
    yield
    res2 = create_not_valid_goal(name2)
    assert res2.status_code == 400
    yield
    res3 = delete_goal(id1)
    assert res3.status_code == 200
    yield

@test_steps("Create new goal1", "Get goal", "delete goal")
def test_get_one_goal():
    res1 = create_goal(name1)
    assert res1.status_code == 200
    id1 = res1.json()["goal"]["id"]
    yield
    goal = requests.get(os.getenv("API_URL") + "/goal/" + id1, headers=my_headers)
    assert goal.status_code == 200
    assert goal.json()["goal"]["name"] == name1
    yield
    res3 = delete_goal(id1)
    assert res3.status_code == 200
    yield

@test_steps("Create new goal1", "Update goal", "delete goal")
def test_update_goal():
    res1 = create_goal(name1)
    assert res1.status_code == 200
    id1 = res1.json()["goal"]["id"]
    yield
    random_name_for_upd = fake.color_name()
    res2 = update_goal(random_name_for_upd, id1)
    assert res2.status_code == 200
    assert res2.json()["goal"]["name"] == random_name_for_upd
    yield
    res3 = delete_goal(id1)
    assert res3.status_code == 200
    yield

@test_steps("Create new goal1", "Delete goal with not valid id", "delete goal")
def test_delete_goals():
    res1 = create_goal(name1)
    assert res1.status_code == 200
    id1 = res1.json()["goal"]["id"]
    yield
    res2 = delete_goal("not_valid")
    assert res2.status_code == 500
    yield
    res3 = delete_goal(id1)
    assert res3.status_code == 200
    yield