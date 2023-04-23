
import streamlit as st
import pandas as pd
import altair as alt
from altair import datum
import numpy as np 
from PIL import Image
import os
import geopandas as gpd

def create_points_df(farmers_markets, garden_sites):
    farmers_markets = farmers_markets[farmers_markets['Market Name'] != 'Saratoga Farm Stand']
    farmers_markets['loc_type'] = 'Farmers market'
    farmers_markets = farmers_markets[['Latitude', 'Longitude', 'Borough', 'loc_type']]
    farmers_markets = farmers_markets.rename(columns = {'Borough': 'borough', 'Latitude': 'lat', 'Longitude': 'long'})

    garden_sites['lat'] = garden_sites.centroid.y
    garden_sites['long'] = garden_sites.centroid.x
    garden_sites['loc_type'] = 'Community garden'
    garden_sites = garden_sites[['lat', 'long', 'borough', 'loc_type']] 

    points_df = pd.concat([farmers_markets, garden_sites], axis = 0)
    return points_df
# Load the data from vega_datasets
gdf = gpd.read_file("geo_export_15e54104-230b-46ff-831d-f8f2bcaa8f59.shp")

grouped_food_df = pd.read_csv("food_security_by_tract.csv")
grouped_walk_df = pd.read_csv("walkability_by_tract.csv")
cd = gpd.read_file("geo_export_7b678860-455d-4c2b-8175-8482e297e882.shp")

farmers_markets = pd.read_csv("DOHMH_Farmers_Markets.csv")
garden_sites = gpd.read_file("geo_export_719c88a3-5724-4f23-b587-e754c0844c6d.shp")
points_df = create_points_df(farmers_markets, garden_sites)
df_2022_bronx=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2022_bronx.csv")
df_2022_brooklyn=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2022_brooklyn.csv")
df_2022_manhattan=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2022_manhattan.csv")
df_2022_queens=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2022_queens.csv")
df_2022_staten_island=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2022_staten_island.csv")
df_2021_bronx=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2021_bronx.csv")
df_2021_brooklyn=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2021_brooklyn.csv")
df_2021_manhattan=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2021_manhattan.csv")
df_2021_queens=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2021_queens.csv")
df_2021_staten_island=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2021_staten_island.csv")
df_2020_bronx=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2020_bronx.csv")
df_2020_brooklyn=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2020_brooklyn.csv")
df_2020_manhattan=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2020_manhattan.csv")
df_2020_queens=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2020_queens.csv")
df_2020_staten_island=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2020_staten_island.csv")
df_2019_bronx=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2019_bronx.csv")
df_2019_brooklyn=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2019_brooklyn.csv")
df_2019_manhattan=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2019_manhattan.csv")
df_2019_queens=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2019_queens.csv")
df_2019_staten_island=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2019_statenisland.csv")
df_2018_bronx=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2018_bronx.csv")
df_2018_brooklyn=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2018_brooklyn.csv")
df_2018_manhattan=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2018_manhattan.csv")
df_2018_queens=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2018_queens.csv")
df_2018_staten_island=pd.read_csv("https://raw.githubusercontent.com/ChenzwNina/final_project_649/main/2018_statenisland.csv")

