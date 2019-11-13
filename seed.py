from model import Amenity, User, Campsite, db, connect_to_db
from faker import Faker
import json
import random

#opening my json object from iOverlander:
with open('iOverlander Places - 2019-11-12.json', 'r') as f:
  campsite_dict = json.load(f)

def load_amenities():
    """Load amenities from json object"""

###############################################################################
    #I attempted to add amenities from json object. It add but it adds the same 
    #amenities over and over for each campsite. Work on later. 

    # for campsite in campsite_dict:
    #     for amenity in campsite['amenities'][amenity]:

    #         amenity = Amenity(name=amenity)
    #         db.session.add(amenity)

    # amenities_lookup = {}

###############################################################################

    amenity_names = ["Open", 
                     "Electricity", 
                     "Wifi", 
                     "Kitchen", 
                     "Restaurant",
                     "Showers",
                     "Water",
                     "Toilets",
                     "Big Rig friendly",
                     "Tent Friendly",
                     "Pet Friendly"
                      ]

    for name in amenity_names:
        amenity = Amenity(name=name)
        db.session.add(amenity)

    #     amenities_lookup[name] = amenity

    db.session.commit()


    ###############################################

# def load_sample_data():
#     """Load a few sample users"""

#     user_1 = User(fname="Stephanie",
#                   lname="Hicks",
#                   email="stephanie22@osborne-hardy.com",
#                   password="72hUgLq0T")
#     campsite_3 = Campsite(name="Tropical Education Center", 
#             lat=17.360490, 
#             lon=-88.544600, 
#             description="Closest place to stay by the Belize Zoo. Good place to camp, brand new bathrooms with gigantic showers and covered picnic tables. Lots of people stay here in the cabins to do the night tour of the zoo. We went during the day and saw everything but the spider monkeys. Electricity available only in the office.",
#             permit=False,
#             permit_info=None)
#     campsite_3.author = user_1
#     db.session.add(campsite_3.author)



#     user_2 = User(fname="Daniel",
#               lname="Harris",
#               email="daniel22@gmail.com",
#               password="%6Khz$v3%")
#     campsite_2 = Campsite(name="Sandy Lane", 
#                 lat=17.744617,
#                 lon=-88.024617, 
#                 description="Very basic. Shared bathrooms but awesome hot showers. There was a place to grill and covered picnic tables outside, but no kitchen. Probably the cheapest place to stay on Caye Caulker if you don’t have a tent and don’t want to stay in a noisy hostel dorm. Ask the groundskeeper named Moses about conch ceviche.",
#                 permit=True,
#                 permit_info="You'll need a permit")
#     campsite_2.author = user_2



#     user_3 = User(fname="Ryan",
#                   lname="Harvey",
#                   email="ryan97@stanley.net",
#                   password="_z1TR4n")
#     campsite_1 = Campsite(name="Backpacker’s Paradise", 
#                           lat=18.344800, 
#                           lon=-88.152880, 
#                           description="Excellent mosquito-screened common area with tables, hammocks, power and a kitchen. Super friendly owners. Wifi in the restaurant and common areas. There is a dedicated modem in the common area/kitchen. Horses roam around free on the campground, its a unique experience to connect with those awesome animals.",
#                           permit=False,
#                           permit_info=None)
#     campsite_1.author = user_3

#     campsite.append
#     campsite_1.amenities.append(amenities_lookup["Electricity"])
#     campsite_1.amenities.append(amenities_lookup["Wifi"])



#     db.session.add(user_1)
#     db.session.add(campsite_1)
#     db.session.add(user_2)
#     db.session.add(campsite_2)
#     db.session.add(user_3)
#     db.session.add(campsite_3)


#     db.session.commit()


################################################################################
def load_campsites():
    """Load campsite info from a json object from iOverlander.com"""

    #setting random variables. User_id randomized and required permit.
    user_id = random.randint(1, 6000)
    permit = random.choice([True, False])

    #looping through json information from iOverlander.com
    for campsite in campsite_dict:
      campsite = campsite
      name = campsite['name']
      description = campsite['description']
      lat = campsite['location']['latitude']
      lon = campsite['location']['longitude']

      new_campsite = Campsite(name=name, 
        lat=lat, 
        lon=-lon, 
        description=description,
        permit=permit,
        permit_info=None)
        # user_id=user_id)

      db.session.add(new_campsite)


    # #append ammenities to campsite
    # amenities = request.form.getlist("amenities")
    # for amenity_id in amenities:

    #     amenity = Amenity.query.get(int(amenity_id))
    #     new_campsite.amenities.append(amenity)

    #setting up amenity relationship for campsites:
    for campsite in campsite_dict:
        amenities = campsite['amenities']
        for amenity in campsite['amenities']:
            if campsite['amenities'][amenity] == "Yes":
                #if i print amenity here I will get a list of all amenities that
                #are a yes in my json object
                #---------------------------
                #setting amenities equal to a query where the amenity is equal to amenity
                amenities = Amenity.query.filter(Amenity.name==amenity).all()

                for amenity in amenities:
                    amenity = amenity.amenity_id
                    new_campsite.amenities.append(amenity)

      #add campsite country: campsite['country']
      #add campsite category: campsite['category']
      #add campsite price: campsite['price']

    db.session.commit()


################################################################################
if __name__ == "__main__":

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    from server import app

    connect_to_db(app)
    print("Connected to DB.")



