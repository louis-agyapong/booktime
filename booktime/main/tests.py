from django.test import TestCase
from http import HTTPStatus


class TestCase(TestCase):
    def test_home_page_works(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "main/index.html")
        self.assertContains(response, "BookTime")
