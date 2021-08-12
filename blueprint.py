from flask import Blueprint, render_template, request
from math import cos, asin, sqrt, pi
import requests

blueprint = Blueprint("blueprint", __name__,
                      static_folder="static", template_folder="templates")


# The Haversine Formula determines the great-circle distance between two points on a sphere given their latitudes and longitudes.
# To calculate the distance of any point to the Moscow Ring Road, an average radius of 20kms has been determined for the ring and
# this radius is redacted from the distance to the central Moscow to find the approximate distance to the closest point of the road itself from the input location.
def haversine(lat1, lon1):
    moscow_lat = 55.75322
    moscow_long = 37.622513
    p = pi/180
    a = 0.5 - cos((moscow_lat-lat1)*p)/2 + cos(lat1*p) * \
        cos(moscow_lat*p) * (1-cos((moscow_long-lon1)*p))/2
    d = 12742 * asin(sqrt(a))
    return d-20


# This function calls the API and returns the location data as a list from the JSON object.
def api_call(add=None):
    API_key = "1370b8e6-1bc9-4c29-a6c8-51c5dbf4d35c"
    add = add if add is not None else request.form['address']
    r = requests.get("https://geocode-maps.yandex.ru/1.x/?format=json&apikey=" +
                     API_key+"&lang=en_us&geocode="+add)
    json_object = r.json()
    # Check if any results were found from the input address.
    if json_object['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found'] != "0":
        latlong = json_object['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        return latlong
    else:
        raise ValueError("Please check your spelling.")


@blueprint.route("/")
def home():
    return render_template("index.html")


@blueprint.route("/distance_from_mkad", methods=['POST'])
def distance_calculator():

    latlong = api_call()
    # Yandex shares geo position as Long-Lat, so after the split operation values are fixed to a Lat-Long format.
    lat = float(latlong[1])
    long = float(latlong[0])
    total_distance = haversine(lat, long) - 20
    # If the calculated distance is smaller than 0, that means the input address is inside the Moscow Ring Road, hence per the instructions, should not be shared with the user.
    if total_distance <= 0:
        return render_template("inside_mkad.html")
    else:
        return render_template("distance_from_mkad.html", total_distance=total_distance)
