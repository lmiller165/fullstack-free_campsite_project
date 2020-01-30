# Roam for Free
Roam for Free is a full-stack web application that acts as a database for travelers. It allows users to add locations where they have previously stayed overnight for free. Other users can view, rate, and review the various locations. You can also build a trip using all the locations and text yourself a list of coordinates to go to. 

To watch a screen cast of the application go to:
https://vimeo.com/382302181

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
 
Search campsites by state:
![](readme-img/init-search-min.gif)

Search campsites by filters:
![](readme-img/filter-min.gif)

