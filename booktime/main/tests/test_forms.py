from django import http
from django.test import TestCase
from django.core import mail
from booktime.main.forms import ContactForm
from django.urls import reverse
from http import HTTPStatus


class TestForm(TestCase):
    def test_valid_contact_form_sends_email(self):
        form = ContactForm({"name": "Kofi Asamoah", "message": "Hi, there!"})
        self.assertTrue(form.is_valid())
        with self.assertLogs("booktime.main.forms", level="INFO") as cm:
            form.send_mail()
        # self.client.post("/contact/", {"name": "Kofi Asamoah", "message": "Hi, there!"})
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "BookTime - Customer Service")
        self.assertIn("Hi", mail.outbox[0].body)

        self.assertGreaterEqual(len(mail.outbox), 1)

    def test_invalid_contact_form(self):
        form = ContactForm({"name": "Kofi Asamoah"})
        self.assertFalse(form.is_valid())

    def test_contact_us_page_works(self):
        response = self.client.get(reverse("main:contact"))
        form = response.context.get("form")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "main/contact_form.html")
        self.assertIsInstance(form, ContactForm)
