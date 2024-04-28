from rest_framework.routers import DefaultRouter

from retail_network.views import RetailNetworkContactsViewSet, RetailNetworkProductViewSet

app_name = 'retail_network'

router = DefaultRouter()
router.register(r'retail-network-contacts', RetailNetworkContactsViewSet, basename='retail-network-contacts')
router.register(r'retail-network-product', RetailNetworkProductViewSet, basename='retail-network-product')

urlpatterns = [

              ] + router.urls
