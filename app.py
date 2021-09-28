from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from werkzeug.wrappers import response

app = Flask(__name__)

api = Api(app)

CORS(app)

identitas = {}

class ContohResource(Resource):
    def get(self):
        # response = {"msg" : "Restfulku"}
        return identitas
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg" : "Data berhasil masuk"}
        return response

api.add_resource(ContohResource, "/api", methods = ['GET',"POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)