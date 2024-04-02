import unittest
from .funk import D



class DTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("\tsetUpClass")
    @classmethod
    def tearDownClass(cls) -> None:
        print("\ttearDownClass")
    def setUp(self) -> None:
        print("\t\tsetUp")
    def tearDown(self) -> None:
        print("\t\ttearDown")


    def test_1(self):
        print("\t\t\ttest_1")
        d = D(1, 2, -3)
        self.assertEqual(d, (-3.0, 1.0))

    def test_2(self):
        print("\t\t\ttest_2")
        d = D(1, 2, 1)
        self.assertEqual(d, -1)
    # def test_3(self):
    #     print("\t\t\ttest_3")
    #     with self.assertRaises(Exception):
    #         d = D(11, 1, 11)

if __name__ == "__main__":
    unittest.main()
