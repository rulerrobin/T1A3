from rooms import rooms
import pytest

def test_monster_room(monkeypatch):
    # Test that the monsterRoom function works as expected
    r = rooms()
    monkeypatch.setattr('builtins.input', lambda _: "fight")  # Simulate player input
    r.monsterRoom()
    assert r.player.weapon == False
    monkeypatch.setattr('builtins.input', lambda _: "flee")  # Simulate player input
    r.monsterRoom()
    assert r.player.weapon == False
    monkeypatch.setattr('builtins.input', lambda _: "fight")  # Simulate player input
    r.player.get_weapon()
    assert r.player.weapon == True
    monkeypatch.setattr('builtins.input', lambda _: "flee")  # Simulate player input
    r.monsterRoom()
    assert r.player.weapon == True
