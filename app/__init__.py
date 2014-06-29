# coding: utf-8
import os

from flask import Flask
from websocket import handle_websocket

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.debug = True


def my_app_wrapper(stopperEvent=None):
    def my_app(environ, start_response):  
        path = environ["PATH_INFO"]  
        if path == "/":  
            return app(environ, start_response)  
        elif path == "/websocket":  
            handle_websocket(environ["wsgi.websocket"])  
        elif path =='/shutdown': #handle shutdown request
            if stopperEvent:
                stopperEvent.set() #activates the event
            return app(environ, start_response)  
        else:  
            return app(environ, start_response)  
    return my_app

import views
