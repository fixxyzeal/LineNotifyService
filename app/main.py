from flask import Flask, jsonify, request
from bl.line_notify import SendLineNotify
from bl.set_web_scraper import GetSetData
app = Flask(__name__)


@app.route("/")
def index() -> str:
    return jsonify({"message": "FixxyStudio LineNotifyService"})


@app.route("/sendlinenotify", methods=['GET'])
def SendNotify() -> str:

    response = {"message": SendLineNotify(
        'Test From FixxyStudio LineNotifyService')}
    return jsonify(response)


@app.route("/sendstocknotify", methods=['GET'])
def SendStockNotify() -> str:
    sendlist = ['ptt','cpf','tisco','scc','scgp']
    msg = GetSetData(sendlist)
    print(msg)
    response = {"message": SendLineNotify(msg)}
    return jsonify(response)
