from fuel import convert, gauge
import pytest


def test_normal():
    assert convert("3/4")==75
def test_negative():
    assert convert("-3/4")==-1
def test_denominator_zero():
    assert convert("3/0")==-1
def test_numirator_greater_than_denominator():
    assert convert("3/2")==-1
def test_full():
    assert gauge(convert("3/3"))=='F'
def test_error():
    assert gauge(convert("0/4"))=='E'
