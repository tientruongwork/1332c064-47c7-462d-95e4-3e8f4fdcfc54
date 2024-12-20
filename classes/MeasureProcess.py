class MeasureProcess:
    covenant_bought = 0
    mystic_bought = 0
    refreshed_times = 0

    def __init__(self, appInfo):
        self.appInfo = appInfo

    def increase_covenant_bought(self):
        self.covenant_bought = self.covenant_bought + 1

    def increase_mystic_bought(self):
        self.mystic_bought = self.mystic_bought + 1

    def increase_refreshed_times(self):
        self.refreshed_times = self.refreshed_times + 1

    def classify_bought_item(self, item_name):
        if item_name == self.appInfo.covenant_bookmarks:
            self.increase_covenant_bought()

        if item_name == self.appInfo.mystic_medals:
            self.increase_mystic_bought()
