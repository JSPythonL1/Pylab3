from tasks.task6 import deck, shuffle_deck, deal


def test_deck_basic():
    d = deck()
    assert len(d) == 52
    assert ('A', 's') in d
    assert len(set(d)) == 52


def test_deal():
    d = deck()
    players = deal(d, 4)
    assert len(players) == 4
    assert all(len(p) == 5 for p in players)
