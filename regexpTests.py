import unittest
from regexpADP import RegexpADP


class TestRegexpFunctions(unittest.TestCase):

    def test_match(self):
        regexp = RegexpADP('hello.world')
        self.assertEqual(regexp.match("hello|world"), ["hello|world"])
        self.assertEqual(regexp.match(
            "hello-world helloworld hello,world hello world"),
            ["hello-world", "hello,world", "hello world"])
        self.assertTrue(True)
        # self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()