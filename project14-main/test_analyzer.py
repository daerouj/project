import pytest
from analyzer import analyze_verb

def test_analyze_verb():
    assert analyze_verb("читав") == {"word": "читав", "time": "past", "number": "sing", "gender": "masc"}
    assert analyze_verb("читати") == {"word": "читати", "time": None, "number": None, "gender": None}
    assert "error" in analyze_verb("будинок")