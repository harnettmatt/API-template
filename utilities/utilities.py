"""Module containing random helper functions"""
import uuid


class Utilities:
    """
    utility functions
    """

    @staticmethod
    def generate_uuid() -> uuid.UUID:
        """
        creates a uuid
        @return: UUID
        """
        return uuid.uuid4()
