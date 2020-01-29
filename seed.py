from model import Amenity, User, Campsite, db, connect_to_db, CampsiteAmenity
from faker import Faker
import json
import random

#opening my json object from iOverlander
# I use this to pull information for my campsites
with open('static/json/iOverlander Places - 2019-11-12.json', 'r') as f:
  campsite_dict = json.load(f)

# Need to run first before running load_campsites
def load_amenities():
    """Load amenities from json object"""

    amenity_names = ["Open", 
                     "Electricity", 
                     "Wifi", 
                     "Kitchen", 
                     "Restaurant",
                     "Showers",
                     "Water",
                     "Toilets",
                     "Big Rig Friendly",
                     "Tent Friendly",
                     "Pet Friendly"
                      ]

    for name in amenity_names:
        amenity = Amenity(name=name)
        db.session.add(amenity)

    #     amenities_lookup[name] = amenity

    db.session.commit()


    ###############################################

def load_sample_data():
    """Load a few sample users"""

    user_1 = User(fname="Stephanie",
                  lname="Hicks",
                  email="stephanie22@osborne-hardy.com",
                  password="72hUgLq0T")
    campsite_3 = Campsite(name="Tropical Education Center", 
            lat=17.360490, 
            lon=-88.544600, 
            description="Closest place to stay by the Belize Zoo. Good place to camp, brand new bathrooms with gigantic showers and covered picnic tables. Lots of people stay here in the cabins to do the night tour of the zoo. We went during the day and saw everything but the spider monkeys. Electricity available only in the office.",
            permit=False,
            permit_info=None)
    campsite_3.author = user_1
    db.session.add(campsite_3.author)


    db.session.commit()


################################################################################
def load_campsites():
    """Load campsite info from a json object from iOverlander.com"""

    #setting random variables. User_id randomized and required permit.
    user_id = random.randint(1, 5000)
    permit = random.choice([True, False])

    #looping through json information from iOverlander.com
    for campsite in campsite_dict:

        features = []

        name = campsite['name']
        description = campsite['description']
        lat = campsite['location']['latitude']
        lon = campsite['location']['longitude']

        new_campsite = Campsite(name=name, 
          lat=lat, 
          lon=-lon, 
          description=description,
          permit=permit,
          permit_info=None,
          user_id=user_id)

        db.session.add(new_campsite)

        db.session.commit()

        # #setting up amenity relationship to campsite

        for amenity in campsite['amenities']:
            if campsite['amenities'][amenity] == "Yes":
              features.append(amenity)

        for feature in features:
            feature = Amenity.query.filter_by(name=feature).first()
            new_campsite.amenities.append(feature)


        #features list - now loop over it to get your amenity names to do query 

                #if i print 'amenity' here I get a list of all amenities that are a yes in my json object
                #------------------------------------------------------------------------
                #query to find all objects for amenities where the name is amenity
        #         amenities = Amenity.query.filter(Amenity.name==amenity).all()
        #         #loop through and amenity objects and append the id to new_campsite
        #         for amenity in amenities:
        #             new_campsite.amenities.append(amenity.amenity_id)

        # print(new_campsite.ammenities)
        

    db.session.commit()
################################################################################

def load_users():
  """Load enough users to correspond with the amount of campsites using Faker"""

  user = Faker()
  i=0

  while i < 5000:
      fname = user.first_name()
      lname = user.last_name()
      email = user.email()
      password = user.password()

      new_user = User(fname=fname,
                      lname=lname,
                      email=email,
                      password=password)

      db.session.add(new_user)

      i += 1

  db.session.commit()



################################################################################
if __name__ == "__main__":

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    from server import app

    connect_to_db(app)
    print("Connected to DB.")



