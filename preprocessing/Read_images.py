import os
import re
import cv2

## Read Images from 10 folders named (00001,00002,...,00010)
## Each folder contains images in .bmp format and a .txt file with the name groundtruth.txt
## groundtruth.txt contains the coordinates of the bounding box of the object in the image
## The images are of size 360x240

# Path to the folder containing the 10 folders
def read_images(path="./datasets/OTCBVS_Pedestrian"):
    # path = "./datasets/OTCBVS_Pedestrian"

    ## Extract Bounding Boxes from groundtruth.txt files
    # Loop over the 10 folders
    boxes = {}
    for i in range(1,11):
        # Path to the folder
        if i < 10:
            path_folder = path + "/0000" + str(i)
        else:
            path_folder = path + "/000" + str(i)
        # Path to the groundtruth.txt file
        path_txt = path_folder + "/groundTruth.txt"
        # Open the groundtruth.txt file
        txt = open(path_txt, "r")
        # Loop over the lines of the file
        for _ in range(4):
            next(txt)           # Skip the first 4 lines
        
        folder_boxes = []
        # Loop over the lines of the file
        for line in txt:
            box = []
            matches = re.findall(r'\((\d+) (\d+) (\d+) (\d+)\)', line)
            # Loop over the matches

            if matches:
                for match in matches:
                    # Extract the coordinates of the bounding box
                    x1, y1 , x2 , y2 = map(int, match)
                    # print("x1: ", x1, "y1: ", y1, "x2: ", x2, "y2: ", y2)
                    # Append the coordinates to the list
                    box.append([x1, y1, x2, y2])
            
            folder_boxes.append(box)
        
        if i < 10:
            boxes["0000" + str(i)] = folder_boxes
        else:
            boxes["000" + str(i)] = folder_boxes

        txt.close()

    # print(len(boxes["00001"]))

    ## Extract Images from .bmp files
    # Loop over the 10 folders
    images = {}
    for i in range(1,11):
        # Path to the folder
        if i < 10:
            path_folder = path + "/0000" + str(i)
        else:
            path_folder = path + "/000" + str(i)
        # Path to the .bmp files
        path_bmp = path_folder
        # List of the .bmp files
        bmp_files = os.listdir(path_bmp)
        # Sort the list of the .bmp files
        bmp_files.sort()
        # Loop over the .bmp files
        folder_images = []

        for bmp_file in bmp_files:
            if bmp_file.endswith(".bmp"):
                
                # Path to the .bmp file
                path_bmp_file = path_bmp + "/" + bmp_file
                # # Open the .bmp file
                # bmp = open(path_bmp_file, "rb")
                # # Read the .bmp file
                # bmp_data = bmp.read()
                # # Append the .bmp file to the list
                # folder_images.append(bmp_data)
                # bmp.close()
                image = cv2.imread(path_bmp_file)

                # Apply Image Enhancement
                # image = image_enhance(image)

                # Append the .bmp file to the list
                folder_images.append(image)


            
        if i < 10:
            images["0000" + str(i)] = folder_images
        else:
            images["000" + str(i)] = folder_images
            
    
    return images, boxes


images, boxes = read_images()

# print(len(boxes["00002"][27]))





