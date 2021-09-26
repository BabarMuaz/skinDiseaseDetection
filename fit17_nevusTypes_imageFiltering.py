#   importing libraries
import os
import pandas as pd
import numpy as np

#   load fitz17 data
fitz17Data = pd.read_csv(r'/Users/babarmuaz/Downloads/fitzpatrick17k.csv')
#    check labels
labels = pd.DataFrame(fitz17Data, columns=['label'])
dropDuplicateLabels = labels.drop_duplicates(subset='label', keep="last")

#    filter halo_nevus labels-82
halo_nevus = fitz17Data.loc[fitz17Data['label'] == 'halo nevus']
#    filter becker_nevus labels-63
becker_nevus = fitz17Data.loc[fitz17Data['label'] == 'becker nevus']
#    filter nevocytic_nevus labels-86
nevocytic_nevus = fitz17Data.loc[fitz17Data['label'] == 'nevocytic nevus']
#    filter nevus_sebaceous_of_jadassohn labels-95
nevus_sebaceous_of_jadassohn = fitz17Data.loc[fitz17Data['label'] == 'nevus sebaceous of jadassohn']
#    filter epidermal_nevus labels-91
epidermal_nevus = fitz17Data.loc[fitz17Data['label'] == 'epidermal nevus']
#    filter naevus_comedonicus labels-73
naevus_comedonicus = fitz17Data.loc[fitz17Data['label'] == 'naevus comedonicus']
#    joining all melanoma types
totalMelanomaTypes = pd.concat(
    [halo_nevus, becker_nevus, nevocytic_nevus, nevus_sebaceous_of_jadassohn, epidermal_nevus, naevus_comedonicus])
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
print(len(halo_nevus))
print(len(becker_nevus))
print(len(nevocytic_nevus))
print(len(nevus_sebaceous_of_jadassohn))
print(len(epidermal_nevus))
print(len(naevus_comedonicus))


print(len(halo_nevus) + len(becker_nevus) + len(nevocytic_nevus) + len(nevus_sebaceous_of_jadassohn) + len(
    epidermal_nevus) + len(naevus_comedonicus))
