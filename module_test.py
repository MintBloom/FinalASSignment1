
import unittest
from unittest.mock import patch
from terminal_based_game import enemy_picker

class TestEnemyPicker(unittest.TestCase):
    def test_enemypicker(self ):
        self.assertEqual(enemy_picker(0), 2)




if __name__ == "__main__":
    unittest.main()
