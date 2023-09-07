from flask import Flask, request, jsonify
from flask import *

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    skills = request.args.get('skills')
    
    if skills:
       
        users = [
            {"first_name": "John", "last_name": "Joseph", "skill": "Python"},
            {"first_name": "Jane", "last_name": "Smith", "skill": "JavaScript"},
        ]
        
        result = [
            f"{user['first_name']} {user['last_name']} has skill {user['skill']}"
            for user in users
        ]
        
        return jsonify(result)
    else:
        return jsonify({"error": "Please enter at least one skill"})

if __name__ == '__main__':
    app.run(debug=True)