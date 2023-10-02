
#import item serial number
from airpoditem import *

#import additional libraries
import csv
import folium
from folium import plugins
import eviltransform
import schedule
import time
import pandas as pd


# user defined parameters wahoo
# 172800000 is 2 days in miliseconds lmao
timeinhour = 48
timeCutoff = timeinhour * 3600000
# opacity decay in hours
opacitydecayinterval = 1
opacityinterval = opacitydecayinterval * 3600000

circleradius = 3




def opacity_gen(dt,opacitydecayinterval):
    interval = round(dt/opacitydecayinterval)
    if interval <= 0:
        return 1
    elif 1/interval < 0.4:
        return 0.4
    else:
        return 1/(interval)


def rgba_to_hex(r, g, b, a):
    return "#{:02x}{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255), int(a * 255))

def hex_to_rgb(hex_color):
    # Remove the '#' symbol if present
    hex_color = hex_color.lstrip('#')

    # Ensure the hex color is 6 characters long
    if len(hex_color) != 6:
        raise ValueError("Invalid hex color. It should be in the format RRGGBB.")

    # Split the hex color into RGB components
    r = int(hex_color[0:2], 16) /255
    g = int(hex_color[2:4], 16) /255
    b = int(hex_color[4:6], 16) /255

    return (r, g, b)


def getlatestTime(filelocation,columninterest):
    csv_reader = pd.read_csv(filelocation)


    # specific_row = csv_reader.iloc[300]

    total_rows = csv_reader.shape[0] -1

    specific_value = csv_reader.loc[total_rows, columninterest]

    return specific_value
    # print (total_rows)
    # print (specific_value)

# print(getlatestTime('Mapgen/Airtags.csv',"locationtimestamp"))


# below is a function to turn serial number input into coords scraped from cvs file lmao
def formatCoord(serialNumber):
    with open('Mapgen/Airtags.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)


        line_count = 0
        coordinates = []
        timstamplocation = []
        latesttime = getlatestTime('Mapgen/Airtags.csv',"locationtimestamp")
        deltatime = 0


        for row in csv_reader:
    
            deltatime = latesttime-int((f'{row["locationtimestamp"]}'))
            if line_count == 0:
                line_count += 1
                
                
            elif str(f'\t{row["serialnumber"]}').strip() == str(serialNumber) and deltatime < timeCutoff and float(f'\t{row["locationhorizontalaccuracy"]}')<100:
#            if less than time cutoff, and matches is correct serial number, and is accurate, then do that below
                if line_count < 3:
                    currentlist = eviltransform.gcj2wgs_exact(float(f'\t{row["locationlatitude"]}'),float(f'\t{row["locationlongitude"]}'))
                    coordinates.append(currentlist)

                currentlist = eviltransform.gcj2wgs_exact(float(f'\t{row["locationlatitude"]}'),float(f'\t{row["locationlongitude"]}'))
                coordinates.append(currentlist)
                
#                connect lines
                group.add_child(
                    folium.PolyLine(
                    smooth_factor=3,
                    locations=coordinates,
                    color=rgba_to_hex(hex_to_rgb(lineColor)[0]*opacity_gen(deltatime,opacityinterval), hex_to_rgb(lineColor)[1]*opacity_gen(deltatime,opacityinterval), hex_to_rgb(lineColor)[2]*opacity_gen(deltatime,opacityinterval), .7),
                    weight=5,
                     popup=str(f'\t{row["name"]}'),
                    ))
#               add markers
                    
                group.add_child(
                    folium.CircleMarker(eviltransform.gcj2wgs_exact(float(f'\t{row["locationlatitude"]}'),float(f'\t{row["locationlongitude"]}')), tooltip=str(f'\t{row["datetime"]}'),
                    radius=circleradius,
                    color=rgba_to_hex(opacity_gen(deltatime,opacityinterval),opacity_gen(deltatime,opacityinterval),1-opacity_gen(deltatime,opacityinterval)/1.5, 1))



                    )


                coordinates.pop(0)
                line_count += 1


    currentlist = eviltransform.gcj2wgs_exact(float(f'\t{row["locationlatitude"]}'),float(f'\t{row["locationlongitude"]}'))
    return coordinates




# Create an empty list to store FeatureGroup instances
feature_groups = []

# loop amount of items in array human name
n = len(humanname)

# make n feature group
for i in range(n):
    feature_group_name = humanname[i]  # Name for each FeatureGroup
    feature_group = folium.FeatureGroup(name=feature_group_name)
    feature_groups.append(feature_group)


looop = 0


# Create a map
m = folium.Map(tiles="cartodbdark_matter")

# Add markers and line to feature group instance n times
for group in feature_groups:
    formatCoord(items[looop])
    m.add_child(group)
    looop += 1


# Add a LayerControl to the map, allowing users to toggle the layers
m.fit_bounds(m.get_bounds(), padding=(30, 30))
folium.FitOverlays(fly = 1).add_to(m)
folium.LayerControl().add_to(m)

# Display the map
m.save("public/airpodsmap.html")
# print (hex_to_rgb(lineColor)[0])
