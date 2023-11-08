import cv2

# get MSER regions
def getMSERregions(img):
    # create MSER object
    mser = cv2.MSER_create()
    # detect MSER regions
    regions, mser_bboxes = mser.detectRegions(img)
    # get bounding boxes from regions
    bboxes = []
    for region in regions:
        x, y, w, h = cv2.boundingRect(region)
        bboxes.append([x, y, x+w, y+h])
    return bboxes , mser_bboxes

# get MSER regions from all images
def getMSERregionsAll(images,dataset="OTCBVS_Pedestrian"):
    # create dictionary to store MSER regions
    regions = {}
    # loop over all images

    if dataset == "OTCBVS_Pedestrian":
        for key in images.keys():
            # create list to store MSER regions
            regions[key] = []
            # loop over all images in folder
            for img in images[key]:
                # convert image to grayscale
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # get MSER regions
                bboxes , mser_bboxes = getMSERregions(img)
                # append MSER regions to list
                regions[key].append(bboxes)
    elif dataset == "ASL-TID":
        for key in images.keys():
            # create list to store MSER regions
            regions[key] = []
            # convert image to grayscale
            img = cv2.cvtColor(images[key], cv2.COLOR_BGR2GRAY)
            # get MSER regions
            bboxes , mser_bboxes = getMSERregions(img)
            # append MSER regions to list
            regions[key] = bboxes
    return regions
