#   importing libraries
import os
import pandas as pd
import numpy as np

#   load fitz17 data
fitz17Data = pd.read_csv(r'/Users/babarmuaz/Downloads/fitzpatrick17k.csv')
#    check labels
labels = pd.DataFrame(fitz17Data, columns=['label'])
dropDuplicateLabels = labels.drop_duplicates(subset='label', keep="last")
# print(dropDuplicateLabels)
#    filter melanoma_ssm labels-118
melanoma_ssm = fitz17Data.loc[fitz17Data['label'] == 'superficial spreading melanoma ssm']
#    filter melanoma_malignant labels-111
melanoma_malignant = fitz17Data.loc[fitz17Data['label'] == 'malignant melanoma']
#    filter melanoma labels-261
melanoma = fitz17Data.loc[fitz17Data['label'] == 'melanoma']
#    joining all melanoma types
totalMelanomaTypes = pd.concat([melanoma_ssm, melanoma_malignant, melanoma])
#   filtering totalMelanomaTypes with needed column
neededListPandas = pd.DataFrame(totalMelanomaTypes, columns=['md5hash'])
neededListPandas = neededListPandas.to_numpy()  # converted to numpy array


#   Enter Fitz17 images folder path
folder_path = '/Users/babarmuaz/Downloads/fitz17'
# Get images details to a list
file_list = os.listdir(folder_path)
imagesInFolderListPandas = pd.DataFrame(file_list)  # converted to dataframe
imagesInFolderListPandas = imagesInFolderListPandas.to_numpy()  # converted to numpy array

#   creating an array after removing .jpg from imagesInFolderListPandas
totalImagesInFolder = []
for temp in imagesInFolderListPandas:
    xx = np.array_str(temp)
    yy = xx[2:-6]
    totalImagesInFolder.append(yy)

totalImagesInFolder = np.array(totalImagesInFolder)  # creating numpy array
#   Sorted 1D array of values in totalImagesInFolder that are not in neededListPandas.
unwantedImagesInFolder = np.setdiff1d(totalImagesInFolder, neededListPandas)

#   Deleting unwanted Images
for unwantedImages in unwantedImagesInFolder:
    imagePaths = "/Users/babarmuaz/Downloads/fitz17/" + unwantedImages + ".jpg"
    os.remove(imagePaths)

print("unwanted images are deleted.")
