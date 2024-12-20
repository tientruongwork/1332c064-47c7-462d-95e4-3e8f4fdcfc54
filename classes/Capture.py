import time
from pytesseract import Output, pytesseract
import win32gui, win32ui
from PIL import Image
from ctypes import windll

pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"


class Capture:
    screenshot_name = "screenshot.png"

    def __init__(self, appInfo):
        self.appInfo = appInfo

    def capture_handler(self):
        hwndDC = win32gui.GetWindowDC(self.appInfo.parent_app)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()

        # Create a bitmap object
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(
            mfcDC, self.appInfo.right, self.appInfo.bottom
        )

        # Select the bitmap object into the device context
        saveDC.SelectObject(saveBitMap)

        # Copy the window's pixels into the device context
        result = windll.user32.PrintWindow(
            self.appInfo.parent_app, saveDC.GetSafeHdc(), 0
        )

        # Convert the device context to a PIL image
        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)
        im = Image.frombuffer(
            "RGB",
            (bmpinfo["bmWidth"], bmpinfo["bmHeight"]),
            bmpstr,
            "raw",
            "BGRX",
            0,
            1,
        )

        # Save the image to a file
        im.save(self.screenshot_name)

    def get_boxes(self):
        for i in range(1):
            self.capture_handler()
            time.sleep(0.1)

        return pytesseract.image_to_data(self.screenshot_name, output_type=Output.DICT)

    def find_all_windows():
        def _enum_windows_callback(hwnd, windows):
            window_text = win32gui.GetWindowText(hwnd)
            if window_text:
                windows.append((hwnd, window_text))

        windows = []
        win32gui.EnumWindows(_enum_windows_callback, windows)

        for hwnd, window_text in windows:
            print(f"Window Handle: {hwnd}, Title: {window_text}")
