import os

path = os.getcwd()
file = path + "\chosun1.jpeg"

if os.path.isfile(file):
    os.remove(file)
