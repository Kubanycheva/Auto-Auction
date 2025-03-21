from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user_profile', UserProfileViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'brand', BrandViewSet)
router.register(r'model', ModelViewSet)
router.register(r'car', CarViewSet)
router.register(r'image', ImageViewSet)
router.register(r'auction', AuctionViewSet)
router.register(r'bid', BidViewSet)
router.register(r'feed_back', FeedBackViewSet)

urlpatterns = [
    path('', include(router.urls))
]