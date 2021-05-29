from rest_framework.test import APITestCase

from app.models import Notice, Record, Match


class ModelTestCase(APITestCase):

    def test_notice(self):
        Notice.objects.create(first_name="Pratiman", last_name="Shahi",
                              province="ON", date_of_birth="1996-11-08",
                              alt_first_name="Prat")
        self.assertEqual(Notice.objects.count(), 1)

    def test_record(self):
        Record.objects.create(first_name="Pratiman", last_name="Shahi",
                              province="ON", date_of_birth="1996-11-08")
        self.assertEqual(Record.objects.count(), 1)

    def test_match(self):
        Notice.objects.create(first_name="Pratiman", last_name="Shahi",
                              province="ON", date_of_birth="1996-11-08",
                              alt_first_name="Prat")
        notice = Notice.objects.get(id=1)

        Record.objects.create(first_name="Pratiman", last_name="Shahi",
                              province="ON", date_of_birth="1996-11-08")
        record = Record.objects.get(id=1)

        Match.objects.create(notice=notice, record=record)
        self.assertEqual(Match.objects.count(), 1)
