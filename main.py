# ------------------------------------------------------------------------------------------ #
# Title: Assignment08 - Main Module - Dec 7 2024 at 6pm Pacific
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: Khursheed Khan, Foundations of Programming - Python, Nov 24 2024
#   RRoot,1/1/2030,Created Script
#   First run, Nov 24 2024 ... second run Nov 26 2024 at 9:14am Pacific
#   Updated run, Dec 7 after 6pm Pacific 2024
# ------------------------------------------------------------------------------------------ #

"""
Employee Registration Program

This program allows users to manage employee ratings by providing functionalities to:
    - Enter new employee rating data.
    - View current employee rating data.
    - Save rating data to a JSON file.
    - Load saved rating data on startup.

The program employs exception handling for file operations and input validation
to maintain data integrity. It uses an interactive menu system for user input
and performs actions based on the selected option.

Features:
    - Register new employee ratings.
    - Display current employee ratings.
    - Save employee ratings to a JSON file.
    - Exit the program.

Constants:
    - MENU: A string constant representing the menu options.
    - FILE_NAME: The file name used to store and load employee data.
    - employees: A list holding dictionaries of employee rating data.
    - menu_choice: A string variable to store the user’s menu selection.

Classes and Modules:
    - IO (from `presentation_classes`): Handles input and output operations.
    - FileProcessor (from `processing_classes`): Handles file operations like reading and writing data.

ChangeLog:
    Khursheed Khan, Dec 7 2024, Updated the script to reflect employee ratings functionality.
    Khursheed Khan, Dec 12 2024, took help from ChatGpt to formalize docustring.
    RRoot, Jan 1 2030, Refactored script for better readability and structure.
"""


from presentation_classes import IO
from processing_classes import FileProcessor

# Define the Data Constants
MENU: str = '''
---- Employee Ratings ----
   Select from the following menu:  
    1. Enter new employee rating data.
    2. Show current employee rating data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "EmployeeRatings.json"
employees: list[dict[str,str]] =[] # Set to empty
menu_choice: str = str() # Hold the choice made by the user.

FileProcessor.read_employee_data_from_file(FILE_NAME,employees)

# Repeat the following tasks
while True:
    #application_classes.IO.output_error_messages(menu=MENU)
    IO.output_menu(menu=MENU) # Display menu
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Get new data (and display the change)
        #students = application_classes.IO.output_menu(menu=MENU)
        employees = IO.input_employee_data(employee_data=employees) # Register student

    elif menu_choice == "2": # Display current data
        IO.output_employee_data( employee_data=employees)

    elif menu_choice == "3":  # Save data in a file
        FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)

    elif menu_choice == "4":  # End the program
        print("Program ended, thanks")
        break  # out of the while loop
    else:
        print ("Please select a valid menu option 1, 2 or 3")

    # Load updated data?
    #students = application_classes.FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)
print ("Program Ended")