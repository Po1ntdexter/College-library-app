# Variables
books_borrowed = 4
books = [
    {"Book_1": "How to code"}, # examples
    {"Book_2": "Cooking for dummies"},
    {"Book_3": "Game of thrones"},
    {"Book_4": "Fortnite: The ultimate guide"}
]

# Main 

def main():
    print("\n\n\n    -----WELCOME TO EXETER LIBRARY-----    \n\n    Please scan your Library card by pressing ENTER")

main()

class MyIndex:
    def __init__(self, value):
        self.value = value

def __index__(self):
    return self.value

def student_logs():
    print("\n Checking your profile...")

    
    num_of_books = len(books)

    if num_of_books > 0:
        print(f"\n You have {num_of_books} books borrowed")
        for i, in range(books[0:num_of_books]):
            idx = MyIndex(i)
            book_name = books[idx]
            print(f"\n Books: {str(book_name)}")


def library_card():
    l_card = input()

    student_logs()

library_card()


def read_barcode():
    barcode = input("\n Click any key to enter the barcode")




# === CHAT ===

# i will start by hard coding user inputs and databses 
# you  follow the tickets and make a function for each one and make a start on that

#continue with the library one




