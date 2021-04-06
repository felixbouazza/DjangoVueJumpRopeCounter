from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import SessionViewSet, load_frame

router = DefaultRouter()
router.register("sessions", SessionViewSet, basename="sessions")

urlpatterns = [
    path('', include(router.urls)),
    path('load_frame/', load_frame, name="load_frame"),
]
