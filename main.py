# -*- coding: utf-8 -*-
"""
Simple Application to plot the average magnitude of earthquakes over the last
7 days

@author: Nikos
"""

import tkinter
import urllib.request, json
#import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

#function for ploting magnitude using matplotlib
def plotData():
    # Set up for info from GeoJSON Feed
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    
    # Create matlibplot
    plot = Figure(figsize = (10,10),
               dpi = 100)
    # Grabbing mag values
    magnitude = []
    sumMag = 0
    count = 0
    for items in data['features']:
        count += 1
        magnitude.append(items['properties']['mag'])
        sumMag += items['properties']['mag']
    average = sumMag / count
    x=[0,count]
    # Adding values to plot via subplot
    subPlot = plot.add_subplot(1,1,1)
    subPlot.plot(magnitude, color='r', label='magnitude')
    subPlot.plot(x, [average, average], color='b', label='average')
    subPlot.legend(loc=0)
    # Tkinter setup
    window = FigureCanvasTkAgg(plot, master = app)
    window.draw()
    window.get_tk_widget()

    window.get_tk_widget().pack()
# Tk app setup
app = tkinter.Tk()
app.geometry("1000x1000")
plot_button = tkinter.Button(master = app, 
                     command = plotData,
                     height = 2, 
                     width = 10,
                     text = "Update")
plot_button.pack()
# Run app
app.mainloop()

