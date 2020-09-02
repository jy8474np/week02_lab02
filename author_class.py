def main():
    
    class Author:
        def __init__(self, name):
            self.name = name
            self.books = []

        def publish(self, title):
            self.books.append(title)

        def __str__(self):
            book_list = ', '.join(self.books)
            return f'Author: {self.name} - Works: {book_list}'

    dickens = Author('Charles Dickens')
    dickens.publish('A Tale of Two Cities')
    dickens.publish('David Copperfield')
    dickens.publish('Nicholas Nickelby')
    dickens.publish('A Christmas Carol')

    twain = Author('Mark Twain')
    twain.publish('The Adventures of Huckleberry Finn')
    twain.publish('The Prince and the Pauper')
    twain.publish("A Connecticut Yankee in King Arthur's Court")
    twain.publish('A Christmas Carol')

    print(dickens)
    print(twain)

main()