# ------------------------------------------------------------------------------------------ #
# Title: Assignment08 - Processing Class - Dec 7 2024 at 6pm Pacific
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: Khursheed Khan, Foundations of Programming - Python, Nov 24 2024
#   RRoot,1/1/2030,Created Script
#   First run, Nov 24 2024 ... second run Nov 26 2024 at 9:14am Pacific
#   Updated run, Dec 7 after 6pm Pacific 2024
#   Final run, Dec 12 2024, 9pm Pacific
# ------------------------------------------------------------------------------------------ #

"""
FileProcessor Class for Managing Employee Data with JSON Files

This class provides static methods for reading and writing employee data to/from a JSON file.
It handles the conversion between Employee objects and dictionaries for storage in JSON format.
Additionally, it includes error handling to manage missing files, invalid data, and other potential issues.

Methods:
    read_employee_data_from_file(file_name: str, employee_data: list):
        Reads employee data from a specified JSON file, handles errors (like file not found or invalid JSON),
        and returns a list of Employee objects.

    write_employee_data_to_file(file_name: str, employee_data: list):
        Writes a list of Employee objects to a specified JSON file, converting them to dictionaries
        and ensuring the data is stored in valid JSON format.

ChangeLog:
    Khursheed Khan, Nov 18 2024, First update
    RRoot, Jan 1 2030, Created Class

Exceptions:
    FileNotFoundError: Raised if the specified file does not exist when attempting to read.
    JSONDecodeError: Raised if the file contains invalid JSON data.
    TypeError: Raised when the data is not in the correct format for JSON serialization.
    General Exception: Catches all other unexpected errors.
"""



import json

from data_classes import Employee
from presentation_classes import (IO)

class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files.

    Methods:
        read_data_from_file(file_name, student_data):
            Reads student data from a specified JSON file and returns it as a list of dictionaries.
        write_data_to_file(file_name, student_data):
            Writes a list of student dictionaries to a specified JSON file.

    ChangeLog:
        Khursheed Khan, Nov 18 2024, first update
        RRoot, Jan 1 2030, Created Class
    """

    # When the program starts, read the file data into table
    # Extract the data from the file
    # Read from the Json file

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list):
        # def read_data_from_file(file_name:str, student_data:list[Student]):
        """
               Reads student data from a JSON file. If the file doesn't exist or contains invalid JSON, handles errors.

               Args:
                   file_name (str): Name of the file to read from.
                   student_data (list[dict[str, str]]): An initial list of student data.

               Returns:
                   list[dict[str, str]]: Updated list of student data read from the file.
               """

        try:
            file = open(file_name, "r")

            list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
            for employee in list_of_dictionary_data:  # Convert the list of dictionary rows into Employee objects

                employee_object: Employee = Employee (
                    employee_first_name=employee["FirstName"],
                    employee_last_name=employee["LastName"],
                    employee_review_date=employee["ReviewDate"],
                    employee_review_rating=employee["ReviewRating"],
                )

                employee_data.append(employee_object)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
            IO.output_error_messages("Creating the file")  # Add this to create file if it does not exist
            file = open(file_name, "w")
            file.close()
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return employee_data

    @staticmethod
    #def write_employee_data_to_file(file_name: str, employee_data: list[dict[str, str]]):
    def write_employee_data_to_file(file_name: str, employee_data: list):
        # def write_data_to_file(file_name:str, student_data:list[Student]):
        """
        Writes employee data to a JSON file.

        Args:
            file_name (str): Name of the file to write to.
            employee_data (list[dict[str, str]]): List of employee dictionaries to write.

        Returns:
            None
        """

        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:  # Convert List of Student objects to list of dictionary rows.
                employee_json: dict \
                    = {"FirstName": employee.first_name,
                       "LastName": employee.last_name,
                       "ReviewDate": employee.review_date.isoformat(), # Convert date to ISO format string
                       "ReviewRating": employee.review_rating,
                       }
                list_of_dictionary_data.append(employee_json)

            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if 'file' in locals() and not file.closed:
                file.close()
            #if file.closed == False:
                #file.close()
