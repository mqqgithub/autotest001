import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print("test start...>")
        self.x = 5
        self.y = 2

    def tearDown(self):
        print("test over...>")

    def test_01(self):
        z = self.x / self.y
        self.assertEqual(z, 2.5, msg="除以")

    def test_02(self):
        z = self.x // self.y
        self.assertEqual(z, 2, msg="商")

    def test_03(self):
        z = self.x % self.y
        self.assertEqual(z, 1, msg="余数")

    def test_04(self):
        z = self.x ** self.y
        self.assertEqual(z, 25, msg="乘方")


if __name__ == "__main__":
    unittest.main()




