import pytest
from ten_thousand.game_logic import GameLogic
from ten_thousand.game import play


def get_inputs(lines):
    """
    Get the sim file's inputs
    :param lines: List of lines from sim text's .readlines().
    :return: List of inputs to mock.
    """
    inputs = []
    for line in lines:
        if line.startswith("> "):
            inputs.append(line[2:].strip())  # use slice syntax to remove "> " and "\n" from input
    return inputs


def test_quitter(monkeypatch, capsys):
    with open("tests/quitter.sim.txt", "r") as f:
        lines = f.readlines()
        inputs = get_inputs(lines)

    def mock_input(prompt):
        print(prompt)
        return inputs.pop(0)

    monkeypatch.setattr("builtins.input", mock_input)
    play()
    captured = capsys.readouterr()
    print(captured)
    output_lines = captured.out.strip().split("\n")
    print(output_lines)
    assert len(output_lines) == 4
