# for loading/processing the images
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input

# models
from keras.applications.vgg16 import VGG16
from keras.models import Model

# clustering and dimension reduction
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# for everything else
import os
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import pandas as pd
import pickle
current_directory = os.getcwd()
print(current_directory)
male_path =r'C:\vs_code\새 폴더\CR\MALE\남성_고프코어_images'
os.chdir(male_path)
male_images =[]
with os.scandir(male_path) as files:
    for file in files:
        male_images.append(file.name)

model = VGG16()
model = Model(inputs=model.inputs, outputs=model.layers[-2].output)

def extract_features(file, model):
    img = load_img(file, target_size=(224,224))
    img = np.array(img)
    reshaped_img = img.reshape(1,224,224,3)
    imgx = preprocess_input(reshaped_img)

    features = model.predict(imgx, user_multiprocessing=True)
    return features
data ={}
os.chdir(male_path)

for clothes in male_images:
    try:
        feat = extract_features(clothes, model)
        print(feat)
        data[clothes] = feat
        print(data[clothes])
    except FileNotFoundError:
        print('File not found!!', clothes)
        continue
    except Exception:
        print('Another Error!!', clothes)
        continue
filenames = np.array(list(data.keys()))
feat = np.array(list(data.values()))
feat = feat.reshape(-1,4096)
print(feat)


import datetime
mth_now = datetime.datetime.now().month

from keras.applications import vgg16
from keras.preprocessing.image import load_img,img_to_array
from keras.models import Model
from keras.applications.imagenet_utils import preprocess_input
from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from keras.applications.vgg16 import VGG16 
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from random import randint
import pickle

def kinds_of():
    select=int(input("남성이십니까 여성이십니까? 남자는 1번/여자는 2번"))
    if (select ==1):
        select_1 = int(input("어떤 스타일을 원하시나요? 고프코어 1번, 댄디는 2번, 스프릿은 3번, 시크 4번, 아메리칸 캐주얼은 5번, 캐주얼는 6번, 포멀은 7번, 골프는 8번, 스포츠는 9번"))
        if(select_1 ==1):
            male_path =r'C:\vs_code\새 폴더\CR\MALE\남성_고프코어_images'
            os.chdir(male_path)
        elif(select_1==2):
            male_path =r'C:\vs_code\새 폴더\CR\MALE\남성_댄디_images'
            os.chdir(male_path)
        elif(select_1==3):
            male_path =r'C:\vs_code\새 폴더\CR\MALE\남성_스트릿_images'
            os.chdir(male_path)
        elif(select_1 ==4):
            male_path =r'C:\vs_code\새 폴더\CR\MALE\남성_시크_images'
            os.chdir(male_path)
        elif(select_1==5):
            male_path =r'C:\vs_code\새 폴더\CR\MALE\남성_아메리칸 캐주얼_images'
            os.chdir(male_path)
        elif(select_1==6):
            male_path =r'C:\vs_code\새 폴더\CR\MALE\남성_캐주얼_images'
            os.chdir(male_path)
        elif(select_1 ==7):
            male_path =r'C:\vs_code\새 폴더\CR\MALE\남성_포멀_images'
            os.chdir(male_path)
        elif(select_1 ==8):
            male_path =r'C:\vs_code\새 폴더\CR\MALE\남성_골프_images'
            os.chdir(male_path)
        elif(select_1 ==8):
            male_path =r'C:\vs_code\새 폴더\CR\MALE\남성_스포츠_images'
            os.chdir(male_path)
    else:
        select_2 = int(input("어떤 스타일을 원하시나요? 걸리시는 1번 고프코어는 2번 골프는 3번, 레트로는 4번, 로맨틱은 5번, 스트릿는 6번, 스포츠는 7번, 시크는 8번, 아메리칸 캐주얼은 9번, 캐주얼은 10번, 포멀은 11번"))
        if(select_1 ==1):
            male_path =r'C:\vs_code\새 폴더\CR\FEMALE\여성_걸리시_images'
            os.chdir(male_path)
        elif(select_1==2):
            male_path =r'C:\vs_code\새 폴더\CR\FEMALE\여성_고프코어_images'
            os.chdir(male_path)
        elif(select_1==3):
            male_path =r'C:\vs_code\새 폴더\CR\FEMALE\여성_골프_images'
            os.chdir(male_path)
        elif(select_1==4):
            male_path =r'C:\vs_code\새 폴더\CR\FEMALE\여성_레트로_images'
            os.chdir(male_path)
        elif(select_1==5):
            male_path =r'C:\vs_code\새 폴더\CR\FEMALE\여성_로맨틱_images'
            os.chdir(male_path)
        elif(select_1==6):
            male_path =r'C:\vs_code\새 폴더\CR\FEMALE\여성_스트릿_images'
            os.chdir(male_path)
        elif(select_1==7):
            male_path =r'C:\vs_code\새 폴더\CR\FEMALE\여성_스포츠_images'
            os.chdir(male_path)
        elif(select_1==8):
            male_path =r'C:\vs_code\새 폴더\CR\FEMALE\여성_시크_images'
            os.chdir(male_path)
        elif(select_1==9):
            male_path =r'C:\vs_code\새 폴더\CR\FEMALE\여성_아메리칸 캐주얼_images'
            os.chdir(male_path)
        elif(select_1==10):
            male_path =r'C:\vs_code\새 폴더\CR\FEMALE\여성_캐주얼_images'
            os.chdir(male_path)
        elif(select_1==11):
            male_path =r'C:\vs_code\새 폴더\CR\FEMALE\여성_포멀_images'
            os.chdir(male_path)

##### 옷 업로드해서 코디 추천 받기
def my_clothes_coordi(myclothes):
    files = fashion.copy()