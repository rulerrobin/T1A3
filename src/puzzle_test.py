import pytest
from rooms import rooms

def test_puzzleEscape_correct_guess(capsys, monkeypatch):
    # Set up
    game = rooms()
    monkeypatch.setattr('builtins.input', lambda _: game.__init__.)  # Monkeypatch user input with the random number
    expected_output = "As soon as you enter the numbers doors begin to move and you escape the dungeon!\nEnd\n"

    # Call the function
    game.puzzleEscape

    # Check output and state
    captured = capsys.readouterr()
    assert captured.out == expected_output
    assert game.current_room == "escape"  # or whichever attribute represents the current room state in the Game class


