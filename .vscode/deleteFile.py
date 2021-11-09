import os

def delImg(imgName):
    path = os.getcwd()
    file = path + "\chosun.jpeg" #여기 수정필요

    if os.path.isfile(file):
        os.remove(file)
