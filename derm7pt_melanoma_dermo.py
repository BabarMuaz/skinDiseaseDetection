#   importing libraries
import os
import pandas as pd
import numpy as np

#   load ISIC_20 data
fitz17Data = pd.read_csv(r'/Users/babarmuaz/Downloads/meta.csv')
#    check labels
labels = pd.DataFrame(fitz17Data, columns=['diagnosis'])
dropDuplicateLabels = labels.drop_duplicates(subset='diagnosis', keep="last")
# print(dropDuplicateLabels)

# labels
# 69                      blue nevus
# 468                    clark nevus
# 481                 combined nevus
# 498               congenital nevus
# 531                   dermal nevus
# 639             melanoma (in situ)
# 741   melanoma (less than 0.76 mm)
# 794      melanoma (0.76 to 1.5 mm)
# 822    melanoma (more than 1.5 mm)
# 826            melanoma metastasis
# 856                recurrent nevus
# 935            reed or spitz nevus
# 1010                      melanoma

#   filter melanoma types
mel_1 = fitz17Data.loc[fitz17Data['diagnosis'] == 'melanoma (in situ)']
mel_2 = fitz17Data.loc[fitz17Data['diagnosis'] == 'melanoma (less than 0.76 mm)']
mel_3 = fitz17Data.loc[fitz17Data['diagnosis'] == 'melanoma (0.76 to 1.5 mm)']
mel_4 = fitz17Data.loc[fitz17Data['diagnosis'] == 'melanoma (more than 1.5 mm)']
mel_5 = fitz17Data.loc[fitz17Data['diagnosis'] == 'melanoma metastasis']
mel_6 = fitz17Data.loc[fitz17Data['diagnosis'] == 'melanoma']
totalMelanomaTypes = pd.concat([mel_1, mel_2, mel_3, mel_4, mel_5, mel_6])
#   filtering melanoma with needed column
neededListPandas = pd.DataFrame(totalMelanomaTypes, columns=['derm'])
neededListPandas = neededListPandas.to_numpy()  # converted to numpy array
#print(neededListPandas)  # results are with .jpg and sub folder which i already removed manually

#   creating an array and removing .jpg , subfolder
neededListPandasFiltered = []
for temp in neededListPandas:
    xx = np.array_str(temp)
    yy = xx[6:-6]
    neededListPandasFiltered.append(yy)

#print(neededListPandasFiltered)


#   Enter derm7pt images folder path
folder_path = '/Users/babarmuaz/Downloads/totalimages'
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
neededListPandasFiltered = np.array(neededListPandasFiltered)  # creating numpy array
unwantedImagesInFolder = np.setdiff1d(totalImagesInFolder, neededListPandasFiltered)
#print(unwantedImagesInFolder)

#   Deleting unwanted Images
for unwantedImages in unwantedImagesInFolder[1:]:
    imagePaths = "/Users/babarmuaz/Downloads/totalimages/" + unwantedImages + ".jpg"
    #print(imagePaths)
    os.remove(imagePaths)

#print("unwanted images are deleted.")
print(len(unwantedImagesInFolder), "unwanted images are deleted, we are left with", len(neededListPandasFiltered),
      "melanoma images")

