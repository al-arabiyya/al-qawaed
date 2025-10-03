"""URLConf for al_qawaed.ui"""

from django.urls import path

from al_qawaed.ui import views

# Create your URLConf here.
app_name = "al_qawaed"

urlpatterns = [
    path("search/", views.SearchView.as_view(), name="search"),
]
