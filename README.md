What is this?
==========

Simple python websocket example with Flask, gevent, gevent-websocket, originally described in this [article](http://www.socketubs.net/2012/10/28/Websocket_with_flask_and_gevent/) by [@socketubs](http://github.com/socketubs/), but I add a little improvement, the websocket server will echo your text.

How to?
==========

run `pip install -r requirements.txt` to install requirements, and start the server with `python runserver.py` then browse `http://localhost:8000/` to try out.

To shutdown the server send a request to: `http://localhost:8000/shutdown`


Largely based on https://github.com/tzangms/python-websocket-example.
