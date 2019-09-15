# -*- coding: utf-8 -*-
# Imports
from flask import Flask, request
import json

app = Flask(__name__)

description =   """
                <!DOCTYPE html>
                <head>
                <title>API Landing</title>
                </head>
                <body>  
                    <h3>A simple API using Flask</h3>
                    <a href="http://localhost:5000/api?value=2">sample request</a>
                </body>
                """




# Routes
@app.route('/', methods=['GET'])
def hello_world():
    # flask prints strings as html rendered in browser
	return description

@app.route('/api', methods=['GET'])
def square():
    if not all(k in request.args for k in (["value"])):
        # but we can also print dynamically 
        # using python f strings with 
        # html elements such as line breaks (<br>)
        error_message =     f"\
                            Required paremeters : 'value'<br>\
                            Supplied paremeters : {[k for k in request.args]}\
                            "
        return error_message
    else:
        # assign and cast variable to int
        value = int(request.args['value'])
        # or use the built in get method and assign a type
        # http://werkzeug.palletsprojects.com/en/0.15.x/datastructures/#werkzeug.datastructures.MultiDict.get
        value = request.args.get('value', type=int)
        return json.dumps({"Value Squared" : value**2})

# these settings will be used/ignore depending 
# on how you run Flask
if __name__ == "__main__":
	app.run(host='0.0.0.0',
            port=1234,
            debug=True)