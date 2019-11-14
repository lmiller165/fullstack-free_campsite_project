campsite_dict = {'id': 115671, 
                 'name': 'Nasa abandoned parking', 
                 'description': "there's nothing here. we came at night to watch a rocket launch. theres one old surveillance camera we think is not working. enjoy and good luck everyone!!", 
                 'date_verified': '2019-11-11T00:00:00.000Z', 
                 'category_icon_path': '/assets/icons/informal-camp-deadf32955371fab2d17a87e8faad988.png', 
                 'category_icon_pin_path': '/assets/icons/informal-camp-pin-08e5901c15c2799f70a283fb7f4980a5.png', 
                 'amenities': {'Open': 'Yes', 'Electricity': 'No', 'Wifi': 'No', 'Kitchen': 'No', 'Restaurant': 'No', 'Showers': 'No', 'Water': 'No', 'Toilets': 'No', 'Big Rig Friendly': 'Yes', 'Tent Friendly': 'Yes', 'Pet Friendly': 'Unknown'}, 
                 'country': 'United States', 
                 'category': 'Informal Campsite', 
                 'location': {'latitude': 28.5102023, 'longitude': -80.6932755, 'altitude': -25.0, 'horizontal_accuracy': None, 'vertical_accuracy': None}}


name = campsite_dict['name']
# name = campsite_dict.get('name')

description = campsite_dict['description']
lat = campsite_dict['location']['latitude']
lon = campsite_dict['location']['longitude']



features = []
amenities = campsite_dict['amenities']
for amenity in campsite_dict['amenities']:
    # print(amenity)
    if campsite_dict['amenities'][amenity] == "Yes":
      features.append(amenity)


print(name)
print(description)
print(lat)
print(lon)
print(features)

