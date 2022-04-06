import cv2
import pygetwindow
import pyautogui
from PIL import Image
import win32gui
import numpy

TARGET_WINDOW = "RuneScape"
path = "./img.png"

def screenshot(window_title: str):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(x, y, x1, y1))
            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im

titles = pygetwindow.getAllTitles()

if TARGET_WINDOW not in titles:
    print("Error: Couldn't find RS window")
    exit(-1)

im = screenshot(TARGET_WINDOW).convert('RGB')

cv2_buff = cv2.imread("img/turmoil-cropped.png", cv2.IMREAD_COLOR)
cv2_screenshot = numpy.array(im)
cv2_screenshot = cv2_screenshot[:, :, ::-1].copy()

cv2_buff_grey = cv2.cvtColor(cv2_buff, cv2.COLOR_BGR2GRAY)
cv2_screenshot_grey = cv2.cvtColor(cv2_screenshot, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(cv2_buff_grey, 0, 255, cv2.THRESH_BINARY)

#mask = cv2.bitwise_not(mask)
#mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)

#cv2.imshow("Output", mask)
#cv2.waitKey(0)


print("[INFO] performing template matching...")
result = cv2.matchTemplate(cv2_screenshot_grey, cv2_buff_grey,
	cv2.TM_CCOEFF_NORMED, None)

cv2.imshow("Output", mask)
cv2.waitKey(0)

(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

print(f"Max loc: {maxVal} @ {maxLoc}")

(startX, startY) = maxLoc
endX = startX + cv2_buff.shape[1]
endY = startY + cv2_buff.shape[0]

# draw the bounding box on the image
cv2.rectangle(cv2_screenshot, (startX, startY), (endX, endY), (255, 0, 0), 3)
# show the output image
#cv2.imshow("Output", mask)
#cv2.waitKey(0)
cv2.imshow("Output", cv2_screenshot)
cv2.waitKey(0)