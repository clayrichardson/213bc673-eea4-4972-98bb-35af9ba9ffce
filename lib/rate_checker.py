import logging
import time
from collections import deque

millis = lambda: time.time()*1000

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s:%(name)s:%(asctime)s: %(message)s')
logger.setLevel(logging.INFO)
logging.debug("Done loading logging")


class RateChecker:
    def __init__(self, n_times, q_millis):
        self.n_times = n_times
        self.q_millis = q_millis
        self.operation_queue = deque()
        pass
    def check(self):
        current_millis = millis()
        logger.debug("current_millis: {}".format(current_millis))
        self.operation_queue.append(current_millis)
        if len(self.operation_queue) < self.n_times:
            return False

        return current_millis - self.operation_queue.popleft() <= self.q_millis
