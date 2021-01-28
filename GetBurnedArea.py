#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Geoscripting 2020
Final Project
Team: Imperfect_GeoCircle
@Authors: Yanuar Bomantara & Thijs Seubring
Date: 21-01-2021
"""

def GetBurnedArea(year,feature):
    """
    Function to get the burnt area and landuse from GEE. The input is the year you are interested in, and a feature of the AOI. 
    The output is a dictionary of the burnt area per lancover type and a .tif with the raster data of the burnt area.  
    """

    #import libraries
    import os
    import requests
    import rasterio
    from rasterio.plot import show
    from rasterio.features import shapes
    import pandas as pd
    import geopandas as gpd
    import matplotlib
    from matplotlib import pyplot as plt
    import gdal
    import ee
    import geemap
    
    #create folders if they are not present
    if not os.path.exists('data'): os.makedirs('data')
    if not os.path.exists('output'): os.makedirs('output')
    
    #filter GEE data based on year and select landcover. 
    startdate = str(year) + '-01-01'
    enddate = str(year) + '-12-31'
    dataset = ee.ImageCollection('ESA/CCI/FireCCI/5_1').filterDate(str(startdate), str(enddate))
    burnedArea = dataset.select('LandCover')
    maxBA = burnedArea.max()
    
    #get feature geometry
    AOI = feature
    roi = AOI.geometry()
    
    #clip feature to GEE raster and save as a .tif
    image = maxBA.clip(AOI).unmask()
    filenameWGS = 'data/BA_'+str(year)+'.tif'
    geemap.ee_export_image(image, filename=str(filenameWGS), scale=250, region=roi, file_per_band=False)
    
    #reproject to tif to use it in calculations
    warp = gdal.Open(str(filenameWGS))
    filenameWM = str('data/BA_'+str(year)+'WM.tif')
    b19 = gdal.Warp(filenameWM,warp, srcNodata=0, dstNodata=0 , srcSRS='EPSG:4326',dstSRS='EPSG:3395')
    del b19
    
    #Read raster into an array
    b19 = rasterio.open(filenameWM)
    array2 = b19.read(1)
    
    #calculate burnt area per landcover type and return a dictionary
    flat_list = [item for sublist in array2 for item in sublist]
    BurnedArea = dict((x,flat_list.count(x)) for x in set(flat_list))
    del BurnedArea[0]
    meta = b19.meta
    area = meta['transform'][0] ** 2/10000
    BurnedArea.update((x, y*area) for x, y in BurnedArea.items())
    
    dicti = {}
    Cropland = [10,20,30]
    Forest = [50,60,70,80,90,100,110,170]
    Shrubland=[120,180,40]
    Grassland=[130,150,140]
    
    area = 0.0
    for k in Cropland :
        try:
            area +=BurnedArea[k]
        except KeyError :
            continue
    dicti["Cropland"]=area

    area = 0.0
    for k in Forest :
        try:
            area +=BurnedArea[k]
        except KeyError :
            continue
    dicti["Forest"]=area

    area = 0.0
    for k in Shrubland :
        try:
            area +=BurnedArea[k]
        except KeyError :
            continue
    dicti["Shrubland"]=area

    area = 0.0
    for k in Grassland :
        try:
            area +=BurnedArea[k]
        except KeyError :
            continue
    dicti["Grassland"]=area
    
    return(dicti)

def BurntAreaPlot(dict_data):
    """
    Function that creates a barchart out of a dictionary.
    """
    
    #import libraries
    import numpy
    import matplotlib.pyplot as plt

    #define style
    plt.style.use('ggplot')
    
    #create barchart out of dictionary values
    plt.figure(figsize=(16,7))
    num_years = len(dict_data)
    values_matrix = numpy.zeros((num_years,4))
    year_labels = []
    for idx,(key, value) in enumerate(dict_data.items()):
        year_labels+=[key]
        values_from_year = list(value.values())
        for i in range(4):
            values_matrix[idx,i] = values_from_year[i]
    
    previous=numpy.zeros(num_years)
    
    for i in range(4):
        labels = dict_data.keys()
        ticks = numpy.arange(len(labels))
        plt.bar(ticks,values_matrix[:,i],bottom=previous, width=.5)
        plt.xticks(ticks,labels)
        plt.legend(value.keys())
        previous=previous+values_matrix[:,i]
        
    # add labels and grid
    plt.xlabel('Year')
    plt.ylabel('Burned down area (ha)')
    plt.title('Burned down area for different landcover types')
    plt.grid(True)
    
    #save file in output folder
    #plt.savefig('output/barplot_burntarea.png')
