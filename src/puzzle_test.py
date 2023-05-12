from rooms import rooms
import pytest

# def test_puzzle_escape(monkeypatch, capsys):
#     # Set up mock user input and random number
#     mock_input = "12345678\ny\n"
#     random_number = "12345678"
#     def mock_user_input(_):
#         nonlocal mock_input
#         return mock_input

#     r = rooms()
#     # Monkeypatch the `input` function to use the mock input
#     monkeypatch.setattr('builtins.input', mock_user_input)

#     # Call `puzzle_escape` and capture the output to the console
#     r.puzzleEscape()
#     captured = capsys.readouterr()

#     # Assert that the expected output was printed to the console
#     expected_output = "As soon as you enter the numbers doors begin to move and you escape the dungeon!\nEnd\n"
#     assert captured.out == expected_output

def test_puzzleEscape_correct_guess(capsys, monkeypatch):
    # Set up
    game = rooms()
    monkeypatch.setattr('builtins.input', lambda _: game.__init__())  # Monkeypatch user input with the random number

    # Call the function
    game.puzzleEscape()

    # Check output and state
    captured = capsys.readouterr()
    expected_output = "As soon as you enter the numbers doors begin to move and you escape the dungeon!"
    assert expected_output in captured.out
