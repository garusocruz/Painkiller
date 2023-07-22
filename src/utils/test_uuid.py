import unittest

from unittest.mock import Mock, patch

from .uuid import generate_uuid, uuid


class TestGenerateUUID(unittest.TestCase):
    """Test case to grantee a function genetare_uuid return an uuid4"""

    @patch("uuid.uuid4", return_value="00000000-0000-0000-0000-000000000000")
    def test_generate_uuid(self, mock_uuid4):
        """Test generate_uuid function.

        Ensures that the generate_uuid function returns the expected UUID.

        This test uses the unittest.mock.patch to mock the uuid.uuid4 function
        and force it to return a known UUID value ('00000000-0000-0000-0000-000000000000').
        """
        result = generate_uuid()
        expected = "00000000-0000-0000-0000-000000000000"

        self.assertEqual(
            result, expected, "The generated UUID does not match the expected value"
        )

    def test_generate_uuid_returns_uuid(self):
        """Test generate_uuid function returns UUID.

        Ensures that the generate_uuid function returns an instance of UUID from pydantic.
        """
        result = generate_uuid()

        self.assertIsInstance(
            result, uuid.UUID, "The generated UUID is not of type UUID4"
        )

    def test_generate_uuid_unique(self):
        """Test generate_uuid function generates unique UUIDs.

        Ensures that the generate_uuid function produces unique UUIDs when called repeatedly.
        """
        unique_uuids = set()
        for _ in range(1000):
            uuid_value = generate_uuid()
            self.assertNotIn(uuid_value, unique_uuids, "Generated UUIDs are not unique")
            unique_uuids.add(uuid_value)
