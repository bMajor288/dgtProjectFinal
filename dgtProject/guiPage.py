from tkinter import *
from tkcalendar import *
import time
# import apiSetup
import gifCode

root = Tk()
root.geometry("200x430") #same as wireframe dimensions
root.title("Super Space Scanner") #Not the final name of the app
root.minsize(200,430)

#Setting background
root.configure(bg="black")

# object_number = apiSetup.object_number

#Creating functions
def alternate_title(): #NOT WORKING
    number = 0
    while True:
        lang_title = titles[number]
        lang_menu.title(lang_title)
        time.wait(2)
        number += 1
        if number >= len(titles):
            number = 0
            continue
def open_language_menu():
    lang_menu = Toplevel(root)
    lang_menu.title(lang_title)
    # Label(lang_menu, text="Language options will appear here").pack()
    alternate_title()
def open_plus_menu():
    pass
def open_settings():
    settings = Toplevel(root)
    settings.title("Settings")
    
    startCal = Calendar(settings, setmode = "day", date_pattern = "yyyy-mm-dd")
    startCal.pack(side=LEFT)
    endCal = Calendar(settings, setmode = "day", date_pattern = "yyyy-mm-dd")
    endCal.pack(side=RIGHT)
    openCal = Button(settings, text="Select Date", command = None)
    openCal.pack(side=BOTTOM)
    # print(apiSetup.new_link)
def goto_prev_event():
#     object_number -= 1
#     if object_number < 0:
#         object_number = apiSetup.parse_json["element_count"]
    pass
def goto_next_event():
#     object_number += 1
#     if object_number > apiSetup.parse_json["element_count"]:
#         object_number = 0
    pass
def show_event_details():
    description = Toplevel(root)
    description.title("Description")
    Label(description, textvariable=current_description).pack()

#Creating frames
top_frame = Frame(root, bg="black")
top_frame.grid(row=0, column=0)
middle_frame = Frame(root, bg="black")
middle_frame.grid(row=1, column=0)
location_frame = Frame(root, bg="black")
location_frame.grid(row=2, column=0)
bottom_frame = Frame(root, bg="black")
bottom_frame.grid(row=3, column=0)

#SETTING VARIABLES
#Regular variable
lang_title = None
lang_menu = None
#Arrays
titles = ["Select a language", "selecciona un idioma", "选择一种语言", "whiriwhiria he reo"]
dict_keys = ["near_earth_object", ""]
#Dictionaries
event_definitions = {
    "near_earth_object":"A near-Earth object (NEO) is any small Solar System body whose orbit brings it into proximity with Earth.\nThese are mostly asteroids or comets.",

}
#StringVar
current_event = StringVar()
current_event.set("Solar Eclipse")
current_countdown = StringVar()
current_countdown.set("16:19")
current_city = StringVar()
current_city.set("Auckland")
current_country = StringVar()
current_country.set("New Zealand")
current_description = StringVar()
current_description.set(event_definitions.get("near_earth_object"))

##Setting icon images
#img=ImageTk.PhotoImage(file="assets/left_arrow.png")
#middle frame
left_arrow = PhotoImage(file="assets/left_arrow_resized.png")#, width=40, height=50)
event_image = Label
right_arrow = PhotoImage(file="assets/right_arrow_resized.png")#, width=40, height=50)
#bottom frame
translate_image = PhotoImage(file="assets/translate_image_resized.png")
plus_image = PhotoImage(file="assets/plus_image_resized.png")
settings_image = PhotoImage(file="assets/settings_button_resized.png")

##Setting labels
#labels in the top frame
next_event_text = Label(top_frame, text="NEXT EVENT:", fg="#7843e6", bg="black")
next_event_text.grid(row=0, column=0)
event_label = Label(top_frame, textvariable=current_event, fg="#ffca28", bg="black")
event_label.grid(row=1, column=0)
countdown_label = Label(top_frame, textvariable=current_countdown, fg="blue", bg="black")
countdown_label.grid(row=2, column=0)
#labels in the middle frame
prev_label = Label(middle_frame, text="PREV", fg="#7843e6", bg="black")
prev_label.grid(row=1, column=0)
next_label = Label(middle_frame, text="NEXT", fg="#7843e6", bg="black")
next_label.grid(row=1, column=2)
#labels in location frame
location_label = Label(location_frame, text="Location:", fg="blue", bg="black")
location_label.grid(row=0, column=1)
city_label = Label(location_frame, textvariable=current_city, fg="#ffca28", bg="black")
city_label.grid(row=1, column=1)
country_label = Label(location_frame, textvariable=current_country, fg="#ffca28", bg="black")
country_label.grid(row=2, column=1)

##Setting buttons
#buttons in middle frame
previous_button = Button(middle_frame, image=left_arrow, command=goto_prev_event, highlightbackground="black")
previous_button.grid(row=0, column=0)
event_button = Button(middle_frame, command=show_event_details, highlightbackground="black")
event_button.grid(row=0, column=1)
next_button = Button(middle_frame, image=right_arrow, command=goto_next_event, highlightbackground="black")
next_button.grid(row=0, column=2)
#buttons in bottom frame
language_button = Button(bottom_frame, image=translate_image, command=open_language_menu, highlightbackground="black")#, width=45, height=45)
language_button.grid(row=0, column=0)
plus_button = Button(bottom_frame, image=plus_image, command=open_plus_menu, highlightbackground="black")#, width=45, height=45)
plus_button.grid(row=0, column=1, padx=20)
settings_button = Button(bottom_frame, image=settings_image, command=open_settings, highlightbackground="black")#, width=45, height=45)
settings_button.grid(row=0, column=2, sticky="nsew")

#Config rows and cols
button_list = [next_button, previous_button, plus_button, event_button, language_button, settings_button]

Grid.rowconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)


root.mainloop()