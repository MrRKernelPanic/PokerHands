import pytest
from poker_hands import check_hand


def test_raise_exception_if_hand_is_empty():
    with pytest.raises(Exception):
        check_hand("")