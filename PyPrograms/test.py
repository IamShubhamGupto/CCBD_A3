# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:25:23 2020

@author: shubham_2
"""
from osgeo import gdal
ds = gdal.Open(r"D:\SHUBHAM\CCBD\QGIS\BLR\BLR.100.tif")
width = ds.RasterXSize
height = ds.RasterYSize
gt = ds.GetGeoTransform()
minx = gt[0]
miny = gt[3] + width*gt[4] + height*gt[5] 
maxx = gt[0] + width*gt[1] + height*gt[2]
maxy = gt[3] 
metadata = gdal.Info(ds)
print(metadata)