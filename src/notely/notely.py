"""notely is a note taking application currently with 2 helper functions for setup."""
from notely.note import Note
import uuid


def get_title() -> str:
    """Gets the title of a note. Currently Always Returns note title.

    Returns: Note Title
    """
    return "Note Title"


def get_note() -> str:
    """Get the body of a note. Currently always returns note body.

    Returns: Note Body
    """
    return "Note Body"


def create_note() -> Note:
    return Note(
        ID=str(uuid.uuid4()),
        body="body",
        title="title"
    )



