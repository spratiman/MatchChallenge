from rest_framework import viewsets, response, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Match, Record, Notice
from .serializers import NoticeSerializer, RecordSerializer, MatchSerializer


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    filter_backends = (DjangoFilterBackend, )


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends = (DjangoFilterBackend, )


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_backends = (DjangoFilterBackend, )
