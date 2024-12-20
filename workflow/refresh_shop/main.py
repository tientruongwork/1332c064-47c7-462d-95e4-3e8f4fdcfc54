from classes.Logger import Logger
from classes.AppInfo import AppInfo
from classes.MeasureProcess import MeasureProcess
from classes.Capture import Capture
from classes.Coordination import Coordination
from actions.Action import Action


class RefreshShopWorkflow:
    def __init__(self):
        print("Executing refresh shop workflow")

        self.app_info = AppInfo()
        self.capture = Capture(self.app_info)
        self.measure_process = MeasureProcess(self.app_info)
        self.coordination = Coordination(self.app_info, self.measure_process)
        logger = Logger(self.measure_process)

        self.log = logger.info

    def click_refresh(self):
        self.log("Refresh current shop")

        Action(
            xPosition=self.coordination.refresh_button_rect[0],
            yPosition=self.coordination.refresh_button_rect[1],
        ).click()
        Action(
            xPosition=self.coordination.refresh_confirm_button_rect[0],
            yPosition=self.coordination.refresh_confirm_button_rect[1],
        ).click()

        self.measure_process.increase_refreshed_times()

    def buy_item_in_list(self, buy_list_coordinate):
        for item in buy_list_coordinate:
            xPosition, yPosition = item
            if xPosition != 0 | yPosition != 0:
                item_buy_button_x = self.app_info.left + xPosition * 1.6667
                item_buy_button_u = self.app_info.top + yPosition * 0.9968

                Action(xPosition=item_buy_button_x, yPosition=item_buy_button_u).click()
                Action(
                    xPosition=self.coordination.buy_confirm_button_rect[0],
                    yPosition=self.coordination.buy_confirm_button_rect[1],
                ).click()

    def scan_for_items(self, scrolled):
        self.log("Scanning for item")
        boxes = self.capture.get_boxes()

        buy_list_coordinate = self.coordination.get_item_coordinate_from_texts(
            boxes, self.app_info.list_items
        )

        self.buy_item_in_list(buy_list_coordinate)
        if scrolled:
            self.click_refresh()

    def execute(self):
        self.scan_for_items(False)
        Action(
            xPosition=self.coordination.blank_rect[0],
            yPosition=self.coordination.blank_rect[1],
        ).scroll()
        self.scan_for_items(True)

    def end(self, duration):
        print("Auto refresh shop ended")
        print("Finished in " + str(duration) + " seconds")
        print("Covenant bought: " + str(self.measure_process.covenant_bought))
        print("Mystic bought: " + str(self.measure_process.mystic_bought))
        print("Refreshed time: " + str(self.measure_process.refreshed_times))
