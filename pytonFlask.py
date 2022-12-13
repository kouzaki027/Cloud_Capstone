from flask import Flask
from flask import Flask,jsonify,request
import datetime;

app = Flask(__name__)

@app.route("/")
def hello():
  return "Welcome to the Python Flask!"

ct = datetime.datetime.now()
L = [str(ct), "\n"]
file = open("timestampText.txt", "w")
file.writelines(L)
file.close()

@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "Class" : 298,
            "Subject" : "Introduction to Cloud Computing",
        }

        return jsonify(data)

if __name__ == '__main__':
     app.run (host="0.0.0.0", port=8080)
