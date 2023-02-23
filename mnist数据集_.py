import numpy as np
from tensorflow.keras.datasets import mnist
import cv2
(x_train,y_train),(x_test,y_test)=mnist.load_data()
# x_train.shape == (60000, 28, 28)  x_test.shape == (10000, 28, 28)  y_train.shape == (60000,)  y_test.shape == (10000,)
x_1=x_train[:100]
n=7 # 5个一组
l=[]
for i in range(0,100,n):
    if i+n<100:
        x_5=[x_1[j] for j in range(i,i+n,1)]
    else:
        x_5=[x_1[j] for j in range(i,100,1)]
        x_5.extend([np.zeros_like(x_1[0]) for k in range(100,i+n)])
    x_=np.concatenate(x_5,axis=1)
    print(x_.shape)
    l.append(x_)
x_h=np.concatenate(l,axis=0)
cv2.imshow('x1',x_h)
cv2.waitKey()



