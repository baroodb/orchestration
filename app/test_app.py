import pytest
from app.main import read_root


def test_get_root():
    message = read_root()
    assert message == {'Response': 'Hello World'}


