import pytest
from plates import is_valid

def test_starts_with_two_letters():
    assert is_valid("CS50")==True
def test_first_number_not_0():
    assert is_valid("CS05")==False
def test_numbers_not_in_middle():
    assert is_valid("CS50P")==False
def test_no_other_characters():
    assert is_valid("PI3.14")==False
def test_minimum_two_characters():
    assert is_valid("H")==False
def test_max_six_characters():
    assert is_valid("OUTATIME")==False

