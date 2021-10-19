import cv2
import os

from tkinter import *
from tkinter import filedialog

def Load():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("MP4 files", "*.mp4"),
                                          ("all files", "*.*")))
    print(filename)

    # filePath = filename.split('/')
    #print(filePath)
    
    if os.path.isfile(filename):
        cap = cv2.VideoCapture(filename)
    else:
        print("File Load Failed!")
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    frame_size = (frameWidth, frameHeight)
    print('frame_size={}'.format(frame_size))

    frameRate = 33

    #while True:
        #ret, frame = cap.read()
        #if not(ret):
            #break

        #cv2.imshow('freme', frame)
        #key = cv2.waitKey(frameRate)

       # if key == 27:
            #break

    #if cap.isOpened():
       # cap.release()
    #cv2.destroyAllWindows()
    

def Save():
    filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                          filetypes=(("PPTX files", "*.pptx"),
                                          ("all files", "*.*")))
    print(filename)

def domenu():
    print("OK")

root = Tk()
root.title("face_protector")
root.geometry("640x480")
root.resizable(True, True)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=domenu)
filemenu.add_command(label="Open", command=Load)
filemenu.add_command(label="Save", command=Save)
filemenu.add_command(label="Save as...", command=Save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy", command=domenu)
editmenu.add_command(label="Paste", command=domenu)
editmenu.add_separator()
editmenu.add_command(label="Delete", command=domenu)
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=domenu)

root.config(menu=menubar)
root.mainloop()


