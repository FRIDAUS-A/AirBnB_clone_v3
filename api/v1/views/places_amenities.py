#!/usr/bin/python3

from flask import Flask
from models.place import Place
from models.amenity import Amenity


@app.route("/places/<place_id>/amenities", strict_slashes=False, methods=["GET"])
@app.route("/places/<place_id>/amenities/<amenity_id>", strict_slashes=False, methods=["DELETE", "POST"])
def place_amenity(place_id=None, amenity_id=None):
    if place_id:
        if request.method == "GET":
            place = storage.get(Place, place_id)
            if not place:
                response = jsonify({"error": "Not found"})
                response.staus_code = 404
                return response
            else:
                allAmenity = []
                amenities = place.amenities
                for amenity in amenities.values():
                    allAmenity.append(amenity.to_dict())
                return jsonify(allAmenity)
    if amenity_id:
        if request.method == "DELETE":
            place = storage.get(Place, place_id)
            if not place:
                response = jsonify({"error": "Not found"})
                response.staus_code = 404
                return response
            amenity = storage.get(Amenity, amenity_id)
            if not amenity:
                response = jsonify({"error": "Not found"})
                response.staus_code = 404
                return response
            placeAmenity_id = amenity.place_id
            placeAmenity = storage.get(Place, placeAmenity_id)
            if not placeAmenity:
                response = jsonify({"error": "Not found"})
                response.staus_code = 404
                return response
            storage.delete(amenity)
            storage.save()
            return jsonify({})
        if request.method == "POST":
            place = storage.get(Place, place_id)
            if not place:
                response = jsonify({"error": "Not found"})
                response.staus_code = 404
                return response
            amenity = storage.get(Amenity, amenity_id)
            if not amenity:
                response = jsonify({"error": "Not found"})
                response.staus_code = 404
                return response
            placeAmenity_id = amenity.place_id
            placeAmenity = storage.get(Place, placeAmenity_id)
            if placeAmenity:
                response = jsonify(amenity.to_dict())
                response.status_code = 201
                return response
            else:
                amenityDict = amenity.to_dict()
                amenityDict['place_id'] = place.place_id
                storage.delete(amenity)
                storage.save()
                amenity = Amenity(**amenityDict)
                storage.new(amenity)
                amenity.save()
                amenity = storage.get(Amenity, amenity_id)
                response = amenity.to_dict()
                response.status_code = 201
                return jsonify(response)
