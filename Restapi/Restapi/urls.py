from django.contrib import admin
from django.urls import path,include
from app.BagViewset import BagViewSet
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'Bag',BagViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
