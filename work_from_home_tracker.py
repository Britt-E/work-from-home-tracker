##############################################################
# Name:          ICTPRG302 practical task
# Purpose:       Employee work from home tracker
# Requires:      See individual Modules following
# Author:        Brittany Evans
# Contributors:  Add name(s) for anyone who might have helped here
# Copyright:     Add copyright info here, if any, such as
#                (c) YourName 2022
# Licence:       Add license here you'd like to use, such as creative
#                commons, GPL, Mozilla Public License, etc.
#                e.g. CC BY 2.0 AU
#                https://creativecommons.org/licenses/by/2.0/au/
# Created:       16/03/2024
# Last Modified: 14/04/2024 
# Versioning    ("MAJOR.MINOR.PATCH") Such as Version 1.0.0
##############################################################
# NOTES:
# https://www.w3schools.com/python/default.asp
# ^ an excellent resource to check as you code
##############################################################
#------------------------------------------------------------
#
#------------------------------------------------------------



def Main_Menu():

    while(True):
        # Forever loop. Needs a break, return, or exit() statement to
        # exit the loop.
        # Placing the menu inside of the while loop "Refreshes" the menu
        # if an incorrect value is supplied.
        # Notice the Multiline """ String

        # option = None  # Declares a menu variable as empty.

        print("""==============================================
MAIN MENU
==============================================
1 - Enter Daily Hours Worked
2 - Produce Hours Worked Report

9 - Exit The Application
-------------------------------------------------""")
        option = input("Enter your menu choice: ")
        print("----------------------------------------------")

        # Check what choice was entered and act accordingly
        # We can add as many choices as needed

        if option == '1':
            Enter_Daily_Hours_Worked()
        elif option == '2':
            Produce_Hours_Worked_Report()
        elif option == '9':
            print("Exiting the application...")

            break
        else:
            print("Invalid option. Please enter a number from the Menu Option.")


## ---> END of MAIN MENU <---

def Enter_Daily_Hours_Worked():
    # Set some variables to hold values for the application
    # Also helps for better code readability
    min_daily_hours = 4
    max_daily_hours = 10
    min_weekly_hours = 30
    max_weekly_hours = 40
    good_min_weekly_hours = 37
    good_max_weekly_hours = 39

    # Data Structure 1
    # https://www.w3schools.com/python/python_dictionaries.asp
    employee_hours_worked = {
        "WeekNumber": "",
        "EmployeeID": "",
        "EmployeeName": "",
        "Monday": "",
        "Tuesday": "",
        "Wednesday": "",
        "Thursday": "",
        "Friday": "",
        }

    # employee_hours_worked data structure:
    # 0 WeekNumber, 1 EmployeeID, and 2 EmployeeName are range 0-2
    # Days of week are range 3-7
    # Using these ranges we can loop between employee detail and day entries
    # See routine: Part A) Enter Daily Hours Worked, and D) Summary for Employee Week

    starting_day = 3

    # Data Structure 2
    weekly_report = {
        "Employee 1": 0,
        "Employee 2": 0,
        "Employee 3": 0,
        "Employee 4": 0,
        "Employee 5": 0,
        "Employee 6": 0,
        "Employee 7": 0,
        }

# Part A) Enter Employee Details
    # Start of For loop for 7 Employees
    for employee_count, employee_number in enumerate(weekly_report):
        print()
        print()
        print("==============================================")
        print("Enter details for Employee", employee_count + 1)
        # employee_count variable starts at 0, so we + 1 to offset the print
        # employee number message.
        print("==============================================")
        employee_hours_worked["WeekNumber"] = "week " + str(input("Enter the current working week number >> "))
        print()  # Line Break
        employee_hours_worked["EmployeeID"] = str(input("Enter the Employee ID >> "))
        print()  # Line Break
        employee_hours_worked["EmployeeName"] = str(input("Enter the employee name >> "))
        print("----------------------------------------------")
        print()  # Line Break

