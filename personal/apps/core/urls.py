from django.urls import path
from apps.core.views import homeTemplateView

urlpatterns = [
    path("", homeTemplateView.as_view(), name="home"),
]
