import logging
import time

from lib.rate_checker import RateChecker

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s:%(name)s:%(asctime)s: %(message)s')
logger.setLevel(logging.INFO)
logging.debug("Done loading logging")


with context(RateChecker):
    with it('1 times in 1000ms'):
        n_times = 3
        q_millis = 1000
        rate_checker = RateChecker(n_times, q_millis)

        returned_data = rate_checker.check()
        expected_data = False
        logger.debug("returned: {}\nexpected: {}".format(returned_data, expected_data))
        assert returned_data == expected_data

    with it('2 times in 1000ms'):
        n_times = 3
        q_millis = 1000
        rate_checker = RateChecker(n_times, q_millis)

        rate_checker.check()
        returned_data = rate_checker.check()
        expected_data = False
        logger.debug("returned: {}\nexpected: {}".format(returned_data, expected_data))
        assert returned_data == expected_data

    with it('3 times in 1000ms'):
        n_times = 3
        q_millis = 1000
        rate_checker = RateChecker(n_times, q_millis)

        rate_checker.check()
        rate_checker.check()
        returned_data = rate_checker.check()
        expected_data = True
        logger.debug("returned: {}\nexpected: {}".format(returned_data, expected_data))
        assert returned_data == expected_data

    with it('3 times in 1000ms, then 4th after sleep(1)'):
        n_times = 3
        q_millis = 1000
        rate_checker = RateChecker(n_times, q_millis)

        rate_checker.check()
        rate_checker.check()
        returned_data = rate_checker.check()
        expected_data = True
        logger.debug("returned: {}\nexpected: {}".format(returned_data, expected_data))
        assert returned_data == expected_data

        time.sleep(1)

        returned_data = rate_checker.check()
        expected_data = False
        logger.debug("returned: {}\nexpected: {}".format(returned_data, expected_data))
        assert returned_data == expected_data
