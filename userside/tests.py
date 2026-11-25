from django.test import TestCase
from django.urls import reverse


class ContactFlashMessageTests(TestCase):
    def test_success_message_is_visible_after_registration(self):
        response = self.client.post(
            reverse("register"),
            {
                "name": "Test User",
                "email": "test@example.com",
                "mobile": "1234567890",
                "subject": "Event inquiry",
                "address": "Test address",
            },
            follow=True,
        )

        self.assertContains(response, "Your details were submitted successfully.")
        self.assertContains(response, 'class="alert alert-success"')

    def test_validation_errors_are_visible_on_contact_page(self):
        response = self.client.post(
            reverse("register"),
            {
                "name": "",
                "email": "",
                "mobile": "",
                "subject": "",
                "address": "",
            },
        )

        self.assertContains(response, "Name is required.")
        self.assertContains(response, 'class="alert alert-danger"')
