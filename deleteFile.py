import os

# 학습시키고 chosun대신 파일 이름 적어서 파일 삭제 시키기
def delImg(imgName):
    path = os.getcwd()
    file = path + "\image\\" + imgName + ".jpeg" #여기 수정필요
    if os.path.isfile(file):
        os.remove(file)
