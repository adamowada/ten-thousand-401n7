import pytest
from ten_thousand.game_logic import GameLogic
from ten_thousand.game import play


def test_quitter():
    with open("quitter.sim.txt", "r") as f:
        text = f.read()
    
