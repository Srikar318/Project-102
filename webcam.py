from unittest import result
import cv2
import random
import time 
import dropbox
start_time = time.time()
def snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = 'img'+str(number)+'.png'
        cv2.imwrite('newPicture.jpg',frame)
        start_time = time.time
        result = False 
    return img_name 
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile():
    access_token = ''
    file = img_name
    file_from = '' 
    file_to = '' 
    dbx = dropbox.Dropbox(access_token)
with open(file_from, 'rb') as f:
    dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)

    print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            nmae = snapshot()
            uploadFile(name)
main()