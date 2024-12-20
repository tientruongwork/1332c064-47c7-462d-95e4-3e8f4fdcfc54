import win32gui


class AppInfo:
    application_name = "Epic Seven"
    covenant_bookmarks = "Covenant"
    mystic_medals = "Mystic"

    list_items = [covenant_bookmarks, mystic_medals]

    default_padding = 20

    def __init__(self, use_child_app=False):
        self.parent_app = win32gui.FindWindow(None, self.application_name)

        if use_child_app == True:
            self.child_app = self.get_child_windows(self.parent_app)
            app_rect = self.get_app_rect(self.child_app)
            self.set_app_rect(app_rect)

            return

        app_rect = self.get_app_rect(self.parent_app)
        self.set_app_rect(app_rect)

    def get_child_windows(self):
        child_windows = []

        def enum_child_windows_callback(hwnd, child_windows):
            child_windows.append(hwnd)

        win32gui.EnumChildWindows(
            self.parent_app, enum_child_windows_callback, child_windows
        )

        return child_windows

    def get_app_rect(self, hwnd):
        left, top, right, bottom = win32gui.GetClientRect(hwnd)
        left, top = win32gui.ClientToScreen(hwnd, (left, top))
        right, bottom = win32gui.ClientToScreen(hwnd, (right - left, bottom - top))

        return [left, top, right, bottom]

    def set_app_rect(self, app_rect):
        self.left = app_rect[0] + self.default_padding
        self.top = app_rect[1] + self.default_padding
        self.right = app_rect[2] + self.default_padding
        self.bottom = app_rect[3] + self.default_padding
