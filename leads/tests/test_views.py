from django.http import response
from django.test import TestCase
from django.shortcuts import reverse


# Create your tests here.
class LangingPageTest(TestCase):

    def test_get(self):
        # to 
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")



