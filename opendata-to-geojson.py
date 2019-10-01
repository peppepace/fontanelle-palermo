'''
    File name: 
        opendata-to-geojson.py
    Author: 
        Peppe Pace
    Date created: 
        01/10/2019
    Date last modified: 
        01/10/2019
    Description:
        Tool to convert online opendata [https://opendata.comune.palermo.it/ws.php?id=1905&fmt=json] in geojson format
'''

import json
import urllib.request

operUrl = urllib.request.urlopen('https://opendata.comune.palermo.it/ws.php?id=1905&fmt=json')
if(operUrl.getcode()==200):
    fontanelle = json.loads(operUrl.read())

    geoJsonFeatures = []

    for fontanella in fontanelle:
        geoJsonItem = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    float(fontanella["longitudine"]),
                    float(fontanella["latitudine"])
                ]
            },
            "properties": {
                "name" : fontanella["Nome"],
                "address" : fontanella["Indirizzo"],
                "marker-color" : "#0080ff",
                "marker-size" : "medium",
                "marker-symbol" : "water"
            }
        }
    
        geoJsonFeatures.append(geoJsonItem)
    
        geoJson = {
            "type": "FeatureCollection",
            "features": geoJsonFeatures
        }
    
    with open("fontanelle.json", "w") as w:
        w.write(json.dumps(geoJson, indent=4))
        w.close()    

else:
    print("Error receiving data", operUrl.getcode())