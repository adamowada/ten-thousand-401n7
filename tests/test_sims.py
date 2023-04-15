import pytest
from ten_thousand.game_logic import GameLogic
from ten_thousand.game import play


def get_inputs(lines):
    inputs = []
    for line in lines:
        if line.startswith("> "):
            inputs.append(line[2:].strip())  # use slice syntax to remove "> " and "\n" from input
    return inputs


def test_quitter(monkeypatch, capsys):
    with open("tests/quitter.sim.txt", "r") as file:
        lines = [line.strip() for line in file]
        # print(lines)
        inputs = get_inputs(lines)

    def mock_input(prompt):
        print(prompt, inputs[0], sep="")
        return inputs.pop(0)

    monkeypatch.setattr("builtins.input", mock_input)
    # print('hello')
    play()
    captured = capsys.readouterr()
    print(captured)
    # print("co", captured.out)
    # print("raw", lines)
    assert False
