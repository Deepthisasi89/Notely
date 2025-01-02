"""This module contains tests for Notely."""

import jsons
from typing import List
from datetime import datetime
from notely.note import Note
from notely.notely import create_note, get_note, get_title


def test_get_title() -> None:
    expected_value = "Note Title"
    assert get_title() == expected_value


def test_get_body() -> None:
    expected_value = "Note Body"
    assert get_note() == expected_value

def test_create_note() -> None:
    expected_value = Note(ID="TODO", title="title", body="body")
    actual_value = create_note()
    print(expected_value)
    assert expected_value.title == actual_value.title
    assert expected_value.body == actual_value.body

def test_jsons() -> None:
    my_json = '{"ID": "TODO", "body": "note is really long", "createdat": "2024-12-31T14:55:15.503494+00:00", "title": "title", "updatedat": "2024-12-31T14:55:15.503500+00:00"}'
    my_note = jsons.loads(my_json, Note)

    assert my_note.body == "note is really long"
    assert my_note.createdat == datetime.fromisoformat("2024-12-31T14:55:15.503494+00:00")


def test_json_list() -> None:
    my_json = '[{"ID": "TODO", "body": "body", "createdat": "2024-12-31T14:55:15.503494+00:00", "title": "title", "updatedat": "2024-12-31T14:55:15.503500+00:00"},{"ID": "TODO", "body": "body", "createdat": "2024-12-31T14:55:15.503494+00:00", "title": "title", "updatedat": "2024-12-31T14:55:15.503500+00:00"},{"ID": "TODO", "body": "body", "createdat": "2024-12-31T14:55:15.503494+00:00", "title": "title", "updatedat": "2024-12-31T14:55:15.503500+00:00"}]'
    my_notes = jsons.loads(my_json, list[Note])

    assert len(my_notes) == 3
