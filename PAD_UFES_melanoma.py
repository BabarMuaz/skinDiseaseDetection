#   importing libraries
import os
import pandas as pd
import numpy as np

#   load fitz17 data
fitz17Data = pd.read_csv(r'/Users/babarmuaz/Downloads/PAD-UFES-20/metadata.csv')
#    check labels
labels = pd.DataFrame(fitz17Data, columns=['diagnostic'])
dropDuplicateLabels = labels.drop_duplicates(subset='diagnostic', keep="last")
#print(dropDuplicateLabels) NEV, MEL

#   filter MEL
mel = fitz17Data.loc[fitz17Data['diagnostic'] == 'MEL']

#   filtering melanoma with needed column
neededListPandas = pd.DataFrame(mel, columns=['img_id'])
neededListPandas = neededListPandas.to_numpy()  # converted to numpy array

#   Enter PAD images folder path
folder_path = '/Users/babarmuaz/Downloads/PAD-UFES-20/pad'
# Get images details to a list
file_list = os.listdir(folder_path)
imagesInFolderListPandas = pd.DataFrame(file_list)  # converted to dataframe
imagesInFolderListPandas = imagesInFolderListPandas.to_numpy()  # converted to numpy array

#   since for comparison format is save both have .png included we dont need additional filtering
totalImagesInFolder = np.array(imagesInFolderListPandas)  # creating numpy array
unwantedImagesInFolder = np.setdiff1d(totalImagesInFolder, neededListPandas)

#   Deleting unwanted Images
for unwantedImages in unwantedImagesInFolder:
    imagePaths = "/Users/babarmuaz/Downloads/PAD-UFES-20/pad/" + unwantedImages #+ ".jpg"
    os.remove(imagePaths)

#print("unwanted images are deleted.")
print(len(unwantedImagesInFolder), "unwanted images are deleted, we are left with", len(mel),  "melanoma images")

