from django.test import TestCase

from .models import Article

# Create your tests here.


class ArticleTest(TestCase):
    def testArticle(self):
        article = Article(title="My Article", body="My first article")
        self.assertEqual(article.make_public, False)
        self.assertEqual(article.title, "My Article")
        self.assertEqual(article.body, "My first article")
