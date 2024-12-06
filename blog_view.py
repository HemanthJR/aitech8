from data import api_data
from flask import jsonify

def post_id_response(data_id):
    
    matches_id = [i for i in api_data if data_id == i['id']]
    return matches_id
