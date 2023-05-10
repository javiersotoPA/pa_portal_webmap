###  "C:\Arcgis\ArcPro\bin\Python\Scripts\propy.bat" agol_uploader.py


## Import Modules
import os
from arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection
from settings import *

## Create list of True layers to be pushed to AGOL account
layers_to_agol = []
for layer in settings:
    if settings[layer]:
        #print(layer)
        layers_to_agol.append(layer)

## Log into AGOL
gis = GIS('https://snh.maps.arcgis.com',agol_user,agol_password)
un = gis.properties.user.username
print(f"Logged in as {un}")

## Overwrite hosted feature layer
for layer in layers_to_agol:
    print(f"\nUpdating layer in AGOL: {layer}")
    itemid = layers[layer]
    #print(itemid)
    dataitem = gis.content.get(itemid)  ## log into your content and find the itemID
    #print(dataitem)
    if dataitem == None:
        print(f"\nI could not find item {layer} in your AGOL account. Check if itemID provided is correct {itemid}")
        exit(1)
    flayercol = FeatureLayerCollection.fromitem(dataitem)  ## turn the item above into feature collection (not changing anything on agol)
    #print(flayercol)
    if layer == 'agol_carbon_peat_map_16':
        flayercol.manager.overwrite(f"{layer}.geojson")
    else:
        flayercol.manager.overwrite(f"{layer}.shp")

print("\n\nEnd of the script")

