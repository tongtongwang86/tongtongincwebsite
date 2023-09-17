
#import item serial number
from ItemsToTrack import *
print (len(items))

#import additional libraries
import csv
import folium
from folium import plugins
import eviltransform
import schedule
import time

timeCutoff =500


# below is a function to turn serial number input into coords scraped from cvs file lmao
def formatCoord(serialNumber):
    with open('Mapgen/Airtags.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 1
        coordinates = []
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            elif str(f'\t{row["serialnumber"]}').strip() == str(serialNumber) :

                
                lastnumber = int(sum(1 for row in csv_reader))
                for row in csv_reader:
                    
                print (lastnumber)
                print (row)
                print (str(f'\t{10["locationtimestamp"]}'))
                # locationtimestamp
                # print (sum(1 for row in csv_reader))
                # print (int(f'\t{row["locationtimestamp"]}'))
                # print (int(f'\t{sum(1 for row in csv_reader)["locationtimestamp"]}'))
                # print (int(f'\t{sum(1 for row in csv_reader)["locationtimestamp"]}'))
                # print (int(f'\t{row["locationtimestamp"]}') - int(f'\t{sum(1 for row in csv_reader)["locationtimestamp"]}'))
                currentlist = eviltransform.gcj2wgs_exact(float(f'\t{row["locationlatitude"]}'),float(f'\t{row["locationlongitude"]}'))
                coordinates.append(currentlist)
        return coordinates

def plotMarkers(serialNumber):
    with open('Mapgen/Airtags.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 1
     
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            elif str(f'\t{row["serialnumber"]}').strip() == str(serialNumber) :
                
                currentlist = eviltransform.gcj2wgs_exact(float(f'\t{row["locationlatitude"]}'),float(f'\t{row["locationlongitude"]}'))
               
                
                folium.CircleMarker(currentlist,radius=4, popup=str(f'\t{row["datetime"]}')
                ).add_to(promax)
                
                





m = folium.Map(tiles="cartodbdark_matter")

# folium.TileLayer('cartodbdark_matter').add_to(m)
# loop for numbers of items, add to layers
promax = folium.FeatureGroup(name="ProMax").add_to(m)
lostair = folium.FeatureGroup(name="LostAirpods",show=False).add_to(m)

icon_plane = folium.plugins.BeautifyIcon(
    icon="plane", border_color="#b3334f", text_color="#b3334f", icon_shape="triangle"
)


for i in range(len(items)):
    
    if (i==0):
     
    #   ---draw line---
        folium.PolyLine(
        smooth_factor=1,
        locations = formatCoord(items[i])[-timeCutoff:], 
        color=lineColor,
        weight=5,
        tooltip=str(humanname[i]),
        ).add_to(promax)
    #   ---drawpoints---
    
        with open('Mapgen/Airtags.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = (sum(1 for row in csv_reader) -timeCutoff)
            # print (sum(1 for row in csv_reader) )
            for row in csv_reader :
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                elif str(f'\t{row["serialnumber"]}').strip() == str(items[i]) :
                    
                    currentlist = eviltransform.gcj2wgs_exact(float(f'\t{row["locationlatitude"]}'),float(f'\t{row["locationlongitude"]}'))
                   
                    
                    folium.CircleMarker(currentlist,radius=2,color=markerColor, popup=str(f'\t{row["datetime"]}')
                    ).add_to(promax)
        
        
      
    elif (i==1):
        folium.PolyLine(
        smooth_factor=1,
        locations=formatCoord(items[i]),
        color=lineColor,
        weight=5,
        tooltip=str(humanname[i]),
        ).add_to(lostair)
    #   ---drawpoints---
        with open('Mapgen/Airtags.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 1
         
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                elif str(f'\t{row["serialnumber"]}').strip() == str(items[i]) :
                    
                    currentlist = eviltransform.gcj2wgs_exact(float(f'\t{row["locationlatitude"]}'),float(f'\t{row["locationlongitude"]}'))
                   
                    
                    folium.CircleMarker(currentlist, radius=4,color=markerColor, popup=str(f'\t{row["datetime"]}')
                    ).add_to(lostair)

    

#folium.FitOverlays().add_to(m)
m.fit_bounds(m.get_bounds(), padding=(30, 30))
folium.LayerControl().add_to(m)

m.save("views/Map/map.html")
