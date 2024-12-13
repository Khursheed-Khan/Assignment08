# ------------------------------------------------------------------------------------------ #
# Title: Assignment08 - Data_Class - Dec 7 2024 at 6pm Pacific
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: Khursheed Khan, Foundations of Programming - Python, Nov 24 2024
#   RRoot,1/1/2030,Created Script
#   First run, Nov 24 2024 ... second run Nov 26 2024 at 9:14am Pacific
#   Updated run, Dec 7 after 6pm Pacific 2024
#   Final run, Dec 12 2024 at 9pm Pacific
# ------------------------------------------------------------------------------------------ #

"""
Person and Employee Classes for Employee Rating System

This module defines two classes: `Person` and `Employee`, representing an individual
and an employee with additional review information. The classes demonstrate object-oriented
principles and use of properties, exception handling, and static methods for data management.

Class: Person
    The `Person` class is used to represent a person with a first name and a last name.
    It includes validation to ensure that both names are alphanumeric.

    Attributes:
        first_name (str): The first name of the person, must be alphanumeric.
        last_name (str): The last name of the person, must be alphanumeric.

    Methods:
        __str__: Returns a formatted string representation of the person (first name and last name).

Class: Employee (inherits from Person)
    The `Employee` class extends `Person` by adding employee-specific attributes, including a review
    date and review rating. It includes validation for the review rating and review date.

    Attributes:
        review_date (date or str): The date of the employee’s review, either as a date object or ISO 8601 string.
        review_rating (int): The review rating of the employee, an integer between 1 and 5.

    Methods:
        __str__: Returns a string representation of the employee, including first name, last name, review date, and review rating.
        from_json: A static method that creates an Employee object from a JSON-like dictionary.

    Exceptions:
        ValueError: Raised if the first or last name is non-alphanumeric, if the review rating is not an integer between 1 and 5,
                    or if the review date is not a valid date object or ISO 8601 string.
"""




import json
from datetime import date, datetime


class Person:
    __first_name: str = "" # Add default empty string
    __last_name: str = "" # Add default empty string

    def __init__(self, user_first_name: str ="", user_last_name: str =""):
        self.first_name = user_first_name
        self.last_name = user_last_name

    @property
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value):
        # Convert to string and make sure it is alphanumeric
        if (not value.isalpha()):
            raise ValueError("First Name must be alphanumeric")
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value):
        value = str(value)
        # Convert to string and ensure it's alphanumeric
        if (not value.isalpha()):
            raise ValueError("Last Name must be alphanumeric")
        self.__last_name = value


    def __str__(self):
        #return f"first_name: {self.first_name}, last_name: {self.last_name}"
        return f"{self.first_name}, {self.last_name}" #Needed to update for UnitTest


class Employee(Person):
    __review_date: date
    __review_rating: int

    def __init__(self,
                 employee_first_name: str = "",
                 employee_last_name: str = "",
                 employee_review_date: date | str = date(1900, 1, 1), #Accept two different values
                 employee_review_rating: int = 0):
        super().__init__(employee_first_name, employee_last_name)  # Initializing parent class
        #self.__review_date = employee_review_date  # Initializing Employee_Class Attrributes --> setting up consturctor, creating instance
        self.review_date = employee_review_date # Using the setter since self.__review_date bypassed setter?
        #self.__review_rating = employee_review_rating # Does not use the setter
        self.review_rating = employee_review_rating # Use the setter

    @property
    def review_date(self):
        return self.__review_date

    @review_date.setter
    #def review_date(self, value):
        # Convert string to date if needed
    # From Claude, Dec 12 2024
    def review_date(self, value: str | date):
        if isinstance(value, date):
            self.__review_date = value
        elif isinstance(value, str):
            self.__review_date = date.fromisoformat(value)
        else:
            raise ValueError("Review date must be a valid date object or ISO 8601 string")


        ### From Becky
        #try:
                ##convert to date
            #self.__review_date = date.fromisoformat(value)
        #except ValueError:
            #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        ###


        # if isinstance(value, str):
        #     try:
        #         value = datetime.strptime(value, "%Y-%m-%d").date()
        #     except ValueError:
        #         # If conversion fails use default date
        #         raise ValueError(f"Invalid date format for '{value}'. Please use 'YYYY-MM-DD'.")
        #         #value = date(1900, 1, 1)
        # # Ensure it is a date object
        # elif not isinstance(value, date):
        #     raise ValueError(f"Expected a date object, got '{type(value).__name__}'.")
        #     #value = date(1900, 1, 1)
        #
        # self.__review_date = value

    @property
    def review_rating(self) -> int:
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value):
        # Convert to int, default to 0 if invalid
        try:
            value = int(value)
            if value not in range(1, 6):
                raise ValueError(f"Review rating '{value}' is out of range. Must be between 1 and 5.")
                #value = 0
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid review rating: {value}. Must be an integer between 1 and 5.") from e
            #value = 0

        self.__review_rating = value


    def __str__(self):
        return f"{super().__str__()},review_date: {self.review_date},review_rating: {self.review_rating}"

    @staticmethod
    def from_json(data):
        return Employee(
            data.get('first_name', ''),
            data.get('last_name', ''),
            data.get('review_date', date(1900, 1, 1)),
            data.get('review_rating', 0)
        )


