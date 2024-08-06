import pyautogui
import cv2
import numpy as np
import time

class Camera:
    def __init__(self):
        self.keys = {
            "camera_increment": "t",
            "camera_decrement": "g"
        }

    def take_screenshot(self):
        imgs = []
        for _ in range(3):
            imgs.append(pyautogui.screenshot(region=(0, 0, 1920, 1080)))
            time.sleep(0.1)
            pyautogui.press(self.keys["camera_increment"])
        for _ in range(3):
            pyautogui.press(self.keys["camera_decrement"])
        return imgs
    
    def process_image(self, imgs):
        pass