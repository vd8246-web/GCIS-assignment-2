import csv

def check_limit(borrowed):
    if borrowed <= 3:
        return "Within limit"
    elif borrowed > 3 and borrowed <= 6:
        return "Over limit: Fine $5"
    elif borrowed > 6:
        return "Over limit: Fine $10"
    else: 
        return "Error: invalid number of books"



File_name = "BooksBorrowed.csv"
def process_borrowers(File_name):
    with open(File_name, "r") as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        
        for line in csv_reader:
                name = line[0]
                try:
                    books_borrowed = int(line[1])
                    status = check_limit(books_borrowed)
                    print(f"{name} borrowed {books_borrowed} books: {status}")
                except ValueError:
                    print(f"Error: Non-numeric value for {name}")

# Run the program with the CSV file
process_borrowers("BooksBorrowed.csv")
