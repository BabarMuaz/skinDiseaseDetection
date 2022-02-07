import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import shutil

folder_path = '/Users/babarmuaz/Desktop/semiFinalSkinDataset_hassan/melanoma'
# Get images details to a list
file_list = os.listdir(folder_path)
images = pd.DataFrame(file_list)  # converted to dataframe
images = images.to_numpy()  # converted to numpy array

train, temp = train_test_split(images, test_size=0.2, random_state=42)

# print(len(train))
# print(len(temp))

# unwantedImagesInFolder = np.setdiff1d(test, train)
# print(len(unwantedImagesInFolder))

validation, test = train_test_split(temp, test_size=0.025, random_state=42)
# print(len(validation))
# print(len(test))

#   Copying Training Images to a new folder
destination_dir = "/Users/babarmuaz/Desktop/tempSkin/melanoma/train"
for img in train:
    imagePaths = "/Users/babarmuaz/Desktop/semiFinalSkinDataset_hassan/melanoma/" + img  # + ".jpg"
    print(imagePaths)
    xx = np.array_str(imagePaths)
    yy = xx[2:-2]
    shutil.copy(yy, destination_dir)

print("Training Images are Copied.")

#   Copying Validation Images to a new folder
destination_dir = "/Users/babarmuaz/Desktop/tempSkin/melanoma/validation"
for img in validation:
    imagePaths = "/Users/babarmuaz/Desktop/semiFinalSkinDataset_hassan/melanoma/" + img  # + ".jpg"
    print(imagePaths)
    xx = np.array_str(imagePaths)
    yy = xx[2:-2]
    shutil.copy(yy, destination_dir)

print("Validation Images are Copied.")

#   Copying Test Images to a new folder
destination_dir = "/Users/babarmuaz/Desktop/tempSkin/melanoma/test"
for img in test:
    imagePaths = "/Users/babarmuaz/Desktop/semiFinalSkinDataset_hassan/melanoma/" + img  # + ".jpg"
    print(imagePaths)
    xx = np.array_str(imagePaths)
    yy = xx[2:-2]
    shutil.copy(yy, destination_dir)

print("Test Images are Copied.")

print("total melanoma images are = ", len(images))
print(len(train), " Training images are split in train folder.")
print(len(test), " Testing images are split in test folder.")
print(len(validation), " Validation images are split in validation folder.")
