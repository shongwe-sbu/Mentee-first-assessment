import unittest
from validate_password import validate_password, password_strength

class TestPasswordValidator(unittest.TestCase):

    def test_is_password_secure(self):
        self.assertTrue(validate_password("Phakelas@123"))
    def test_is_password_secure(self):
        self.assertEqual(password_strength("Phakelas@123"), "Strong")

    def test_is_not_secure_short(self):
        self.assertFalse(validate_password("Sibu5"))
    def test_is_not_secure_short(self):
        self.assertEqual(password_strength("Sibu5"), "Weak")

    def test_no_uppercase(self):
        self.assertFalse(validate_password("phakela1-"))
    def test_no_uppercase(self):
        self.assertEqual(password_strength("phakela1-"), "Moderate")

    def test_no_lowercase(self):
        self.assertFalse(validate_password("PHAKELA@"))
    def test_no_lowercase(self):
        self.assertEqual(password_strength("PHAKELA@"), "Moderate")

    def test_no_digit(self):
        self.assertFalse(validate_password("PHAKELA#"))
    def test_no_digit(self):
        self.assertEqual(password_strength("PHAKELA#"), "Moderate")

    def test_no_special_character(self):
        self.assertFalse(validate_password("Phakela$"))
    def test_no_special_character(self):
        self.assertEqual(password_strength("Phakela$"), "Moderate")

    def test_only_letters(self):
        self.assertFalse(validate_password("Phakela"))
    def test_only_letters(self):
        self.assertEqual(password_strength("Phakela"), "Weak")
    
    def test_empty(self):
        self.assertFalse(validate_password(""))
    def test_empty(self):
        self.assertEqual(password_strength(""), "Weak")


if __name__ == "__main__":
    unittest.main()