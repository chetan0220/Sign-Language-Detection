# Sign Language Detection

# General Info
The project converts the American hand sign gesture image to text. It uses Convolutional Neural Networks to process images with the help of Transfer Learning. The pre-trained model used here is VGG16.<br>
**About VGG16**<br>
VGG16 refers to the VGG model, also called VGGNet. It is a convolution neural network (CNN) model supporting 16 layers. K. Simonyan and A. Zisserman from Oxford University proposed this model. The VGG16 model can achieve a test accuracy of 92.7% in ImageNet, a dataset containing more than 14 million training images across 1000 object classes. It is one of the top models from the ILSVRC-2014 competition. 

# Demo
1. _Jupyter Notebook_<br>
![prediction](https://github.com/chetan0220/sign_language_detection/assets/97821311/ef944ad9-80b8-4794-8737-6c47132153b9)
2. _Streamlit_<br>
Watch video demo here<br>
[sld-demo.webm](https://github.com/chetan0220/sign_language_detection/assets/97821311/af1d6bd6-e7a9-4d78-a106-688b1a877aab)

# Dataset 
The dataset encompasses all the English alphabet letters, providing extensive coverage for American Sign Language (ASL) gestures. Size of training dataset is 12875. Size of testing dataset is 4268. Images are of the size (310, 310).<br>
**Dataset Source**
[Dataset](https://github.com/luvk1412/Sign-Language-to-Text)

# Technologies and Tools
Python(^3)<br>
Numpy<br>
Pandas<br>
Matplotlib<br>
Pillow<br>
Tensorflow<br>
Keras<br>
OpenCV<br>
Streamlit<br>

# Streamlit Setup for localhost
```
pip install streamlit
cd app
streamlit run app.py
```
# Conclusion<br>
The model was able to predict with test accuracy of 96.37%. The test loss is 1.511 

---
Read the Blog [*Here*](https://medium.com/@chetan0220/speaking-with-signs-harnessing-vgg16-transfer-learning-for-sign-language-a79fc8db27eb)
---
If you have any query, feedback or suggestion feel free to drop a mail at chetan.mahale0220@gmail.com :) 
