import json
from geojson import Point, Feature, FeatureCollection, dump
from mapbox_requests import get_state, get_zipcode, get_city, get_country
from mapbox_requests import get_place_info


def get_geojson(file):
    #How I open/source the file may change
    with open(file, 'r') as f:
        geojson = f.read()

    geojson = json.loads(geojson)
    data = geojson['features']

    return data


def filterby_info(get_input):

    data = get_geojson('static/json/all_campsites.geojson')

    features = []

    for feature in data:
        if get_input == feature['properties']['place_info']:
            features.append(feature)

    feature_collection = FeatureCollection(features)

    return feature_collection



#will need to get user input from form in server
def filterby_state(state):
    """return geojson from state query"""

    data = get_geojson('static/json/all_campsites.geojson')

    features = []

    for feature in data:
        if state == feature['properties']['state']:
            features.append(feature)

    feature_collection = FeatureCollection(features)

    return feature_collection


#will need to get user input from form in server
def filterby_zipcode(zipcode):
    """return geojson from zipcode query"""

    data = get_geojson('static/json/all_campsites.geojson')

    features = []

    for feature in data:
        if zipcode == feature['properties']['zipcode']:
            features.append(feature)

    feature_collection = FeatureCollection(features)

    return feature_collection


#will need to get user input from form in server
def filterby_city(city):
    """return geojson from zipcode query"""

    data = get_geojson('static/json/all_campsites.geojson')

    features = []

    for feature in data:
        if city == feature['properties']['city']:
            print("\n\n\n\n")
            print(city)
            features.append(feature)

    feature_collection = FeatureCollection(features)

    return feature_collection


def get_coordinates(state):

    state_coord = {
                "Alabama": [-86.791130, 32.806671],
                "Alaska": [-152.404419, 61.370716],
                "Arizona": [-111.431221, 33.729759],
                "Arkansas": [-92.373123, 34.969704],
                "California": [-119.681564, 36.116203],
                "Colorado": [-105.311104, 39.059811],
                "Connecticut": [-72.755371, 41.597782],
                "Delaware": [-75.507141, 39.318523],
                "District of Columbia": [-77.026817, 38.897438],
                "Florida": [-81.686783, 27.766279],
                "Georgia": [-83.643074, 33.040619],
                "Hawaii": [-157.498337, 21.094318],
                "Idaho": [-114.478828, 44.240459],
                "Illinois": [-88.986137, 40.349457],
                "Indiana": [-86.258278, 39.849426],
                "Iowa": [-93.210526, 42.011539],
                "Kansas": [-96.726486, 38.526600],
                "Kentucky": [-84.670067, 37.668140],
                "Louisiana": [-91.867805, 31.169546],
                "Maine": [-69.381927, 44.693947],
                "Maryland": [-76.802101, 39.063946],
                "Massachusetts": [ -71.530106, 42.230171],
                "Michigan": [ -84.536095, 43.326618],
                "Minnesota": [-93.900192, 45.694454],
                "Mississippi": [-89.678696, 32.741646],
                "Missouri": [-86.791130, 32.806671],
                "Montana": [-110.454353, 46.921925],
                "Nebraska": [-98.268082, 41.125370],
                "Nevada": [-117.055374, 38.313515],
                "New Hampshire": [-71.563896, 43.452492],
                "New Jersey": [-74.521011, 40.298904],
                "New Mexico": [-106.248482, 34.840515],
                "New York": [-74.948051, 42.165726],
                "North Carolina": [-79.806419, 35.630066],
                "North Dakota": [-99.784012, 47.528912],
                "Ohio": [-82.764915, 40.388783],
                "Oklahoma": [-96.928917, 35.565342],
                "Oregon": [-122.070938, 44.572021],
                "Pennsylvania": [-77.209755, 40.590752],
                "Rhode Island": [-71.511780, 41.680893],
                "South Carolina": [-80.945007, 33.856892],
                "South Dakota": [-99.438828, 44.299782],
                "Tennessee": [-86.692345, 35.747845],
                "Texas": [-97.563461, 31.054487],
                "Utah": [-111.862434, 40.150032],
                "Vermont": [-72.710686, 44.045876],
                "Virginia": [-78.169968, 37.769337],
                "Washington": [-121.490494, 47.400902],
                "West Virginia": [-80.954453, 38.491226],
                "Wisconsin": [-89.616508, 44.268543],
                "Wyoming": [-107.302490, 42.755966],

    }


    return state_coord[state]


def filterby_amenities_state(amenities_lst, state):
    """Return the campsites with the same list of amenities"""

    data = get_geojson('static/json/all_campsites.geojson')

    features = []

    new_amenities = ["Open"]
    new_amenities.extend(amenities_lst)

    if amenities_lst == ["Open"]:

        for feature in data:
        # print(feature['properties']['amenities'])

            if state == feature['properties']['state'] and new_amenities == feature['properties']['amenities']:
                features.append(feature)

    else:
        for feature in data:
            # print(feature['properties']['amenities'])

            if state == feature['properties']['state'] and new_amenities == feature['properties']['amenities']:
                features.append(feature)


    feature_collection = FeatureCollection(features)

    return feature_collection


def filterby_amenities(amenities_lst):
    """Return the campsites with the same list of amenities"""

    data = get_geojson('static/json/all_campsites.geojson')

    features = []

    new_amenities = ["Open"]
    new_amenities.extend(amenities_lst)

    for feature in data:
    # print(feature['properties']['amenities'])
        if new_amenities == feature['properties']['amenities']:
            features.append(feature)

    feature_collection = FeatureCollection(features)

    return feature_collection



    # if amenities_lst == ["Open"]:

    #     for feature in data:
    #         if new_amenities == feature['properties']['amenities']:
    #             features.append(feature)

    # else:
















