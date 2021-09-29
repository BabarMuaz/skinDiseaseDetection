#   importing libraries
import os
import pandas as pd
import numpy as np

#   load ISIC_20 duplicate information
fitz17Data = pd.read_csv(r'/Users/babarmuaz/Downloads/ISIC_2020/ISIC_2020_Training_Duplicates.csv')
#    check labels
labels = pd.DataFrame(fitz17Data, columns=['image_name_2'])
#dropDuplicateLabels = labels.drop_duplicates(subset='image_name_2', keep="last")
#print(labels)  # we need , melanoma , nevus
#print(len(labels))


#
# #   filter melanoma
# mel = fitz17Data.loc[fitz17Data['diagnosis'] == 'melanoma']
#
# #   filtering melanoma with needed column
# neededListPandas = pd.DataFrame(mel, columns=['image_name'])
neededListPandas = labels.to_numpy()  # converted to numpy array
print(neededListPandas)  # results are without .jpg
#
#
#   Enter ISIC_20 melanoma_images folder path
folder_path = '/Users/babarmuaz/Downloads/ISIC_2020/nevus'
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
print(totalImagesInFolder)
#unwantedImagesInFolder = np.setdiff1d(totalImagesInFolder, neededListPandas)
#print(unwantedImagesInFolder)
#
#   Deleting unwanted Images
# counter = 0
# for originalImagesInsideFolder in totalImagesInFolder:
#     for duplicateImages in neededListPandas:
#         if originalImagesInsideFolder == duplicateImages:
#             print("Found Match ", originalImagesInsideFolder)
#             counter = counter +1
counter = 0
for duplicateImages in range(len(neededListPandas)):
    for originalImagesInsideFolder in range(len(totalImagesInFolder)):
        if neededListPandas[duplicateImages] == totalImagesInFolder[originalImagesInsideFolder]:
            print("Found Match ", totalImagesInFolder[originalImagesInsideFolder])
            counter = counter + 1
            imagePaths = "/Users/babarmuaz/Downloads/ISIC_2020/nevus/" + totalImagesInFolder[originalImagesInsideFolder] + ".jpg"
            print(imagePaths)
            os.remove(imagePaths)

print('Total images  matched', counter)
print(len(totalImagesInFolder))
print(len(imagesInFolderListPandas))
print(len(neededListPandas))

    #imagePaths = "/Users/babarmuaz/Downloads/ISIC2020/" + unwantedImages + ".jpg"
    #os.remove(imagePaths)
#
# #print("unwanted images are deleted.")
# print(len(unwantedImagesInFolder), "unwanted images are deleted, we are left with", len(mel),  "melanoma images")
#
# 2 duplicates were found in melanoma and deleted
#Found Match  ISIC_4261232
#Found Match  ISIC_7528783
#5193-5191