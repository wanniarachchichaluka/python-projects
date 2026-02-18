import pytest
from twttr import shorten

def test_all_capital():
    assert shorten("CHALUKA PAMINTHA")=="CHLK PMNTH"
def test_all_simple():
    assert shorten("chaluka pamintha")=="chlk pmnth"
def test_mix():
    assert shorten("Chaluka PaMInThA")=="Chlk PMnTh"
def test_with_characters():
    assert shorten("Cha7l89Uka Pa*minTha")=="Ch7l89k P*mnTh"