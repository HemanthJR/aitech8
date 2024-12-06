from flask import Flask, jsonify, request
from data import api_data
from title_view import post_response
from blog_view import post_id_response
from common_view import post_prompt_response
import requests

app = Flask(__name__)

#basic route for testing
@app.route('/')
def home():
    return jsonify({"message":"hola coders"})

#fetching data from api and displaying
@app.route('/api/response', methods = ['GET'])
def view_response():
    return jsonify(api_data)


@app.route('/api/response', methods = ['POST'])
def post_view_response():
    data = request.json
    print(data)
    data_title = data.get('title')
    # data_id = data.get('id')
    data_prompt = data.get('prompt')
    #if there request is empty or no request
    if not data:
        return jsonify({"message": "No request Found"}), 404
    
    
    if not data_title:
        #common response
        matching_prompt = post_prompt_response(data_prompt)
        print(matching_prompt)
        # prompt_response = matching_prompt[0]['response']
        # prompt_title = matching_prompt[0]['title']
        prompt_result = []
        # title_list = ['book title', "blog post", "BISAC"]
        if matching_prompt:
            for i in matching_prompt:
                prompt_result.append({"response": i['response'], 'title': i['title']})
            return jsonify(prompt_result), 200
        else:
            return jsonify({"message": "prompt was not proper"}), 404
            
        # #id or blog response
        # matching_id = post_id_response(data_id)
        # if matching_id:
        #     return jsonify({"id": matching_id[0]['id'],"response": matching_id[0]['body']}), 200
        # else:
        #     return jsonify({"message": "No record found to this Id"}), 404

        # return jsonify({"message":"no title found"}), 404

    #title or book title response
    print(data_title)
    matching_data = post_response(data_title)
    if matching_data:
        return jsonify({"title": matching_data[0]['title'],"response": matching_data[0]['response']}), 200
    else:
        return jsonify({"message": "No matching title"}), 404  
    
    

if __name__ == "__main__":
    app.run(debug=True)
    