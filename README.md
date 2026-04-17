# UtechLinks-Student-Discount-Club
Members:
Rojaunie Brown (ID:2400699)
Joel Williams (ID: 2405374)
Dominic Tracey  (ID: 2407700)
Khaleel Kellerman  (ID:2002442)


Problem Statement:
In the university setting, such as UTech, students are faced with various challenges throughout their courses of study. Two commonly observed challenges are financial constraints and time-bound limitations, which can prevent students from being fully focused on their studies. The aim of this project is to alleviate some of these challenges by implementing more efficient and effective ways for students to gain access to essential resources. These resources include food and food delivery, mailing services (bearer), tax and bill payments, utensils, printing and photocopying services, transportation options, school supplies, and other everyday needs that support student life.Project UtechLinks is a Student Discount Club that facilitates a network of goods and services for students at a discounted rate once registered, using their student ID. The club partners with local suppliers of goods and services to provide students with access to reduced rates.

Program Description/Features:The program that controls the club’s systems and processes will include the following menu options: signup/registration, login, categorized listings of products and services, a list of available items, and options to initiate purchases. The system will maintain a basic inventory of products and service availability provided by partnered suppliers, specifically allocated for students. When a user initiates a purchase or request, the system will update the availability accordingly to reflect usage.Additionally, the program will include administrative features that allow authorized users to add, remove, or update products and services, as well as make adjustments to listings when necessary. It will also include features to generate reports such as total registered members, available partner listings, current inventory and service usage summaries.

Programming concepts:
Functions:
The program is broken down into several user-defined functions including registration, login, viewing services, requesting services and the administration controls. This enhances the organization, readability and reusability of the code.
Conditionals (if/else statements):
Applied to decide on things like verifying the login credentials, whether a user has been created, whether a service is online, and menu choices.
Loops (for and while loops):
Loops are employed to maintain the program running and show menus until the user leaves. Lists of services and categories are iterated in for loops and displayed.
Data Structures (Lists and Dictionary):
Services are categorized and stored in dictionaries, and lists are used to handle various items of services in each category.
Input/Output (I/O):
The program involves the input() to take the user information and the print() to show the user a menu, a message and results.
Input Validation:
Simple validation is provided to deal with wrong entries like invalid menu options, registered people, and wrong usernames and passwords.
Main Function:
The control of the overall flow of the program and navigation between various features are managed in a main() function.

How to Use the program:
Click on the project folder.
Double-click UTechLinks.exe
Follow the on screen instructions.

Sample Inputs/Outputs:

Example 1: Registration

Input:
Enter name: Tom
Enter student ID: 2300234
Enter email:

Output:
Registration successful!

Example 2: Login

Input:
Enter email:
Enter student ID: 2301234

Output:
Login successful!

Example 3: Invalid Input

Input:
Enter option: 9

Output:
Invalid option. Please try again.

Manual Testing/Validation:

|     Test Case # | Description                       | Input                           |   Expected Output                   |    Actual Output                | Result|
|  
| 1               | Valid Registration          | Name, new student ID, email, password | Registration successful message    | Registration successful message  |  Pass     |
| 2               | Duplicate Registration      | Existing student ID                   | Error message displayed            | Error message displayed          |  Pass     |
| 3               | Valid Login                 | Correct ID and password               | Login successful                   | Login successful                 |  Pass     |
| 4               | Invalid Login               | Correct ID, wrong password            | Access denied message              | Access denied message            |  Pass     |
| 5               | View Services               | Select "View Services" option         | Display list of available services | Services displayed correctly     |  Pass     |
| 6               | Request Available Service   | Select available service              | Confirmation message               | Request confirmed                |  Pass     |
| 7               | Request Unavailable Service | Select unavailable service            | Error/unavailable message          | Item not available message       |  Pass     |
| 8               | Invalid Menu Option         | Enter invalid option (9)              | Error message                      | Invalid option message displayed |  Pass     |


Challenges:
Arranging the program so as to accommodate various features including user management, listing of services and administrative controls without overcomplicating the code was one of the challenges.

Lessons Learned

This project enhanced my knowledge about:

Organizing a whole Python program.
Working with dictionaries and lists.
Introduction of user input validation.
Creating a system to resolve an issue in the real world.



AI Assistance Disclosure:

AI tools  were applied to:

(Chatgpt) was used inUnderstanding programming concepts
(Copilot) was used Assisting with debugging and improving code









