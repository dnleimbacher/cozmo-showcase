#!/usr/bin/env python3
from flask import Flask
from flask import request
from observable import Observable
app = Flask(__name__)
_obs = None

@app.route('/drive', methods=['GET'])
def index():
    dist = request.args.get('dist')
    webhook = request.args.get('webhook')
    print("dist: ", dist)
    print("webhook: ", webhook)
    _obs.trigger("drive", dist, webhook)
    return "ok"

@app.route("/turn", methods=['GET'])
def index_turn():
    angle = request.args.get('angle')
    webhook = request.args.get('webhook')
    print("angle: ", angle)
    print("webhook: ", webhook)
    _obs.trigger("turn", int(float(angle)), webhook)
    return "ok"

@app.route("/greet", methods=['GET'])
def index_greet():
    greeting = request.args.get('greeting')
    webhook = request.args.get('webhook')
    print("text: ", greeting)
    print("webhook: ", webhook)
    _obs.trigger("greet", greeting , webhook)
    return "ok"

@app.route('/speak', methods=['GET'])
def speak():
    text = request.args.get('text')
    webhook = request.args.get('webhook')
    print("text: ", text)
    print("webhook: ", webhook)
    _obs.trigger("speak", text, webhook)
    return "ok"

@app.route('/command/<string:command>/<string:argument>', methods=['GET'])
def command1(command, argument):
    _obs.trigger("command1", command, argument)
    return "ok"

@app.route('/command/<string:command>/<string:argument1>/<string:argument2>', methods=['GET'])
def command2(command, argument1, argument2):
    _obs.trigger("command2", command, argument1, argument2)
    return "ok"

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return "Server shutting down..."

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

def run(obs: Observable):
    global _obs
    _obs = obs
    _obs.trigger("init", "Init Web")
    app.run(debug=False)
    print("Web stopped!!!")
