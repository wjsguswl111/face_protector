import os

# 학습시키고 chosun대신 파일 이름 적어서 파일 삭제 시키기
def delImg(imgName):
    path = os.getcwd()
    file = path + "\image\\" + imgName + ".jpeg" #여기 수정필요
    if os.path.isfile(file):
        os.remove(file)

########################
def delYml(imgName):
    path = os.getcwd()
    file = path + "\samples\\" + imgName + ".yml" #여기 수정필요

    if os.path.isfile(file):
        os.remove(file)


#############파일이름바꾸기
def renameYml(old,new):
    path = os.getcwd()
    file = path+"\samples\\"+old+".yml"
    nfile = file.replace(old,new)
    os.renames(file,nfile)
    return nfile
