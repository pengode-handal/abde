
import phonenumbers
import folium
number = '+6285806952398'

from phonenumbers import geocoder

key = '94dbe1c296ac45a89541ad7e02417b14'
sanNumber = phonenumbers.parse(number)

yourlocation = geocoder.description_for_number(sanNumber, "en")
print(yourlocation)

from phonenumbers import carrier

service_prov = phonenumbers.parse(number)
print(carrier.name_for_number(service_prov, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourlocation)

result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

mymap = folium.Map(location=[lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup= yourlocation).add_to((mymap))

mymap.save('location.html')

import os

os.system('open location.html')