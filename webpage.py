import os
import streamlit as st
from PIL import Image
from main import model_image,model_video
import numpy as np
import tempfile


def load_image(image_file):
    img = Image.open(image_file)
    return img

def image_upload():
    img_array=None
    image_file_buffer = st.file_uploader("Upload Image")
    if image_file_buffer is not None:
        image = Image.open(image_file_buffer)
        img_array = np.array(image)
    return img_array,image_file_buffer

def video_upload():
    f = st.file_uploader("Upload Video")
    if f is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(f.read())
        return f,tfile
    else:
        return None    

#download the video
# def download_video(path):
#     if path!= None:
#         with open(path, "rb") as fp:
#             btn = st.download_button(
#                         label="Download Video",
#                         data=fp,
#                         file_name="output.mp4",
#                         mime="video/mp4"
#                     )
    


def main():
    st.title('Weapon Detection from IMAGES and VIDEOS')

    menu=["Images","Video"]
    # choice = st.sidebar.selectbox("Menu",menu)
    choice ="Video"

    if choice == "Images":
       st.subheader('Upload a Images')

       # Two return type first is ndarray class and second is streamlit upload class
       img_file,original_img = image_upload()
       st.write(type(img_file))
       
       
       if img_file is not None:
           
           # See the detail of the image this code is written in dictionary
           img_detail = {"filename":original_img.name,
                        "filetype":original_img.type,
                        "filesize":original_img.size}
           st.write(img_detail)

           #Display the image
           st.image(load_image(image_file=original_img),width=300)


           final_image = model_image(img_file)
           dis_img = Image.fromarray(final_image,'RGB')

           st.image(dis_img)
    



    
    if choice == "Video":
        st.subheader("Paste a youtube video url")
        url = st.text_input('Paste a Youtube url','https://www.youtube.com/watch?v=_LlJKf2UcU4')

        st.subheader("Upload a Video")
        flag_upload = video_upload()
        if flag_upload is not None:
            vid_file,temp_file = video_upload()


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

                #saving the video
                # with open(os.path.join("video","video.mp4"),"wb") as f:
                #     f.write((vid_file).getbuffer())

                final_vid = model_video(temp_file)
            
            
                #downloading the final video
                #download_video(final_vid)
        else:
            if url is not None:
                st.write("Please wait your youtube video file is loading")
                model_video(url)
            
                        
if __name__ == "__main__":
    main()
