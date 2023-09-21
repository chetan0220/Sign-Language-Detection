# Sign Language Detection
## General Info
The project converts the American hand sign gesture image to text. It uses Convolutional Neural Networks to process images with the help of Transfer Learning. The pre-trained model used here is VGG16.
**About VGG16**
VGG16 refers to the VGG model, also called VGGNet. It is a convolution neural network (CNN) model supporting 16 layers. K. Simonyan and A. Zisserman from Oxford University proposed this model. The VGG16 model can achieve a test accuracy of 92.7% in ImageNet, a dataset containing more than 14 million training images across 1000 object classes. It is one of the top models from the ILSVRC-2014 competition. 
## Demo
1. Jupyter Notebook
![Prediction](https://github.com/chetan0220/sign_language_detection/assets/97821311/d4a9ebfd-7aed-4a9d-ac30-5f032a8048d7)
2. Streamlit
## Dataset 
The dataset encompasses all the English alphabet letters, providing extensive coverage for American Sign Language (ASL) gestures. Size of training dataset is 12875. Size of testing dataset is 4268. Images are of the size (310, 310).
**Dataset Source**
1. [Training Dataset](https://drive.google.com/drive/u/0/folders/1-XTAjPPRPFeRqu3848z8dMXaolILWizn)
2. [Testing Dataset](https://drive.google.com/drive/u/0/folders/18e1F1n1SWPF8lUF8pCKdUzSzKAbmSbVN)
## Technologies and Tools
Python(^3)
Numpy
Pandas
Matplotlib
Pillow
Tensorflow
Keras
OpenCV
Streamlit
## Streamlit Setup for localhost
```
pip install streamlit
cd app
streamlit run app.py
```
## Conclusion
The model was able to predict with test accuracy of 96.37%. The test loss is 1.511 
