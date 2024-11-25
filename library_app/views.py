#  Python3 Code for Library Management System using OOPs Concept.
import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lenddict = {}

    def displaybook(self):
        logging.info(f"We have following books in our library  : {self.name}")
        for book in self.booksList:
            logging.info(book)

    def lendbook(self, user, book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book: user})
            logging.info(
                "Lender-Book database has been updated. You can take the book now"
            )
        else:
            logging.info(f"Book is already being used by {self.lenddict[book]}")

    def searchbook(self, book):
        if book not in self.booksList:
            logging.info("This book is not avaliable.")
            logging.info("You want to add this book: 'Y' or 'N' ")
            c = input()
            if c == "Y":
                book = input("Enter the book name:")
                ram.addbook(book)
            else:
                pass

    def addbook(self, book):
        self.booksList.append(book)
        logging.info("Book has been added to the book list.")

    def returnbook(self, book):
        self.lenddict.pop(book)

    def choices(self):
        logging.info(
            f"Welcome to the {ram.name} Library. \nEnter your choice to continue: "
        )
        logging.info("1. Display Books")
        logging.info("2. Lend a Book")
        logging.info("3. Add a Book")
        logging.info("4. Return a Book")
        logging.info("5. Enter the book to Search")

if __name__ == "__main__":
    ram = Library(
        ["Python", "Rich Daddy Poor Daddy", "Harry Potter", "C++ Basics"],
        "World",
    )
    while True:

        ram.choices()
        user_choice = int(input())

        if user_choice == 1:
            ram.displaybook()
        elif user_choice == 2:
            book = input("Enter the name of book you want to land")
            user = input("Enter your name")
            ram.lendbook(user, book)
        elif user_choice == 3:
            book = input("Enter the name of book you want to add")
            ram.addbook(book)
        elif user_choice == 4:
            book = input("Enter the book you want to return")
            ram.returnbook(book)
        elif user_choice == 5:
            book = input("Enter the book to search")
            ram.searchbook(book)
        else:
            logging.info("Not a valid choice")

        logging.info("Press q to Quit and c to continue")
        user_choice2 = ""
        while user_choice2 != "c" and user_choice2 != "q":
            user_choice2 = input("Enter your choice:")
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
            else:
                logging.info("\n\tPlease Enter a valid choice (q or c)\n")
                continue
