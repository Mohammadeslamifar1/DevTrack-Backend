from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class ProjectTests(APITestCase):
    def test_create_project(self):
        user = User.objects.create_user("test", "test@test.com", "pass123")
        self.client.force_authenticate(user=user)
        response = self.client.post("/api/projects/", {"name": "Test Project"})
        self.assertEqual(response.status_code, 201)
