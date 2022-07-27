from django.conf.urls.static import static
from django.urls import path
from .views import ShopListView
from django.conf import settings

urlpatterns = [
                  path('', ShopListView.as_view(), name='main'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
