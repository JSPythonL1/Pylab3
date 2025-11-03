from tasks.task5 import histogram
from pathlib import Path

def test_histogram(tmp_path):
    # przygotowanie pliku wejściowego
    input_file = tmp_path / "input.txt"
    input_file.write_text("Ala ma kota", encoding="utf-8")

    output_file = tmp_path / "output.txt"
    result = histogram(input_file, output_file)

    # sprawdzenie, czy wynik jest słownikiem
    assert isinstance(result, dict)

    # sprawdzenie liczebności liter (ignorujemy wielkość liter)
    assert result["a"] == 4   # 'Ala ma kota' → a:4
    assert result["l"] == 1
    assert result["m"] == 1
    assert result["k"] == 1
    assert result["o"] == 1
    assert result["t"] == 1

    # sprawdzenie, że plik wynikowy istnieje
    assert output_file.exists()

    # sprawdzenie, że plik zawiera poprawny format
    content = output_file.read_text(encoding="utf-8")
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    assert all(":" in line for line in lines)
    assert any(line.startswith("a:") for line in lines)
