from django.urls import path

from .views import IndexView, ApplicationView, ApplicationDetailsView

app_name = "core"
urlpatterns = [
    path("", view=IndexView.as_view(), name="index"),
    path("application/", view=ApplicationView.as_view(), name="application"),
    path("application_detail/", view=ApplicationDetailsView.as_view(), name="application_details"),
]
