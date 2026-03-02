import pytest
from working import convert

def test_1():
    assert convert("9:00 AM to 5:00 PM")=="09:00 to 17:00"
    assert convert("9:45 AM to 5:23 PM")=="09:45 to 17:23"
def test_2():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
def test_3():
    assert convert("9:00 AM to 5 PM")=="09:00 to 17:00"
    assert convert("9 AM to 5:00 PM")=="09:00 to 17:00"
def test_4():
    with pytest.raises(ValueError):
        convert("9:78 AM to 5:45 PM")==0
        convert("9:18 AM to 13:45 PM")==0


