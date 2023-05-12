from rooms import rooms
import pytest

def test_monster_room(monkeypatch, capsys):     # tests False weapon and fight
    # Test that the monsterRoom function works as expected
    r = rooms()
    r.player.weapon = False  # Set player weapon to False
    monkeypatch.setattr('builtins.input', lambda _: "fight")  # Simulate player input

    r.monsterRoom()

    captured = capsys.readouterr()  # Get printed output
    expected_output = "YOU HAVE NO WEAPON AND DIED"
    assert expected_output in captured.out
