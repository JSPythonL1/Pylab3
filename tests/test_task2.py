from tasks.task2 import reverse_input_characters

def test_reverse_basic(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: 'Python')
    assert reverse_input_characters() == 'nohtyP'
