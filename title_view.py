from data import api_data
from flask import jsonify

def post_response(data_title):
    
    matches = [i for i in api_data if data_title.lower() == i['title'].lower()]
    print(matches)
    return matches
