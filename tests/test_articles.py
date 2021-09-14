import unittest
from app.models import Articles

class Articles(unittest.TestCase):
    def setUp(self):
        self.new_articles = Articles(  )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))
