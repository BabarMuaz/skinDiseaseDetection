# https://machinelearningknowledge.ai/keras-implementation-of-vgg16-architecture-from-scratch-with-dogs-vs-cat-data-set/

import cv2
import numpy as np
import os
import tensorflow
from matplotlib import pyplot as plt

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense,Flatten,Conv2D,Activation,Dropout
from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.callbacks import EarlyStopping,ModelCheckpoint
from tensorflow.keras.layers import MaxPool2D
from google.colab.patches import cv2_imshow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import model_from_json

print("packages have been imported.")

train_path="/Users/babarmuaz/Google Drive/Dog Vs Cats/train"
test_path="/Users/babarmuaz/Google Drive/Dog Vs Cats/validation"
class_names=os.listdir(train_path)
class_names_test=os.listdir(test_path)

print(class_names)
print(class_names_test)

train_datagen = ImageDataGenerator(zoom_range=0.15,width_shift_range=0.2,height_shift_range=0.2,shear_range=0.15)
test_datagen = ImageDataGenerator()

train_generator = train_datagen.flow_from_directory("/Users/babarmuaz/Google Drive/Dog Vs Cats/train",target_size=(224, 224),batch_size=32,shuffle=True,class_mode='binary')
test_generator = test_datagen.flow_from_directory("/Users/babarmuaz/Google Drive/Dog Vs Cats/validation",target_size=(224,224),batch_size=32,shuffle=False,class_mode='binary')

def VGG16():
    model = Sequential()
    model.add(Conv2D(input_shape=(224,224,3),filters=64,kernel_size=(3,3),padding="same", activation="relu"))
    model.add(Conv2D(filters=64,kernel_size=(3,3),padding="same", activation="relu"))
    model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
    model.add(Conv2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))
    model.add(Conv2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))
    model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
    model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
    model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
    model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
    model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
    model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
    model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
    model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
    model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
    model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
    model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
    model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
    model.add(MaxPool2D(pool_size=(2,2),strides=(2,2),name='vgg16'))
    model.add(Flatten(name='flatten'))
    model.add(Dense(256, activation='relu', name='fc1'))
    model.add(Dense(128, activation='relu', name='fc2'))
    model.add(Dense(1, activation='sigmoid', name='output'))
    return model



model=VGG16()
model.summary()

Vgg16 = Model(inputs=model.input, outputs=model.get_layer('vgg16').output)
Vgg16.load_weights("/Users/babarmuaz/Google Drive/vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5")

for layer in Vgg16.layers:
    layer.trainable = False

for layer in model.layers:
    print(layer, layer.trainable)

opt = SGD(learning_rate=1e-4, momentum=0.9)
model.compile(loss="binary_crossentropy", optimizer=opt,metrics=["accuracy"])
model.load_weights("/Users/babarmuaz/Google Drive/model_file.h5")
#model.evaluate(test_generator)



#######

model_json = model.to_json()
with open("/Users/babarmuaz/PycharmProjects/skinDiseaseDetection/model_file.json","w") as json_file:
  json_file.write(model_json)

#testing


def predict_(image_path):
    #Load the Model from Json File
    json_file = open('/Users/babarmuaz/PycharmProjects/skinDiseaseDetection/model_file.json', 'r')
    model_json_c = json_file.read()
    json_file.close()
    model_c = model_from_json(model_json_c)
    #Load the weights
    model_c.load_weights("/Users/babarmuaz/Google Drive/model_file.h5")
    #Compile the model
    opt = SGD(lr=1e-4, momentum=0.9)
    model_c.compile(loss="categorical_crossentropy", optimizer=opt,metrics=["accuracy"])
    #load the image you want to classify
    # img=image.load_img(image_path,target_size=(224,224))
    # imgage = np.asarray(img)
    # plt.imshow(imgage)

    # image=cv2.imread(image_path)
    #image = cv2.resize(image, (224,224))
    # cv2_imshow(image)

    # image = cv2.imread(image_path)
    # image = cv2.resize(image, (224,224))
    # cv2_imshow(image)
    #predict the image
    # preds = model_c.predict(np.expand_dims(image, axis=0))[0]
    # print(preds)
    # if preds==1:
    #     print("Predicted Label: Yash")
    # else :
    #     print("Predicted Label: MIMI")

    img = image.load_img(image_path, target_size=(224, 224))
    img = np.asarray(img)
    plt.imshow(img)
    img = np.expand_dims(img, axis=0)

    output = model_c.predict(img)
    if output[0][0] > output[0][1]:
        print("cat")
    else:
        print('dog')




predict_("/Users/babarmuaz/Google Drive/Dog Vs Cats/validation/Dog/dog.12382.jpg")


