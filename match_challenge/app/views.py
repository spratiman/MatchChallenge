from rest_framework import viewsets, response, status
from django_filters.rest_framework import DjangoFilterBackend
from .utils import match
from .models import Match, Record, Notice
from .serializers import NoticeSerializer, RecordSerializer, MatchSerializer

import json


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    filter_backends = (DjangoFilterBackend, )


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends = (DjangoFilterBackend, )

    def create(self, request, *args, **kwargs):
        data = json.loads(request.body)
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        province = data.get("province", None)
        date_of_birth = data.get("date_of_birth", None)

        try:
            result = super().create(request, *args, **kwargs)
            record_id = result.data['id']
        except Exception as e:
            res = {"message": "CREATE Record failed due to {}"
                   .format(e)}
            return response.Response(res,
                                     status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            match(first_name, last_name, province, date_of_birth, record_id)
        except Exception as e:
            res = {"message": "CREATE Match failed due to {}"
                   .format(e)}
            return response.Response(res,
                                     status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        res = {"message": "CREATE Record with id {}".format(result.data['id'])}
        return response.Response(res, status=status.HTTP_201_CREATED)


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_backends = (DjangoFilterBackend, )
