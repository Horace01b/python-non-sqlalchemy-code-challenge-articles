# lib/classes/many_to_many.py

class Article:
    all = []  # class-level storage for all articles

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters")
        self._title = title

        from classes.many_to_many import Author, Magazine
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance")

        self.author = author
        self.magazine = magazine

        # Register article in author's and magazine's collections
        author._articles.append(self)
        magazine._articles.append(self)

        # 🔑 Track all created articles
        Article.all.append(self)

    @property
    def title(self):
        return self._title  # immutable

    @classmethod
    def clear_all(cls):
        """Helper to reset all articles (useful in tests)."""
        cls.all = []


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) == 0:
            raise Exception("Name must not be empty")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name  # immutable

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        from classes.many_to_many import Article
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise Exception("Name must be 2–16 characters long")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string")
        if len(value) == 0:
            raise Exception("Category must not be empty")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None
