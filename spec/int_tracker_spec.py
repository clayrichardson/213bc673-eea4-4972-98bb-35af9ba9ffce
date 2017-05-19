import logging
import time

from lib.int_tracker import IntTracker
from collections import Counter

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s:%(name)s:%(asctime)s: %(message)s')
logger.setLevel(logging.INFO)
logging.debug("Done loading logging")


with context(IntTracker):
    with it('1, 2, 3, 4, 5'):
        n_track = 5
        int_tracker = IntTracker(n_track)

        int_list = [1, 2, 3, 4, 5]
        returned_data = int_tracker.process(int_list)
        expected_data = [1, 2, 3, 4, 5]

        logger.debug("returned: {}\nexpected: {}".format(returned_data, expected_data))
        assert returned_data == expected_data

    with it('counter: 1, 2, 3, 4, 5'):
        n_track = 5
        int_tracker = IntTracker(n_track)

        int_list = [1, 2, 3, 4, 5]
        returned_data = int_tracker.process(int_list)
        expected_data = [1, 2, 3, 4, 5]

        logger.debug("returned: {}\nexpected: {}".format(returned_data, expected_data))
        assert returned_data == expected_data

        returned_data = int_tracker.counter
        expected_data = Counter({
            1: 1,
            2: 1,
            3: 1,
            4: 1,
            5: 1
        })
        logger.debug("returned: {}\nexpected: {}".format(returned_data, expected_data))
        assert returned_data == expected_data

    with it('counter: 0 - 9'):
        n_track = 5
        int_tracker = IntTracker(n_track)

        int_list = range(10)
        returned_data = int_tracker.process(int_list)
        expected_data = list(range(5,10))

        logger.debug("returned: {}\nexpected: {}".format(returned_data, expected_data))
        assert returned_data == expected_data

        returned_data = int_tracker.counter
        expected_data = Counter({5: 1, 6: 1, 7: 1, 8: 1, 9: 1})
        logger.debug("returned: {}\nexpected counter: {}".format(returned_data, expected_data))
        assert returned_data == expected_data


    with it('1 - 10'):
        n_track = 5
        int_tracker = IntTracker(n_track)

        int_list = range(10)
        returned_data = int_tracker.process(int_list)
        expected_data = list(range(5,10))

        logger.debug("returned: {}\nexpected: {}".format(returned_data, expected_data))
        assert returned_data == expected_data

    with it('1 - 100'):
        n_track = 5
        int_tracker = IntTracker(n_track)

        int_list = range(100)
        returned_data = int_tracker.process(int_list)
        expected_data = list(range(95,100))

        logger.debug("returned: {}\nexpected: {}".format(returned_data, expected_data))
        assert returned_data == expected_data
