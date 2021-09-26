#   importing libraries
import os
import pandas as pd
import numpy as np

#   load ISIC_20 data
fitz17Data = pd.read_csv(r'/Users/babarmuaz/Desktop/skinThesis/DataSets/ISIC_2020_Training_GroundTruth_v2.csv')
#    check labels
labels = pd.DataFrame(fitz17Data, columns=['diagnosis'])
dropDuplicateLabels = labels.drop_duplicates(subset='diagnosis', keep="last")
#print(dropDuplicateLabels)  # we need , melanoma , nevus


#   filter melanoma
mel = fitz17Data.loc[fitz17Data['diagnosis'] == 'melanoma']

#   filtering melanoma with needed column
neededListPandas = pd.DataFrame(mel, columns=['image_name'])
neededListPandas = neededListPandas.to_numpy()  # converted to numpy array
#print(neededListPandas)  # results are without .jpg


#   Enter ISIC_20 images folder path
folder_path = '/Users/babarmuaz/Downloads/ISIC2020'
# Get images details to a list
file_list = os.listdir(folder_path)
imagesInFolderListPandas = pd.DataFrame(file_list)  # converted to dataframe
imagesInFolderListPandas = imagesInFolderListPandas.to_numpy()  # converted to numpy array
#print(imagesInFolderListPandas)  # results are with .jpg involved so we need some extra filtration

#   creating an array after removing .jpg from imagesInFolderListPandas
totalImagesInFolder = []
for temp in imagesInFolderListPandas:
    xx = np.array_str(temp)
    yy = xx[2:-6]
    totalImagesInFolder.append(yy)
#print(totalImagesInFolder)

#   now we have data in same format for comparison
totalImagesInFolder = np.array(totalImagesInFolder)  # creating numpy array
unwantedImagesInFolder = np.setdiff1d(totalImagesInFolder, neededListPandas)
#print(unwantedImagesInFolder)

#   Deleting unwanted Images
for unwantedImages in unwantedImagesInFolder:
    imagePaths = "/Users/babarmuaz/Downloads/ISIC2020/" + unwantedImages + ".jpg"
    os.remove(imagePaths)

#print("unwanted images are deleted.")
print(len(unwantedImagesInFolder), "unwanted images are deleted, we are left with", len(mel),  "melanoma images")

