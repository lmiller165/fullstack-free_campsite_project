#for more information on sesssion basics and create engine go to: https://docs.sqlalchemy.org/en/13/orm/session_basics.html
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import connect_to_db, db, Campsite, User, Rating, Review, Amenity, CampsiteAmenity
from geojson import Point, Feature, FeatureCollection, dump
from mapbox_requests import get_state, get_zipcode, get_city, get_country

#connect to my db to allow for queries
engine = create_engine('postgresql:///campsites')
session = Session(engine)

################################################################################

#Testing db connection and simple queries
def test_basic_query():
    campsites = session.query(Campsite).first()
    print(campsites)
    print(campsites.name)
    #closing my session in every funtion: ask if this is neccesssary.
    session.close()

def test_filterby_name():
    campsite1 = session.query(Campsite).filter_by(name='Anza Borrego - NICE').first()
    print(campsite1)
    #closing my session in every funtion: ask if this is neccesssary.
    session.close()

################################################################################

#Queries for geojson data from the campsites db
def get_points(camp_id): #update name to id after testing
    """will return a set of coordinates"""

    campsite = session.query(Campsite).filter_by(campsite_id=camp_id).first()
    lat = campsite.lat
    lon = campsite.lon
    if lon > 0:
        lon = lon * -1
    point = Point((lon, lat))
    session.close()

    return point


def get_coordinates(camp_id): #update name to id after testing
    """will return a set of coordinates"""

    campsite = session.query(Campsite).filter_by(campsite_id=camp_id).first()
    lat = campsite.lat
    lon = campsite.lon
    if lon > 0:
        lon = lon * -1
    coordinates = [lon, lat]
    session.close()

    return coordinates


def get_properties(camp_id):
    """will return campsite title"""


    campsite = session.query(Campsite).filter_by(campsite_id=camp_id).first()
    name = campsite.name
    description = campsite.description

    #Implement these

    # state = get_state(camp_id)
    # zipcode = get_zipcode(camp_id)
    # city = get_city(camp_id)

    properties = {'title': name,
                  'description': description,
                  'state' : state,
                  'zipcod' : zipcode
                  #add city maybe
                  }

    session.close()

    return properties


def get_total_campsites():
    """Finds total count of campsites entered in my db"""

    total = session.query(Campsite).count()
    session.close()

    return total

################################################################################
#Write a geojson file using my db queries
def write_geojson():
    """writes a geojson file using campsites db"""

    i = 1
    total = get_total_campsites()
    features = []

    while i <= 500:
        # i is campsite id here:
        point = get_points(i) 
        # i is campsite id here:
        properties = get_properties(i)

        #!!add get coordinates function here

        features.append(Feature(geometry=point, 
                                properties=properties))

        #add get_info_by_coordinates

        i += 1

        # if you want to add more features do it here. Look up geojson and mapbox for more into.
        # add more features...
        # features.append(...)

    feature_collection = FeatureCollection(features)
    # my_feature = Feature(geometry=Point((1.6432, -19.123)))
    # my_other_feature = Feature(geometry=Point((-80.234, -22.532)))
    # feature_collection = FeatureCollection([my_feature, my_other_feature])

    with open('static/json/all_campsites.geojson', 'w') as f:
       dump(feature_collection, f)


def read_geojson():
    """Reads geoson file"""

    with open('static/json/all_campsites.geojson', 'r') as f:
        geojson = f.read()
    
    geojson = json.loads(geojson)
    # print(type(geojson))

    return geojson




