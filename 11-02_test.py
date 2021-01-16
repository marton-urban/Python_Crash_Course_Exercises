import unittest

from eleven_per_two import city_country


class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_country('santiago', 'chile'), 'Santiago, Chile')

    def test_city_country_population(self):
        self.assertEqual(city_country('santiago', 'chile', 50000), 'Santiago, Chile - population 50000')


if __name__ == '__main__':
    unittest.main()
