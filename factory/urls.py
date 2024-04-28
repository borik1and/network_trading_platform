from rest_framework.routers import DefaultRouter
from factory.views import FactoryContactsViewSet, FactoryProductViewSet

app_name = 'factory'

router = DefaultRouter()
router.register(r'factory-contacts', FactoryContactsViewSet, basename='factory-contacts')
router.register(r'factory-product', FactoryProductViewSet, basename='factory-product')

urlpatterns = [

              ] + router.urls
