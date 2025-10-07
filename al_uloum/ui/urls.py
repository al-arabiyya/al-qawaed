"""URLConf for al_uloum.ui"""

from django.urls import path

from al_uloum.ui import views

# Create your URLConf here.
app_name = "al_uloum"

urlpatterns = [
    path("search/", views.SearchView.as_view(), name="search"),
]
