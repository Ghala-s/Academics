"""
CS1026a 2023
Assignment 02
Ghala Basaad
251384549
gbasaad
"""

def start():
    allBooks = [
        ['9780596007126', "The Earth Inside Out", "Mike B", 2, ['Ali']],
        ['9780134494166', "The Human Body", "Dave R", 1, []],
        ['9780321125217', "Human on Earth", "Jordan P", 1, ['David', 'b1', 'user123']]
    ]
    borrowedISBNs = []

    def adding_book():
        bookName = input("Book name: ")
        while '%' in bookName or '*' in bookName:  # loop until valid name is entered
            print("Invalid book name!")
            bookName = input("Book name: ")
        author = input("Author name: ")
        edition = input("Book edition: ")
        while not edition.isdigit():   # loop until valid edition (numeric, integer) is entered
            print("Invalid edition!")
            edition = input("Book edition: ")
        isbn = input("isbn: ")
        while not isbn.isdigit():    # loop until valid ISBN (numeric)  is entered
            print("Invalid ISBN!")
            isbn = input("isbn: ")
        while not len(isbn) == 13:   # loop until 13-digit ISBN is entered
            print("Invalid ISBN!")
            isbn = input("isbn: ")
        if len(isbn) == 13:
            multiplyFactor = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]  # this var holds the weight factor
            sum = 0
            for i in isbn:   # 'for' loop to multiply digits in isbn with digits in multiplyFactor that share same index
                for j in multiplyFactor:
                    product = int(i) * j
                    sum += product
            if sum % 10 == 0:
                duplicateISBN = True
                for book in allBooks:
                    if isbn == book[0]:   # to check if the isbn is already found in allBooks
                        duplicateISBN = False
                if not duplicateISBN:
                    print("Duplicate ISBN found! Cannot add the book.")
                else:
                    oneNewBook = [isbn, bookName, author, edition, []] # this var holds our new book list
                    allBooks.append(oneNewBook)
                    print("A new book is added successfully.")
            else:
                print("Invalid ISBN!")

    def borrowing_book():
        borrowerName = input("Enter the borrower name: ")
        bookName = input("Search term: ").lower()  # getting the name from user, and converting it to lowercase
        if bookName.endswith('*'):
            bookName = bookName.replace('*', '')  # to remove '*' from the bookName
            i = 0
            borrowedBooks = 0
            for book in allBooks:  # 'for' loop to look for the bookName
                if bookName in book[1].lower(): # to check if book in allBooks contains bookName
                    searchBookISBN = allBooks[i][0]  # after finding bookName, we assigned var to the isbn of the bookName
                    if searchBookISBN not in borrowedISBNs:   # to check the availability of the book
                        allBooks[i][4].append(borrowerName)
                        borrowedISBNs.append(allBooks[i][0])
                        print('"', book[1], '"', "is borrowed!")
                        borrowedBooks += 1   # counter increment
                i += 1
            if borrowedBooks == 0: # if no bookName is found or searchBookISBN is not available
                print("No books found!")

        elif bookName.endswith('%'):
            bookName = bookName.replace('%', '')  # to remove '%' from the bookName
            i = 0
            borrowedBooks = 0
            for book in allBooks: # 'for' loop to look for the bookName
                temp_book = book[1]
                temp_book = temp_book.lower()
                if temp_book.startswith(bookName):  # to check if book in allBooks starts with bookName
                    searchBookISBN = allBooks[i][0] # after finding bookName, we assigned var to the isbn of the bookName
                    if searchBookISBN not in borrowedISBNs:  # to check the availability of the book
                        allBooks[i][4].append(borrowerName)
                        borrowedISBNs.append(allBooks[i][0])
                        print('"', book[1], '"', "is borrowed!")
                        borrowedBooks += 1    # counter increment
                i += 1
            if borrowedBooks == 0:  # if no bookName is found or searchBookISBN is not available
                print("No books found!")
        else:
            i = 0
            borrowedBooks = 0
            for book in allBooks:
                if bookName == book[1].lower():  # to check if bookName is exactly the same
                    searchBookISBN = allBooks[i][0]
                    if searchBookISBN not in borrowedISBNs:
                        allBooks[i][4].append(borrowerName)
                        borrowedISBNs.append(allBooks[i][0])
                        print('"', book[1], '"', "is borrowed!")
                        borrowedBooks += 1   # counter increment
                i += 1
            if borrowedBooks == 0:  # if no bookName is found or searchBookISBN is not available
                print("No books found!")
         

    def returning_book():
        isbn = input("ISBN: ")
        if isbn in borrowedISBNs:  # to check if the book is in the borrowing list
            borrowedISBNs.remove(isbn)
            for book in allBooks:       # we use 'for' loop to find the name of the returned book
                if isbn in book[0]:
                    print('"', book[1], '"', "is returned.")
        else:
            print("No book is found!")

    def listing_all_books():
        for book in allBooks:
            if book[0] in borrowedISBNs:   # to check the availability of the book
                print("[Unavailable]")
            else:
                print("[Available]")
            print(book[1], "-", book[2])
            print("E: ", book[3], "ISBN: ", book[0])
            print("Borrowed by: ", book[4])

    def exiting():
        print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
        listing_all_books()
        exit()            # to end the program
    def printMenu():
        print('\n######################')
        print('1: (A)dd a new book.')
        print('2: Bo(r)row books.')
        print('3: Re(t)urn a book.')
        print('4: (L)ist all books.')
        print('5: E(x)it.')
        print('######################\n')

    valid = False
    while not valid:

        printMenu()
        userSelection = input("Your Selection: ")
        # we used .lower() in the following 'if statements' to convert all strings to lowercase
        if userSelection.lower() == 'a' or userSelection == '1':
            adding_book()

        elif userSelection.lower() == 'r' or userSelection == '2':
            borrowing_book()

        elif userSelection.lower() == 't' or userSelection == '3':
            returning_book()

        elif userSelection.lower() == 'l' or userSelection == '4':
            listing_all_books()

        elif userSelection.lower() == 'x' or userSelection == '5':
            exiting()

        else:  # if the user entered any other value
            valid = False
            print("Wrong selection! Please selection a valid option.")


start()






