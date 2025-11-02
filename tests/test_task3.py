import os
from tasks.task3 import save_random_array

tmp_path = "result.txt"


def test_random_array(tmp_path):
    filename = tmp_path
    data = save_random_array(filename)
    assert len(data) == 10
    assert all(-5 <= x <= 5 for x in data)
    with open(filename) as f:
        lines = f.readlines()
    assert len(lines) == 10
