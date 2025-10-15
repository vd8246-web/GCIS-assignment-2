"""
Vaibhav - 753003527
Karim - 431002994
Khamza - kz7991


*********Student Manifesto*********

Karim 
- Worked on creating the function check_limit()
- Worked on creating the function process_borrowers()
- Handled exceptions for non-numeric values in process_borrowers()
- Tested the functions with sample data



Vaibhav
- Worked on creating the function calculate_average_books()
- worked on creating the function count_over_limit()
- Handled exceptions for non-numeric values in both functions
- Tested the functions with sample data



Khamza
- Assiteed in the development of a logic flow for Tasks 1-4
- Worked on creating the main function
- Handled file input and exceptions for file not found
- Integrated all functions and ensured smooth execution
- Finished all the docstrings and comments for the entrie code
- Tested the entire program with sample data



"""


import csv

def check_limit(borrowed):
    """
    This function will determine what the borrowing status is based
    on the number of book ordered.

    The function is called check_limit and use if,elif, and else statements

    """
    if borrowed <= 3 and borrowed > 0: #condition one - If borrowed ≤ 3 → Return "Within limit"
        return "Within limit"
    elif borrowed > 3 and borrowed <= 6: #condition two - If borrowed > 3 and ≤ 6 → Return "Over limit: Fine $5"
        return "Over limit: Fine $5"
    elif borrowed > 6: #condition three - If borrowed > 6 → Return "Over limit: Fine $10"
        return "Over limit: Fine $10"
    else: #condition four - If borrowed < 0 → Return "Error: Invalid number of books"
        return "Error: invalid number of books"



def process_borrowers(File_name):
    """
    This function will process a CSV file (borrowers.csv) to check the students name and record
    We can find out of the borrowing status of the student and show it.

    """
    with open(File_name, "r") as f: # Read a csv file
        csv_reader = csv.reader(f)
        next(csv_reader)
        
        for line in csv_reader:  # Use a loop to process the file line by line.
                name = line[0]
                try:
                    books_borrowed = int(line[1]) # Important to convert books_borrowed to an integer
                    status = check_limit(books_borrowed) # Call check_limit() to determine the status.
                    print(f"{name} borrowed {books_borrowed} books: {status}") #Print the student’s name and their status.
                except ValueError:
                    print(f"Error: Non-numeric value for {name}") # If Value is not a valid integer, print an error message: "Error: Non-numeric value for <Name>


def calculate_average_books(filename):
    """
    This function will calculate the average number of books borrowed by all students with valid entries.
    It will then print the result (rounded to 2 decimal places).

    """
    total_books = 0
    valid_entries = 0

    with open(filename, mode='r') as file: # Open a csv file
        reader = csv.reader(file)

        for line in reader:
                
            name, books_borrowed = line[0], line[1]
                
            try:
                borrowed = int(books_borrowed) # Convert books_borrowed to an integer
                    
                if borrowed >= 0:  # Take into account valid entries only
                    total_books += borrowed
                    valid_entries += 1
            except ValueError:
                continue  # Non-numeric value skipped

    if valid_entries > 0:
        average = total_books / valid_entries # Calculate and print the average
        print(f"Average number of books borrowed: {average:.2f}") 
    else:
        print("No valid entries to calculate the average.")



def count_over_limit(filename):
    """
    This function will count the number of students that borrowed more than 3 books.
    It will then Print the total count.

    """
    count = 0

    with open(filename, mode='r') as file: # Open a csv file
        reader = csv.reader(file)

        for line in reader:
                
            name, books_borrowed = line[0], line[1]
                
            try:
                borrowed = int(books_borrowed) # Convert books_borrowed to an integer
                    
                if borrowed > 3:  # count the number of students that borrowed more than 3 books
                    count += 1 #increase the count by 1
            except ValueError:
                continue  # Skip non-numeric values

    print(f"Number of students over the limit: {count}") # Print the total count


def main():
    """
    This is the Main function  - 
    It will also request the file name from the user
    Use a while loop to retry until a valid file is provided.
    
    Call all the above functions: 
    1. process_borrowers()  
    2. calculate_average_books()  
    3. count_over_limit()

    """
    while True:
        file = input("Enter the file name: ") # requesting file name that is needed

        try:  # Check if the file exists by attempting to open it
            with open(file, mode = "r"): # oppening file to read it's information

                process_borrowers(file)
                calculate_average_books(file)
                count_over_limit(file)

                break #Exit the loop once the file name is correct

        except FileNotFoundError: #Error if the file is not correctly entered 
            print("Error occured, please ensure the file name is written correctly")
        

if __name__ == "__main__":
    main()
