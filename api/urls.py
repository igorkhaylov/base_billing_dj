from django.urls import path, include


urlpatterns = [
    # /project_name/api/urls

    path('v1/', include('api.v1.urls')),
]
