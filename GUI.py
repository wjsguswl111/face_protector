import cv2
import os

import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image


root = tk.Tk()
root.title("face_protector")
root.geometry("1200x700+200+50")
root.resizable(True, True)

filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                    filetypes=(("MP4 files", "*.mp4"),("AVI files","*.avi"),
                                    ("all files", "*.*")))


frm = tk.Frame(root, bg="white", width=720, height=480)
frm.grid(row=1, column=0)

lbl1 = tk.Label(frm)
lbl1.grid()

#os.chdir('D:/GEODATA') # 현재 작업 디렉토리 변경
cap = cv2.VideoCapture(filename) # VideoCapture 객체 정의

def video_play():
    ret, frame = cap.read()
    if not ret:
        cap.release()
        return
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    lbl1.imgtk=imgtk
    lbl1.configure(image=imgtk)
    lbl1.after(10, video_play)

# 작업 완료 후 해제

'''cap = cv2.VideoCapture(filename)
frameRate = 33

while True: # 동영상 재생
    ret, frame = cap.read()
    if not(ret):
        break

    cv2.imshow('freme', frame)
    key = cv2.waitKey(frameRate)

    if key == 27:
        break

    if cap.isOpened():
        cap.release()
cv2.destroyAllWindows()'''


video_play()
root.mainloop()


