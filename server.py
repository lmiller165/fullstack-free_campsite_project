
"""Free Camping Project."""

from jinja2 import StrictUndefined
from flask import Flask, session, render_template, request, flash, redirect, jsonify, request_finished
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Campsite, User, Rating, Review, Amenity, CampsiteAmenity 
import config
import json
import mapbox
import requests
from mapbox import Geocoder
from write_geojson import write_geojson_file, read_geojson, write_geojson_dict
from filter_results import filterby_state, filterby_zipcode, filterby_info, get_coordinates


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "SECRET"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


############################## LOGIN PROCESS ###################################
@app.route('/')
def index():
    """Homepage: Login or signup"""

    #you can log in or choose to create an account from the homepage.
    return render_template("homepage.html")


@app.route('/', methods=['POST'])
def login_process():
    """Logging in from homepage"""

    # Get form variables from homepage log in
    email = request.form["email"]
    password = request.form["password"]

    # query user info using email variable
    user = User.query.filter_by(email=email).first()

    if not user:
        flash("No such user")
        return redirect("/")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/")

    #saving user_id
    session["user_id"] = user.user_id

    flash("Logged in")
    return redirect("/view-campsites")


@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/")

############################# SIGN UP PROCESS ##################################

@app.route('/sign-up', methods=['GET'])
def signup_form():
    """Show form for user signup."""

    return render_template("sign-up.html")


@app.route('/sign-up', methods=['POST'])
def signup_process():
    """Signup process and adding user to db"""

    # Get form variables from sign-up.html
    fname = request.form["fname"]
    lname = request.form["lname"]
    email = request.form["email"]
    password = request.form["password"]

    new_user = User(fname=fname, lname=lname, email=email, password=password)

    #add new user to our db
    db.session.add(new_user)
    db.session.commit()

    flash(f"User {email} added.")
    return redirect("/")

############################### VIEW CAMPSITES #################################

@app.route('/view-campsites', methods=['GET'])
def list_campsites():
    """Show list of all campsites"""

    campsites = Campsite.query.all()

    #User_id pulled from session
    user_id = session.get("user_id")
    user = User.query.filter_by(user_id=user_id).first()

    token = config.mapbox_access_token

    return render_template("view-campsites.html", campsites=campsites,
                                                  user=user,
                                                  token=token)


@app.route('/view-campsites', methods=['POST'])
def filter_campsites():
    """Show list of all campsites"""

    campsites = Campsite.query.all()

    #User_id pulled from session
    user_id = session.get("user_id")
    user = User.query.filter_by(user_id=user_id).first()

    token = config.mapbox_access_token

    # Get form variables 
    region = request.form["state"]

    # Use mapbox API to fetch data
    # california_request = requests.get("https://api.mapbox.com/geocoding/v5/mapbox.places/" + region + ".json?access_token=pk.eyJ1IjoibG1pbGxlcjE2NSIsImEiOiJjazI0MXN6ZjIwNDNoM21tbmI4dnFobjMxIn0.Xf5-STNNUuVlsRZalbZrXA")
    geocoder = Geocoder()

    print("\n\n\n\n\n")
    response = geocoder.forward(region)
    response.status_code
    print("\n\n\n\n\n")
    print(response)
    response = response.json()
    print("\n\n\n\n\n")
    print(response)

    return redirect("/view-campsites")


########################### VIEW CAMPSITE DETAILS ##############################

@app.route('/campsite-details', methods=['GET'])
def show_campsite_details():
    """Show single campsite details"""

    #Campsite details
    campsite_name = request.args.get('campsite')
    campsite = Campsite.query.filter_by(name=campsite_name).first()
    amenities = campsite.amenities
    ratings = campsite.ratings
    reviews = campsite.reviews

    #User_id pulled from session
    user_id = session.get("user_id")
    user = User.query.filter_by(user_id=user_id).first()



    return render_template("campsite-details.html", campsite=campsite,
                                                    amenities=amenities,
                                                    ratings=ratings,
                                                    user=user,
                                                    reviews=reviews)

################################# REVIEW PAGE ##################################

@app.route('/add-review', methods=['GET'])
def show_review():
    """Show add review form"""

    campsite_name = request.args.get('campsite')
    campsite = Campsite.query.filter_by(name=campsite_name).first()

    #User_id pulled from session
    user_id = session.get("user_id")
    user = User.query.filter_by(user_id=user_id).first()

    return render_template("add-review.html", campsite=campsite,
                                              user=user)


