import requests

import configuration
import data
import sender_stand_request

def get_user_body(first_name):
    current_body = data.users_body.copy()
    current_body['firstName'] = first_name
    return current_body




