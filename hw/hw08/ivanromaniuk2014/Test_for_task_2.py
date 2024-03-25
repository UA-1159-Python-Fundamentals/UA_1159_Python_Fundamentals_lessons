import unittest
from  PRACTICAL_TASK_8_2 import valid_pasword

class TestValidPassword(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(valid_pasword("Passw0rd$#@"))
        self.assertTrue(valid_pasword("MyP@ssw0rd"))
        self.assertTrue(valid_pasword("QWERT12#w"))
        self.assertFalse(valid_pasword("password"))
        self.assertFalse(valid_pasword("P@sswrd"))
        self.assertFalse(valid_pasword("Pssword12"))
        self.assertFalse(valid_pasword("12345"))
        self.assertFalse(valid_pasword("1234567890qwertyuio"))

if __name__ == "__main__":
    unittest.main()