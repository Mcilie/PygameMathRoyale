import flask
from flask import Flask, request
import random

app = Flask(__name__)
newlist = {}

@app.route('/')
def index():
    return """
    <h1> Welcome to the home page of this proto.sh server!</h1> <br>
    <h2>We hope you enjoy your games</h2>
    """

@app.route('/new')
def newGame():
    r = random.randint(0,10000000)
    while (r in newlist):
        r = random.randint(0,10000000)
    newlist[r] = {"ids" : [], "users": {}}
    return str(r)
    
@app.route('/games/<id>/')
def mainGame(id):
    if (int(id) in newlist ):
        return "Welcome to protobowl lobby #{}".format(id)
    else:
        return "GAME NOT FOUND"

@app.route('/games/<id>/join/', methods = ["GET", "POST"])
def joinGame(id):
    if request.method == "POST":
        userName = request.form['name']
        userID  =  request.form['userID']
        if (userID) in newlist[int(id)]["ids"]:
            return: 'HAXXXOR'
        else:
            newlist[int(id)]["ids"].append(userID)
            newlist[int(id)]["users"][userID]["name"] = userName
            newlist[int(id)]["users"][userID]["points"] = 0
            return "LOGGED IN"
    else:
        return "lmfao"
app.run() 