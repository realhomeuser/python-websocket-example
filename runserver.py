#!/usr/bin/env python
# coding: utf-8
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from gevent.event import Event

from app import my_app_wrapper

stopper = Event()

# as suggested by ThiefMaster in:
# http://stackoverflow.com/questions/15932298/how-to-stop-a-flask-server-running-gevent-socketio
# 

if __name__ == '__main__':
    http_server = WSGIServer(('',8000), my_app_wrapper(stopper), handler_class=WebSocketHandler)
    http_server.start()

    try:
        stopper.wait()        
    except KeyboardInterrupt:
        print "" 