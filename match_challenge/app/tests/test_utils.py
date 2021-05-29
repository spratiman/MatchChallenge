from app.utils import strong_match, possible_match, weak_match
from rest_framework.test import APITestCase


class UtilTestCase(APITestCase):

    def test_strong(self):
        data = {"first_name": "Lionel", "last_name": "Messi",
                "alt_first_name": "Leo", "province": "ON",
                "date_of_birth": "1997-01-12"}
        url = "/api/v1/notices/"
        self.response = self.client.post(url, data)

        self.assertEqual(self.response.status_code, 201)
        self.assertTrue(strong_match("Lionel", "Messi", "1997-01-12"))
        self.assertIsNone(strong_match("Lionel", "Messi", "1997-01-01"))

    def test_possible(self):
        data = {"first_name": "Lionel", "last_name": "Messi",
                "alt_first_name": "Leo", "province": "ON",
                "date_of_birth": "1997-01-12"}
        url = "/api/v1/notices/"
        self.response = self.client.post(url, data)

        self.assertEqual(self.response.status_code, 201)
        self.assertTrue(possible_match("Lionel", "Messi", "ON"))
        self.assertIsNone(possible_match("Lionel", "Messi", "QC"))

    def test_weak(self):
        data = {"first_name": "Lionel", "last_name": "Messi",
                "alt_first_name": "Leo", "province": "ON",
                "date_of_birth": "1997-01-12"}
        url = "/api/v1/notices/"
        self.response = self.client.post(url, data)

        self.assertEqual(self.response.status_code, 201)
        self.assertTrue(weak_match("Lionel", "Messi"), 0)
        self.assertIsNone(weak_match("Lionel", "Mess"))
