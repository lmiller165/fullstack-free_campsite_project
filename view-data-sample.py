# import json
# from faker import Faker


from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model import connect_to_db, db, Campsite, User, Rating, Review, Amenity, CampsiteAmenity

engine = create_engine('postgresql:///campsites')
session = Session(engine)

campsites = session.query(Campsite).first()
print(campsites)
session.close()

# Helper functions

# def connect_to_db(app):
#     """Connect the database to our Flask app."""

#     # Configure to use our PostgreSQL database
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///campsites'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SQLALCHEMY_ECHO'] = True
#     db.app = app
#     db.init_app(app)


#####################################################################
#Query test:




# feature = Amenity.query.filter_by(name='Pet Friendly').first()
# print(feature)

#####################################################################

# def load_campsite_json():

#     with open('iOverlander Places - 2019-11-12.json', 'r') as f:
#         campsite_dict = json.load(f)

#     return campsite_dict


# def general_info():
#     """save campsite name, description, lat, lon"""

#     load_campsite_json()
    
#     for campsite in campsite_dict:

#         name = campsite['name']
#         description = campsite['description']
#         lat = campsite['location']['latitude']
#         lon = campsite['location']['longitude']

#     return name, description, lat, lon


# def amenity_list():
#     """save amenities where amenity value is a yes"""

#     load_campsite_json()

#     for campsite in campsite_dict:

#         features = []
#         amenities = campsite['amenities']

#         for amenity in amenities:
#             print(amenity)
#             if amenity == "Yes":
#               features.append(amenity)


#     for feature in features:
#         print(feature)

##################################################################### 

#reading json object
# with open('iOverlander Places - 2019-11-12.json', 'r') as f:
#     campsite_dict = json.load(f)

#####################################################################  
#printing into json file
# for campsite in campsite_dict:

#     features = []

#     name = campsite['name']
#     description = campsite['description']
#     lat = campsite['location']['latitude']
#     lon = campsite['location']['longitude']

#     for amenity in campsite['amenities']:
#         if campsite['amenities'][amenity] == "Yes":
#           features.append(amenity)

#     for feature in features:
#         print(feature)

# print(name)
# print(description)
# print(lat)
# print(lon)
# print(features)

# for campsite in campsite_dict:
#     print(campsite)
#     print("###########################################")

#####################################################################
#testing adding just amenity

# for campsite in campsite_dict:
#     for amenity in campsite['amenities']:
#         print(amenity)

# for campsite in campsite_dict:
#     if campsite['id'] == "115683":
#         print(campsite)

#####################################################################
#getting amenity to print only if it is a yes. 
#I will append this to my relationship table:

#nice print out
# for campsite in campsite_dict:
#     print(campsite['name'])
#     amenities = campsite['amenities']
#     print(amenities)
#     for amenity in campsite['amenities']:
#         if campsite['amenities'][amenity] == "Yes":
#             print(amenity)
#     print("###########################################")

# #needed data
# for campsite in campsite_dict:
#     amenities = campsite['amenities']
#     for amenity in campsite['amenities']:
#         if campsite['amenities'][amenity] == "Yes":
#             print(amenity)


#####################################################################
#identifying the value of different variables:

    # if campsite['category'] == "Informal Campsite":
    #     print(campsite['name'])
    #     print(campsite['description'])
    #     print(campsite['location']['latitude'])
    #     print(campsite['location']['longitude'])
    #     print(campsite['country'])
    #     print(campsite['category'])

#####################################################################
#using faker to populate my data:

# user = Faker()
# i = 0

# while i < 20:
#     print(user.first_name())
#     print(user.last_name())
#     print(user.email())
#     print(user.password())

#     i+=1
