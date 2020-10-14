import os
import glob
import sys

banner = '''
 _____                                           _
|  ___|         ___   _ __   __ _   __ _  _ __  (_) ____  ___  _ __
| |_    _____  / _ \ | '__| / _` | / _` || '_ \ | ||_  / / _ \| '__|
|  _|  |_____|| (_) || |   | (_| || (_| || | | || | / / |  __/| |
|_|            \___/ |_|    \__, | \__,_||_| |_||_|/___| \___||_|
                            |___/
by sandakelum priyamantha ..........................................

'''
print(banner)
#file types
audio = ['.mp3','.wav','.flac','.ogg','.m3u','.acc','.wma','.midi','.aif','.mpa','.pls']
vedio = ['.mp4','.avi','.wmv','.webm','.flv']
doc = ['.txt','.pdf','.docx','.xlsx','.pptx']
image = ['.png','.jpg','.gif','.jpeg']
apps = ['.exe','.bat','.msi']
##

def createFolders():
    try:
        os.mkdir("Audios[fo]")
    except:
        print("done!")
    try:
        os.mkdir("Vedios[fo]")
    except:
        print("done!")
    try:
        os.mkdir("Documents[fo]")
    except:
        print("done!")
    try:
        os.mkdir("Images[fo]")
    except:
        print("done!")
    try:
        os.mkdir("Apps[fo]")
    except:
        print("done!")
    try:
        os.mkdir("Unknown[fo]")
    except:
        print("done!")

def getFiles():
    f_list = glob.glob("*")
    return f_list

def getExtension(name):
    e = os.path.splitext(name)
    return e[1]

createFolders()
#main loop
file_list = getFiles()
for f in file_list:
    ex = getExtension(f).lower()
    if ex in doc:
        print("%s is document"%(f))
        os.replace(f,"Documents[fo]/"+f)
    elif ex in audio:
        print("%s is audio"%(f))
        os.replace(f,"Audios[fo]/"+f)
    elif ex in vedio:
        print("%s is vedio"%(f))
        os.replace(f,"Vedios[fo]/"+f)
    elif ex in image:
        print("%s is image"%(f))
        os.replace(f,"Images[fo]/"+f)
    elif ex in apps:
        print("%s is app"%(f))
        os.replace(f,"Apps[fo]/"+f)
    else:
        print("%s is unknown file format"%(f))
        os.replace(f,"Unknown[fo]/"+f)

print("#all files are organized!")
sys.exit()

