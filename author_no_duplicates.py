def main():
    
    # Create class and define its componenets
    class Author:
        def __init__(self, name):
            self.name = name
            books = set() # Do I need to be concered about this "unused variable" warning?
                          # The program appears to work correctly despite it.

        # Displayed information format
        def __str__(self):
            return f'Author: {self.name} - Works: {self.books}'

    # Author and book data (duplicate titles added)
    dickens = Author('Charles Dickens')
    dickens.books = {'A Tale of Two Cities', 'David Copperfield', 'David Copperfield', 'Nicholas Nickelby', 'A Christmas Carol'}

    twain = Author('Mark Twain')
    twain.books = {'The Adventures of Huckleberry Finn', 'The Adventures of Huckleberry Finn', 'The Prince and the Pauper', "A Connecticut Yankee in King Arthur's Court"}

    # Display authors and their works (no duplicate titles displayed)
    print(dickens)
    print(twain)

main()