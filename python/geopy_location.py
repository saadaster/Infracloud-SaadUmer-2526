from geopy.geocoders import Nominatim
import folium
geolocator = Nominatim(user_agent="http://biasc.be")
city_country = "Ixelles, Belgium"
location = geolocator.geocode(city_country)
devnet_lat = location.latitude
devnet_lon = location.longitude
devnet_alt = location.altitude

coordinates = [devnet_lat, devnet_lon]
map = folium.Map(location=coordinates, tiles='OpenStreetMap', zoom_start=16)
map.save("geopy_location.html")