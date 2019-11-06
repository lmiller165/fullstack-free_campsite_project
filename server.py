
"""Free Camping Project."""

from jinja2 import StrictUndefined

from flask import Flask, session, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Campsite, User, Rating, Review, Campsite_amenities, Amenity 


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "SECRET"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def index():
    """Homepage: Login or signup"""

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

    #flash message not currently working 
    flash("Logged in")
    return render_template(f"/view-all-campsites/{user.user_id}")


@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/")


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

    # return redirect(f"/users/{new_user.user_id}")

@app.route("/campsites")
def movie_list():
    """Show list of campsites."""

    campsites = Campsite.query.order_by('title').all()
    return render_template("view-all-campsites.html", campsites=campsites)


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


@app.route('/add-campsite', methods=['POST'])
def add_campsite():
    """Add a campsite as a registered user."""

    # Get form variables
    name = request.form["name"]
    lat = int(request.form["lat"])
    lon = int(request.form["lon"])
    description = request.form["description"]

    #Amenities form variables
    electricity_checked = request.form.get("electricity") != None
    wifi_checked = request.form.get("wifi") != None
    showers_checked = request.form.get("showers") != None
    water_checked = request.form.get("water") != None
    toilets_checked = request.form.get("toilets") != None
    petfriendly_checked = request.form.get("petfriendly") != None
    tentfriendly_checked = request.form.get("tentfriendly") != None

    #Ratings form varialbes 
    noise_level = int(request.form["noiselevel"])
    privacy_level = int(request.form["privacylevel"])
    risk_level = int(request.form["risklevel"])

    #User_id pulled from session
    user_id = session.get("user_id")

    #Checking for user_id
    if not user_id:
        raise Exception("No user logged in.")


    db.session.commit()

    return render_template("view-all.campsites")


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







