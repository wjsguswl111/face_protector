from tkinter import *
from PIL import ImageTk, Image
import cv2
from tkinter import filedialog
import os

window = Tk()

window.title("Face Protector")
window.geometry("1200x700+200+50")
window.resizable(True, True)

label = Label(window, text="동영상")
label.grid(row=0, column=0)

frame_video = Frame(window, bg="white", width=720, height=480)
frame_video.grid(row=1,column=0)

label1 = Label(frame_video)
label1.grid()

def Load():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("MP4 files", "*.mp4"),("AVI files","*.avi"),
                                          ("all files", "*.*")))
    print(filename) # 파일 경로 + 파일명 + 확장자

    cap = cv2.VideoCapture(filename) 

    '''def video_stream():
        _, frame = cap.read()
        cv2video = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2video)
        imgtk = ImageTk.PhotoImage(image=img)
        label1.imgtk = imgtk
        label1.configure(image=imgtk)
        label1.after(1, video_stream)'''
    
# 메뉴바 구현


def Save():
    filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                          filetypes=(("PPTX files", "*.pptx"),
                                          ("all files", "*.*")))
    print(filename)

def domenu():
    print("OK")

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=domenu)
filemenu.add_command(label="Open", command=Load)
filemenu.add_command(label="Save", command=Save)
filemenu.add_command(label="Save as...", command=Save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy", command=domenu)
editmenu.add_command(label="Paste", command=domenu)
editmenu.add_separator()
editmenu.add_command(label="Delete", command=domenu)
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=domenu)

window.config(menu=menubar)
window.mainloop()


