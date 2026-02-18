from bank import value
import pytest


def test_starts_with_hello():
    assert value("hello... ...")==0
def test_start_with_h():
    assert value("h... ...")==20
def test_otherwise():
    assert value("... ...")==100