@app.route('/add-review', methods=['POST'])
def add_review_process():
    """Get information from review form page"""

    campsite_name = request.form["campsite_name"]
    campsite = Campsite.query.filter_by(name=campsite_name).first()
    campsite_id = campsite.campsite_id
    amenities = campsite.amenities
    ratings = campsite.ratings


    # Get form variables 
    review = request.form["review"]
    noise_level = int(request.form["noiselevel"])
    privacy_level = int(request.form["privacylevel"])
    risk_level = int(request.form["risklevel"])

    #User_id pulled from session
    user_id = session.get("user_id")
    user = User.query.filter_by(user_id=user_id).first()

    new_rating = Rating(noise_level=noise_level,
                    risk_level=risk_level,
                    privacy_level=privacy_level,
                    user_id=user_id,
                    campsite_id=campsite_id)

    new_review = Review(user_id=user_id,
                        campsite_id=campsite_id,
                        review_description=review)

    db.session.add(new_rating)
    db.session.add(new_review)

    db.session.commit()


    return render_template("campsite-details.html", campsite=campsite,
                                                    amenities=amenities,
                                                    ratings=ratings,
                                                    user=user)

################################ ADD CAMPSITES #################################

@app.route('/add-campsite')
def add_campsite_form():
    """Show a logged in user the add campsite form"""

    #User_id pulled from session
    user_id = session.get("user_id")

    #Checking for user_id
    if not user_id:
        flash(f"You must be logged in to add a campsite")
        raise Exception("No user logged in.")

        return redirect("/")

    else:
        return render_template("add-campsite.html", amenities=Amenity.query.all())


@app.route('/add-campsite', methods=['POST'])
def add_campsite():
    """Add a campsite as a registered user."""

    # Campsite form variables
    name = request.form["name"]
    lat = request.form["lat"]
    lon = request.form["lon"]
    description = request.form["description"]
    permit = request.form["permit"]
    if permit == "False":
        permit = False
    else:
        permit = True
    permit_info = request.form["permit_info"]

    #Ratings form varialbes 
    noise_level = int(request.form["noiselevel"])
    privacy_level = int(request.form["privacylevel"])
    risk_level = int(request.form["risklevel"])

    #User_id pulled from session
    user_id = session.get("user_id")

    new_campsite = Campsite(name=name, 
                        lat=lat, 
                        lon=lon, 
                        description=description,
                        permit=permit,
                        permit_info=permit_info,
                        user_id=user_id)

    new_rating = Rating(noise_level=noise_level,
                        risk_level=risk_level,
                        privacy_level=privacy_level,
                        user_id=user_id)

    db.session.add(new_campsite)

    db.session.commit()
    #append ammenities to campsite
    amenities = request.form.getlist("amenities")
    for amenity_id in amenities:

        amenity = Amenity.query.get(int(amenity_id))
        new_campsite.amenities.append(amenity)

    #append new rating to campsite
    new_campsite.ratings.append(new_rating)

    #add all info to our db
    db.session.commit()

    campsite_ams = CampsiteAmenity.query.filter(CampsiteAmenity.campsite_id==new_campsite.campsite_id).all()
    print(campsite_ams)

    return redirect("/view-campsites")


###################################  MAPBOX MARKERS #############################
@app.route('/map', methods=['GET'])
def view_map():
    """Show user map of campsites."""

    return render_template("map.html", token=config.mapbox_access_token)


@app.route('/map_data', methods=['GET'])
def get_points():
    """Show user map of campsites."""

    # all campsites
    geojson = read_geojson('static/json/all_campsites.geojson')
    # geojson = write_geojson_dict()
    # print(geojson)

    # geojson = filterby_info(get_input)

    return jsonify(geojson)


@app.route('/map-filter.json', methods=['GET'])
def map_filter():
    """Show user map of campsites with filter."""

    state = request.args.get("state")
    # amenity = request.args.get("amenity")

    #state filter
    geojson = filterby_state(state)
    # coordinates = get_coordinates(state)

    print("\n\n\n")
    print(state)
    # print(amenity)
    # print(coordinates)
    print(geojson)

    return jsonify(geojson)

    #zipcode
    # geojson = filterby_zipcode("99683")

    #state
    # geojson = filterby_state(state)

    #city
    # geojson = filterby_state("Winslow")

################################################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")


############################################################################







