class Logger:
    flow_times_placeholder = "___FLOW_PLACEHOLDER___"

    def __init__(self, measure_process):
        self.log_prefix = "Working on flow [" + self.flow_times_placeholder + "]"

        self.measure_process = measure_process
        pass

    def info(self, message):
        log_prefix = self.log_prefix.replace(
            self.flow_times_placeholder, str(self.measure_process.refreshed_times)
        )

        print(log_prefix + " " + message)
