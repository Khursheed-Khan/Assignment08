import os
import tempfile
import unittest
import json


from data_classes import Employee
from processing_classes import FileProcessor



class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile()
        self.temp_file_name = self.temp_file.name
        self.student_data=[]

    def tearDown(self):
        self.temp_file.close()

    def test_write_data_to_file(self):
        sample_employees = [
            Employee("John", "Doe", "2020-01-01", 3),
            Employee("Vic", "Vu", "2024-01-01", 1)
        ]

        ### You need to provide a list to FileProcessor not object...
        #sample_students=[{
        #    Student("John", "Doe", "Python-100"),
        #    Student("Vic", "Vu", "Python-100")
        #}]

        FileProcessor.write_employee_data_to_file(self.temp_file_name,sample_employees)
        self.assertTrue(os.path.isfile(self.temp_file.name))

        # Read and verify the written data
        with open(self.temp_file_name, 'r') as file:
            loaded_data = json.load(file)

        # Check number of records
        self.assertEqual(len(loaded_data), 2)

        # Check specific data
        self.assertEqual(loaded_data[0]['FirstName'], 'John')
        self.assertEqual(loaded_data[0]['LastName'], 'Doe')
        self.assertEqual(loaded_data[0]['ReviewDate'], '2020-01-01')
        self.assertEqual(loaded_data[0]['ReviewRating'], 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)