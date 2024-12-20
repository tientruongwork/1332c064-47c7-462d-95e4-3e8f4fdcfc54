class Coordination:
    def __init__(self, measure_process):
        self.measure_process = measure_process
        pass

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
