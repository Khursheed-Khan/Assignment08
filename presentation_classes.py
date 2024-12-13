# ------------------------------------------------------------------------------------------ #
# Title: Assignment08 - Presentation Class - Dec 7 2024 at 6pm Pacific
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: Khursheed Khan, Foundations of Programming - Python, Nov 24 2024
#   RRoot,1/1/2030,Created Script
#   First run, Nov 24 2024 ... second run Nov 26 2024 at 9:14am Pacific
#   Updated run, Dec 7 after 6pm Pacific 2024
#   Final run, Dec 12 2024 at 9pm Pacific
# ------------------------------------------------------------------------------------------ #

"""
IO Class for User Interaction in Employee Rating System

This class provides static methods for handling user input and output in the Employee Rating System.
It includes functions for displaying error messages, menus, and employee data, as well as collecting
employee information from the user.

Methods:
    output_error_messages(message: str, error: Exception = None):
        Displays a custom error message along with an optional technical error message.

    output_menu(menu: str):
        Displays a formatted menu to the user.

    input_menu_choice():
        Prompts the user to select a menu option and validates the choice.

    input_employee_data(employee_data: list = None) -> list:
        Collects employee details (first name, last name, review date, review rating) from the user
        and adds them to the provided list of employee data.

    output_employee_data(employee_data: list):
        Displays a list of employees along with their review date and rating.

ChangeLog:
    Khursheed Khan, Nov 18 2024, First update
    RRoot, Jan 1 2030, Created Class

Exceptions:
    ValueError, TypeError: Raised if the user input is invalid when collecting employee data.
"""

import json


from data_classes import Employee

# Presentation --------------- #

class IO:
    """
    A collection of presentation layer functions that manage user input and output.

    Methods:
        output_error_messages(message, error):
            Displays a custom error message and optionally a technical error message.
        output_menu(menu):
            Displays a formatted menu to the user.
        input_menu_choice():
            Prompts the user to select a menu option and validates the choice.
        input_student_data(student_data):
            Collects student details from the user and adds them to the student data list.
        output_student_courses(student_data):
            Displays the list of registered students and their courses.

    ChangeLog:
        Khursheed Khan, Nov 18 2024, first update
        RRoot, Jan 1 2030, Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays a custom error message to the user.

        Args:
            message (str): A descriptive error message.
            error (Exception, optional): The technical error, if available.

        Returns:
            None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        Displays a menu of choices to the user.

        Args:
            menu (str): The formatted menu string to display.

        Returns:
            None
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """
        Prompts the user to select a menu option.

        Returns:
            str: The user's validated menu choice.
        """
        choice = "0"  # Why needed?
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ["1", "2", "3", "4"]:  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(
                e.__str__())  # Not passing the exception object to avoid the technical message # clarify?
        return choice

    @staticmethod
    def input_employee_data(employee_data: list = None) -> list:
        # def input_student_data(student_data:list[Student]=None) -> list[Student]:
        """
        Collects employee data (first name, last name, review date, review grade) from the user.

        Args:
            employee_data (list[dict[str, str]], optional): Existing employee data to update.

        Returns:
            list[dict[str, str]]: Updated list of employee data.
        """
        # Ensure student_data is a list
        if employee_data is None:
            employee_data = []

        try:
            # Collect employee information
            first_name = input("What is the employee's first name? ")
            last_name = input("What is the employee's last name? ")
            review_date = input("What is the employee's review date? ")
            review_rating = input("What is the employee's review rating? ")

            # Create a new Employee object with the collected information
            # Catch any errors

            employee = Employee(first_name, last_name, review_date, review_rating)
            #employee_data.append(employee.__dict__)
            # Add the employee to the list
            employee_data.append(employee)

        except (ValueError, TypeError) as e:
            # Clear the list if any input is invalid
            employee_data.clear()
            IO.output_error_messages("Invalid input provided", e)
            IO.output_error_messages("Invalid input provided", e)

        #except Exception as e:
            #IO.output_error_messages("There was an error registering the employee!", e)

        return employee_data

    @staticmethod
    def output_employee_data(employee_data: list[dict[str, str]]):
        # def output_student_courses(student_data:list[Student]):
        """
                Displays the list of employees with their review date and rating

                Args:
                    employee_data (list[dict[str, str]]): List of student dictionaries to display.

                Returns:
                    None
                """
        if employee_data:
            print("Registered Employees:")
            for employee in employee_data:
                print(f"{employee.first_name} {employee.last_name} {employee.review_date} {employee.review_rating}")
        else:
            print("You have not registered an employee yet")