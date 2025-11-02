from tasks.task5 import histogram

tmp_path = "text.txt"


def test_histogram(tmp_path):
    f = tmp_path
    f.write_text("Ala ma kota")
    h = histogram(f)
    assert isinstance(h, dict)
    assert h['a'] >= 2
