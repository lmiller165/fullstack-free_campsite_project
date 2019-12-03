
from twilio.rest import Client
import config

# # Your Account SID from twilio.com/console
# account_sid = config.twilio_sid
# # Your Auth Token from twilio.com/console
# auth_token  = config.twilio_access_token

# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     to="+18438604767", 
#     from_="+12013791066",
#     body="Hello from Python!")

# print(message.sid)



# Python program to convert a list 
# of character 
  
def convert(s): 
  
    # initialization of string to "" 
    str1 = "" 
  
    # using join function join the list s by  
    # separating words by str1 
    return(str1.join(s)) 
      
# driver code    



def text_trip(trip):
    """sends you a list of your trip stops"""
    # campsite_name, lat, lon

    # Your Account SID from twilio.com/console
    account_sid = config.twilio_sid
    # Your Auth Token from twilio.com/console
    auth_token  = config.twilio_access_token

    client = Client(account_sid, auth_token)

    print(trip)

    list_to_text = []

    for campsite in trip: 
        campsite_name = campsite.name
        lat = campsite.lat
        lon = campsite.lon * -1

        lat = str(lat)
        lon = str(lon)

        location = "\n" + "\u26FA" + campsite_name + "\n" + ":" + "http://maps.google.com/maps?z=12&t=m&q=loc:" + lat + "+" + lon + "\n" 
# \U0001F31F
        list_to_text.append(location)

    string_to_text = convert(list_to_text)
                
    message = client.messages.create(
        to="+18438604767", 
        from_="+12013791066",
        body=string_to_text)

    print(message.sid)

