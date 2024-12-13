import unittest
from datetime import date
from data_classes import Employee

from data_classes import Person


class TestPerson(unittest.TestCase):
    def test_person_init(self):
        p = Person('vic', 'vu')
        self.assertEqual(p.first_name,'Vic')
        self.assertEqual(p.last_name,'Vu')

    def test_person_invalid_name(self):
        with self.assertRaises(ValueError):
            p = Person('V1c', 'V1u')

    def test_person_str(self):
        p = Person('Vic', 'Vu')
        self.assertEqual("Vic, Vu", str(p))

class TestEmployee(unittest.TestCase):
    def test_employee_init(self):
        emp = Employee('vic', 'vu', date(2024, 12, 12), 5)
        self.assertEqual(emp.first_name, 'Vic')
        self.assertEqual(emp.last_name, 'Vu')
        self.assertEqual(emp.review_date, date(2024, 12, 12))
        self.assertEqual(emp.review_rating, 5)

    def test_employee_invalid_name(self):
        with self.assertRaises(ValueError):
            Employee('V1c', 'Vu', date(2024, 12, 12), 5)

    #def test_employee_invalid_date(self):
    #    with self.assertRaises(ValueError):
    #       Employee('Vic', 'Vu', '2024-12-12', 5)  # Date must be a `date` object, not a string

    def test_employee_invalid_rating(self):
        with self.assertRaises(ValueError):
            Employee('Vic', 'Vu', date(2024, 12, 12), 6)  # Rating above 5

        with self.assertRaises(ValueError):
            Employee('Vic', 'Vu', date(2024, 12, 12), 0)  # Rating below 1

    #def test_employee_str(self):
    #    emp = Employee('Vic', 'Vu', date(2024, 12, 12), 4)
    #    self.assertEqual(str(emp), "Vic Vu (2024-12-12): 4/5")

if __name__ == '__main__':
    unittest.main()
