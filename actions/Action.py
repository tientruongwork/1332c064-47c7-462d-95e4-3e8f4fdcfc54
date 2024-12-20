import pyautogui
import time


class Action:
    def __init__(self, xPosition, yPosition):
        self.x = xPosition
        self.y = yPosition
        pass

    def click(self):
        pyautogui.moveTo(x=self.x, y=self.y)
        pyautogui.click()
        time.sleep(0.2)

    def scroll(self):
        self.click()
        pyautogui.vscroll(-9999)
        time.sleep(0.2)
