from rest_framework.urls import path
from .views import CreateContry, ListCountries

urlpatterns = [
    path('countries', ListCountries.as_view(), name='list_countries'),
    path('country', CreateContry.as_view(), name="create_country")
]