
from rest_framework.routers import DefaultRouter

from entrepreneur.views import EntrepreneurViewSet

app_name = 'entrepreneur'

router = DefaultRouter()
router.register(r'entrepreneur', EntrepreneurViewSet, basename='entrepreneur')

urlpatterns = [

              ] + router.urls
