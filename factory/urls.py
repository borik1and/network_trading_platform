from rest_framework.routers import DefaultRouter
from factory.views import FactoryViewSet

app_name = 'factory'

router = DefaultRouter()
router.register(r'factory', FactoryViewSet, basename='factory')

urlpatterns = [

              ] + router.urls
