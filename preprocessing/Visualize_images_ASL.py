### Visualize images
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import cv2
from Read_ASL import read_images
from MSER import getMSERregionsAll

# Path to the folder
path="./datasets/ASL-TID"

# Get images and bounding boxes
images, boxes = read_images(path)

# Get MSER regions
regions = getMSERregionsAll(images,"ASL-TID")

# Path to the folder
path_folder = path + "/" + "train"
# Path to the labelTxt folder
path_labelTxt = path_folder + "/labels"
# Path to the images folder
path_images = path_folder + "/images"

# Loop over the images folder

image_list = os.listdir(path_images)
image_list.sort()

for filename in image_list:
    # Path to the image
    path_image = path_images + "/" + filename
    # Read the image
    filename = filename[:-4]            # Remove the .jpg extension

    image = images[filename]
    # Convert image to grayscale
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Create figure and axes
    fig, ax = plt.subplots(1)
    # Display the image
    ax.imshow(img, cmap='gray')
    # Loop over the MSER regions
    

    for region in regions[filename]:
        # Create a Rectangle patch
        rect1 = patches.Rectangle((region[0],region[1]),region[2]-region[0],region[3]-region[1],linewidth=1,edgecolor='r',facecolor='none')
        # Add the patch to the Axes
        ax.add_patch(rect1)
    # Loop over the groundtruth bounding boxes
    for box in boxes[filename]:
        # Create a Rectangle patch
        print(box)
        rect2 = patches.Rectangle((box[0],box[1]),box[2]-box[0],box[3]-box[1],linewidth=1,edgecolor='g',facecolor='none')
        # Add the patch to the Axes
        ax.add_patch(rect2)

    # Display the figure
    plt.show()
    # Close the figure
    plt.close(fig)

