import flask
from flask import Flask, jsonify
import json
from flask import request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = flask.jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    request_decodificado = json.loads(request_body)
    print("Incoming request with the following body", request_body)
    if isinstance(request_decodificado, list):
        for i in request_decodificado:
            todos.append(i)
    elif isinstance(request_decodificado, dict):
        todos.append(request_decodificado)
    else: 
        return print("error 400")
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    
    todos.pop(position)
    
    return jsonify(todos)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)