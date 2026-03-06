import pytest
from seasons import cal_mins

def test_1():
    assert cal_mins("2025-03-06")==525600
def test_2():
    assert cal_mins("2024-03-06")==1051200




