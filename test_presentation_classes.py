# ------------------------------------------------------------------------------------------------- #
# Title: test_presentation_classes
# # Description: Test harness for the presentation classes
# ChangeLog: (Who, When, What)
# NPare, 6.18.2025, Created Script
# ------------------------------------------------------------------------------------------------- #


import unittest
from unittest.mock import patch # This lets us test inputs automatically
import io
from contextlib import redirect_stdout # This lets us test outputs automatically
from presentation_classes import IO
from data_classes import Employee

# Define IO tests for each method

class TestIO(unittest.TestCase):
    def setUp(self): # Creates an empty list for testing
        self.employee_data = []

    def test_input_menu_choice(self): # Tests return
        with patch('builtins.input', side_effect='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')

    def test_input_employee_data(self): # Tests setters, invalid data types
        with patch('builtins.input', side_effect=['Test', 'Tester','2001-01-01',5]):
            IO.input_employee_data(employee_data=self.employee_data,employee_type=Employee)
            self.assertEqual(self.employee_data[0].first_name, 'Test')
            self.assertEqual(self.employee_data[0].last_name, 'Tester')
            self.assertEqual(self.employee_data[0].review_date, '2001-01-01')
            self.assertEqual(self.employee_data[0].review_rating, 5)

        with patch('builtins.input', side_effect=[5, 'Tester','2001-01-01',5]): # Invalid first name
            IO.input_employee_data(employee_data=self.employee_data,employee_type=Employee)
            self.assertEqual(len(self.employee_data),1)

        with patch('builtins.input', side_effect=['Test',5,'2001-01-01',5]): # Invalid last name
            IO.input_employee_data(employee_data=self.employee_data,employee_type=Employee)
            self.assertEqual(len(self.employee_data),1)

        with patch('builtins.input', side_effect=['Test', 'Tester',5,5]): #Invalid review date
            IO.input_employee_data(employee_data=self.employee_data,employee_type=Employee)
            self.assertEqual(len(self.employee_data),1)

        with patch('builtins.input', side_effect=['Test', 'Tester','2001-01-01',7]):
            IO.input_employee_data(employee_data=self.employee_data,employee_type=Employee)
            self.assertEqual(len(self.employee_data),1) # Should be an empty list due to invalid data

    def test_output_employee_data(self): # Test output formatting
        # Create a test employee
        test_employee = Employee("Test", "Tester", "2001-01-01", 3)
        self.employee_data.append(test_employee)

        # Check formatting
        with io.StringIO() as buf, redirect_stdout(buf):
            IO.output_employee_data(employee_data=self.employee_data)
            self.assertEqual(buf.getvalue(), "\n" + "-"* 50 + "\n"
                                            " As of 2001-01-01, Test Tester is rated as 3 (Solid)\n"
                                            + "-" * 50 + "\n\n")



if __name__ == '__main__':
    unittest.main()