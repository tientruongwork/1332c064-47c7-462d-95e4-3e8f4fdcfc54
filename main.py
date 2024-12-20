import argparse
import time
from workflow.refresh_shop.main import RefreshShopWorkflow

parser = argparse.ArgumentParser()
parser.add_argument(
    "--times", dest="times", type=int, help="Number of shop reset times"
)
args = parser.parse_args()


class Main:
    def __init__(self):
        if not args.times:
            raise Exception("Invalid refresh times")

        self.workflow = RefreshShopWorkflow()
        self.start_time = time.time()

        pass

    def execute(self):
        for i in range(args.times):
            time.sleep(1)
            self.workflow.execute()

        duration = time.time() - self.start_time
        self.workflow.end(duration)


if __name__ == "__main__":
    Main().execute()
