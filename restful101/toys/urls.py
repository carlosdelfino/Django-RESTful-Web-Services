from django.urls import path
from toys import views
urlpatterns = [
    path('', views.toy_list),
    path('<int:pk>', views.toy_detail),
]