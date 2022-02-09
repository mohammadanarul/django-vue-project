from django.urls import path
from .views import (
    user_list_api,
    user_register_api,
    api_view,
    user_login_api,
)


urlpatterns = [
    path('api-list/', user_list_api),
    path('user-register/', user_register_api),
    path('login/', user_login_api),
    path('api/', api_view),
]
