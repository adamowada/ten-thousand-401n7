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
    with open("tests/quitter.sim.txt", "r") as f:
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


@pytest.mark.parametrize(
    "test_input",
    [
        ("tests/bank_first_for_two_rounds.sim"),
        ("tests/bank_one_roll_then_quit.sim"),
        ("tests/cheat_and_fix.sim"),
        ("tests/hot_dice.sim"),
        ("tests/one_and_done.sim"),
        ("tests/quitter.sim"),
        ("tests/repeat_roller.sim"),
        ("tests/zilcher.sim"),
    ],
)
def test_all(test_input):
    pass
