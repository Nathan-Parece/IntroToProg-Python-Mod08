# ------------------------------------------------------------------------------------------------- #
# Title: test_processing_classes
# # Description: Test harness for the processing classes
# ChangeLog: (Who, When, What)
# NPare, 6.18.2025, Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest
import tempfile # Needed to test reading and writing
import json
import data_classes as data
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile()
        self.test_file.close()
        self.employee_data = []

    def tearDown(self):
        self.test_file.close()

    def test_read_employee_data_from_file(self):
        # Create test data and write to test file
        test_data = [
            {"FirstName": "Test", "LastName": "Tester", "ReviewDate": "2001-01-01", "ReviewRating": 5},
            {"FirstName": "Vic", "LastName": "Vu", "ReviewDate": "2021-05-04", "ReviewRating": 1}
        ]
        with open(self.test_file.name, "w") as file:
            json.dump(test_data, file)

        # Read the data
        FileProcessor.read_employee_data_from_file(self.test_file.name, self.employee_data, data.Employee)

        # Check the data
        for n in range(0,len(test_data)):
            self.assertEqual(self.employee_data[n].first_name, test_data[n]["FirstName"])
            self.assertEqual(self.employee_data[n].last_name, test_data[n]["LastName"])
            self.assertEqual(self.employee_data[n].review_date, test_data[n]["ReviewDate"])
            self.assertEqual(self.employee_data[n].review_rating, test_data[n]["ReviewRating"])


    def test_write_employee_data_to_file(self):
        # Create test data and add to employee data list
        test_data = [
            {"FirstName": "Test", "LastName": "Tester", "ReviewDate": "2001-01-01", "ReviewRating": 5},
            {"FirstName": "Vic", "LastName": "Vu", "ReviewDate": "2021-05-04", "ReviewRating": 1}
        ]
        for employee in test_data:
            employee_object = data.Employee()
            employee_object.first_name = employee["FirstName"]
            employee_object.last_name = employee["LastName"]
            employee_object.review_date = employee["ReviewDate"]
            employee_object.review_rating = employee["ReviewRating"]
            self.employee_data.append(employee_object)

        # Write test data to test file
        FileProcessor.write_employee_data_to_file(self.test_file.name, self.employee_data)

        # Read and check test data
        with open(self.test_file.name, "r") as file:
            processed_test_data = json.load(file)
            for n in range(0, len(test_data)):
                self.assertEqual(processed_test_data[n]["FirstName"], test_data[n]["FirstName"])
                self.assertEqual(processed_test_data[n]["LastName"], test_data[n]["LastName"])
                self.assertEqual(processed_test_data[n]["ReviewDate"], test_data[n]["ReviewDate"])
                self.assertEqual(processed_test_data[n]["ReviewRating"], test_data[n]["ReviewRating"])


if __name__ == "__main__":
    unittest.main()