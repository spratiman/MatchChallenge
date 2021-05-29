from app.utils import strong_match, possible_match, weak_match
from app.models import Notice
from rest_framework.test import APITestCase


class UtilTestCase(APITestCase):

    def test_strong(self):
        Notice.objects.create(first_name="Pratiman", last_name="Shahi",
                              province="ON", date_of_birth="1996-11-08",
                              alt_first_name="Prat")
        self.assertTrue(strong_match("Pratiman", "Shahi", "1996-11-08"))
        self.assertTrue(strong_match("Prat", "Shahi", "1996-11-08"))
        self.assertIsNone(strong_match("Lionel", "Shahi", "1996-11-08"))

    def test_possible(self):
        Notice.objects.create(first_name="Pratiman", last_name="Shahi",
                              province="ON", date_of_birth="1996-11-08",
                              alt_first_name="Prat")
        self.assertTrue(possible_match("Pratiman", "Shahi", "ON"))
        self.assertTrue(possible_match("Prat", "Shahi", "ON"))
        self.assertIsNone(possible_match("Prat", "Shahi", "QC"))

    def test_weak(self):
        Notice.objects.create(first_name="Pratiman", last_name="Shahi",
                              province="ON", date_of_birth="1996-11-08",
                              alt_first_name="Prat")
        self.assertTrue(weak_match("Pratiman", "Shahi"))
        self.assertTrue(weak_match("Prat", "Shahi"))
        self.assertIsNone(weak_match("Lionel", "Shahi"))
