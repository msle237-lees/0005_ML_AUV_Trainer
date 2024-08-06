import json
import os
import pyautogui
import time
import logging

class Movement_Package:
    def __init__(self):
        self.keys = {
            "forward": "w",
            "backward": "s",
            "left": "a",
            "right": "d",
            "rotate_left": "q",
            "rotate_right": "e",
            "up": "c",
            "down": "z",
            "cam_increment": "t",
            "cam_decrement": "g"
        }

        self.inputs = {
            "X": 0.0,
            "Y": 0.0,
            "Z": 0.0,
            "Yaw": 0.0
        }

        self.delay = 0.1

    def process(self):
        if self.inputs["X"] > 0:
            pyautogui.keyDown(self.keys["forward"])
            time.sleep(self.delay)
            pyautogui.keyUp(self.keys["forward"])
        elif self.inputs["X"] < 0:
            pyautogui.keyDown(self.keys["backward"])
            time.sleep(self.delay)
            pyautogui.keyUp(self.keys["backward"])
        
        if self.inputs["Y"] > 0:
            pyautogui.keyDown(self.keys["right"])
            time.sleep(self.delay)
            pyautogui.keyUp(self.keys["right"])
        elif self.inputs["Y"] < 0:
            pyautogui.keyDown(self.keys["left"])
            time.sleep(self.delay)
            pyautogui.keyUp(self.keys["left"])

        if self.inputs["Z"] > 0:
            pyautogui.keyDown(self.keys["up"])
            time.sleep(self.delay)
            pyautogui.keyUp(self.keys["up"])
        elif self.inputs["Z"] < 0:
            pyautogui.keyDown(self.keys["down"])
            time.sleep(self.delay)
            pyautogui.keyUp(self.keys["down"])

        if self.inputs["Yaw"] > 0:
            pyautogui.keyDown(self.keys["rotate_right"])
            time.sleep(self.delay)
            pyautogui.keyUp(self.keys["rotate_right"])
        elif self.inputs["Yaw"] < 0:
            pyautogui.keyDown(self.keys["rotate_left"])
            time.sleep(self.delay)
            pyautogui.keyUp(self.keys["rotate_left"])

        
    def set_inputs(self, inputs):
        self.inputs = inputs

    def reset(self):
        self.inputs = {
            "X": 0.0,
            "Y": 0.0,
            "Z": 0.0,
            "Yaw": 0.0
        }
        pyautogui.keyDown("space")
        pyautogui.click(pyautogui.locateOnScreen("images/startButton.png"))
        time.sleep(self.delay)


if __name__ == "__main__":
    movement = Movement_Package()
    movement.process()
    movement.reset()