# Part A) Enter Daily Hours Worked
        print("==============================================")
        print("Enter hours per day for employee ", employee_hours_worked["EmployeeName"].capitalize())
        print("==============================================")
        # https://www.w3schools.com/python/python_dictionaries.asp
        # https://www.programiz.com/python-programming/methods/built-in/enumerate
        for count, Day in enumerate(employee_hours_worked):
            if  count >= starting_day:  # Monday ->
                print("Enter employee hours worked for ", Day, " >> ", end='')
                employee_hours_worked[Day] = str(input())
                print()  # Line Break
        print("----------------------------------------------")
        print()  # Line Break

# Part B) and D) Summary for Employee Week
        # Build our string ID_name_week_for_heading (String concatenation)
        # Heading will show as "Summary for employee ID:%s NAME:%s Week:%s"
        # Example: Summary for employee" ID:"43" NAME:"Jackson" Week:"17"
        ID_name_week_for_heading = "ID: "
        ID_name_week_for_heading = ID_name_week_for_heading + employee_hours_worked["EmployeeID"]
        ID_name_week_for_heading = ID_name_week_for_heading + " Name: "
        ID_name_week_for_heading = ID_name_week_for_heading + employee_hours_worked["EmployeeName"].capitalize()
        ID_name_week_for_heading = ID_name_week_for_heading + " "
        ID_name_week_for_heading = ID_name_week_for_heading + employee_hours_worked["WeekNumber"]

# Part B) and D)
        print("==============================================")
        print("Summary for Employee", ID_name_week_for_heading)
        print("==============================================")
        day_within_limits_flag = 0
        # A variable to set up a flag that allows for a split if-else block
        # inside of the following loop.
        total_hours = 0
        for count, Day in enumerate(employee_hours_worked):
            if  count >= starting_day:  # Monday ->
                # Add all hours for the weekly total.
                total_hours = total_hours + int(employee_hours_worked[Day])
                if int(employee_hours_worked[Day]) < min_daily_hours:
                    # See min_daily_hours variable at start of program
                    # where we set this amount.
                    day_within_limits_flag = 1
                    # Flag is set to true, so we can skip the following if that
                    # is outside of this loop.
                    print(employee_hours_worked["EmployeeName"], "has not worked enough hours on", Day)
                elif int(employee_hours_worked[Day]) > max_daily_hours:
                    # See max_daily_hours variable at start of program
                    # where we set this amount.
                    day_within_limits_flag = 1
                    print(employee_hours_worked["EmployeeName"], "has worked too many hours on", Day)
            else:
                pass
        if day_within_limits_flag == 0:
            # The if-else block part 2.  If flag is set to 1 (True) we
            # can skip this.
            print(employee_hours_worked["EmployeeName"], "has worked within the expected daily hours.")

        print(employee_hours_worked["EmployeeName"], "worked a total of", total_hours, "hours in", employee_hours_worked["WeekNumber"])

# Part B)
        weekly_report[employee_number] = total_hours
        if total_hours < min_weekly_hours:
            # See min_weekly_hours variable at start of program
            # where we set this amount.
            print(employee_hours_worked["EmployeeName"], "did not work enough hours in", employee_hours_worked["WeekNumber"])
        elif total_hours > max_weekly_hours:
            # See max_weekly_hours variable at start of program
            # where we set this amount.
            print(employee_hours_worked["EmployeeName"], "worked too many hours in", employee_hours_worked["WeekNumber"])
        else:
            print(employee_hours_worked["EmployeeName"], "has worked the expected weekly hours.")

        print("----------------------------------------------")
        print()  # Line Break

# Part C) Write to CSV
        # Note! The file write is still inside our for loop and appends the data
        # for each employee until the 3 employee records are reached.
        # The file is opened and then closed for each employee in this example.
        file_csv_out = "DailyHours_DB.csv"
        # Output file to write to.  Notice we save not as *.txt but to *.csv
        # ==> Open Output file for text append ops
        with open(file_csv_out, "a") as file:
            str_buffer = ",".join(employee_hours_worked.values())
            # Join the elements of employee_hours_worked to a
            # single ',' delimited string.
            str_buffer = str_buffer + '\n'  # append a new line character \n
            file.write(str_buffer)
            # Write/append 'a' str_buffer to file.

    # End of For loop for 3 Employees <---

