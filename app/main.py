from flask import Flask, jsonify,request
from bl.line_notify import SendLineNotify
app = Flask(__name__)


@app.route("/")
def index() -> str:
    return jsonify({"message": "FixxyStudio LineNotifyService"})


@app.route("/sendlinenotify", methods=['GET'])
def SendNoti() -> str:
    
    response = {"message": SendLineNotify('Test From FixxyStudio LineNotifyService')}
    return jsonify(response)
