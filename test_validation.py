import unittest
from validation import normalize_date


class TestValidation(unittest.TestCase):

    def test_dash_date(self):
        self.assertEqual(
            normalize_date("2026-11-01"),
            "2026-11-01",
        )

    def test_slash_date(self):
        self.assertEqual(
            normalize_date("2026/11/01"),
            "2026-11-01"
        )

    def test_invalid_date(self):
        self.assertIsNone(
            normalize_date("banana")
        )


if __name__ == "__main__":
    unittest.main()