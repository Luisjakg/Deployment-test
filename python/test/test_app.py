from src import app
from unittest import TestCase
import sys
sys.path.append('../src')

class appTest(TestCase):
    def test_app(self):
        result = app.lambda_handler(None, None)
        self.assertEqual(result, "Luis Javier Karam")
