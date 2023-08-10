###  "C:\Arcgis\ArcPro\bin\Python\Scripts\propy.bat" "C:\javi\in_progress\Webmapping\agol_uploader.py"

## Import Modules
import os
import glob
import geopandas as gpd
import pandas as pd
from sqlalchemy import create_engine
from settings import *
import datetime
import numpy as np
import shutil


## Workspace

def create_folder(folder_name):
    if os.path.exists(folder_name):
        # Delete the folder if it already exists
        shutil.rmtree(folder_name)
    # Create the folder
    os.mkdir(folder_name)

create_folder('agol_layers')



## parameters
db_connection_url = db_credentials
con = create_engine(db_connection_url) 

for layer in settings:
    if settings[layer]:
        if layer == 'agol_pa_reported_hectares':
            print(f"\nDownloading layer '{layer}' from DB\n")
            sql = f"SELECT * FROM pa_agol_views.{layer}"
            gdf = pd.read_sql_query(sql, con)  ## convert to dataframe
            isdate = gdf.select_dtypes(include=[np.datetime64])  ## check if there is any datatime column
            date_column = list(isdate.columns)
            if date_column:
                for date in date_column:
                    gdf[date] = gdf[date].dt.strftime("%Y-%m-%d")
                gdf.to_csv(f"agol_layers/{layer}.csv", index=False)
            if not date_column:
                gdf.to_csv(f"agol_layers/{layer}.csv", index=False)
        else:
            print(f"\nDownloading layer '{layer}' from DB\n")
            sql = f"SELECT * FROM pa_agol_views.{layer}"
            gdf = gpd.GeoDataFrame.from_postgis(sql, con)  ## convert to dataframe
            isdate = gdf.select_dtypes(include=[np.datetime64])  ## check if there is any datatime column
            date_column = list(isdate.columns)
            if date_column:
                for date in date_column:
                    gdf[date] = gdf[date].dt.strftime("%Y-%m-%d")
                gdf.to_file(f"agol_layers/{layer}.geojson", driver='GeoJSON')
            if not date_column:
                gdf.to_file(f"agol_layers/{layer}.geojson", driver='GeoJSON')
        


## push layers to agol

#agol_uploader = "C:\\Arcgis\\ArcPro\\bin\\Python\\Scripts\\propy.bat agol_uploader.py"
#os.system(agol_uploader)
        

