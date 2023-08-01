import requests
import os
import json
import pytest
from dotenv import load_dotenv
import json
import pytest


@pytest.fixture
def load_json_data():
    load_dotenv()
    file_name = os.getenv("load_env")
    print(file_name)
    with open(file_name, 'r') as f:
        data = json.load(f)
        return data


def test_make_request(load_json_data):
    # response = requests.get((load_json_data["url"]))
    print(load_json_data["url"])
