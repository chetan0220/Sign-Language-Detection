import streamlit as st
import tensorflow as tf
import cv2
from PIL import Image, ImageOps
import numpy as np

st.set_page_config(layout="wide")


def import_and_predict(image_data, model):
        size = (224, 224)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)       
        img_reshape = img[np.newaxis,...]
        prediction = model.predict(img_reshape)
        return prediction

class_names = {
    0: 'Blank',
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
    10: 'J',
    11: 'K',
    12: 'L',
    13: 'M',
    14: 'N',
    15: 'O',
    16: 'P',
    17: 'Q',
    18: 'R',
    19: 'S',
    20: 'T',
    21: 'U',
    22: 'V',
    23: 'W',
    24: 'X',
    25: 'Y',
    26: 'Z'
}

@st.cache_data()
def run_model():
    model = tf.keras.models.load_model('./model.h5')
    return model

with st.spinner('Loading Model ...'):
    model = run_model()

st.markdown("<h1 style='text-align: center; font-weight: bold; font-family: Lucida Sans Unicode;'>Sign Language Detector</h1>", unsafe_allow_html=True)
file = st.file_uploader("Upload Image Here", type=["jpg", "png"])

st.set_option('deprecation.showfileUploaderEncoding', False)

if file is None:
    st.text("Please upload an image")
else:
    image = Image.open(file)
    st.image(image, use_column_width=700)
    predictions = import_and_predict(image, model)
    score = tf.nn.softmax(predictions[0])

    predicted_class_index = np.argmax(score)
    predicted_class_name = class_names[predicted_class_index]
    
    st.write(f"""## Predicted Letter : {predicted_class_name}""")
