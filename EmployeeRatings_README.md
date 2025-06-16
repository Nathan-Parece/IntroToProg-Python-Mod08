# Intro to Programming Final: Employee Ratings

Employee Ratings is a Python script for writing and reviewing employee ratings.

## Features

Employee Ratings is a feature-rich application. 

### UI 

- This application runs in a terminal window. All options are available on launch and reported to the user as a part of the menu choice prompt.
- Invalid menu choices return the user to the main menu. 
- The application formats both saved data and new data in a user-friendly and readable way.

### Unit Testing

Employee Ratings comes with robust unit testing. Each module has its own test harness, and all functions that mutate or return data have test functions. These unit test use Python's unittest library, as well as some standard libraries not used in the main file.  
    To test your install, run each of the labeled test files from the terminal:
  
> python test_presentation_classes.py  
> python test_data_classes.py  
> python test_processing_classes.py

The main module does not have a test harness; instead, it comes equipped with custom error messages to help troubleshoot any issues that might occur.

### Error Handling

Employee Ratings handles many common errors using custom error messages which describe the error in detail. Any unexpected errors are caught and reported in full, preventing many potential crashes and ensuring data integrity.  
Employee Ratings also supports new custom error messages through the output_error_messages method. This method can display both verbose and sparse error messages, depending on its arguments. 

### Data Validation

Employee Ratings validates data when it's input and every time it's accessed. The application includes three different kinds of data validation. 
- Name Validation: This application requires that all names include only letters, and automatically adjusts capitalization. Invalid names are discarded immediately. 
- Review Date Validation: This application automatically ensures that review dates are in the standard YYYY-MM-DD format, and allows reviews to be backdated to any valid date. 
- Review Rating Validation: This application can automatically detect ratings that don't fit into the 1-5 point scale and discards these ratings.
Invalid inputs return the user to the main menu. 

### Saving and Loading  

Employee Ratings is capable of saving user input to a JSON file, EmployeeRatings.json. This file is provided in this repository, but isn't essential: if the file doesn't exist, the application will create one the first time data is saved. 
- Saving: Data isn't automatically saved. Instead, it can be manually saved from the application menu. The application turns the saved Employee objects into a JSON-formatted string and uses json.dump to save that string to a file. 
- Loading: Data is automatically loaded when the application runs. Employee Ratings transforms valid JSON data into a list of Employee objects, and will warn the user if it attempts to load invalid data.

### Scope Control
Each non-main module used by Employee Ratings has code that ensures it can only be imported, and not run as the  main module. Likewise, the main module has code that ensures it won't be accidentally imported. By checking whether the file is being used in a valid way before running, these modules save resources and time. 

## Installation

You can use git to install Employee Ratings. 

## Contribute

Source Code: [github](https://github.com/Nathan-Parece/IntroToProg-Python-Mod08)    
This project isn't currently accepting contributions. 

## Support

This project is unsupported as of June 18th, 2025. 

