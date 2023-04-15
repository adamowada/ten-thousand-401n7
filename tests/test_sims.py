import pytest
from ten_thousand.game_logic import GameLogic
from ten_thousand.game import play


def get_inputs(lines):
    inputs = []
    for line in lines:
        if line.startswith("> "):
            inputs.append(line[2:].strip())  # use slice syntax to remove "> " and "\n" from input
    return inputs


def get_mock_rolls(lines)
    mock_rolls = []
    for line in lines:
        if line.startswith("*** "):
            mock_rolls.append(tuple(int(i) for i in line if ))


@pytest.mark.parametrize(
    "test_input",
    [
        ("tests/bank_first_for_two_rounds.sim.txt"),
        ("tests/bank_one_roll_then_quit.sim.txt"),
        ("tests/cheat_and_fix.sim.txt"),
        ("tests/hot_dice.sim.txt"),
        ("tests/one_and_done.sim.txt"),
        ("tests/quitter.sim.txt"),
        ("tests/repeat_roller.sim.txt"),
        ("tests/zilcher.sim.txt"),
    ],
)
def test_all(monkeypatch, capsys, test_input):
    with open(test_input, "r") as f:
        lines = f.readlines()
        inputs = get_inputs(lines)

    def mock_input(prompt):
        print(prompt, inputs[0], sep="")
        return inputs.pop(0)

    monkeypatch.setattr("builtins.input", mock_input)
    play()
    captured = capsys.readouterr().out.replace("\n\n", "\n")  # jank
    output_lines = captured.split("\n")
    for i, v in enumerate(lines):
        assert v.strip() == output_lines[i]
