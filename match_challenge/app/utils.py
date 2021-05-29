from django.db.models import Q
from .models import Notice, Record, Match, STRONG, POSSIBLE, WEAK


def strong_match(first_name, last_name, date_of_birth):
    """Check if there is a match for first_name, last_name and date_of_birth"""
    notice = Notice.objects.filter((Q(first_name=first_name) |
                                   Q(alt_first_name=first_name)) &
                                   (Q(last_name=last_name) |
                                   Q(alt_last_name=last_name)) &
                                   Q(date_of_birth=date_of_birth))

    if notice:
        return notice[0]


def possible_match(first_name, last_name, province):
    """Check if there is a match for first_name, last_name and province"""
    notice = Notice.objects.filter((Q(first_name=first_name) |
                                   Q(alt_first_name=first_name)) &
                                   (Q(last_name=last_name) |
                                   Q(alt_last_name=last_name)) &
                                   Q(province=province))

    if notice:
        return notice[0]


def weak_match(first_name, last_name):
    """Check if there is a match for first_name and last_name"""
    notice = Notice.objects.filter((Q(first_name=first_name) |
                                   Q(alt_first_name=first_name)) &
                                   (Q(last_name=last_name) |
                                   Q(alt_last_name=last_name)))

    if notice:
        return notice[0]


def match(first_name, last_name, province, date_of_birth, record_id):
    """Find the Type of Match, if there is any and create Match object"""

    def update_match(notice, match_type):
        """Create Match object"""
        try:
            record = Record.objects.get(id=record_id)
            Match.objects.create(notice=notice, record=record, type=match_type)
        except Exception as e:
            raise e

    if date_of_birth:  # Check for a strong match since date_of_birth is present
        notice = strong_match(first_name, last_name,
                              date_of_birth)
        match_type = STRONG
        if notice:
            return update_match(notice, match_type)

    if province:  # Check for a possible match since province is present and its not a strong match
        notice = possible_match(first_name, last_name,
                                province)
        match_type = POSSIBLE
        if notice:
            return update_match(notice, match_type)

    # Check for a weak match since its not a strong or possible match
    notice = weak_match(first_name, last_name)
    match_type = WEAK
    if notice:
        return update_match(notice, match_type)
