# please note this package - imagededup was custom-installed in this kernel 
from imagededup.methods import CNN
from imagededup.utils import plot_duplicates
import pandas as pd
#import matplotlib.pyplot as plt
#plt.rcParams['figure.figsize'] = (15, 10)
def finddedup():
    cnn = CNN()


    image_dir = "uploaded_files/"


    encodings = cnn.encode_images(image_dir=image_dir)


    duplicates = cnn.find_duplicates(encoding_map=encodings, scores = True)


    len(duplicates)

    NOT_Duplicate = []
    Duplicate = []
    for key, value in duplicates.items():

        if len(value) > 0:
            Duplicate.append(key)
            #print("Duplicate:-", key)
        else:
            NOT_Duplicate.append(key)
            #print("NOT Duplicate:-", key)
    return (NOT_Duplicate,Duplicate)
#print(NOT_Duplicate)
#print(Duplicate)
#tuple1=finddedup()
#Not_duplicate, Duplicate=tuple1[0],tuple1[1]
# print(Not_duplicate)
# print(Duplicate)

