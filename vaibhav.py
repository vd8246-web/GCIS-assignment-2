

# Task 3: Implement calculate_average_books(filename) function
# - Read the file again.
# - Calculate the average number of books borrowed by all students with valid entries.
# - Print the result (rounded to 2 decimal places).
# Task 4: Implement count_over_limit(filename) function
# - Count how many students borrowed more than 3 books.
# - Print the total count.

#Task 3 - 
def calculate_average_books(filename):
    total_books = 0
    valid_entries = 0
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                try:
                    books_borrowed = int(parts[1])
                    total_books += books_borrowed
                    valid_entries += 1
                except ValueError:
                    continue
    if valid_entries > 0:
        average = total_books / valid_entries
        print(f"Average number of books borrowed: {average:.2f}")
    else:
        print("No valid entries found.")



#Task 4 - 
def count_over_limit(filename):
    over_limit = 0
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                try:
                    books_borrowed = int(parts[1])
                    if books_borrowed > 3:
                        over_limit += 1
                except ValueError:
                    continue
    print(f"Number of students who borrowed more than 3 books: {over_limit}")


def main():
    filename = 'students.txt'
    calculate_average_books(filename)
    count_over_limit(filename)
    
if __name__ == "__main__":
    main()
