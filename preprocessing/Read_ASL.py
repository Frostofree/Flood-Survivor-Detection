import os
import re
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches


### Read Images from Test,Train and Valisation folders
### Each folder contains 2 subfolders - images and labels
### images contains images in .jpg format and of size 416x416
### labelTxt contain annotations in PyTorch YOLOv5 format

# Path to the folder containing the dataset
def read_images(path="./datasets/ASL-TID", folder="train"):
    ## Extract Bounding Boxes from labelTxt files
    # Path to the folder
    path_folder = path + "/" + folder
    # Path to the labelTxt folder
    path_labelTxt = path_folder + "/labels"
    # Path to the images folder
    path_images = path_folder + "/images"

    # Loop over the images folder
    images = {}

    image_list = os.listdir(path_images)
    image_list.sort()

    for filename in image_list:
        # Path to the image
        path_image = path_images + "/" + filename
        # Read the image

        filename = filename[:-4]            # Remove the .jpg extension

        image = cv2.imread(path_image)
        # Append the image to the list
        images[filename] = image
    
    # Loop over the labelTxt folder
    # Format of the labelTxt file: <class> <x_center> <y_center> <width> <height>   in normalized format 
    all_boxes = {}

    bbox_list = os.listdir(path_labelTxt)
    bbox_list.sort()

    for filename in bbox_list:
        # Path to the labelTxt file
        path_txt = path_labelTxt + "/" + filename
        # Open the labelTxt file
        txt = open(path_txt, "r")

        filename = filename[:-4]            # Remove the .txt extension
        
        # Loop over the lines of the file

        file_boxes = []

        lines = txt.readlines()

        matches = []
        
        for line in lines:
            temp = line.strip().split(" ")
            temp = temp[1:]
            # convert to int
            temp = [float(i) for i in temp]

            matches.append(temp)

        # print(matches)

        
        # Loop over the matches
        if matches:
            for match in matches:
                # Extract the coordinates of the bounding box
                box = []
                center_x = match[0]
                center_y = match[1]
                width = match[2]
                height = match[3]

                # print("center_x: ", center_x, "center_y: ", center_y, "width: ", width, "height: ", height)
                # Multiply with Image size to get the coordinates in pixels - 416x416
                x1 = (center_x - width/2) * 416
                y1 = (center_y - height/2) * 416
                x2 = (center_x + width/2) * 416
                y2 = (center_y + height/2) * 416
                if(x1 < 0):
                    x1 = 0
                if(y1 < 0):
                    y1 = 0
                if(x2 >= 416):
                    x2 = 415
                if(y2 >= 416):
                    y2 = 415
                # print("x1: ", x1, "y1: ", y1, "x2: ", x2, "y2: ", y2)

                # Convert to int
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)
                # Append the coordinates to the list
                box.append(x1)
                box.append(y1)
                box.append(x2)
                box.append(y2)

            file_boxes.append(box)
        
        all_boxes[filename] = file_boxes
        txt.close()
    


    return images, all_boxes


# images and boxes are dictionaries

# images, boxes = read_images()

# print("Number of images: ", len(images))
# print("Number of bounding boxes: ", len(boxes))



# Display the image and the bounding box

# fig, ax = plt.subplots(1)
# ax.imshow(images["1--1-_png.rf.0bf260602d8d60e6f3e1ddaf94523f72"], cmap='gray')

# for box in boxes["1--1-_png.rf.0bf260602d8d60e6f3e1ddaf94523f72"]:

#     print(box)
#     if(len(box) == 0):
#         continue

#     x1 = box[0]
#     y1 = box[1]
#     x2 = box[2]
#     y2 = box[3]
#     rect = patches.Rectangle((x1, y1), x2-x1, y2-y1, linewidth=1, edgecolor='r', facecolor='none')
#     print("x1: ", x1, "y1: ", y1, "x2: ", x2, "y2: ", y2)
#     ax.add_patch(rect)
# plt.show()







