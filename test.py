from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("즐겨찾기")
root.geometry("640x480+400+100") #창크키 and 위치 조정

root.resizable(False, False) #창 크기 변경 불가

pilimg = Image.open("C:\choun2.jpg")
phoimg = ImageTk.PhotoImage(pilimg)

img_var = StringVar()
btn_img1 = Checkbutton(root, text="img1", image = phoimg, onvalue = pilimg, variable=img_var)
btn_img2 = Checkbutton(root, text="img2", variable=img_var)
btn_img3 = Checkbutton(root, text="img3", variable=img_var)

btn_img1.deselect()
btn_img2.deselect()
btn_img3.deselect()

btn_img1.pack(anchor='center') #위치
btn_img2.pack()
btn_img3.pack()

def btncmd():
    print(img_var.get())

btn1 = Button(root, text="버튼1", command= btncmd)
btn1.pack()


root.mainloop()