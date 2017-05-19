import logging
import time
from collections import Counter

millis = lambda: time.time()*1000

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s:%(name)s:%(asctime)s: %(message)s')
logger.setLevel(logging.INFO)
logging.debug("Done loading logging")


class IntTracker:
    def __init__(self, n_track):
        self.n_track = n_track
        self.queue = []
        self.counter = Counter()
        pass
    def process(self, array):
        for item in array:
            if item not in self.counter:
                self.counter[item] = 1
            else:
                self.counter[item] += 1
            if item not in self.queue:
                logger.debug("if item not in self.queue: {}".format(self.queue))
                self.queue.append(item)
                logger.debug("queue append: {}".format(self.queue))
                self.queue.sort()
                if len(self.queue) > 5:
                    removed_items = self.queue[:-5]
                    for removed_item in removed_items:
                        del self.counter[removed_item]
                    self.queue = self.queue[-5:]
                logger.debug("queue: {}".format(self.queue))
        return self.queue
