import geocoder
import folium

g = geocoder.ip('me')

myaddres = g.latlng

mymap1 = folium.Map(location=myaddres, zoom_start=12)

folium.CircleMarker(location=myaddres, radius=80, popup='Yorkshire').add_to(mymap1)

folium.Marker(myaddres, popup='Yorkshire').add_to(mymap1)

mymap1.save('location.html')

a = input('do you want to open the location [Y/n]')

if a == 'y':
    import os
    os.system('open location.html')
elif a == 'Y':
    import os 
    os.system('location.html')
else:
    exit()