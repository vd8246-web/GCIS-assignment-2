## task 5


from assignment_2_GCIS import process_borrowers, calculate_average_books, count_over_limit


def main():
    ## main function for printing data user requested


    while True:

        ## requesting file name that is needed
        file = input("Enter file name: ")

        ## cheking file's extintion
        try:

            ## oppening file to read it's information
            with open(file, mode = "r"):

                process_borrowers(file)
                calculate_average_books(file)
                count_over_limit(file)

                break

        except:
            print("Error occured,please check file name was written correctly")

            break
        

if __name__ == "__main__":

    main()