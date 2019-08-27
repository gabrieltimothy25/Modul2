import pandas as pd
import folium

df = pd.read_csv('zomato.csv', encoding="ISO-8859-1")

peta = folium.Map(
    location = [-6.1753924,106.8271528],
    tiles = 'OpenStreetMap',
    # OpenStreetMap StamenToner StamenTerrain MapboxBright
    zoom_start = 15
)

for lat,long,_id,city,name in zip(list(df['Latitude']), list(df['Longitude']), list(df['Restaurant ID']), list(df['City']), list(df['Restaurant Name'])):
    folium.Marker(
    [lat, long],
    popup = '<b>{}</b><br><i>{}</i>'.format(_id, city),
    tooltip = name,
    icon = folium.Icon(color='red', prefix='fa', icon='home')
    ).add_to(peta)
    
peta.add_child(
    folium.ClickForMarker()
)
peta.save('zomato.html')
