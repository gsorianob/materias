from django.test import TestCase
from django.test import Client


class CalendarUrlConfigTests(TestCase):

    def test_get_to_calendar_will_return_a_view(self):
        # Setup
        c = Client()

        # Execute
        response = c.get('/calendario/', {})

        # Verify
        self.assertEquals(response.status_code, 200)

    def test_get_to_create_will_return_a_404(self):
        # Setup
        c = Client()

        # Execute
        response = c.get('/calendario/create/', {})

        # Verify
        self.assertEquals(response.status_code, 404)

    def test_post_to_create_will_return_a_view(self):
        # Setup
        c = Client()

        # Execute
        response = c.post('/calendario/create/', {})

        # Verify
        self.assertEquals(response.status_code, 200)

