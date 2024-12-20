import csv


class Coordination:
    coordination_file_path = "coordination.csv"

    def __init__(self, app_info, measure_process):
        self.app_info = app_info
        self.measure_process = measure_process

        self.set_action_rect()

    def set_action_rect(self):
        with open(self.coordination_file_path, mode="r") as file:
            csvFile = csv.reader(file)
            for column in csvFile:
                type = column[0]
                rect = [
                    self.app_info.left + self.app_info.width * (float(column[1]) / 100),
                    self.app_info.top + self.app_info.height * (float(column[2]) / 100),
                ]

                if type == "refresh_button":
                    self.refresh_button_rect = rect
                elif type == "refresh_confirm":
                    self.refresh_confirm_button_rect = rect
                elif type == "buy_confirm":
                    self.buy_confirm_button_rect = rect
                elif type == "blank":
                    self.blank_rect = rect

    def get_item_coordinate_from_texts(self, boxes, texts):
        item_coordinates = []

        for i in range(len(boxes["level"])):
            box_text = boxes["text"][i]
            if box_text in texts:
                self.measure_process.classify_bought_item(box_text)
                item_coordinates.append([boxes["left"][i], boxes["top"][i]])

        if len(item_coordinates) == 0:
            return []

        return item_coordinates
