import os
import streamlit as st
import numpy as np
from PIL import Image
import cv2
from main import model_image,model_video

def load_image(image_file):
    img = Image.open(image_file)
    return img

def image_upload():
    image_file = st.file_uploader("Upload Image")
    return image_file

def video_upload():
    vid_upload = st.file_uploader("Upload Video")
    return vid_upload

#download the video
def download_video(path):
    if path!= None:
        with open("runs\output.mp4", "rb") as fp:
            btn = st.download_button(
                        label="Download Video",
                        data=fp,
                        file_name="output.mp4",
                        mime="video/mp4"
                    )
    

def image2Array(uploaded_file):
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

    #st.image(opencv_image, channels="BGR")
    return opencv_image



def main():
    st.title('Weapon Detection from IMAGES and VIDEOS')

    menu=["Images","Video"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Images":
       st.subheader('Upload a Images')
       img_file = image_upload()

       
       
       if img_file is not None:
           
           # See the detail of the image this code is written in dictionary
           img_detail = {"filename":img_file.name,
                        "filetype":img_file.type,
                        "filesize":img_file.size}
           st.write(img_detail)

           #Display the image
           st.image(load_image(image_file=img_file),width=300)

           #Saving the image to Images folder
        #    with open(os.path.join("images","pistol.png"),"wb") as f:
        #        f.write((img_file).getbuffer())

           npImage = image2Array(img_file)

           final_image = model_image(npImage)
           st.image(final_image)
    



    
    if choice == "Video":
        st.subheader("Upload a Video")
        vid_file = video_upload()

        if vid_file is not None:
            #vid detail dictionary
            vid_detail = {
                "filename":vid_file.name,
                "filetype":vid_file.type,
                "filesize":vid_file.size
            }
            st.write("Video Uploaded Successfully")
            st.write(vid_detail)
            st.write("Please wait while we process the video")

            with open(os.path.join("video","video.mp4"),"wb") as f:
                f.write((vid_file).getbuffer())

            final_video_path = model_video()
            st.write(final_video_path)
           
            #downloading the final video
            download_video(final_video_path)
            
                        
if __name__ == "__main__":
    main()
