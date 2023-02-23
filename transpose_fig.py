import numpy as np
from tensorflow.keras.datasets import mnist
import cv2
(x_train,y_train),(x_test,y_test)=mnist.load_data()

x=x_train[:100]

x=x.transpose(1,0,2)
x=x.reshape(28,-1,28*5)
x=x.transpose(1,0,2)
x=x.reshape(-1,28*5)



cv2.imshow('x',x)
cv2.waitKey()