'''---------------Import libraries-------------------'''
from tkinter import *

'''--------------global variables----------------'''
frame_list = []      # List to hold all the frames
frame_index = 0 
count = 0
anim = None

'''-----------------methods---------------------'''
def animate_gif(count):  
    global anim
    event_image_label.config(image = frame_list[count])
    count +=1
        
    if count > last_frame:
        count = 0  
    #recall animate_gif method    
    anim = root.after(50, lambda :animate_gif(count))        
          
def describe():
    print("IT WORKS")

'''-------------Tkinter GUI main root----------------------'''
root = Tk()
root.title("GIF LOADED")
root.geometry("800x800")
'''--------------count all frames in gif and saved in a list-----------------'''
while True:
    try:
        # Read a frame from GIF file
        part = 'gif -index {}'.format(frame_index)
        frame = PhotoImage(file='assets/resizeMeteor.gif', format=part)
    except:
        print("break")
        last_frame = frame_index - 1    # Save index for last frame
        break               # Will break when GIF index is reached
    frame_list.append(frame)
    print(len(frame_list))
    frame_index += 1 
'''------------label to show gif--------------------'''
event_image_label = Button(root, bg='#202020', image = "", command=describe)
event_image_label.pack()
'''-----------------start gif--------------------'''
animate_gif(0)

root.mainloop()