"""Models and database functions for Free Camping project."""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


##############################################################################
# Model definitions

class Campsite(db.Model):
    """Table for campsites"""

    __tablename__ = "campsites"

    campsite_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    lat = db.Column(db.Float(), nullable=False)
    lon = db.Column(db.Float(), nullable=False)
    description = db.Column(db.String, nullable=False)
    permit = db.Column(db.Boolean, default=False)
    permit_info = db.Column(db.String)

    #Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    # Define relationships
    author = db.relationship("User",
                            backref=db.backref("campsites",
                                               order_by=campsite_id))
    amenities = db.relationship("Amenity",
                                secondary="campsite_amenities",
                                backref="campsites"
                                )


    def __repr__(self):
        """Show helpful campsite information when printed"""
        return f"""<Campsite={self.name} 
                    lat={self.lat} 
                    lon={self.lon} 
                    description={self.description}>"""


class User(db.Model):
    """Table for all our campers"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)


    def __repr__(self):
        """Show helpful user information when printed"""
        return f"""<user_id={self.user_id} 
                    name={self.fname} {self.lname} 
                    username={self.username} 
                    email={self.email}>"""


class Rating(db.Model):
    """Table for three ratings"""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    noise_level = db.Column(db.Integer)
    risk_level = db.Column(db.Integer)
    privacy_level = db.Column(db.Integer)

    #Foreign Keys
    campsite_id = db.Column(db.Integer, db.ForeignKey('campsites.campsite_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    # Define relationships
    author = db.relationship("User",
                            backref=db.backref("ratings",
                                               order_by=rating_id))
    campsite = db.relationship("Campsite",
                            backref=db.backref("ratings",
                                               order_by=rating_id))


    def __repr__(self):
        """Show helpful rating information when printed"""    

        return f"""<rating_id={self.rating_id} 
                noise_level={self.noise_level} 
                risk_level={self.risk_level} 
                privacy_level={self.privacy_level}>"""


class Review(db.Model):
    """Table for our campsite reviews"""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    review_description = db.Column(db.String, nullable=False)
    reviewed_at=db.Column(db.DateTime)

    #Foreign Keys
    campsite_id = db.Column(db.Integer, db.ForeignKey('campsites.campsite_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    # Define relationships
    author = db.relationship("User",
                            backref=db.backref("reviews",
                                               order_by=review_id))
    campsite = db.relationship("Campsite",
                            backref=db.backref("reviews",
                                               order_by=review_id))

    def __repr__(self):
        """Show helpful rating information when printed"""    

        return f"""<review_id={self.review_id} 
                review_description={self.review_description}>"""


class CampsiteAmenity(db.Model):
    """Table to link our amenities to our campsite"""

    __tablename__ = "campsite_amenities" 

    campsite_amenities_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    #Foreign Keys
    amenity_id = db.Column(db.Integer, db.ForeignKey('amenities.amenity_id'))
    campsite_id = db.Column(db.Integer, db.ForeignKey('campsites.campsite_id'))

    def __repr__(self):
        """Show helpful rating information when printed"""   

        return f"<CampsiteAmenity amenity={self.amenity_id} campsite_id={self.campsite_id}>"


class Amenity(db.Model):
    """Table to hold all our amenity options"""

    __tablename__ = "amenities"

    amenity_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        """Show helpful rating information when printed"""    

        return f"""<amenity_id={self.amenity_id} 
                name={self.name}>"""



##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///campsites'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    from server import app

    connect_to_db(app)
    print("Connected to DB.")