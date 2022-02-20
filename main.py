import torch
import os
import shutil
import cv2
from PIL import Image
from io import BytesIO

def make_path():
    #when the path is already present delete the path to avoid changing of path
    path = 'runs/detect/'

    #checking if the path is already there
    isdir = os.path.isdir(path)

    #deleting the path if it is already there
    if isdir==True:
        shutil.rmtree(path)



def model_image(image):
    #image='not pistol.jpg'
    make_path()
    model = torch.hub.load('ultralytics/yolov5','custom',path = 'weapon.pt')
    
    result = model(image)

    
    result.render()
    result.imgs
    
    final_image=None

    for img in result.imgs:
        buffered = BytesIO()
        img_base64 = Image.fromarray(img)
        img_base64.save(buffered, format="JPEG")
        #print(base64.b64encode(buffered.getvalue()).decode('utf-8')) 
        final_image=img   
  
    return final_image



def model_video():

    make_path()



    #loading the model using yolo v5
    model = torch.hub.load('ultralytics/yolov5','custom',path = 'weapon.pt')



    path = 'video/video.mp4'
    vid = cv2.VideoCapture(path)

    frame_width = int(vid.get(3))
    frame_height = int(vid.get(4))
    frame_size = (frame_width,frame_height)


    output = cv2.VideoWriter('runs/output.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 20, frame_size)

    while(vid.isOpened()):
        ret,frame = vid.read()
        if ret == True:
            make_path()
            result = model(frame)
            result.save()


            #reading the image using opencv
            img_path = 'runs\detect\exp\image0.jpg'
            read_image = cv2.imread(img_path)
            # final_img = cv2.cvtColor(read_image,cv2.COLOR_BGR2RGB)


            output.write(read_image)  #change here or apply the model here
            #delete the image
            if os.path.exists(img_path):
                os.remove(img_path)

        else:
            print("stream disconnected")
            break
    
    output_path = 'runs\output.mp4'
    return output_path




    























