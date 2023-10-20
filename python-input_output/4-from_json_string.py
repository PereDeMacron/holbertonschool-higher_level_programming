#!/usr/bin/python3
import json
"""def a function that returns an Python data structure represent by a JSON string"""
def from_json_string(my_str):
    return json.loads(my_str)
