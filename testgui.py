from tkinter import *
from PIL import ImageTk, Image
import cv2
from tkinter import filedialog

cap = cv2.VideoCapture('C:/Users/wjsgu/Desktop/test.avi')

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

def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    label1.imgtk = imgtk
    label1.configure(image=imgtk)
    label1.after(1, video_stream) 

video_stream()

window.mainloop()