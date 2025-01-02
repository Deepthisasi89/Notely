"""Data Class for our Note."""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Note:
    """Note DataClass."""
    ID: str
    title: str
    body: str
    createdat: datetime = field(default_factory=datetime.now)
    updatedat: datetime = field(default_factory=datetime.now)
