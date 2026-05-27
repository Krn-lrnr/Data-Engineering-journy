import time

class PipelineTimer:

    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        end_time = time.time()

        runtime = end_time - self.start_time

        print(f"\nPipeline runtime: {runtime:.2f} seconds")

        return runtime