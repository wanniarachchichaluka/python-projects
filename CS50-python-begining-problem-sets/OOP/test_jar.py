import pytest
from jar import Jar

def test_init():
    ...

def test_str():
    jar = Jar()
    assert str(jar)==""
    jar.deposit(8)
    assert str(jar)=="🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(3)
    assert str(jar)=="🍪🍪🍪🍪🍪"
def test_deposit():
    ...
def test_withdraw():
    ...




