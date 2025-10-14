"""
Vaibhav - 753003527
Karim - 
Khamza - 

Tasks finished my teammates
Karim - Finished Task1 and Task2
Vaibhav - Finished Task3 and Task4
Khamza - Finished Task5 and Main function and reviewed doctsrings and comments
"""



import csv

def check_limit(borrowed):
    """
    Determines the borrowing status based on the number of books borrowed.

    Args:
        borrowed (int): The number of books borrowed by a student.

    Returns:
        str: A message indicating the borrowing status:
             - "Within limit" if borrowed ≤ 3
             - "Over limit: Fine $5" if 4 ≤ borrowed ≤ 6
             - "Over limit: Fine $10" if borrowed > 6
             - "Error: Invalid number of books" if borrowed < 0
    """
    if borrowed < 0:
        return "Error: Invalid number of books"
    elif borrowed <= 3:
        return "Within limit"
    elif borrowed <= 6:
        return "Over limit: Fine $5"
    else:
        return "Over limit: Fine $10"


def process_borrowers(filename):
    """
    Processes a CSV file containing student names and the number of books borrowed.
    For each student, determines their borrowing status and prints it.

    Args:
        filename (str): The name of the CSV file to process.

    Returns:
        None
    """
    try:
        # Open the CSV file for reading
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            
            # Process each line in the file
            for line in reader:
                if len(line) != 2:
                    print("Error: Invalid line format")
                    continue
                
                name, books_borrowed = line[0], line[1]
                
                try:
                    # Convert books_borrowed to an integer
                    borrowed = int(books_borrowed)
                    
                    # Call check_limit to determine the borrowing status
                    status = check_limit(borrowed)
                    print(f"{name}: {status}")
                except ValueError:
                    # Handle non-numeric values for books_borrowed
                    print(f"Error: Non-numeric value for {name}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
# Save the CSV data in a file named "borrowers.csv" and call the function:
# process_borrowers("borrowers.csv")

def calculate_average_books(filename):
    """
    Calculates the average number of books borrowed by all students with valid entries.

    Args:
        filename (str): The name of the CSV file to process.

    Returns:
        None
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

    Args:
        filename (str): The name of the CSV file to process.

    Returns:
        None
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

    Args:
        None

    Returns:
        None
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


# Example usage:
# Uncomment the following line to run the program:
# main()