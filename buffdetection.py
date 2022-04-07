from screencapture import screenshot
import cv2
from PIL import Image
import numpy

from constants import TARGET_WINDOW

def crop_center(img,cropx,cropy):
    y,x = img.shape
    startx = x//2-(cropx//2)
    starty = y//10
    endy = y//2 + starty
    return img[starty:endy,startx:startx+cropx]

def crop(img):
    (y,x,z) = img.shape
    return img[0: (y//10) * 8, 0: x]

def find_buff(threshold, buff_img):
    im = screenshot(TARGET_WINDOW).convert('RGB')

    cv2_buff = cv2.imread(buff_img, cv2.IMREAD_COLOR)
    cv2_screenshot = numpy.array(im)
    cv2_screenshot = cv2_screenshot[:, :, ::-1].copy()
    cv2_screenshot = cv2_screenshot[0:256, 0:240]

    cv2_buff_grey = cv2.cvtColor(cv2_buff, cv2.COLOR_BGR2GRAY)
    cv2_screenshot_grey = cv2.cvtColor(cv2_screenshot, cv2.COLOR_BGR2GRAY)

    cv2_buff_cropped = crop(cv2_buff)

    width = int(cv2_buff_cropped.shape[1] * 5)
    height = int(cv2_buff_cropped.shape[0] * 5)
    dim = (width, height)
    cv2_buff_resized = cv2.resize(cv2_buff_cropped, dim)

    #cv2.imshow('image',cv2_buff_cropped)
    #cv2.waitKey(0)

    # TODO: try reimplementing masking at a later date
    #ret, mask = cv2.threshold(cv2_buff_resized, 0, 255, cv2.THRESH_BINARY)

    #cv2.imshow('image',cv2_buff_cropped)
    #cv2.waitKey(0)

    result = cv2.matchTemplate(cv2_screenshot, cv2_buff_cropped,
        cv2.TM_CCOEFF_NORMED, None)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

    if buff_img == "img/kalg.png":
        print(maxVal)

    #cv2.imshow('image',cv2_buff_cropped)
    #cv2.imshow('image',cv2_screenshot_grey)
    #cv2.waitKey(0)


    return maxVal > threshold