from django.urls import include, path
from rest_framework.routers import DefaultRouter

from entrepreneur.views import Entrepreneur_contactsViewSet, Entrepreneur_productViewSet

app_name = 'entrepreneur'

router = DefaultRouter()
router.register(r'entrepreneur-contacts', Entrepreneur_contactsViewSet, basename='entrepreneur-contacts')
router.register(r'entrepreneur-product', Entrepreneur_productViewSet, basename='entrepreneur-product')

urlpatterns = [

              ] + router.urls
