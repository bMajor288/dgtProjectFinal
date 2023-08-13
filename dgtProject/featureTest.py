from tkinter import *
from tkcalendar import *
import time

root=Tk()
root.geometry("200x430") #same as wireframe dimensions
root.title("Superstar") #Not the final name of the app
root.minsize(200,430)

plus_image = PhotoImage(file="GUI/assets/plus_image_resized.png")

def open_plus_menu():
    for i in range(30):
        plus_button.place(x=80, y=i)
        time.sleep(1)
    for i in range(60):
        plus_button.place(x=80, y=i)
        time.sleep(1)
    for i in range(90):
        plus_button.place(x=80, y=i)
        time.sleep(1)

plus_button = Button(root, image=plus_image, command=open_plus_menu, highlightbackground="black")#, width=45, height=45)
plus_button.pack(side=BOTTOM)

# def selectDate():
#     start_date = startCal.get_date()
#     end_date = endCal.get_date()
#     print(start_date)
#     print(end_date)


# startCal = Calendar(root, setmode = "day", date_pattern = "yyyy-mm-dd")
# startCal.pack(side=LEFT)
# endCal = Calendar(root, setmode = "day", date_pattern = "yyyy-mm-dd")
# endCal.pack(side=RIGHT)

# openCal = Button(root, text="Select Date", command = selectDate)
# openCal.pack(side=BOTTOM)

root.mainloop()