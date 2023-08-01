import os

import dotenv
import requests
from dotenv import load_dotenv

from src.constains.apiconstains import url_create_booking
from src.helper.api_wrapper import post_request
from src.helper.common_verification import verify_http_code
from src.helper.payload_manager import create_booking
from src.helper.utils import common_headers


def test_put_req():
    load_dotenv()
    temp_token = "token=" + os.getenv("token")
    print("\n The Token Id is :" + temp_token)
    load_dotenv()
    user_name = "username=" + os.getenv("username")
    print("\n The user name fetching from environment:"+user_name)
    response = post_request(url_create_booking(), auth=None, headers=common_headers(), payload=create_booking(),
                            in_json=False)
    print(response.status_code)
    print(response.json())
    verify_http_code(response, 200)
    booking_id = response.json()["bookingid"]
    print("The data type is :", type(booking_id))
    bookingno = str(booking_id)
    print("The data type is :", type(bookingno))
    print("Your Booking Is is:", booking_id)