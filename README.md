# distance-to-MKAD-flaskapp
This Flask application calculates the distance to Moscow Ring Road from any given address using geolocation provided by Yandex Geocoder API. The calculations are based on the Haversine Great-Circle Distance Formulas and are approximations. Calculated distance is based on the closest point of the road from the given location and not a fixed location on the road. Any input address that is inside the Moscow Ring Road does not get shared, instead another message is given stating that the given address is located inside the ring road.

The project contains a Flask Blueprint and a main Flask application setup to run it. To use the application, simply run the app on your local host or visit the deployed version at https://mkad-distance.herokuapp.com/ . 

All functions and algorithms are explained with comments inside the files.
