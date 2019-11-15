#for more information on sesssion basics and create engine go to: https://docs.sqlalchemy.org/en/13/orm/session_basics.html
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

#Query for geojson data from the db "campsites"

def get_points(name):
    """will return a set of coordinates"""

    campsite = session.query(Campsite).filter_by(name=name).first()
    lat = campsite.lat
    lon = campsite.lon
    point = Point((lat, lon))
    print(point)

    return point


point = Point((-115.81, 37.24))


features = []
features.append(Feature(geometry=point, properties={"country": "Spain"}))

# add more features...
# features.append(...)

feature_collection = FeatureCollection(features)


#write file with campsites
# with open('myfile.geojson', 'w') as f:
#    dump(feature_collection, f)





