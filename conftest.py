import pytest


def pytest_terminal_summary(terminalreporter, exitstatus):
    total = terminalreporter._numcollected
    passed = len(terminalreporter.stats.get("passed", []))

    terminalreporter.write_sep("-", "📊 PODSUMOWANIE TESTÓW 📊")
    terminalreporter.write_line(f"✅ ZDANE TESTY: {passed}/{total} testów")
