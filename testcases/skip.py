# Unittest supports skipping individual test methods or even entire classes
# the keyword skip()(@unittest.skip()) is used
# This happens because some tests are bound to fail so..marking a test as an “expected failure,” a test that is broken
# and will fail, but should not be counted as a failure on a TestResult.
import unittest
import sys


# Basic skipping

class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(my_lib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass


# class skip
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass


# expected fails are skipped using expectedFailure() decorator.
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")



# @unittest.skip(reason)
# Unconditionally skip the decorated test. reason should describe why the test is being skipped.
#
# @unittest.skipIf(condition, reason)
# Skip the decorated test if condition is true.
#
# @unittest.skipUnless(condition, reason)
# Skip the decorated test unless condition is true.
#
# @unittest.expectedFailure
# Mark the test as an expected failure. If the test fails when run, the test is not counted as a failure.
#
# exception unittest.SkipTest(reason)
# This exception is raised to skip a test.