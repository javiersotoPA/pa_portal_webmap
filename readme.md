# Scripts for updating PeatlandAction restoration layers in AGOL

The scripts in this repo can be used to update the layers in AGOL portal. First, refresh each matematerialized view on the PA database.  

## How to run it using Conda environment (Recommended)

Open miniconda terminal and activate your conda environment containg the relevant dependencies, e.g. `conda activate gis_env`

If you don't have an existing conda environment configured you can use the contained `environment.yml` file to create one:

`conda env create -f environment.yml`

## Configuring settings file

Within the settings.py there are two dictionaries:<br>
* “Layers” dictionary will have the ID of the layer as existis in AGOL. Do not make any changes here.<br>
* “Settings” dictionary will have each layer as a key and each value as true or false Boolean, depending on if the user wants to update or not the layers in AGOL.<br> 

Additionally, the settings.py has three string variables:<br>
* “Agol_user”: Update with your credentials<br>
* “Agol_password”: Update with your credentials<br>
* “DB_credentials”: Update with your credentials<br>


<br>

## How to run it

* For running the script, use the main.py. <br>
* Bare in mind that if lines 61 and 62 are not commented, the script will update on AGOL any layer that has TRUE on the settings.py file. <br>