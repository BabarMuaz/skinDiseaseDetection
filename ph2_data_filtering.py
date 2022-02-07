
# importing required libraries

import os
import pandas as pd
import numpy as np
from PIL import Image, ImageOps
import shutil
from numpy import array

# Setting Paths to directories
datapath  = '/Users/babarmuaz/Downloads/ph2/ph2_dataset/trainx/'
excelfilepath = '/Users/babarmuaz/Desktop/babarMasterThesisDir/Datasets/ph2/babarVersionSortedImagesInfo.xlsx'
mel_destination_dir = '/Users/babarmuaz/Downloads/ph2/Melanoma'
nev_destination_dir = '/Users/babarmuaz/Downloads/ph2/Nevus'

#  reading excelfile
df = pd.read_excel(excelfilepath)

# reading only nevus data
nevImages = pd.DataFrame(df, columns=['NEV'])
nevImages = nevImages.to_numpy() # converting to numpy array

# reading only melanoma data
melImages = pd.DataFrame(df, columns=['MEL'])
melImages = melImages[:40] # checked from excel file only 40 entries
melImages = melImages.to_numpy() # converting to numpy array


#  filtering and copying melanoma to destination directory
for img in melImages:
    temp = datapath + img +'.bmp'
    temp2 = np.array_str(temp)
    temp2 = temp2[2:-2]
    print(temp2)
    shutil.copy(temp2, mel_destination_dir)


#  filtering and copying nevus to destination directory
for img in nevImages:
    temp = datapath + img +'.bmp'
    temp2 = np.array_str(temp)
    temp2 = temp2[2:-2]
    print(temp2)
    shutil.copy(temp2, nev_destination_dir)