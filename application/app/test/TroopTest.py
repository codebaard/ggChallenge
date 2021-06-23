import unittest
from app.model.Troop import Troop

class TroopTest(unittest.TestCase):
    def test_CorrectInitialization(self):
        testTroop = Troop("Test", 10)
        self.assertEqual(testTroop.name, "Test")
        self.assertEqual(testTroop.count, 10)

if __name__ == '__main__':
    unittest.main()
