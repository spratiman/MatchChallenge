
from app.views import MatchViewSet, NoticeViewSet, RecordViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("notices", NoticeViewSet)
router.register("record", RecordViewSet)
router.register("matches", MatchViewSet)


urlpatterns = [
    path("", include(router.urls))
]