from flask import Flask, render_template, flash, redirect, url_for, request
from flask_socketio import SocketIO
import os, math, shutil, sqlite3, unicodedata, re, json, subprocess, shlex, time
import subprocess
from gevent.subprocess import Popen, DEVNULL, STDOUT
from threading import Timer


app = Flask(__name__)
app.config['SECRET_KEY'] = ('This is a secret key')
socketio = SocketIO(app)


@app.route('/')
def begin():
    return redirect(url_for('sockets'))

@app.route('/login', methods = ['GET', 'POST'])
def login():

    if request.method == "POST":
        details = request.form;
        firstName = str(details['firstname'])
        lastName = str(details['lastname'])
        print("First name is: " + firstName)

        if(firstName == "test"):
            return redirect(url_for('sockets'))
    return render_template('login.html')

@app.route('/sockets', methods = ['GET', 'POST'])
def sockets():
    return render_template('sockets.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    #app.run()
    socketio.run(app, host='0.0.0.0', port=5000, debug = True)