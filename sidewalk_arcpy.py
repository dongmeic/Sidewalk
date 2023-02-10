import arcpy
from arcgis import GIS
import pandas as pd
from arcgis.features import FeatureLayerCollection

arcpy.env.overwriteOutput = True
path = r'T:\DCProjects\Modeling\Sidewalk\ProPrj\ProPrj.gdb'
gis = GIS('home')

# n is the feature layer number
def download_feature_layer(url, n, filename):
    flyrs = FeatureLayerCollection(url)
    sdf = pd.DataFrame.spatial.from_layer(flyrs.layers[n])
    datacopy = sdf.spatial.to_featureclass(path + f'\\{filename}')
    print(f'Data saved at {datacopy}')
