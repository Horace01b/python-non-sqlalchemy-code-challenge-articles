class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @classmethod
    def all_articles(cls):
        return cls.all

    @classmethod
    def clear_all(cls):
        cls.all = []
