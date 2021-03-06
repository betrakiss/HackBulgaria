import unittest
from fight import Fight
from hero import Hero
from orc import Orc
from weapon import Weapon


class TestFight(unittest.TestCase):
    def setUp(self):
        self.varyan = Hero("Varyan Wrynn", 100, "King")
        self.garrosh = Orc("Garrosh Hellscream", 100, 7)

        self.weak_weapon = Weapon("Noob Weapon", 10, 0.1)
        self.strong_weapon = Weapon("Woo Weapon", 20, 0.7)

        self.fight = Fight(self.varyan, self.garrosh)

    def test_simulate_fight_win(self):
        self.varyan.equip_weapon(self.strong_weapon)
        self.garrosh.equip_weapon(self.weak_weapon)
        self.assertIsNotNone(self.fight.simulate_fight())

if __name__ == '__main__':
    unittest.main()
