# ------------------------------------------------------------------------------------------------- #
# Title: presentation_classes
# # Description: Classes for user interface
# ChangeLog: (Who, When, What)
# NPare, 6.18.2025, Created Script
# ------------------------------------------------------------------------------------------------- #


# Only run as an imported module
try:
    if __name__ == "__main__":
        raise Exception("Please use the main.py file to start this application.")
except Exception as e:
    print(e.__str__())

class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    NPare,6.18.2025,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays custom error messages to the user

        ChangeLog: (Who, When, What)
        NPare,6.18.2025,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        NPare,6.18.2025,Created function

        :return: None
        """
        print()
        print(menu)
        print()


    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        NPare,6.18.2025,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice


    @staticmethod
    def output_employee_data(employee_data: list):
        """ This function displays employee data to the user

        ChangeLog: (Who, When, What)
        NPare,6.18.2025,Created function

        :param employee_data: list of employee object data to be displayed
        :local review_dict: matches review ratings to their meaning

        :return: None
        """
        review_dict: dict = {1: "Not Meeting Expectations",
                             2: "Building",
                             3: "Solid",
                             4: "Strong",
                             5: "Leading"}

        print()
        print("-" * 50)
        for employee in employee_data:
            msg = " As of {}, {} {} is rated as {} ({})"
            print(msg.format(employee.review_date,
                             employee.first_name,
                             employee.last_name,
                             employee.review_rating,
                             review_dict[employee.review_rating]))
        print("-" * 50)
        print()


    @staticmethod
    def input_employee_data(employee_data: list, employee_type: object):
        """ This function gets the first name, last name, review date, and review rating from the user

        ChangeLog: (Who, When, What)
        NPare,6.18.2025,Created function

        :param employee_data: list of dictionary rows to be filled with input data
        :param employee_type: holds a reference to a data_classes.Employee object

        :return: list
        """

        try:
            # Input the data
            employee_object = employee_type() # This will construct a new Employee object
            employee_object.first_name = input("What is the employee's first name? ")
            employee_object.last_name = input("What is the employee's last name? ")
            employee_object.review_date = input("What is their review date? ")
            employee_object.review_rating = int(input("What is their review rating? "))
            employee_data.append(employee_object)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data
