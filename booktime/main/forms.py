import logging

from django import forms
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)
    message = forms.CharField(label="Your message", max_length=600, widget=forms.Textarea)

    def send_mail(self):
        logger.info("Sending email to customer service")
        from_email = "site@booktime.com"
        subject = "BookTime - Customer Service"
        recipient_list = ["customerservice@booktime.com"]
        message = f"From: {self.cleaned_data['name']}\n\n{self.cleaned_data['message']}"
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
