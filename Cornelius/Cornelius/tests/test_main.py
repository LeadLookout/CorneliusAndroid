import unittest
from main import main

class TestMain(unittest.TestCase):
    def test_launch(self):
        try:
            main()
        except Exception as e:
            self.fail(f"Launch failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()
