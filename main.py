import time
from workflow.refresh_shop.main import RefreshShopWorkflow


class Main:
    def __init__(self):
        self.workflow = RefreshShopWorkflow()
        self.start_time = time.time()

    def execute(self, refresh_times):
        for i in range(refresh_times):
            time.sleep(1)
            self.workflow.execute()

        duration = time.time() - self.start_time
        self.workflow.end(duration)


if __name__ == "__main__":
    refresh_times = int(input("Refresh times: "))
    Main().execute(refresh_times)
