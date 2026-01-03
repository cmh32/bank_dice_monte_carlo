import pytest
import os
import sys
# ensure repo root is on sys.path so tests can import the top-level module `dice`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dice import simulate_round


class SequenceRNG:
    def __init__(self, seq):
        self.seq = list(seq)
        self.i = 0

    def randint(self, a, b):
        if self.i >= len(self.seq):
            raise IndexError("No more numbers in SequenceRNG")
        val = self.seq[self.i]
        self.i += 1
        return val


def test_seven_in_first_three_adds_70():
    # Rolls (pairs): (1,6)=7, (1,1)=2, (2,3)=5, (3,4)=7 (ends after 3rd roll)
    seq = [1, 6, 1, 1, 2, 3, 3, 4]
    rng = SequenceRNG(seq)
    total, hist = simulate_round(rng, verbose=False)

    assert total == 77
    assert hist[0]["sum"] == 7
    assert hist[0]["total"] == 70


def test_doubles_after_three_double_total():
    # Rolls: (2,3)=5, (2,4)=6, (1,1)=2 -> total 13 after 3 rolls
    # then (3,3) doubles total to 26, then (4,3)=7 ends round
    seq = [2, 3, 2, 4, 1, 1, 3, 3, 4, 3]
    rng = SequenceRNG(seq)
    total, hist = simulate_round(rng, verbose=False)

    assert total == 26

    doubles_entries = [h for h in hist if h["dice_1"] == h["dice_2"] and h["rolls_after"] > 3]
    assert doubles_entries, "expected at least one post-3-roll doubles roll"
    doubles_entry = doubles_entries[0]
    idx = hist.index(doubles_entry)
    prev_total = hist[idx - 1]["total"] if idx > 0 else 0
    assert doubles_entry["total"] == prev_total * 2


def test_seven_after_three_ends_round_without_adding():
    # Rolls: (1,1)=2, (2,2)=4, (3,3)=6 -> total 12 after 3 rolls
    # then (3,4)=7 ends round without adding
    seq = [1, 1, 2, 2, 3, 3, 3, 4]
    rng = SequenceRNG(seq)
    total, hist = simulate_round(rng, verbose=False)

    assert total == 12
    assert len(hist) == 3


def test_plain_sums_accumulate_before_end():
    # Rolls: (1,1)=2, (1,2)=3, (1,3)=4 -> total 9 after 3 rolls
    # then (3,4)=7 ends round; final total should be 9
    seq = [1, 1, 1, 2, 1, 3, 3, 4]
    rng = SequenceRNG(seq)
    total, hist = simulate_round(rng, verbose=False)

    assert total == 9
    assert sum(h["sum"] for h in hist) == 9
    assert len(hist) == 3
