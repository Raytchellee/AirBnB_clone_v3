#!/usr/bin/python3
"""
Creates a route that returns a JSON
"""


from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route("/status", strict_slashes=False)
def status_check():
    """
    Sends okay status
    """
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def ret_type():
    """
    Rturns count of objects grouped by type
    """
    return jsonify({
        'users': storage.count('User'),
        'cities': storage.count('City'),
        'states': storage.count('State'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'amenities': storage.count('Amenity')
    })
