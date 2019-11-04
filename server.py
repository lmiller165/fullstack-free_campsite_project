###############################################################################################
#::NOTES::
#[ ] Clean up requirements.txt doc, lifted from a requirement doc from the ratings lab





##############################################################################################


#This code is straight from the documentation of Flask-SQLAlchemy
#Shows how to make a connection via SQL Alchemy 
def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = #change route:'postgresql:///hackbright'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


#Example of using QUERY (SQL) in python. Note to remember to add "db_cursor"
#You will probably not need this b/c you will use SQL Alchemy
def get_student_by_github(github):
    """Given a GitHub account name, print info about the matching student."""

    QUERY = """
        SELECT first_name, last_name, github
        FROM students
        WHERE github = :github
        """
    #similar to a file handler, the mechanism used to look at rows contained in our query results.
    db_cursor = db.session.execute(QUERY, {'github': github})

    #fetchone is pulling one result
    row = db_cursor.fetchone()

    print("Student: {} {}\nGitHub account: {}".format(row[0], row[1], row[2]))

    #you should always close your connection to your data base.
    #look up if you still need this with SQL Alchemy
    db.session.close()

#Example of a route using SQLAlchemy, you could also use raw SQL 
@app.route('/register', methods=['POST'])
def register_process():
    """Process registration."""

    # Get form variables
    email = request.form["email"]
    password = request.form["password"]
    age = int(request.form["age"])
    zipcode = request.form["zipcode"]

    new_user = User(email=email, password=password, age=age, zipcode=zipcode)

    db.session.add(new_user)
    db.session.commit()

    flash(f"User {email} added.")
    return redirect(f"/users/{new_user.user_id}")


