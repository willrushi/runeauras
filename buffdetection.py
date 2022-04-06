from screencapture import screenshot
import cv2
from PIL import Image
import numpy

def find_buff(target_window, threshold, buff_img):
    im = screenshot(target_window).convert('RGB')

    cv2_buff = cv2.imread(buff_img, cv2.IMREAD_COLOR)
    cv2_screenshot = numpy.array(im)
    cv2_screenshot = cv2_screenshot[:, :, ::-1].copy()

    cv2_buff_grey = cv2.cvtColor(cv2_buff, cv2.COLOR_BGR2GRAY)
    cv2_screenshot_grey = cv2.cvtColor(cv2_screenshot, cv2.COLOR_BGR2GRAY)

    ret, mask = cv2.threshold(cv2_buff_grey, 0, 255, cv2.THRESH_BINARY)

    result = cv2.matchTemplate(cv2_screenshot_grey, cv2_buff_grey,
        cv2.TM_CCOEFF_NORMED, None)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

    return maxVal > threshold