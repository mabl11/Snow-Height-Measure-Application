from flask import Flask
from request_handler import CRequestHandler
from http import HTTPStatus

SnowDepthApp = Flask(__name__)
req_handler = CRequestHandler()

@SnowDepthApp.route("/snowbla/snowdata/<rep>", methods=['GET'])
def snow_depth(rep):
    try: 
        data = req_handler.get_timed_snow_depth(rep)
        return data, HTTPStatus.OK

    except Exception:
        return "error occured during measurement", HTTPStatus.NO_CONTENT

@SnowDepthApp.route("/snowbla/reference/", methods=['GET'])
def get_reference():
    try:
        ref = req_handler.get_reference()
        return ref, HTTPStatus.OK

    except Exception:
        return "not able ro read reference", HTTPStatus.NO_CONTENT
        

@SnowDepthApp.route("/snowbla/reference/", methods=['POST'])
def new_reference():
    try:
        new_ref = req_handler.new_reference()
        return new_ref, HTTPStatus.OK
    
    except Exception:
        return "not able to create a new reference", HTTPStatus.NO_CONTENT
        

@SnowDepthApp.route("/snowbla/reference/", methods=['DELETE'])
def delete_reference():
    try:
        old_ref = req_handler.delete_reference()
        return "reference deleted successfully", old_ref, HTTPStatus.OK

    except Exception:
        return "unable to locate and delete reference", HTTPStatus.NO_CONTENT

if __name__ == '__main__':
    """Run server on IP (0.0.0.0) at port 5000, with debug enabled"""
    
    SnowDepthApp.run(host="0.0.0.0", port="5000", debug=True)
  