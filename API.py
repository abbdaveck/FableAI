from flask import Flask, request
from flask_restful import Resource, Api
import requests, time, json, os

app = Flask(__name__)
api = Api(app)

if os.environ['COMPUTERNAME'] == "HOME":
    testpath = r"C:\Users\david\OneDrive - ABB Industrigymnasium\Teknik\VT 20\Create your own story\communication.txt"
    changepath = r"C:\Users\david\OneDrive - ABB Industrigymnasium\Teknik\VT 20\Create your own story\change.txt"
else:
    testpath = r"C:\Users\S8daveck\OneDrive\OneDrive - ABB Industrigymnasium\Teknik\VT 20\Create your own story\communication.txt"
    changepath = r"C:\Users\S8daveck\OneDrive\OneDrive - ABB Industrigymnasium\Teknik\VT 20\Create your own story\change.txt"


class myAPI(Resource):

    def post(self):
        inp = request.get_json(force = True)
        with open(testpath, 'w') as file:
            file.write(json.dumps(inp)) # use `json.loads` to do the reverse
        print(inp)
        with open(changepath, 'w') as file:
            file.write(json.dumps(False)) # use `json.loads` to do the reverse
        return "success"

        
    def get(self):
        change = open(changepath, 'r')
        readchange = change.read()
        change.close()
        
        if readchange == "true":
            get = open(testpath, 'r')
            read = get.read()
            re = json.loads(read)
            get.close()
            story = re['story']
            return story
        else:
            return False


api.add_resource(myAPI, "/")

if __name__ == "__main__":
    app.run(debug=True)