# Part E) Employee Weekly Report
    not_enough_hours = 0
    too_many_hours = 0
    good_number_of_hours = 0

    for employee_number_counter_2 in weekly_report:
        if weekly_report[employee_number_counter_2] <= min_weekly_hours:
            # See min_weekly_hours variable at start of program
            # where we set this amount.
            not_enough_hours = not_enough_hours + 1
        elif weekly_report[employee_number_counter_2] >= max_weekly_hours:
            # See max_weekly_hours variable at start of program
            # where we set this amount.
            too_many_hours = too_many_hours + 1
        elif (weekly_report[employee_number_counter_2]
        >= good_min_weekly_hours) and (int(weekly_report[employee_number_counter_2])
        <= good_max_weekly_hours):
            # From earlier elif to here, this could be all on one line
            # Python recommends max. 99 characters to one line, so split this
            # statement across three lines
            # see https://www.python.org/dev/peps/pep-0008/#maximum-line-length
            good_number_of_hours = good_number_of_hours + 1
        else:
            pass

# Part E)
    print("=================================================")
    print("Weekly Employee Report")
    print("=================================================")
    print(not_enough_hours, "employees worked less than 30 hours a week")
    print(too_many_hours, "employees worked more than 40 hours a week")
    print(good_number_of_hours, "employees worked between 37-39 hours a week")
    print("-------------------------------------------------")
    print()  # Line Break
    input("Press [Enter] to return to the MAIN MENU...")

    return None
# END of Enter_Daily_Hours_Worked <---

def Produce_Hours_Worked_Report():
# Part G)

    # fields = ['Week Number', 'Employee ID', 'Employee Name', 'Monday Hrs',
    # 'Tuesday  Hrs', 'Wednesday Hrs', 'Thursday Hrs', 'Friday Hrs']
    # range(start, stop)
    file_csv_in = "DailyHours_DB.csv"
    # Our earlier CSV formatted file. Notice we open *.csv and not *.txt.
    csv_list = []
    # main Data List. CSV converted to list.

    # It is possible that the file may not yet exist. Opening it
    # as "r" will return an exception. Let's test if the file exists first.
    try:
        with open(file_csv_in, "r") as file:  # Open the CSV File.
        # read the file into Data Structure 3 (2 dimensional Linked List)
            for buffer in file:
                # Walk each line from the file (returns ',' in the string
                # with '\n' at the end
                buffer = buffer.strip('\n')
                # Strip the newline character from the line.
                buffer_list = buffer.split(',')
                # Separate the lines at ',' to a single list.
                csv_list.append(buffer_list)
                # Append each single dimension list to a 2 dimension list.

        print("==============================================")
        print("Hours Worked Report")
        option = input('How many reports would you like to display >> ')
        # Will default to str/text input
        print("----------------------------------------------")

        # Check if the report number is more than the entries available.
        if len(csv_list) < int(option):
            int_rep_number = len(csv_list)
        else:
            int_rep_number = int(option)

        # Calculate the position of the last item in the list
        # minus our report number to display.
        report_start = len(csv_list) - 1
        report_stop = len(csv_list) - int_rep_number - 1
        report_step = -1
        # Walk over list -1 step at a time (or in other words, reversed)

        # Walk through the List in reverse order and print each
        # line(Row) as text.
        # Remember that a list with 5 elements has an index
        # from [0] to [4], thus the -1
        # range() automatically converts real numbers to index numbers
        for i in range(report_start, report_stop, report_step):
            # csv_list steps backward through the number of rows.
            for j in range(len(csv_list[i])):
                # Step through each element(column) in the row.
                print(csv_list[i][j], end=" ")
                # print each cell value in the row. This will repeat for
                # the number of columns in j.
            print()  # End of row [j], next i in range()

        input("Press [Enter] to return to the MAIN MENU...")
        return None

    except FileNotFoundError:  # If the file does not yet exist.
        print("The CSV file has not yet been created.")
        print("Please select Option 1 from the MAIN Menu")
        print("to start the data entry.")
        input("Press [Enter] to return to the MAIN MENU...")
        return None

## ---> END Application Specific Routines <---

Main_Menu()

## ---> Script Exit <---

