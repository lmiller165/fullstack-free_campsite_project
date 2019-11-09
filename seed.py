from model import Amenity, User, Campsite, db, connect_to_db
from faker import Faker

def load_amenities():
    """Load amenities"""

    amenities_lookup = {}

    amenity_names = ["Electricity", 
                     "Wifi", 
                     "Showers", 
                     "Water", 
                     "Toilets",
                     "Pet Friendly",
                     "Tent Friendly"
                      ]

    for name in amenity_names:
        amenity = Amenity(name=name)
        db.session.add(amenity)

        amenities_lookup[name] = amenity

    db.session.commit()

    ###############################################

    #append ammenities to campsite
    amenities = request.form.getlist("amenities")
    for amenity_id in amenities:

        amenity = Amenity.query.get(int(amenity_id))
        new_campsite.amenities.append(amenity)

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



    user_2 = User(fname="Daniel",
              lname="Harris",
              email="daniel22@gmail.com",
              password="%6Khz$v3%")
    campsite_2 = Campsite(name="Sandy Lane", 
                lat=17.744617,
                lon=-88.024617, 
                description="Very basic. Shared bathrooms but awesome hot showers. There was a place to grill and covered picnic tables outside, but no kitchen. Probably the cheapest place to stay on Caye Caulker if you don’t have a tent and don’t want to stay in a noisy hostel dorm. Ask the groundskeeper named Moses about conch ceviche.",
                permit=True,
                permit_info="You'll need a permit")
    campsite_2.author = user_2



    user_3 = User(fname="Ryan",
                  lname="Harvey",
                  email="ryan97@stanley.net",
                  password="_z1TR4n")
    campsite_1 = Campsite(name="Backpacker’s Paradise", 
                          lat=18.344800, 
                          lon=-88.152880, 
                          description="Excellent mosquito-screened common area with tables, hammocks, power and a kitchen. Super friendly owners. Wifi in the restaurant and common areas. There is a dedicated modem in the common area/kitchen. Horses roam around free on the campground, its a unique experience to connect with those awesome animals.",
                          permit=False,
                          permit_info=None)
    campsite_1.author = user_3

    campsite.append
    campsite_1.amenities.append(amenities_lookup["Electricity"])
    campsite_1.amenities.append(amenities_lookup["Wifi"])



    db.session.add(user_1)
    db.session.add(campsite_1)
    db.session.add(user_2)
    db.session.add(campsite_2)
    db.session.add(user_3)
    db.session.add(campsite_3)


    db.session.commit()


# def load_sample_campsites():
#     """Load sample campsites"""

#     # campsite_1 = Campsite(name="Backpacker’s Paradise", 
#     #                     lat=18.344800, 
#     #                     lon=-88.152880, 
#     #                     description="Excellent mosquito-screened common area with tables, hammocks, power and a kitchen. Super friendly owners. Wifi in the restaurant and common areas. There is a dedicated modem in the common area/kitchen. Horses roam around free on the campground, its a unique experience to connect with those awesome animals.",
#     #                     permit=False,
#     #                     permit_info=None,
#     #                     user_id=3)


#     campsite_2 = Campsite(name="Sandy Lane", 
#                     lat=17.744617,
#                     lon=-88.024617, 
#                     description="Very basic. Shared bathrooms but awesome hot showers. There was a place to grill and covered picnic tables outside, but no kitchen. Probably the cheapest place to stay on Caye Caulker if you don’t have a tent and don’t want to stay in a noisy hostel dorm. Ask the groundskeeper named Moses about conch ceviche.",
#                     permit=True,
#                     permit_info="You'll need a permit",
#                     user_id=4)


#     campsite_3 = Campsite(name="Tropical Education Center", 
#                 lat=17.360490, 
#                 lon=-88.544600, 
#                 description="Closest place to stay by the Belize Zoo. Good place to camp, brand new bathrooms with gigantic showers and covered picnic tables. Lots of people stay here in the cabins to do the night tour of the zoo. We went during the day and saw everything but the spider monkeys. Electricity available only in the office.",
#                 permit=False,
#                 permit_info=None,
#                 user_id=2)

#     db.session.add(campsite_1)
#     db.session.add(campsite_2)
#     db.session.add(campsite_3)

#     db.session.commit()



if __name__ == "__main__":

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    from server import app

    connect_to_db(app)
    print("Connected to DB.")



