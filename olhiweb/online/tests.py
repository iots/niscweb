from django.test import TestCase
from django.test import Client

class TestView(TestCase):
    def setUP(self):
        self.client = Client()

    def testOnlineView(self):
        response = self.client.get('/online/list/')
        self.assertEqual(response.status_code, 200)

