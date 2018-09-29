import unittest
import counter

# NOTE: besides these, I did "integration" testing on the commandline with
# large text files. I didn't bother to include those tests here for a few
# reasons, including speed and not being 100% sure what the true trigram
# counts were for the texts. I didn't want to assume assertion values I
# couldn't prove.


class Case(unittest.TestCase):

    def test_empty_string_should_return_empty_dict(self):
        output = counter.count([""])
        self.assertEqual({}, output)

    def test_super_simple_three_word_input(self):
        test_input = "super simple test"
        output = counter.count([test_input])
        self.assertTrue("super simple test" in output)
        self.assertEqual(output["super simple test"], 1)

    def test_super_simple_mixed_case(self):
        test_input = "super simple test SUPER SIMPLE TEST"
        output = counter.count([test_input])
        self.assertTrue("super simple test" in output)
        self.assertEqual(output["super simple test"], 2)

    def test_two_trigrams(self):
        test_input = "this has two trigrams"
        output = counter.count([test_input])
        self.assertTrue("this has two" in output)
        self.assertTrue("has two trigrams" in output)
        self.assertEqual(output["this has two"], 1)
        self.assertEqual(output["has two trigrams"], 1)
        # negative tests to make sure our gram "window" isn't sliding too far
        self.assertTrue("two trigrams" not in output)
        self.assertTrue("trigrams" not in output)

    def test_three_trigrams(self):
        test_input = "this has three trigrams now"
        output = counter.count([test_input])
        self.assertTrue("this has three" in output)
        self.assertTrue("has three trigrams" in output)
        self.assertTrue("three trigrams now" in output)
        self.assertEqual(output["this has three"], 1)
        self.assertEqual(output["has three trigrams"], 1)
        self.assertEqual(output["three trigrams now"], 1)
        # negative tests to make sure our gram "window" isn't sliding too far
        self.assertTrue("trigrams now" not in output)
        self.assertTrue("now" not in output)

    def test_simple_repeated_trigram(self):
        test_input = "apples are tasty and also apples are tasty"
        output = counter.count([test_input])
        self.assertTrue("apples are tasty" in output)
        self.assertEqual(output["apples are tasty"], 2)

    def test_strip_special_chars(self):
        test_input = r"super,simple.test:a;few!more&words\"here'and?there"
        output = counter.count([test_input])
        self.assertTrue("super simple test" in output)
        self.assertEqual(output["super simple test"], 1)
        self.assertTrue("simple test a" in output)
        self.assertEqual(output["simple test a"], 1)
        self.assertTrue("test a few" in output)
        self.assertEqual(output["test a few"], 1)
        self.assertTrue("a few more" in output)
        self.assertEqual(output["a few more"], 1)
        self.assertTrue("few more words" in output)
        self.assertEqual(output["few more words"], 1)
        self.assertTrue("more words here" in output)
        self.assertEqual(output["more words here"], 1)
        self.assertTrue("words here and" in output)
        self.assertEqual(output["words here and"], 1)
        self.assertTrue("here and there" in output)
        self.assertEqual(output["here and there"], 1)

    @unittest.skip("Set to ignore because this takes upwards of 5 minutes to run")
    def test_extremely_large_input(self):
        """ This was for doing a convenient in-memory stress test without having to
            gather real files """
        test_input = ""

        # This will produce a string the size of just over 54 copies of Origin of Species
        total_occurrences = 5000000

        for i in range(total_occurrences):
            test_input += "big text here "

        output = counter.count([test_input])
        self.assertTrue("big text here" in output)
        self.assertEqual(output["big text here"], total_occurrences)
