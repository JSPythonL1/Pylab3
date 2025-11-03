from tasks.task3 import save_random_array
from pathlib import Path


def test_random_array(tmp_path):
    directory = tmp_path
    filename = "wyniki.txt"

    data = save_random_array(directory, filename)

    # Długość i zakres wartości
    assert len(data) == 10
    assert all(-5 <= x <= 5 for x in data)

    # Czy plik został utworzony
    result_file = Path(directory) / filename
    assert result_file.exists()

    # Czy plik zawiera 10 linii
    lines = result_file.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 10
