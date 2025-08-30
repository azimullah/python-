class book:
    def __init__(self, name ,pages,published_on):
        self.name = name
        self.pages = pages
        self.published_on = published_on

    def __len__(self):
        return self.pages
    
book1 = book("python", 200, 2020)
book2 = book("java", 300, 2019)
print(len(book1))
print(len(book2))