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

#   filter nevus types
nev_1 = fitz17Data.loc[fitz17Data['diagnosis'] == 'blue nevus']
nev_2 = fitz17Data.loc[fitz17Data['diagnosis'] == 'clark nevus']
nev_3 = fitz17Data.loc[fitz17Data['diagnosis'] == 'combined nevus']
nev_4 = fitz17Data.loc[fitz17Data['diagnosis'] == 'congenital nevus']
nev_5 = fitz17Data.loc[fitz17Data['diagnosis'] == 'dermal nevus']
nev_6 = fitz17Data.loc[fitz17Data['diagnosis'] == 'recurrent nevus']
nev_7 = fitz17Data.loc[fitz17Data['diagnosis'] == 'reed or spitz nevus']
totalNevusTypes = pd.concat([nev_1, nev_2, nev_3, nev_4, nev_5, nev_6, nev_7])
#   filtering melanoma with needed column
neededListPandas = pd.DataFrame(totalNevusTypes, columns=['clinic'])
neededListPandas = neededListPandas.to_numpy()  # converted to numpy array
# print(neededListPandas)  # results are with .jpg and sub folder which i already removed manually

#   creating an array and removing .jpg , subfolder
neededListPandasFiltered = []
for temp in neededListPandas:
    xx = np.array_str(temp)
    yy = xx[6:-6]
    neededListPandasFiltered.append(yy)

# print(neededListPandasFiltered)


#   Enter derm7pt images folder path
folder_path = '/Users/babarmuaz/Downloads/totalimages'
# Get images details to a list
file_list = os.listdir(folder_path)
imagesInFolderListPandas = pd.DataFrame(file_list)  # converted to dataframe
imagesInFolderListPandas = imagesInFolderListPandas.to_numpy()  # converted to numpy array
# print(imagesInFolderListPandas)  # results are with .jpg involved so we need some extra filtration


#   creating an array after removing .jpg from imagesInFolderListPandas
totalImagesInFolder = []
for temp in imagesInFolderListPandas:
    xx = np.array_str(temp)
    yy = xx[2:-6]
    totalImagesInFolder.append(yy)
# print(totalImagesInFolder)


#   now we have data in same format for comparison
totalImagesInFolder = np.array(totalImagesInFolder)  # creating numpy array
neededListPandasFiltered = np.array(neededListPandasFiltered)  # creating numpy array
unwantedImagesInFolder = np.setdiff1d(totalImagesInFolder, neededListPandasFiltered)
# print(unwantedImagesInFolder)

#   Deleting unwanted Images
for unwantedImages in unwantedImagesInFolder[1:]:
    imagePaths = "/Users/babarmuaz/Downloads/totalimages/" + unwantedImages + ".jpg"
    # print(imagePaths)
    os.remove(imagePaths)

# print("unwanted images are deleted.")
print(len(unwantedImagesInFolder), "unwanted images are deleted, we are left with", len(neededListPandasFiltered),
      "nevus images")

print(len(nev_1), "blue nevus")
print(len(nev_2), 'clark nevus')
print(len(nev_3), 'combined nevus')
print(len(nev_4), 'congenital nevus')
print(len(nev_5), 'dermal nevus')
print(len(nev_6), 'recurrent nevus')
print(len(nev_7), 'reed or spitz nevus')
print(len(neededListPandasFiltered))

