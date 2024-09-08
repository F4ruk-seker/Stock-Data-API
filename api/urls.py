from django.urls import path, include

app_name: str = 'api'

urlpatterns = [
    path('assets/', include('asset.api.urls'), name='asset'),
]
