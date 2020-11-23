import unittest
from login_verification import regexp_example


class TestLogin(unittest.TestCase):
    def test_start_latin_true(self):
        self.assertTrue(regexp_example("t")[0])

    def test_start_latin_false(self):
        self.assertFalse(regexp_example("丈")[0])

    def test_start_latin_dot(self):
        self.assertFalse(regexp_example(".")[0])

    def test_start_latin_dash(self):
        self.assertFalse(regexp_example("-")[0])

    def test_contain_symbol_true(self):
        self.assertTrue(regexp_example("sdfg-sdg.sddf")[0])

    def test_contain_symbol_false(self):
        self.assertFalse(regexp_example("sdfg-sdg$sddf")[0])

    def test_last_symbol_true(self):
        self.assertTrue(regexp_example("sdfg-fsdf1")[0])

    def test_last_symbol_false(self):
        self.assertFalse(regexp_example("sdfg-sdg$sddf-")[0])

    def test_length_true(self):
        self.assertTrue(regexp_example("sdgsdfggfd")[0])

    def test_length_false(self):
        self.assertFalse(regexp_example("sdgsdfggfdsdgsdfggfd1")[0])


if __name__ == "__main__":
    unittest.main()
