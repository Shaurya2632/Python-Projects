class Library:

    def __init__(self):

        self.collection = {
            "The Nun": [400, 200],
            "Python Basics": [800, 500],
            "Java Course": [500, 100],
            "The Hero": [700, 300]
        }

        self.availableBooks = list(self.collection.keys())

        self.buyPrice = [self.collection[book][0] for book in self.availableBooks]
        self.rentPrice =  [self.collection[book][1] for book in self.availableBooks]

        self.noOfBooks = len(self.availableBooks)

        self.userCollection = {}

        self.subscription = 2500
        self.isSubscription = False

    def showAllBook(self):

        if self.availableBooks:
             print("Available Books\n")

             for index, book in enumerate(self.availableBooks):
                print(f"{index+1}. {book}")

        else: print("No Books Available in Library")

    def buyBook(self, bookName):

        if bookName.lower().title() in self.availableBooks:
           self.userCollection[bookName] = [self.collection[bookName][0], self.collection[bookName][1]]

           print(f"'{bookName}' Successfully Added to Your Collection")

        else: print(f"Sorry, But '{bookName}' is Not Available in Our Library")

    def rentBook(self, bookName):

        if bookName.lower().title() in self.availableBooks:
            self.userCollection[bookName] = [self.collection[bookName][0], self.collection[bookName][1]]

            print(f"'{bookName}' Successfully Added to Your Collection")

        else:
            print(f"Sorry, But '{bookName}' is Not Available in Our Library")

    def bookInfo(self, book):

        if book.lower().title() in self.availableBooks:
            print("Book Info\n")

            print(f"Name : {book}")
            print(f"Price: {self.collection[book][0]}")
            print(f"Rent : {self.collection[book][1]}")

        else: print(f"Sorry, But '{book}' is Not Available in Our Library")

    def __str__(self):

        return f"{self.collection}"

    def addBook(self, book, price, rent):

        if self.isSubscription:
            price = int(round(price * 0.50, 0))
            rent = int(round(rent * 0.75, 0))

        self.collection[book] = [price, rent]

        self.availableBooks.append(book)
        self.buyPrice.append(price)
        self.rentPrice.append(rent)

    def manageSubscription(self, action):

        self.isSubscription = action

        if action:

            for i,book in enumerate(self.collection.keys()):
                self.buyPrice[i] = int(round(self.buyPrice[i] * 0.50, 0))
                self.collection[book] = [self.buyPrice[i], self.rentPrice[i]]

            for i, book in enumerate(self.collection.keys()):
                self.rentPrice[i] = int(round(self.rentPrice[i] * 0.75, 0))
                self.collection[book] = [self.buyPrice[i], self.rentPrice[i]]


book = "Python Basics"

lib = Library()
lib.manageSubscription(False)
lib.bookInfo(book)

print()

lib.manageSubscription(True)
lib.bookInfo(book)

