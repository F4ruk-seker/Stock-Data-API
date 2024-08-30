from django.urls import path, include

app_name: str = 'api'

urlpatterns = [
    path('offers/', include('offer.api.urls'), name='offer'),
]
