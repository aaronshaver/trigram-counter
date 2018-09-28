import unittest
import main


class Case(unittest.TestCase):

    def setup(self):
        pass

    def test_empty_string_should_return_empty_dict(self):
        output = main.count([""])
        self.assertEqual({}, output)

    def test_super_simple_three_word_input(self):
        test_input = "super simple test"
        output = main.count([test_input])
        self.assertTrue("super simple test" in output)
        self.assertEqual(output["super simple test"], 1)

    def test_two_trigrams(self):
        test_input = "this has two trigrams"
        output = main.count([test_input])
        self.assertTrue("this has two" in output)
        self.assertTrue("has two trigrams" in output)
        self.assertEqual(output["this has two"], 1)
        self.assertEqual(output["has two trigrams"], 1)
        # negative tests to make sure our gram "window" isn't sliding too far
        self.assertTrue("two trigrams" not in output)
        self.assertTrue("trigrams" not in output)

    def test_three_trigrams(self):
        test_input = "this has three trigrams now"
        output = main.count([test_input])
        self.assertTrue("this has three" in output)
        self.assertTrue("has three trigrams" in output)
        self.assertTrue("three trigrams now" in output)
        self.assertEqual(output["this has three"], 1)
        self.assertEqual(output["has three trigrams"], 1)
        self.assertEqual(output["three trigrams now"], 1)
        # negative tests to make sure our gram "window" isn't sliding too far
        self.assertTrue("trigrams now" not in output)
        self.assertTrue("now" not in output)
