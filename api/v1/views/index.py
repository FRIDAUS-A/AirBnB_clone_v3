#!/usr/bin/python3
"""Create views"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


@app_views.route("/status", methods=["GET"])
def status():
    """Status of your API"""
    status = {'status': 'OK'}
    return jsonify(status)


@app_views.route("/stats", methods=["GET"])
def stats():
    """stats of each objects"""
    stat = {}
    objs = {
        "city": City,
        "amenities": Amenity,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User,   
    }
    for key, value in objs.items():
        stat[key] = storage.count(value)
    return jsonify(stat)