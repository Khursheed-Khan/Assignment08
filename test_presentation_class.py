
#### With Help from Claude - Dec 7 2024

import unittest
import builtins
from datetime import date
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee


class TestIO(unittest.TestCase):
    def test_input_data_to_table(self):
        employees = []
        with patch("builtins.input", side_effect=["Vic","Vu","2024-10-10","4"]):
            employees = IO.input_employee_data(employees)

        # Check that a Student object is created
        self.assertEqual(len(employees), 1)
        self.assertIsInstance(employees[0], Employee)
        self.assertEqual(employees[0].first_name, "Vic")
        self.assertEqual(employees[0].last_name, "Vu")
        self.assertEqual(employees[0].review_date, date(2024, 10, 10))
        self.assertEqual(employees[0].review_rating, 4)

    def test_invalid_employee_data(self):
        employees = []
        with patch("builtins.input", side_effect=["", "Vu", "invalid-date", "9"]):
            employees = IO.input_employee_data(employees)

        # Check that no Employee objects are created
        self.assertEqual(len(employees), 0)

    def test_multiple_employee_inputs(self):
        employees = []
        with patch("builtins.input", side_effect=[
            "Vic", "Vu", "2024-10-10", "4",
            "John", "Doe", "2024-11-11", "5"
        ]):
            # Simulate multiple inputs
            employees = IO.input_employee_data(employees)
            employees = IO.input_employee_data(employees)

        # Check multiple employees can be added
        self.assertEqual(len(employees), 2)
        self.assertEqual(employees[0].first_name, "Vic")
        self.assertEqual(employees[1].first_name, "John")

    #def test_edge_case_rating(self):
        #employees = []
        #with patch("builtins.input", side_effect=["Vic", "Vu", "2024-10-10", "0"]):
            #with self.assertRaises(ValueError):
                #IO.input_employee_data(employees)

# In this module that I wrote, I am using a list.. not object, my achilles heel, I need to relearn!
#class TestIO(unittest.TestCase):
#   def test_input_data_to_table(self, side_effect=None):
#        students =[]
#        with patch("builtins.input", side_effect = ["Vic", "Vu", "Python"]):
#            IO.input_student_data(students)
#            #IO.input_data_to_table(students)
#        self.assertEqual(students, [["Vic", "Vu", "Python"]])
#        #self.assertEqual(1, len(students))  # add assertion here


if __name__ == '__main__':
    unittest.main()
