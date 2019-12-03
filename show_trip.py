def show_trip():
    """query to show all trips"""

    # Create a list to hold campsites to display later 
    all_campsites = []

    # Get the cart dictionary out of the session (or an empty one if none
    # exists yet)
    trip = session.get("trip", {})
    # print("\n\n\n")
    # print("trip route trip:")
    # print(trip)


    for campsite in trip.items():
        campsite_name = campsite[0]
        # print("\n\n\n")
        # print(campsite_name)
        campsite = Campsite.query.filter_by(name=campsite_name).first()
        all_campsites.append(campsite)

    return all_campsites