import unittest
from app.model.Army import Army
from app.model.Troop import Troop

class ArmyTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.Army = Army(10)

    def test_CorrectInitialization(self):
        self.assertEqual(10, self.Army.total)
        self.assertEqual(0, len(self.Army.troops))

    def test_CorrectPopulation(self):
        self.Army.populate()
        self.assertEqual(len(self.Army.troops),3)
        self.assertTrue(isinstance(self.Army.troops, list))
        self.assertTrue(isinstance(self.Army.troops[0], Troop))

if __name__ == '__main__':
    unittest.main()
