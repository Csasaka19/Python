# A testcase is created by subclassing unittest.TestCase
import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('clive'.upper(), 'CLIVE')

    def test_isupper(self):
        self.assertTrue("ClIVE".isupper())
        self.assertFalse("clive".isupper())

    def test_split(self):
        s = "Come here"
        self.assertEqual(s.split(), ["Come", "here"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
