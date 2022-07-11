# Tests can be numerous, and their set-up can be repetitive. Luckily, we can factor out set-up code by implementing a
# method called setUp(), which the testing framework will automatically call for every single test we run
# tearDown() method tidies up after the test method has been run
import unittest


class SimpleWidgetTestCase(unittest.Testcase):


    def setUp(self, Widget):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150),
                         'wrong size after resize')

    def tearDown(self):
        self.widget.dispose()