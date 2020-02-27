#!/usr/bin/python3
"""
Web server 
"""
# Add by JFK from ABNB v4.
from api.v1.views import app_views
from flask import Flask, jsonify, make_response, render_template, url_for
from flask_cors import CORS, cross_origin
from flasgger import Swagger
import os
from werkzeug.exceptions import HTTPException


# from api.v1.views import app_views
# from flask import Flask, jsonify, make_response
# from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.register_blueprint(app_views)

# Cross-Origin Resource Sharing. Added by JFK
cors = CORS(app, resources={r'/api/v1/*': {'origins': '*'}})

# @app.route("/api/v1/views")
# def status():
#     index.py

@app.errorhandler(404)
def not_found(error):
    """ json 404 page """
    return make_response(jsonify({"error": "Not found"}), 404)


# Added by JFK from ABNB v4.
# @app.errorhandler(Exception)
# def global_error_handler(err):
#     """
#         Global Route to handle All Error Status Codes
#     """
#     if isinstance(err, HTTPException):
#         if type(err).__name__ == 'NotFound':
#             err.description = "Not found"
#         message = {'error': err.description}
#         code = err.code
#     else:
#         message = {'error': err}
#         code = 500
#     return make_response(jsonify(message), code)


# def setup_global_errors():
#     """
#     This updates HTTPException Class with custom error function
#     """
#     for cls in HTTPException.__subclasses__():
#         app.register_error_handler(cls, global_error_handler)


# if __name__ == "__main__":
#     """
#     MAIN Flask App
#     """
#     # initializes global error handling
#     setup_global_errors()
#     # start Flask app
#     app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    # python -m api.v1.app 
    app.run(host="0.0.0.0", port=5000)
