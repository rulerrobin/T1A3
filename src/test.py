from rooms import player, rooms
import pytest

def test_monster_room(monkeypatch):
    # Test that the monsterRoom function works as expected

    r = rooms()

    r.monsterRoom()
    assert r.player.weapon == True

    monkeypatch.setattr('builtins.input', lambda _: "fight")
    i = input("What is your name?")
    assert i == "fight"

    r.monsterRoom()
    assert r.player.weapon == True

    r.monsterRoom("flee")
    assert r.player.weapon == False

    r.monsterRoom("fight")
    assert r.player.weapon == False
