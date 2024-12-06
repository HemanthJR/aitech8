from data import api_data
from flask import jsonify

def post_prompt_response(data_prompt):
    
    matches_prompt = [i for i in api_data if data_prompt == i['response']]
    return matches_prompt