df_2022_bronx['new_SALE_PRICE'] = df_2022_bronx['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2022_bronx = df_2022_bronx.loc[~(df_2022_bronx['new_SALE_PRICE']==0)]
df_2022_bronx['new_GROSS_SQUARE_FEET'] = df_2022_bronx['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2022_bronx = df_2022_bronx.loc[~(df_2022_bronx['new_GROSS_SQUARE_FEET']==0)]
df_2022_bronx = df_2022_bronx[df_2022_bronx['new_GROSS_SQUARE_FEET'].notna()]
df_2022_bronx['average_price'] = df_2022_bronx['new_SALE_PRICE']/df_2022_bronx['new_GROSS_SQUARE_FEET']

df_2022_manhattan['new_SALE_PRICE'] = df_2022_manhattan['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2022_manhattan = df_2022_manhattan.loc[~(df_2022_manhattan['new_SALE_PRICE']==0)]
df_2022_manhattan['new_GROSS_SQUARE_FEET'] = df_2022_manhattan['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2022_manhattan = df_2022_manhattan.loc[~(df_2022_manhattan['new_GROSS_SQUARE_FEET']==0)]
df_2022_manhattan = df_2022_manhattan[df_2022_manhattan['new_GROSS_SQUARE_FEET'].notna()]
df_2022_manhattan['average_price'] = df_2022_manhattan['new_SALE_PRICE']/df_2022_manhattan['new_GROSS_SQUARE_FEET']

df_2022_brooklyn['new_SALE_PRICE'] = df_2022_brooklyn['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2022_brooklyn = df_2022_brooklyn.loc[~(df_2022_brooklyn['new_SALE_PRICE']==0)]
df_2022_brooklyn['new_GROSS_SQUARE_FEET'] = df_2022_brooklyn['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2022_brooklyn = df_2022_brooklyn.loc[~(df_2022_brooklyn['new_GROSS_SQUARE_FEET']==0)]
df_2022_brooklyn = df_2022_brooklyn[df_2022_brooklyn['new_GROSS_SQUARE_FEET'].notna()]
df_2022_brooklyn['average_price'] = df_2022_brooklyn['new_SALE_PRICE']/df_2022_brooklyn['new_GROSS_SQUARE_FEET']

df_2022_queens['new_SALE_PRICE'] = df_2022_queens['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2022_queens = df_2022_queens.loc[~(df_2022_queens['new_SALE_PRICE']==0)]
df_2022_queens['new_GROSS_SQUARE_FEET'] = df_2022_queens['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2022_queens = df_2022_queens.loc[~(df_2022_queens['new_GROSS_SQUARE_FEET']==0)]
df_2022_queens = df_2022_queens[df_2022_queens['new_GROSS_SQUARE_FEET'].notna()]
df_2022_queens['average_price'] = df_2022_queens['new_SALE_PRICE']/df_2022_queens['new_GROSS_SQUARE_FEET']

df_2022_staten_island['new_SALE_PRICE'] = df_2022_staten_island['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2022_staten_island = df_2022_staten_island.loc[~(df_2022_staten_island['new_SALE_PRICE']==0)]
df_2022_staten_island['new_GROSS_SQUARE_FEET'] = df_2022_staten_island['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2022_staten_island = df_2022_staten_island.loc[~(df_2022_staten_island['new_GROSS_SQUARE_FEET']==0)]
df_2022_staten_island = df_2022_staten_island[df_2022_staten_island['new_GROSS_SQUARE_FEET'].notna()]
df_2022_staten_island['average_price'] = df_2022_staten_island['new_SALE_PRICE']/df_2022_staten_island['new_GROSS_SQUARE_FEET']

df_2021_bronx['new_SALE_PRICE'] = df_2021_bronx['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2021_bronx = df_2021_bronx.loc[~(df_2021_bronx['new_SALE_PRICE']==0)]
df_2021_bronx['new_GROSS_SQUARE_FEET'] = df_2021_bronx['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2021_bronx = df_2021_bronx.loc[~(df_2021_bronx['new_GROSS_SQUARE_FEET']==0)]
df_2021_bronx = df_2021_bronx[df_2021_bronx['new_GROSS_SQUARE_FEET'].notna()]
df_2021_bronx['average_price'] = df_2021_bronx['new_SALE_PRICE']/df_2021_bronx['new_GROSS_SQUARE_FEET']

df_2021_manhattan['new_SALE_PRICE'] = df_2021_manhattan['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2021_manhattan = df_2021_manhattan.loc[~(df_2021_manhattan['new_SALE_PRICE']==0)]
df_2021_manhattan['new_GROSS_SQUARE_FEET'] = df_2021_manhattan['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2021_manhattan = df_2021_manhattan.loc[~(df_2021_manhattan['new_GROSS_SQUARE_FEET']==0)]
df_2021_manhattan = df_2021_manhattan[df_2021_manhattan['new_GROSS_SQUARE_FEET'].notna()]
df_2021_manhattan['average_price'] = df_2021_manhattan['new_SALE_PRICE']/df_2021_manhattan['new_GROSS_SQUARE_FEET']

df_2021_brooklyn['new_SALE_PRICE'] = df_2021_brooklyn['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2021_brooklyn = df_2021_brooklyn.loc[~(df_2021_brooklyn['new_SALE_PRICE']==0)]
df_2021_brooklyn['new_GROSS_SQUARE_FEET'] = df_2021_brooklyn['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2021_brooklyn = df_2021_brooklyn.loc[~(df_2021_brooklyn['new_GROSS_SQUARE_FEET']==0)]
df_2021_brooklyn = df_2021_brooklyn[df_2021_brooklyn['new_GROSS_SQUARE_FEET'].notna()]
df_2021_brooklyn['average_price'] = df_2021_brooklyn['new_SALE_PRICE']/df_2021_brooklyn['new_GROSS_SQUARE_FEET']

df_2021_queens['new_SALE_PRICE'] = df_2021_queens['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2021_queens = df_2021_queens.loc[~(df_2021_queens['new_SALE_PRICE']==0)]
df_2021_queens['new_GROSS_SQUARE_FEET'] = df_2021_queens['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2021_queens = df_2021_queens.loc[~(df_2021_queens['new_GROSS_SQUARE_FEET']==0)]
df_2021_queens = df_2021_queens[df_2021_queens['new_GROSS_SQUARE_FEET'].notna()]
df_2021_queens['average_price'] = df_2021_queens['new_SALE_PRICE']/df_2021_queens['new_GROSS_SQUARE_FEET']

df_2021_staten_island['new_SALE_PRICE'] = df_2021_staten_island['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2021_staten_island = df_2021_staten_island.loc[~(df_2021_staten_island['new_SALE_PRICE']==0)]
df_2021_staten_island['new_GROSS_SQUARE_FEET'] = df_2021_staten_island['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2021_staten_island = df_2021_staten_island.loc[~(df_2021_staten_island['new_GROSS_SQUARE_FEET']==0)]
df_2021_staten_island = df_2021_staten_island[df_2021_staten_island['new_GROSS_SQUARE_FEET'].notna()]
df_2021_staten_island['average_price'] = df_2021_staten_island['new_SALE_PRICE']/df_2021_staten_island['new_GROSS_SQUARE_FEET']

df_2020_bronx['new_SALE_PRICE'] = df_2020_bronx['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2020_bronx = df_2020_bronx.loc[~(df_2020_bronx['new_SALE_PRICE']==0)]
df_2020_bronx['new_GROSS_SQUARE_FEET'] = df_2020_bronx['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2020_bronx = df_2020_bronx.loc[~(df_2020_bronx['new_GROSS_SQUARE_FEET']==0)]
df_2020_bronx = df_2020_bronx[df_2020_bronx['new_GROSS_SQUARE_FEET'].notna()]
df_2020_bronx['average_price'] = df_2020_bronx['new_SALE_PRICE']/df_2020_bronx['new_GROSS_SQUARE_FEET']

df_2020_manhattan['new_SALE_PRICE'] = df_2020_manhattan['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2020_manhattan = df_2020_manhattan.loc[~(df_2020_manhattan['new_SALE_PRICE']==0)]
df_2020_manhattan['new_GROSS_SQUARE_FEET'] = df_2020_manhattan['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2020_manhattan = df_2020_manhattan.loc[~(df_2020_manhattan['new_GROSS_SQUARE_FEET']==0)]
df_2020_manhattan = df_2020_manhattan[df_2020_manhattan['new_GROSS_SQUARE_FEET'].notna()]
df_2020_manhattan['average_price'] = df_2020_manhattan['new_SALE_PRICE']/df_2020_manhattan['new_GROSS_SQUARE_FEET']

df_2020_brooklyn['new_SALE_PRICE'] = df_2020_brooklyn['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2020_brooklyn = df_2020_brooklyn.loc[~(df_2020_brooklyn['new_SALE_PRICE']==0)]
df_2020_brooklyn['new_GROSS_SQUARE_FEET'] = df_2020_brooklyn['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2020_brooklyn = df_2020_brooklyn.loc[~(df_2020_brooklyn['new_GROSS_SQUARE_FEET']==0)]
df_2020_brooklyn = df_2020_brooklyn[df_2020_brooklyn['new_GROSS_SQUARE_FEET'].notna()]
df_2020_brooklyn['average_price'] = df_2020_brooklyn['new_SALE_PRICE']/df_2020_brooklyn['new_GROSS_SQUARE_FEET']

df_2020_queens['new_SALE_PRICE'] = df_2020_queens['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2020_queens = df_2020_queens.loc[~(df_2020_queens['new_SALE_PRICE']==0)]
df_2020_queens['new_GROSS_SQUARE_FEET'] = df_2020_queens['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2020_queens = df_2020_queens.loc[~(df_2020_queens['new_GROSS_SQUARE_FEET']==0)]
df_2020_queens = df_2020_queens[df_2020_queens['new_GROSS_SQUARE_FEET'].notna()]
df_2020_queens['average_price'] = df_2020_queens['new_SALE_PRICE']/df_2020_queens['new_GROSS_SQUARE_FEET']

df_2020_staten_island['new_SALE_PRICE'] = df_2020_staten_island['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2020_staten_island = df_2020_staten_island.loc[~(df_2020_staten_island['new_SALE_PRICE']==0)]
df_2020_staten_island['new_GROSS_SQUARE_FEET'] = df_2020_staten_island['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2020_staten_island = df_2020_staten_island.loc[~(df_2020_staten_island['new_GROSS_SQUARE_FEET']==0)]
df_2020_staten_island = df_2020_staten_island[df_2020_staten_island['new_GROSS_SQUARE_FEET'].notna()]
df_2020_staten_island['average_price'] = df_2020_staten_island['new_SALE_PRICE']/df_2020_staten_island['new_GROSS_SQUARE_FEET']

df_2019_bronx['new_SALE_PRICE'] = df_2019_bronx['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2019_bronx = df_2019_bronx.loc[~(df_2019_bronx['new_SALE_PRICE']==0)]
df_2019_bronx['new_GROSS_SQUARE_FEET'] = df_2019_bronx['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2019_bronx = df_2019_bronx.loc[~(df_2019_bronx['new_GROSS_SQUARE_FEET']==0)]
df_2019_bronx = df_2019_bronx[df_2019_bronx['new_GROSS_SQUARE_FEET'].notna()]
df_2019_bronx['average_price'] = df_2019_bronx['new_SALE_PRICE']/df_2019_bronx['new_GROSS_SQUARE_FEET']


df_2019_manhattan['new_SALE_PRICE'] = df_2019_manhattan['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2019_manhattan = df_2019_manhattan.loc[~(df_2019_manhattan['new_SALE_PRICE']==0)]
df_2019_manhattan['new_GROSS_SQUARE_FEET'] = df_2019_manhattan['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2019_manhattan = df_2019_manhattan.loc[~(df_2019_manhattan['new_GROSS_SQUARE_FEET']==0)]
df_2019_manhattan = df_2019_manhattan[df_2019_manhattan['new_GROSS_SQUARE_FEET'].notna()]
df_2019_manhattan['average_price'] = df_2019_manhattan['new_SALE_PRICE']/df_2019_manhattan['new_GROSS_SQUARE_FEET']

df_2019_brooklyn['new_SALE_PRICE'] = df_2019_brooklyn['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2019_brooklyn = df_2019_brooklyn.loc[~(df_2019_brooklyn['new_SALE_PRICE']==0)]
df_2019_brooklyn['new_GROSS_SQUARE_FEET'] = df_2019_brooklyn['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2019_brooklyn = df_2019_brooklyn.loc[~(df_2019_brooklyn['new_GROSS_SQUARE_FEET']==0)]
df_2019_brooklyn = df_2019_brooklyn[df_2019_brooklyn['new_GROSS_SQUARE_FEET'].notna()]
df_2019_brooklyn['average_price'] = df_2019_brooklyn['new_SALE_PRICE']/df_2019_brooklyn['new_GROSS_SQUARE_FEET']

df_2019_queens['new_SALE_PRICE'] = df_2019_queens['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2019_queens = df_2019_queens.loc[~(df_2019_queens['new_SALE_PRICE']==0)]
df_2019_queens['new_GROSS_SQUARE_FEET'] = df_2019_queens['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2019_queens = df_2019_queens.loc[~(df_2019_queens['new_GROSS_SQUARE_FEET']==0)]
df_2019_queens = df_2019_queens[df_2019_queens['new_GROSS_SQUARE_FEET'].notna()]
df_2019_queens['average_price'] = df_2019_queens['new_SALE_PRICE']/df_2019_queens['new_GROSS_SQUARE_FEET']

df_2019_staten_island['new_SALE_PRICE'] = df_2019_staten_island['SALE_PRICE'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2019_staten_island = df_2019_staten_island.loc[~(df_2019_staten_island['new_SALE_PRICE']==0)]
df_2019_staten_island['new_GROSS_SQUARE_FEET'] = df_2019_staten_island['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2019_staten_island = df_2019_staten_island.loc[~(df_2019_staten_island['new_GROSS_SQUARE_FEET']==0)]
df_2019_staten_island = df_2019_staten_island[df_2019_staten_island['new_GROSS_SQUARE_FEET'].notna()]
df_2019_staten_island['average_price'] = df_2019_staten_island['new_SALE_PRICE']/df_2019_staten_island['new_GROSS_SQUARE_FEET']

df_2018_bronx['new_SALE_PRICE'] = df_2018_bronx['SALE_PRICE'].str.replace('$','').str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2018_bronx = df_2018_bronx.loc[~(df_2018_bronx['new_SALE_PRICE']==0.0)]
df_2018_bronx['new_GROSS_SQUARE_FEET'] = df_2018_bronx['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2018_bronx = df_2018_bronx.loc[~(df_2018_bronx['new_GROSS_SQUARE_FEET']==0)]
df_2018_bronx = df_2018_bronx[df_2018_bronx['new_GROSS_SQUARE_FEET'].notna()]
df_2018_bronx['average_price'] = df_2018_bronx['new_SALE_PRICE']/df_2018_bronx['new_GROSS_SQUARE_FEET']

df_2018_manhattan['new_SALE_PRICE'] = df_2018_manhattan['SALE_PRICE'].str.replace('$','').str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2018_manhattan = df_2018_manhattan.loc[~(df_2018_manhattan['new_SALE_PRICE']==0.0)]
df_2018_manhattan['new_GROSS_SQUARE_FEET'] = df_2018_manhattan['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2018_manhattan = df_2018_manhattan.loc[~(df_2018_manhattan['new_GROSS_SQUARE_FEET']==0.0)]
df_2018_manhattan = df_2018_manhattan[df_2018_manhattan['new_GROSS_SQUARE_FEET'].notna()]
df_2018_manhattan['average_price'] = df_2018_manhattan['new_SALE_PRICE']/df_2018_manhattan['new_GROSS_SQUARE_FEET']

df_2018_brooklyn['new_SALE_PRICE'] = df_2018_brooklyn['SALE_PRICE'].str.replace('$','').str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2018_brooklyn = df_2018_brooklyn.loc[~(df_2018_brooklyn['new_SALE_PRICE']==0.0)]
df_2018_brooklyn['new_GROSS_SQUARE_FEET'] = df_2018_brooklyn['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2018_brooklyn = df_2018_brooklyn.loc[~(df_2018_brooklyn['new_GROSS_SQUARE_FEET']==0.0)]
df_2018_brooklyn = df_2018_brooklyn[df_2018_brooklyn['new_GROSS_SQUARE_FEET'].notna()]
df_2018_brooklyn['average_price'] = df_2018_brooklyn['new_SALE_PRICE']/df_2018_brooklyn['new_GROSS_SQUARE_FEET']

df_2018_queens['new_SALE_PRICE'] = df_2018_queens['SALE_PRICE'].str.replace('$','').str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2018_queens = df_2018_queens.loc[~(df_2018_queens['new_SALE_PRICE']==0.0)]
df_2018_queens['new_GROSS_SQUARE_FEET'] = df_2018_queens['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2018_queens = df_2018_queens.loc[~(df_2018_queens['new_GROSS_SQUARE_FEET']==0.0)]
df_2018_queens = df_2018_queens[df_2018_queens['new_GROSS_SQUARE_FEET'].notna()]
df_2018_queens['average_price'] = df_2018_queens['new_SALE_PRICE']/df_2018_queens['new_GROSS_SQUARE_FEET']

df_2018_staten_island['new_SALE_PRICE'] = df_2018_staten_island['SALE_PRICE'].str.replace('$','').str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2018_staten_island = df_2018_staten_island.loc[~(df_2018_staten_island['new_SALE_PRICE']==0.0)]
df_2018_staten_island['new_GROSS_SQUARE_FEET'] = df_2018_staten_island['GROSS_SQUARE_FEET'].str.replace(',','').apply (pd.to_numeric, errors='coerce')
df_2018_staten_island = df_2018_staten_island.loc[~(df_2018_staten_island['new_GROSS_SQUARE_FEET']==0.0)]
df_2018_staten_island = df_2018_staten_island[df_2018_staten_island['new_GROSS_SQUARE_FEET'].notna()]
df_2018_staten_island['average_price'] = df_2018_staten_island['new_SALE_PRICE']/df_2018_staten_island['new_GROSS_SQUARE_FEET']

df_bronx_price_2022 = df_2022_bronx['average_price'].median()
df_bronx_price_2022_75 = np.percentile(df_2022_bronx['average_price'].values,75)
df_bronx_price_2022_25 = np.percentile(df_2022_bronx['average_price'].values,25)
df_manhattan_price_2022 = df_2022_manhattan['average_price'].median()
df_manhattan_price_2022_75 = np.percentile(df_2022_manhattan['average_price'].values,75)
df_manhattan_price_2022_25 = np.percentile(df_2022_manhattan['average_price'].values,25)
df_brooklyn_price_2022 = df_2022_brooklyn['average_price'].median()
df_brooklyn_price_2022_75 = np.percentile(df_2022_brooklyn['average_price'].values,75)
df_brooklyn_price_2022_25 = np.percentile(df_2022_brooklyn['average_price'].values,25)
df_queens_price_2022 = df_2022_queens['average_price'].median()
df_queens_price_2022_75 = np.percentile(df_2022_queens['average_price'].values,75)
df_queens_price_2022_25 = np.percentile(df_2022_queens['average_price'].values,25)
df_staten_island_price_2022 = df_2022_staten_island['average_price'].median()
df_staten_island_price_2022_75 = np.percentile(df_2022_staten_island['average_price'].values,75)
df_staten_island_price_2022_25 = np.percentile(df_2022_staten_island['average_price'].values,25)

df_bronx_price_2021 = df_2021_bronx['average_price'].median()
df_bronx_price_2021_75 = np.percentile(df_2021_bronx['average_price'].values,75)
df_bronx_price_2021_25 = np.percentile(df_2021_bronx['average_price'].values,25)
df_manhattan_price_2021 = df_2021_manhattan['average_price'].median()
df_manhattan_price_2021_75 = np.percentile(df_2021_manhattan['average_price'].values,75)
df_manhattan_price_2021_25 = np.percentile(df_2021_manhattan['average_price'].values,25)
df_brooklyn_price_2021 = df_2021_brooklyn['average_price'].median()
df_brooklyn_price_2021_75 = np.percentile(df_2021_brooklyn['average_price'].values,75)
df_brooklyn_price_2021_25 = np.percentile(df_2021_brooklyn['average_price'].values,25)
df_queens_price_2021 = df_2021_queens['average_price'].median()
df_queens_price_2021_75 = np.percentile(df_2021_queens['average_price'].values,75)
df_queens_price_2021_25 = np.percentile(df_2021_queens['average_price'].values,25)
df_staten_island_price_2021 = df_2021_staten_island['average_price'].median()
df_staten_island_price_2021_75 = np.percentile(df_2021_staten_island['average_price'].values,75)
df_staten_island_price_2021_25 = np.percentile(df_2021_staten_island['average_price'].values,25)

df_bronx_price_2020 = df_2020_bronx['average_price'].median()
df_bronx_price_2020_75 = np.percentile(df_2020_bronx['average_price'].values,75)
df_bronx_price_2020_25 = np.percentile(df_2020_bronx['average_price'].values,25)
df_manhattan_price_2020 = df_2020_manhattan['average_price'].median()
df_manhattan_price_2020_75 = np.percentile(df_2020_manhattan['average_price'].values,75)
df_manhattan_price_2020_25 = np.percentile(df_2020_manhattan['average_price'].values,25)
df_brooklyn_price_2020 = df_2020_brooklyn['average_price'].median()
df_brooklyn_price_2020_75 = np.percentile(df_2020_brooklyn['average_price'].values,75)
df_brooklyn_price_2020_25 = np.percentile(df_2020_brooklyn['average_price'].values,25)
df_queens_price_2020 = df_2020_queens['average_price'].median()
df_queens_price_2020_75 = np.percentile(df_2020_queens['average_price'].values,75)
df_queens_price_2020_25 = np.percentile(df_2020_queens['average_price'].values,25)
df_staten_island_price_2020 = df_2020_staten_island['average_price'].median()
df_staten_island_price_2020_75 = np.percentile(df_2020_staten_island['average_price'].values,75)
df_staten_island_price_2020_25 = np.percentile(df_2020_staten_island['average_price'].values,25)

df_bronx_price_2019 = df_2019_bronx['average_price'].median()
df_bronx_price_2019_75 = np.percentile(df_2019_bronx['average_price'].values,75)
df_bronx_price_2019_25 = np.percentile(df_2019_bronx['average_price'].values,25)
df_manhattan_price_2019 = df_2019_manhattan['average_price'].median()
df_manhattan_price_2019_75 = np.percentile(df_2019_manhattan['average_price'].values,75)
df_manhattan_price_2019_25 = np.percentile(df_2019_manhattan['average_price'].values,25)
df_brooklyn_price_2019 = df_2019_brooklyn['average_price'].median()
df_brooklyn_price_2019_75 = np.percentile(df_2019_brooklyn['average_price'].values,75)
df_brooklyn_price_2019_25 = np.percentile(df_2019_brooklyn['average_price'].values,25)
df_queens_price_2019 = df_2019_queens['average_price'].median()
df_queens_price_2019_75 = np.percentile(df_2019_queens['average_price'].values,75)
df_queens_price_2019_25 = np.percentile(df_2019_queens['average_price'].values,25)
df_staten_island_price_2019 = df_2019_staten_island['average_price'].median()
df_staten_island_price_2019_75 = np.percentile(df_2019_staten_island['average_price'].values,75)
df_staten_island_price_2019_25 = np.percentile(df_2019_staten_island['average_price'].values,25)

df_bronx_price_2018 = df_2018_bronx['average_price'].median()
df_bronx_price_2018_75 = np.percentile(df_2018_bronx['average_price'].values,75)
df_bronx_price_2018_25 = np.percentile(df_2018_bronx['average_price'].values,25)
df_manhattan_price_2018 = df_2018_manhattan['average_price'].median()
df_manhattan_price_2018_75 = np.percentile(df_2018_manhattan['average_price'].values,75)
df_manhattan_price_2018_25 = np.percentile(df_2018_manhattan['average_price'].values,25)
df_brooklyn_price_2018 = df_2018_brooklyn['average_price'].median()
df_brooklyn_price_2018_75 = np.percentile(df_2018_brooklyn['average_price'].values,75)
df_brooklyn_price_2018_25 = np.percentile(df_2018_brooklyn['average_price'].values,25)
df_queens_price_2018 = df_2018_queens['average_price'].median()
df_queens_price_2018_75 = np.percentile(df_2018_queens['average_price'].values,75)
df_queens_price_2018_25 = np.percentile(df_2018_queens['average_price'].values,25)
df_staten_island_price_2018 = df_2018_staten_island['average_price'].median()
df_staten_island_price_2018_75 = np.percentile(df_2018_staten_island['average_price'].values,75)
df_staten_island_price_2018_25 = np.percentile(df_2018_staten_island['average_price'].values,25)

data = [['bronx','2022', df_bronx_price_2022, df_bronx_price_2022_75, df_bronx_price_2022_25], 
        ['manhattan','2022', df_manhattan_price_2022, df_manhattan_price_2022_75, df_manhattan_price_2022_25], 
        ['brooklyn','2022', df_brooklyn_price_2022, df_brooklyn_price_2022_75, df_brooklyn_price_2022_25],
        ['queens','2022',df_queens_price_2022, df_queens_price_2022_75, df_queens_price_2022_25], 
        ['staten island','2022',df_staten_island_price_2022, df_staten_island_price_2022_75, df_staten_island_price_2022_25],
        ['bronx','2021', df_bronx_price_2021, df_bronx_price_2021_75, df_bronx_price_2021_25], 
        ['manhattan','2021', df_manhattan_price_2021, df_manhattan_price_2021_75, df_manhattan_price_2021_25], 
        ['brooklyn','2021', df_brooklyn_price_2021, df_brooklyn_price_2022_75, df_brooklyn_price_2022_25],
        ['queens','2021',df_queens_price_2021, df_queens_price_2021_75, df_queens_price_2021_25], 
        ['staten island','2021',df_staten_island_price_2021, df_staten_island_price_2021_75, df_staten_island_price_2021_25], 
        ['bronx','2020', df_bronx_price_2020, df_bronx_price_2020_75, df_bronx_price_2020_25], 
        ['manhattan','2020', df_manhattan_price_2020, df_manhattan_price_2020_75, df_manhattan_price_2020_25], 
        ['brooklyn','2020', df_brooklyn_price_2020, df_brooklyn_price_2020_75, df_brooklyn_price_2020_25],
        ['queens','2020',df_queens_price_2020,  df_queens_price_2020_75, df_queens_price_2020_25], 
        ['staten island','2020',df_staten_island_price_2020, df_staten_island_price_2020_75, df_staten_island_price_2020_25],
        ['bronx','2019', df_bronx_price_2019, df_bronx_price_2019_75, df_bronx_price_2019_25], 
        ['manhattan','2019',df_manhattan_price_2019, df_manhattan_price_2019_75, df_manhattan_price_2019_25], 
        ['brooklyn','2019', df_brooklyn_price_2019, df_brooklyn_price_2019_75, df_brooklyn_price_2019_25], 
        ['queens','2019',df_queens_price_2019, df_queens_price_2019_75, df_queens_price_2019_25], 
        ['staten island','2019',df_staten_island_price_2019, df_staten_island_price_2019_75, df_staten_island_price_2019_25],
        ['bronx','2018', df_bronx_price_2018, df_bronx_price_2018_75, df_bronx_price_2018_25], 
        ['manhattan','2018', df_manhattan_price_2018, df_manhattan_price_2018_75, df_manhattan_price_2018_25], 
        ['brooklyn','2018', df_brooklyn_price_2018, df_brooklyn_price_2018_75, df_brooklyn_price_2018_25],
        ['queens','2018', df_queens_price_2018, df_queens_price_2018_75, df_queens_price_2018_25], 
        ['staten island','2018',df_staten_island_price_2018, df_staten_island_price_2018_75, df_staten_island_price_2018_25]]

df1 = pd.DataFrame(data, columns=['district','year','price','75_percentile','25_percentile'])


image = Image.open('Park.png')
# Add some text

st.sidebar.title("About")
st.sidebar.info(
        """
        This walkability dashboard was created by Nina Chen, Fiona Fox, Haley Johnson, Gurleen Kaur, and Avanti Paturkar
        as a final project for SI 649 at the University of Michigan. We examine housing prices, food access, and nearby
        amenities to see how they might be related to walkability in New York City.
        """
    )


# Display the table
#st.table(cars.head())

# Drop down menu to select a variable


# Create a slider for # of cylinders


# Create the chart
nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['year'], empty='none', clear="mouseout")
pan_zoom = alt.selection_interval(bind="scales", encodings=["y"])

line_chart = alt.Chart(df1, title='Median Housing Price Per Square Foot in NYC Districts 2018-2022', width=500).mark_line(size=2.5).encode(
    x=alt.X('year:O', title=None),
    y=alt.Y('price:Q'),
    color='district:N'
)

selectors = alt.Chart(df1).mark_point().encode(
    x='year:O',
    y=alt.Y('price', title='Median Price'),
    opacity=alt.value(0),
).add_selection(
    nearest, pan_zoom
)

points = line_chart.mark_point(size=90).encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)

text = line_chart.mark_text(align='left', dx=7, fontSize=14).encode(
    text=alt.condition(nearest, alt.Text('price:Q', format=',.02f'), alt.value(' '))
)

vline = alt.Chart(df1).mark_rule(size=4, color='lightgray').encode(
    x='year:O',
).transform_filter(
    nearest
)

errorbars = alt.Chart(df1, title='25% and 75% Percentile of Housing Price Per Square Foot', width=500).mark_errorbar(ticks=True).encode(
    x="year:O",
    y=alt.Y('25_percentile', title='Housing Price'),
    y2="75_percentile:Q",
    color='district:N'
)

chart1 = alt.layer(
    line_chart, vline, selectors, points, text)

chart2 = errorbars

chart = alt.vconcat(chart1, chart2).resolve_scale(y="shared")





import streamlit.components.v1 as components



HtmlFile = open("food_plot.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
image2 = Image.open('bivariate_map_final.png')

    
tab1, tab2, tab3, tab4 = st.tabs(['Walkability in Urban Neighborhoods','Walkability Score and Food Access', 'Housing Prices', 'Bivariate Map of Walkability and Housing Prices'])







# Display the chart with a different theme on each tab
with tab3:
    st.altair_chart(chart, theme=None)
    st.caption(
        """
        Trend: Housing prices in Manhattan are the highest among the five districts. However, there is a noticeable drop in housing prices in 2019, which continues to worsen in 2020. Prices experience a slight increase in 2021 but then decrease again in 2022. Bronx, Queens, Staten Island, and Brooklyn: In contrast to Manhattan, these districts generally experience a steady increase in housing prices during the observed period.

        Possible Explanation: The pandemic had a significant impact on the housing market, particularly in densely populated urban areas like Manhattan.  As remote work gained traction during the pandemic, many employees realized that they no longer needed to live close to their workplace. As a result, some Manhattan residents relocated to less expensive areas in the other four districts. This increased demand led to a rise in housing prices in those areas
        """)
with tab1:
    st.image(image)
with tab2:
    components.html(source_code,height = 400,width=10000)
    st.caption("Farmers markets and community gardens provide neighborhoods with access to fresh, healthy produce. Unfortunately, many New Yorkers don’t have access to them. Farmers market and community garden tend to generally be located in more walkable neighborhoods. Some of these neighborhoods have a high proportion of residents receiving Supplemental Nutrition Assistance Program (SNAP) benefits, but many parts of New York City with high levels of food insecurity are far away from farmers markets and community gardens. Having access to fresh food in the places people live is an important part of creating equitable and adaptable food systems.")
with tab4:
    st.image(image2)

