from utils import funny_message


def test_funny_message():
    assert isinstance(funny_message(), str)
