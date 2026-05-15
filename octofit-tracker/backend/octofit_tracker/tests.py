from rest_framework.test import APITestCase
from django.urls import reverse


class APIRootTest(APITestCase):
    def test_api_root_links(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        for key in ['teams', 'users', 'activities', 'leaderboard', 'workouts']:
            self.assertIn(key, response.data)
