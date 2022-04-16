from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse

class TestCase(TestCase):
    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "main/index.html")
        self.assertContains(response, "BookTime")

    def test_about_page(self):
        response = self.client.get(reverse("main:about"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "main/about.html")
        self.assertContains(response, "About")
