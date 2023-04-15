import pytest
from ten_thousand.game_logic import GameLogic
from ten_thousand.game import play


def get_inputs(text):
    """Takes text from a sim file and returns a list of strings, representing inputs"""
    text = text.split("\n")
    for line in text:
        if line.starts


def test_quitter(monkeypatch, capsys):
    with open("quitter.sim.txt", "r") as f:
        text = f.read()

