import unittest
from app.functions.randomNumberProvider import randomNumberProvider

class randomNumberProviderTest(unittest.TestCase):

    randomNumberProvider = None
    total = 100
    unitTypeCount = 3

    @classmethod
    def setUp(self):
        self.rnp = randomNumberProvider(self.total, self.unitTypeCount)

    def test_initialization(self):
        self.assertEqual(100, self.rnp.total)
        self.assertEqual(3, self.rnp.unitTypeCount)

    def test_BadQuery(self):
        rnp = randomNumberProvider(2,3)
        self.assertRaises(Exception)

    def test_TotalIsUnitTypeCount(self):
        rnp = randomNumberProvider(3,3)
        self.assertEqual(1, rnp.ggRand())
        self.assertEqual(1, rnp.ggRand())
        self.assertEqual(1, rnp.ggRand())

    def test_RandomNumbersStarved(self):
        rnp = randomNumberProvider(3, 3)

        for i in range(4):
            rnp.ggRand()

        self.assertRaises(Exception)

    def test_TotalIsUnitTypeCountPlusOne(self):
        rnp = randomNumberProvider(4,3)

    def test_lastUnitType(self):
        type1 = self.rnp.ggRand()
        type2 = self.rnp.ggRand()
        residue = 100 - type1 - type2

        self.assertEqual(self.rnp.total, residue)

    def test_randomNumberGenerated(self):
        for i in range(3):
            self.assertTrue(self.rnp.ggRand() >= 1)

if __name__ == '__main__':
    unittest.main()
