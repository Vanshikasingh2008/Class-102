import cv2
import dropbox
import time
import random 

startTime = time.time()
def snapShot():
    number = random.randint(0,100)
    result = True
    videoCaptureObject = cv2.VideoCapture(0)
    while(result):
        ret, frame = videoCaptureObject.read()
        imgName = "img"+ str(number) + ".png"
        cv2.imwrite(imgName, frame)
        startTime = time.time()
        result = False
    return imgName
    print("Snapshot taken!!!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload(image):
    accessToken = "CrjnNLeU8pMAAAAAAAAAAdK87A7CoyFxBotCN6nT_cOzUOoNAo0BOsN-5QXYd7w5"
    file_to = "/TestFolder/" + image
    file_from = image
    dbx = dropbox.Dropbox(accessToken)
    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overWrite)
        print("File uploaded successfully")

def main():
    while(True):
        if((time.time() - starttime) >= 10):
            name = snapShot()
            upload(name)

main()
