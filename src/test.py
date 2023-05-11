from rooms import rooms
import pytest

# def test_monster_room(monkeypatch):
#     # Test that the monsterRoom function works as expected
#     r = rooms()
#     monkeypatch.setattr('builtins.input', lambda _: "fight")  # Simulate player input
#     r.monsterRoom()
#     assert r.player.weapon == False
#     monkeypatch.setattr('builtins.input', lambda _: "flee")  # Simulate player input
#     r.monsterRoom()
#     assert r.player.weapon == False
#     monkeypatch.setattr('builtins.input', lambda _: "fight")  # Simulate player input
#     r.player.get_weapon()
#     assert r.player.weapon == True
#     monkeypatch.setattr('builtins.input', lambda _: "flee")  # Simulate player input
#     r.monsterRoom()
#     assert r.player.weapon == True

def test_monster_room(monkeypatch, capsys):
    # Test that the monsterRoom function works as expected
    r = rooms()
    r.player.weapon = False  # Set player weapon to False
    monkeypatch.setattr('builtins.input', lambda _: "fight")  # Simulate player input

    r.monsterRoom()

    captured = capsys.readouterr()  # Get printed output
    expected_output = "YOU HAVE NO WEAPON AND DIED"
    assert captured.out == expected_output

    monkeypatch.setattr('builtins.input', lambda _: "flee")  # Simulate player input

    r.monsterRoom()

    captured = capsys.readouterr()  # Get printed output
    expected_output = "You escape the room and return to the previous location"
    assert captured.out == expected_output