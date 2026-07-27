"""
Christopher Craig
CSD-325, Module 7

test_cities.py - unit tests for the city_country() function defined
in city_functions.py.
"""
import unittest

from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    """Tests for the city_country() function."""

    def test_city_country(self):
        """Do two simple names, like Santiago and Chile, work?"""
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()
