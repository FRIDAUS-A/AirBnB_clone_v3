#!/usr/bin/python3
"""Create views"""
from api.v1.views import app_views
from flask import jsonify 


@app_views.route("/status", methods=["GET"])
def status():
    """Status of your API"""
    status = {'status': 'OK'}
    return jsonify(status)