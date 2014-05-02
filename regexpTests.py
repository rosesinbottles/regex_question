import unittest
from regexpADP import RegexpADP


class TestRegexpADPFunctions(unittest.TestCase):
    """Test cases for the RegepADP class"""

    def test_match_dot_one(self):
        regexp = RegexpADP('hello.world')
        self.assertEqual(regexp.match("hello|world"), ["hello|world"])

    def test_match_dot_two(self):
        regexp = RegexpADP('hello.world')
        self.assertEqual(regexp.match(
            "hello-world helloworld hello,world hello world"),
            ["hello-world", "hello,world", "hello world"])

    def test_match_question(self):
        regexp = RegexpADP('hello?world')
        # self.assertEqual(regexp.match("hello"), ["hello"])
        # self.assertEqual(regexp.match("hell"), ["hell"])
        # self.assertEqual(regexp.match("helloworld"), ["helloworld"])
        # self.assertEqual(regexp.match("hellworld"), ["hellworld"])

if __name__ == '__main__':
    unittest.main()