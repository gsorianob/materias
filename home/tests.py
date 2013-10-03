from django.test import TestCase
from django.test import Client


class HomeUrlConfigTests(TestCase):

    def test_get_to_empty_will_return_a_permanent_redirect(self):
        # Setup
        c = Client()

        # Execute
        response = c.get('/', {})

        # Verify
        self.assertEquals(response.status_code, 301)

    def test_get_to_home_will_return_a_view(self):
        # Setup
        c = Client()

        # Execute
        response = c.get('/home/', {})

        # Verify
        self.assertEquals(response.status_code, 200)
