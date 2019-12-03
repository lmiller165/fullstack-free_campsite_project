#for more information on sesssion basics and create engine go to: https://docs.sqlalchemy.org/en/13/orm/session_basics.html
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import connect_to_db, db, Campsite, User, Rating, Review, Amenity, CampsiteAmenity
from geojson import Point, Feature, FeatureCollection, dump
import requests
from mapbox import Geocoder
import config
import pygeoj


#connect to my db to allow for queries
engine = create_engine('postgresql:///campsites')
session = Session(engine)

################################################################################
#Global variables

TOKEN = config.mapbox_access_token

################################################################################


def get_place_info(camp_id):
    """retrieves state from campsite coordinates"""

    #query into db to pull campsite info. 
    campsite = session.query(Campsite).filter_by(campsite_id=camp_id).first()
    lon = str(campsite.lon * -1)
    lat = str(campsite.lat)
    #Mapbox api request to get state
    response = requests.get('https://api.mapbox.com/geocoding/v5/mapbox.places/' + lon + ',' + lat + '.json?access_token=' + TOKEN)
    #turn object into json
    response_json  = response.json()
    #indexing into geojson object from mapbox: 45/500 are incorrect. 
    place_info = response_json['features'][1]['place_name']
    place_info = place_info.split(', ')

    return place_info


def get_state(camp_id):
    """retrieves state from campsite coordinates"""

    #need to update to retrieve cleaner data by building out more conditionals
    #to handle varied outputs by mapbox.
    place_info = get_place_info(camp_id)
    # print(place_info)
    # print(type(place_info))

    if len(place_info) < 2:
        state = "United States"
    else:
        state = place_info[1]
        state = state.split()
        state = state[0]

    return state


def get_city(camp_id):
    """retrieves city from campsite coordinates"""

    place_info = get_place_info(camp_id)
    city = place_info[0]

    return city


def get_country(camp_id):
    """retrieves city from campsite coordinates"""

    place_info = get_place_info(camp_id)
    country = place_info[2]

    return country


def get_zipcode(camp_id):
    """retrieves state from campsite coordinates"""

    place_info = get_place_info(camp_id)

    if len(place_info) < 2:
        zipcode = None

    else:
        zipcode = place_info[1]
        zipcode = zipcode.split()   
        zipcode = zipcode[0]

    # print("city:", place_info[0])
    # print("State & Zip:", place_info[1])
    # print("Country:", place_info[2])

    return zipcode


################################################################################
#tester function delete later: 

# def get_state_all():
#     """used to test how many states were returned as united states"""

#     i = 1
#     united_states = []
#     info_error = []

#     while i <= 500:
#         # i is campsite id here:
#         place_info = get_zipcode(i) 
#         # if state == "United States":
#         #     united_states.append("United States")
#         print(place_info)

#         if len(place_info) > 3:
#             info_error.append("error")
        
#         print("num of errors:", len(info_error))

#         i += 1


