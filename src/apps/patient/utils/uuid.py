"""uuid generic functions
"""
import uuid
from pydantic import UUID4


def generate_uuid() -> UUID4:
    """generate a UUID4

    Returns:
        UUID4: uuid4 field
    """
    return uuid.uuid4()
