"""
Vaibhav - 753003527
Karim - 
Khamza - 

Tasks finished my teammates
Karim - Finished Task 1 and Task 2
Vaibhav - Finished Task 3 and Task 4
Khamza - Finished Task 5, docstring, and documentation
"""



import csv

def check_limit(borrowed):
    """
    This function will determine what the borrowing status is based
    on the number of book ordered.

    The function is called check_limit and use if,elif, and else statements

    """
    if borrowed <= 3: #condition one - If borrowed ≤ 3 → Return "Within limit"
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



# Example
# Run the program with the CSV file
#process_borrowers("BooksBorrowed.csv")

def calculate_average_books(filename):
    """
    Calculates the average number of books borrowed by all students with valid entries.

    """
    try:
        total_books = 0
        valid_entries = 0

        # Open the CSV file for reading
        with open(filename, mode='r') as file:
            reader = csv.reader(file)

            for line in reader:
                if len(line) != 2:
                    continue  # Skip invalid lines
                
                name, books_borrowed = line[0], line[1]
                
                try:
                    # Convert books_borrowed to an integer
                    borrowed = int(books_borrowed)
                    
                    if borrowed >= 0:  # Only consider valid entries
                        total_books += borrowed
                        valid_entries += 1
                except ValueError:
                    continue  # Skip non-numeric values

        # Calculate and print the average
        if valid_entries > 0:
            average = total_books / valid_entries
            print(f"Average number of books borrowed: {average:.2f}")
        else:
            print("No valid entries to calculate the average.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def count_over_limit(filename):
    """
    Counts the number of students who borrowed more than 3 books.

    """
    try:
        count = 0

        # Open the CSV file for reading
        with open(filename, mode='r') as file:
            reader = csv.reader(file)

            for line in reader:
                if len(line) != 2:
                    continue  # Skip invalid lines
                
                name, books_borrowed = line[0], line[1]
                
                try:
                    # Convert books_borrowed to an integer
                    borrowed = int(books_borrowed)
                    
                    if borrowed > 3:  # Count students over the limit
                        count += 1
                except ValueError:
                    continue  # Skip non-numeric values

        # Print the total count
        print(f"Number of students over the limit: {count}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to prompt the user for a filename and call all other functions.

    """
    while True:
        # Prompt the user for a filename
        filename = input("Enter the filename: ")
        
        try:
            # Check if the file exists by attempting to open it
            with open(filename, mode='r'):
                pass
            
            # Call all the functions
            process_borrowers(filename)
            calculate_average_books(filename)
            count_over_limit(filename)
            break  # Exit the loop if everything succeeds
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
