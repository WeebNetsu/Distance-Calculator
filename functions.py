# By Stephen van der Westhuizen

from geopy.geocoders import Nominatim # https://pypi.org/project/geopy/
from geopy.distance import great_circle
from tkinter import Label, messagebox

mesure = "Kilometer" # default mesuing

def setMesure(event): # event because it is triggered by an event
	global mesure
	mesure = event # event is also what is selected inside the drop down

def callback(event, root):
    root.after(50, select_all, event.widget)

def select_all(widget): # allows ctrl+a to select all the text
    # select text
    widget.select_range(0, 'end')
    # move cursor to the end
    widget.icursor('end')

def calcDistance(place1, place2, lbl, root):
	global mesure

	geolocator = Nominatim(user_agent="dister")
	location1 = geolocator.geocode(place1)
	location2 = geolocator.geocode(place2)

	try: # may return error if no location can be found
		location1 = (location1.latitude, location1.longitude)
		location2 = (location2.latitude, location2.longitude)
	except AttributeError as e:
		messagebox.showerror("No location found", "Please check your locations, one or both could not be found...")
		return

	if mesure == "Kilometer":
		distance = great_circle(location1, location2).km;	
		distance = "{:.2f}".format(distance) + " km"
	elif mesure == "Meter":
		distance = great_circle(location1, location2).m;	
		distance = "{:.2f}".format(distance) + " m"
	elif mesure == "Mile":
		distance = great_circle(location1, location2).mi;	
		distance = "{:.2f}".format(distance) + " mi"
	else:
		distance = great_circle(location1, location2).ft;	
		distance = "{:.2f}".format(distance) + " ft"

	lbl = Label(root, text=distance, width=20)
	lbl.grid(row=4, column=0, columnspan=3, pady=10)

def giveHelp():
	messagebox.showinfo("More info!", "Dister can be used to get the distance between 2 locations.\nFor more help, visit the github page: https://www.github.com/....")