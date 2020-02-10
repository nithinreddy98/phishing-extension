from flask import Flask, render_template,request
from model import phishing_or_not
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
# index
@app.route('/')
def index():
    return "Hello"

@cross_origin
@app.route("/findout",methods=["GET"])
def findout():
    url = request.args.get('url')
    op = phishing_or_not(url)
    print('\n ------------ ' + url + '-- ' + op +' --------------- \n')
    return op

if __name__ == "__main__":
    app.run()