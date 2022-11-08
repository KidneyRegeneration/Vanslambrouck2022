import czifile
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import napari
from glob import glob
from os import path
import scipy
import pandas as pd
#function for reading czi files
def read_czi(file_path):
    img = czifile.imread(file_path)
    img = img[0,0,:,0,0,:,:,0] # remove extra dimensions
    return (img)
img_files = sorted(glob("../data/*.czi"))
file_names = [path.basename(a) for a in img_files]

print(file_names)

#generate sample matrix with file name and condition

condition = ["IWR", "IWR", "IWR", "PBS", "PBS", "PBS"]

sample_matrix = pd.DataFrame({'file':file_names, 'condition': condition})
sample_matrix.to_csv("sample_matrix.csv")

#view the sample matrix
sample_matrix

# This block loads each image, checks if an labels annotation file already exists and create one if not.
# A napari window is then loaded allowing manual labelling of the beads in each each image.
# Finally, the code chunk below is run to save the annotation file.

# file index below corresponds to the index in the sample matrix above
file_idx = 0
labels_file = 'labels_' + str(file_idx) + ".tif"

print(img_files[file_idx])
img = read_czi(img_files[file_idx])
print(img.shape)

#if file exists load, else generate ...
if path.exists(labels_file):
    print('file already exists')
    labels = io.imread(labels_file)
else:
    labels = np.zeros_like(img[0,:,:])

print(labels.shape)

viewer = napari.view_image(img, channel_axis=0)

labels_layer = viewer.add_labels(labels, name="segmentation")

napari.run()

# Code to save labels - run this when annotation complete

print (labels_file)

preserve = True

if path.exists(labels_file) and preserve:
    print('file already exists')
else:
    print('creating new labels file')
    io.imsave(labels_file, labels)
