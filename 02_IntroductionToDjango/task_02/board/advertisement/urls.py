from django.urls import path
from . import views

urlpatterns = [
    path("", views.advertisement_list, name='advertisement_list'),
    path('adv_sql/', views.adv_sql,
         name='advertisement_list'), path('adv_web/', views.adv_web,
                                          name='advertisement_list'),
    path('adv_django/', views.adv_django,
         name='advertisement_list'),
    path('adv_python_basic/', views.adv_python_basic,
         name='advertisement_list'),
    path('adv_python_advanced/', views.adv_python_advanced,
         name='advertisement_list'),
]
