import unittest
from app.functions.randomNumberProvider import randomNumberProvider

class randomNumberProviderTest(unittest.TestCase):

    randomNumberProvider = None
    total = 100
    unitTypeCount = 3

    @classmethod
    def setUp(self):
        self.randomNumberProvider = randomNumberProvider(self.total, self.unitTypeCount)

    def test_initialization(self):
        self.assertEqual(100, self.randomNumberProvider.total)
        self.assertEqual(3, self.randomNumberProvider.unitTypeCount)


    def test_BadQuery(self):
        rnp = randomNumberProvider(2,3)

    def test_TotalIsUnitTypeCount(self):
        rnp = randomNumberProvider(3,3)

    def test_TotalIsUnitTypeCountPlusOne(self):
        rnp = randomNumberProvider(4,3)

    def test_lastUnitType(self):
        print("prending")

    def test_randomNumberGenerated(self):
        self.assertTrue()

if __name__ == '__main__':
    unittest.main()
