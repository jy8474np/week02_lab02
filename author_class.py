class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        book_list = ', '.join(self.books)
        return self.name + ' : ' + book_list

dickens = Author('Charles Dickens')
dickens.publish('A Tale of Two Cities')
dickens.publish('David Copperfield')
dickens.publish('Nicholas Nickelby')
dickens.publish('A Christmas Carol')

twain = Author('Mark Twain')
dickens.publish('The Adventures of Huckleberry Finn')
dickens.publish('The Prince and the Pauper')
dickens.publish("A Connecticut Yankee in King Arthur's Court")
dickens.publish('A Christmas Carol')

print(dickens)
