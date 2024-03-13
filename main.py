import numpy as np
import pygetwindow as gw
from PIL import ImageGrab
import cv2
import time

def screen_record(window_title):
    target_window = gw.getWindowsWithTitle(window_title)[0]

    last_time = time.time()

    border_thickness = 8

    while True:
        window_left, window_top = target_window.left + border_thickness, target_window.top + border_thickness + 22
        window_width, window_height = target_window.width - 2 * border_thickness, target_window.height - 5 * border_thickness

        printscreen = np.array(ImageGrab.grab(bbox=(window_left, window_top, window_left + window_width, window_top + window_height)))
        print("Loop took {} seconds".format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow("window", cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record("Minecraft* 1.16.5")
