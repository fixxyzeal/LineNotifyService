from logging import fatal
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from bl.user import Authenticate
from bl.line_notify import SendLineNotify
from bl.set_web_scraper import GetSetData
app = Flask(__name__)
auth = HTTPBasicAuth()



@auth.verify_password
def verify_password(username, password):
    res = Authenticate(username,password)
    if not res:
        return False
    return True

@app.route("/")
def index() -> str:
    return jsonify({"message": "FixxyStudio LineNotifyService"})


@app.route("/sendlinenotify", methods=['POST'])
def SendNotify() -> str:

    response = {"message": SendLineNotify(
        'Test From FixxyStudio LineNotifyService')}
    return jsonify(response)


@app.route("/sendstocknotify", methods=['POST'])
@auth.login_required
def SendStockNotify() -> str:
    sendlist = ['or','amanah','makro','scc','scgp','true','spvi']
    msg = GetSetData(sendlist)
    print(msg)
    response = {"message": SendLineNotify(msg)}
    return jsonify(response)