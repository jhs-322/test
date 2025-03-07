import streamlit as st
import numpy as np
import cv2
from PIL import Image

class FaceMosaic :
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        
    def apply_mosaic(self, img, scale_factor, min_neighbors, mosaic_ratio):
        # 이미지 받아서 바로 흑백으로
        gray = cv2. cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 모자이크 적용 - 사용자 입력 값으로
        faces = self.face_cascade.detectMultiScale(gray, scale_factor, min_neighbors)
        for (x, y, w, h) in faces:
            face_img = img[y:y+h, x:x+w]
            
            # 얼굴 부분을 축소 후 다시 확대하여 모자이크 효과 적용
            face_img = cv2.resize(face_img, dsize=(0, 0), fx=mosaic_ratio, fy=mosaic_ratio) 
            face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
            img[y:y+h, x:x+w] = face_img
        return img   
        
class Web():
    def __init__(self) -> None:
        self.draw_text()

    def draw_text(self):
        st.set_page_config(
            page_title="Mosaic-Converter",
            layout="centered",
            initial_sidebar_state="expanded"
        )
        st.title("Mosaic-Converter")
        self.upload = st.file_uploader("Upload Image Here", type=['jpg', 'jpeg', 'png', 'webp'])
        
        # float / int / float
        self.scale_ratio = st.slider('Recognize Less Person ->', 101, 150, 120, 1) # 1.01 ~ 1.5 / 1.2 / 0.01
        self.neigh_ratio = st.slider('High Accuracy ->', 1, 9, 5, 1) # int로
        self.ratio = st.slider('Mosaic Roughly -> ', 10, 50, 10, 1) # 0.1 ~ 0.5 / 0.1 / 0.01

        self.original, self.converted = st.columns(2)
        self.original.title("original img")
        self.converted.title("converted img")

if __name__ == "__main__":
    web = Web()
    mosaic = FaceMosaic()
    
    if web.upload != None:
        img = Image.open(web.upload)
        img = np.array(img)
        
        web.original.image(web.upload) #원래 사진
        
        mosaic.apply_mosaic(img, (web.scale_ratio)/100, web.neigh_ratio, (web.ratio)/100)
        web.converted.image(img) #모자이크 한 사진
