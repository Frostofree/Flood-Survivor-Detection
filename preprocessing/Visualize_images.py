### Visualize images
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import cv2
from Read_images import read_images
from MSER import getMSERregionsAll

# Path to the folder
path="./datasets/OTCBVS_Pedestrian"

# Get images and bounding boxes
images, boxes = read_images(path)

# Get MSER regions
regions = getMSERregionsAll(images)

# Loop over the 10 folders
for i in range(1,11):
    # Path to the folder
    if i < 10:
        path_folder = path + "/0000" + str(i)
        key = "0000" + str(i)
    else:
        path_folder = path + "/000" + str(i)
        key = "000" + str(i)
    # Path to the .bmp files
    path_bmp = path_folder
    # List of the .bmp files
    list_bmp = os.listdir(path_bmp)

    list_bmp.sort()
    list_bmp.pop(0)
    list_bmp.pop(0)
    # Loop over the .bmp files
    # print(len(boxes[key]))
    for j in range(0,len(boxes[key])):
        print("Image " + str(j) + " : " + list_bmp[j])
        if list_bmp[j].endswith(".bmp"):
            # Path to the .bmp file
            # print(list_bmp[j])
            path_bmp_file = path_bmp + "/" + list_bmp[j]
            # Read the .bmp file
            img = cv2.imread(path_bmp_file)
            # Convert image to grayscale
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Create figure and axes
            fig, ax = plt.subplots(1)
            # Display the image
            ax.imshow(img, cmap='gray')
            # Loop over the MSER regions

            for region in regions[key][j]:
                # Create a Rectangle patch
                # print(region)
                rect1 = patches.Rectangle((region[0],region[1]),region[2]-region[0],region[3]-region[1],linewidth=1,edgecolor='r',facecolor='none')
                # Add the patch to the Axes
                ax.add_patch(rect1)
            # Loop over the groundtruth bounding boxes
            for box in boxes[key][j]:
                # Create a Rectangle patch
                print("No. of boxes in image " + str(j) + " : " + str(len(boxes[key][j])))
                rect2 = patches.Rectangle((box[0],box[1]),box[2]-box[0],box[3]-box[1],linewidth=1,edgecolor='g',facecolor='none')
                # Add the patch to the Axes
                ax.add_patch(rect2)
            # Display the figure
            
            plt.show()
            # Close the figure
            plt.close(fig)

