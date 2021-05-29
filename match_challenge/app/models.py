from django.db import models
from django.db.models.deletion import CASCADE

STRONG = 1
POSSIBLE = 2
WEAK = 3
MATCH_TYPES = (
    (STRONG, "STRONG"),
    (POSSIBLE, "POSSIBLE"),
    (WEAK, "WEAK"),
)


class ClientInfo(models.Model):
    first_name = models.CharField(max_length=100, help_text="Enter First Name")
    last_name = models.CharField(max_length=100, help_text="Enter Last Name")
    province = models.CharField(max_length=2, help_text="Enter the abbreviated \
        form of Province")
    date_of_birth = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True


class Notice(ClientInfo):
    id = models.AutoField(primary_key=True)
    alt_first_name = models.CharField(max_length=100, help_text="Enter\
        Alternative First Name", blank=True, null=True)
    alt_last_name = models.CharField(max_length=100, help_text="Enter \
        Alternative Last Name", blank=True, null=True)

    def __str__(self):
        return 'Notice for {} {}'.format(self.first_name, self.last_name)


class Record(ClientInfo):
    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=2, help_text="Enter the abbreviated \
        form of Province", blank=True, null=True)

    def __str__(self):
        return 'Record of {} {}'.format(self.first_name, self.last_name)


class Match(models.Model):
    id = models.AutoField(primary_key=True)
    record = models.ForeignKey(Record, on_delete=CASCADE)
    notice = models.ForeignKey(Notice, on_delete=CASCADE)
    type = models.PositiveIntegerField(choices=MATCH_TYPES, default=0)

    def __str__(self):
        return 'Match for Record# {} & Notice# {}'.format(self.record,
                                                          self.notice)
