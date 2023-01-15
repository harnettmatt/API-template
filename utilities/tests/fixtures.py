"""Module containing helpful object constructors for mocking purposes"""
from uuid import UUID


def get_mock_uuid():
    """
    creates a mock uuid
    @return: UUID
    """
    return UUID("00000000-0000-0000-0000-000000000000")
