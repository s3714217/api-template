from flask_restful import Resource
from flask import *
class GetExample(Resource):
    def get(self,message):
        message = {
        "response" : 
            {
            "state" : "SUCCESS",
            "message" : message
            }
        }
        return message

class PostExample(Resource):
   def post(self):
        message = {
        "response" : 
            {
            "state" : "SUCCESS",
            "date received": request.json
            }
        }
        return message
    