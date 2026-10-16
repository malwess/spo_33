from django.contrib.auth.models import User
from django.test import TestCase


class ProfileAccessTests(TestCase):
    def setUp(self):
        User.objects.create_user(username="student1", password="Kuznetsova2026!")

    def test_profile_redirects_anonymous_user(self):
        response = self.client.get("/profile/")
        self.assertRedirects(response, "/accounts/login/?next=/profile/")

    def test_login_page_opens(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)

    def test_profile_after_login(self):
        self.client.login(username="student1", password="Kuznetsova2026!")
        response = self.client.get("/profile/")
        self.assertContains(response, "student1")

    def test_logout_redirects_to_login(self):
        self.client.login(username="student1", password="Kuznetsova2026!")
        response = self.client.post("/accounts/logout/")
        self.assertRedirects(response, "/accounts/login/")
