# ------------------------------------------------------------------------------------------------- #
# Title: test_data_classes
# # Description: Test harness for the data classes
# ChangeLog: (Who, When, What)
# NPare, 6.18.2025, Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest
from data_classes import Person
from data_classes import Employee

# Define a function to test the Person and Student classes

class TestPerson(unittest.TestCase):

    def test_person_init(self): # Tests the constructor
        person = Person("Test", "Tester")
        self.assertEqual(person.first_name, "Test")
        self.assertEqual(person.last_name, "Tester")

    def test_person_invalid_first_name(self): # Test first name validation
        person = Person("Test", "Tester")
        with self.assertRaises(ValueError):
            person.first_name = "123"

    def test_person_invalid_last_name(self):  # Test last name validation
        person = Person("Test", "Tester")
        with self.assertRaises(ValueError):
            person.last_name = "123"


    def test_person_str(self): # Test the __str__() dunder
        person = Person("Test", "Tester")
        self.assertEqual(str(person), "Test,Tester")

class TestEmployee(unittest.TestCase):

    def test_employee_class(self):
        employee = Employee("Test", "Tester", "2020-01-01", 3)
        self.assertEqual(employee.first_name, "Test")
        self.assertEqual(employee.last_name, "Tester")
        self.assertEqual(employee.review_date, "2020-01-01")
        self.assertEqual(employee.review_rating, 3)

    def test_employee_invalid_review_date(self):
        employee = Employee("Test", "Tester", "2020-01-01", 3)
        with self.assertRaises(ValueError):
            employee.review_date = "123"

    def test_employee_invalid_review_rating(self):
        employee = Employee("Test", "Tester", "2020-01-01", 3)
        with self.assertRaises(ValueError):
            employee.review_rating = 6

if __name__ == "__main__":
    unittest.main()

