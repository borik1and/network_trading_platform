from rest_framework.routers import DefaultRouter

from retail_network.views import RetailNetworkViewSet

app_name = 'retail_network'

router = DefaultRouter()
router.register(r'retail-network-contacts', RetailNetworkViewSet, basename='retail-network-contacts')

urlpatterns = [

              ] + router.urls
