"""This module contains tests for Notely."""

from notely.notely import get_note, get_title


def test_get_title() -> None:
    expected_value = "Note Title"
    assert get_title() == expected_value


def test_get_body() -> None:
    expected_value = "Note Body"
    assert get_note() == expected_value
