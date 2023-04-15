import pytest
from ten_thousand.game_logic import GameLogic
from ten_thousand.game import play


def get_inputs(lines):
    """
    Get the sim file's inputs
    :param text: List of lines from sim text's .readlines().
    :return: List of inputs to mock.
    """
    inputs = []
    for line in lines:
        if line.startswith("> "):
            inputs.append(line[2:])  # use slice syntax to remove "> " from input
    return inputs


def test_quitter(monkeypatch, capsys):
    with open("quitter.sim.txt", "r") as f:
        inputs = get_inputs(f.readlines())

