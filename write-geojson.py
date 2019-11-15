#for more information on sesssion basics and create engine go to: https://docs.sqlalchemy.org/en/13/orm/session_basics.html
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import connect_to_db, db, Campsite, User, Rating, Review, Amenity, CampsiteAmenity
from geojson import Point, Feature, FeatureCollection, dump

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

#Query for geojson data from the campsites db

def get_points(id): #update name to id after testing
    """will return a set of coordinates"""

    campsite = session.query(Campsite).filter_by(campsite_id=id).first()
    lat = campsite.lat
    lon = campsite.lon
    point = Point((lon, lat))

    return point


def get_properties(id):
    """will return campsite title"""

    campsite = session.query(Campsite).filter_by(campsite_id=id).first()
    name = campsite.name
    description = campsite.description

    properties = {"title": name,
                  "description": description}

    return properties



def write_geojson():
    """writes a geojson file using campsites db"""

    i = 1
    features = []

    while i < 5:

        point = get_points(i) 
        properties = get_properties(i)
        features.append(Feature(geometry=point, 
                                properties=properties))

        i += 1

        # add more features...
        # features.append(...)

    feature_collection = FeatureCollection(features)

    # my_feature = Feature(geometry=Point((1.6432, -19.123)))

    # my_other_feature = Feature(geometry=Point((-80.234, -22.532)))

    # feature_collection = FeatureCollection([my_feature, my_other_feature])


    with open('map-markers.geojson', 'w') as f:
       dump(feature_collection, f)





