from flask import *
from flask_restful import Api
from datetime import datetime
from resources.example import *
import requests

app = Flask(__name__)
api = Api(app)

#api.add_resource(GetExample, "/get/message=<string:message>")
#api.add_resource(PostExample, "/post")

@app.route('/post', methods=['POST'])
def post_task():
  message = {
    "reponse":
    {
      "state" : "SUCCESS",
      "date received": request.json
    }
  }
  return message

@app.route('/get/message=<string:message>', methods=['GET'])
def get_task(message):
 
  message = {
    "response" : 
      {
        "state" : "SUCCESS",
        "message" : message
      }
    }
  return message

if __name__ == "__main__":
  app.run(debug=True)