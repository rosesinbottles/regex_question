import unittest
from regexpADP import RegexpADP


class TestRegexpADPFunctions(unittest.TestCase):
    """Test cases for the RegepADP class"""

    def test_no_match_one(self):
        regexp = RegexpADP('hello')
        self.assertEqual(regexp.match("world"), [])

    def test_no_match_two(self):
        regexp = RegexpADP('hello')
        self.assertEqual(regexp.match(""), [])

    def test_no_match_three(self):
        regexp = RegexpADP('')
        self.assertEqual(regexp.match("helloworld"), [])

    def test_no_match_four(self):
        regexp = RegexpADP('hello')
        self.assertEqual(regexp.match("hell"), [])

    def test_match_dot_one(self):
        regexp = RegexpADP('hello.world')
        self.assertEqual(regexp.match("hello|world"), ["hello|world"])

    def test_match_dot_two(self):
        regexp = RegexpADP('hello.world')
        self.assertEqual(regexp.match(
            "hello-world helloworld hello,world hello world"),
            ["hello-world", "hello,world", "hello world"])

    def test_match_dot_three(self):
        regexp = RegexpADP('hello..orld')
        self.assertEqual(regexp.match(
            "hello-world helloworld hello,world hello world"),
            ["hello-world", "hello,world", "hello world"])

    def test_match_question_one(self):
        regexp = RegexpADP('hello?world')
        self.assertEqual(regexp.match("helloworld"), ["helloworld"])

    def test_match_question_two(self):
        regexp = RegexpADP('hello?world')
        self.assertEqual(regexp.match("hellworld"), ["hellworld"])

    def test_match_question_three(self):
        regexp = RegexpADP('hello?world')
        self.assertEqual(regexp.match("hellpworld"), [])

    def test_match_question_four(self):
        regexp = RegexpADP('helo?world')
        self.assertEqual(regexp.match("helloworld"), [])

    def test_match_question_five(self):
        regexp = RegexpADP('abcd?efg')
        self.assertEqual(regexp.match("abcdefg"), ['abcdefg'])

    def test_match_question_six(self):
        regexp = RegexpADP('abcd?efg')
        self.assertEqual(regexp.match("bcefg"), [])

    def test_match_question_seven(self):
        regexp = RegexpADP('ab')
        self.assertEqual(regexp.match("aaaabbbb"), ['ab'])

    def test_match_star_one(self):
        regexp = RegexpADP('hello*world')
        self.assertEqual(regexp.match("hellworld"), ['hellworld'])

    def test_match_star_two(self):
        regexp = RegexpADP('hello*world')
        self.assertEqual(regexp.match("helloworld"), ['helloworld'])

    def test_match_star_three(self):
        regexp = RegexpADP('hello*world')
        self.assertEqual(regexp.match("hellooooworld"), ['hellooooworld'])

    def test_match_star_four(self):
        regexp = RegexpADP('hello*world')
        self.assertEqual(regexp.match("heloworld"), [])

    def test_match_question_dot_one(self):
        regexp = RegexpADP('hell?.')
        self.assertEqual(regexp.match("hello"), ["hell", "hello"])

    def test_match_question_dot_two(self):
        regexp = RegexpADP('hell?.')
        self.assertEqual(regexp.match("help"), ["help"])

if __name__ == '__main__':
    unittest.main()