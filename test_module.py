import unittest
from demographic_data_analyzer import calculate_demographic_data

data = calculate_demographic_data(print_data=False)


class CensusAnalyzerTests(unittest.TestCase):

    def test_race_count(self):
        self.assertIsInstance(data['race_count'], object)
        self.assertEqual(data['race_count']['White'], 27816)

    def test_average_age_men(self):
        self.assertEqual(data['average_age_men'], 39.4)

    def test_percentage_bachelors(self):
        self.assertEqual(data['percentage_bachelors'], 16.4)

    def test_higher_education_rich(self):
        self.assertEqual(data['higher_education_rich'], 46.5)

    def test_lower_education_rich(self):
        self.assertEqual(data['lower_education_rich'], 17.4)

    def test_min_work_hours(self):
        self.assertEqual(data['min_work_hours'], 1)

    def test_rich_percentage(self):
        self.assertEqual(data['rich_percentage'], 10.0)

    def test_highest_earning_country(self):
        self.assertEqual(data['highest_earning_country'], 'Iran')

    def test_highest_earning_country_percentage(self):
        self.assertEqual(data['highest_earning_country_percentage'], 41.9)

    def test_top_IN_occupation(self):
        self.assertEqual(data['top_IN_occupation'], 'Prof-specialty')


if __name__ == '__main__':
    unittest.main()