from tkinter import *

#Global variables
framelist = []
frame_index = 0
count = 0
anim = None

#Functions
def animate_gif(count):
    global anim
    label1.config(image=framelist[count])
    count =+ 1

    if count > last_frame:
        count = 0
        
    anim = root.after(50, lambda : animate_gif(count))

def stop_gif():
    global anim
    root.after_cancel(anim)

root = Tk()
root.geometry("800x800")
root.title("Gif")

while True:
    try:
        """read a frame from gif file"""
        part = 'gif -index {}'.format(frame_index)
        frame = PhotoImage(file="assets/resizeMeteor.gif", format=part)
    except:
        print("break")
        last_frame = frame_index -1 #save index for last frame
        break
    framelist.append(frame)
    print(len(framelist))
    frame_index += 1

label1 = Label(root, bg="black", image="")
label1.pack()

start_button = Button(root, text='start', command= lambda : animate_gif(0))
start_button.pack()

stop_button = Button(root, text='stop', command=stop_gif)
stop_button.pack()

root.mainloop()