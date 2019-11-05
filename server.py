
"""Free Camping Project."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
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

    session["user_id"] = user.user_id

    flash("Logged in")
    # return redirect(f"/users/{user.user_id}")


    return render_template("homepage.html")


@app.route('/sign-up', methods=['GET'])
def register_form():
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


@app.route('/add-campsite', methods=['GET'])
def add_campsite():
    """Show form for user signup."""

    return render_template("add-campsite.html")


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







