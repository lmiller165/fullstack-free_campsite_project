# Roam for Free
Roam for Free (previously named "Free Camping Project") is a full-stack web application that allows users to add points to a map where they have previously stayed overnight for free. 

![](readme-img/homescreen.png)

## Overview
**The Map**  
* Shows campsites that have been added to the database.
* Levrages mapbox javascrip methods to build informational pop-ups for each site.
* Allow user to add a location to their trip. 

**Users can:** 
* Sign in/sign out/sign up (create an account)
* Add a new location with latitude, longitute, campsite title, and description. 
* See all campsites uploaded by other users.
* Add reviews and risk ratings to each campsite. 
* Send yourself a list of locations from your trip. 
* Click on icons to view campsite information and navigate to detail pages.
* View campsite detail pages. 

## Technologies and stack
**Backend:**  
Python, Flask, Flask-SQLAlchemy, ParseLib, Jinja2

**Frontend:**   
JavaScript, jQuery, AJAX, Jinja, jQuery,HTML5, CSS3, Twitter Bootstrap (html/css/js framework), RWD (responsive web design).

**APIs:**   
Mapbox, Twilio

## Features
**Campsite Storage**  
 Get latitude and longitude from user's browser using HTML5 geolocation.
 Store location data in a database with associated tables for users, campsites, reviews, ratings and amenities.
 Flask app routes AJAX requests to the database and Flask session. 
 
**Map**  
 Mapbox javascript methods to initialize a visual map for each campsite. 
 Query database to construct geojson master file which is supplied to my javascript function to populate the map.
 Used mapbox javascrip methods to contruct pop-ups for each campsite that allows users to view information, navigate to detail page and add campsite to trip.
![](readme-img/popup2-min.gif)
 
**Filtering campsites**  
 Used Mapbox API endpoints to gather additional information for each campsite with reverse geolocation. 
 Use the added information 
 

![](readme-img/init-search-min.gif)
![](readme-img/filter-min.gif)

