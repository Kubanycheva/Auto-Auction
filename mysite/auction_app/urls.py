from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user_profile', UserProfileViewSet)
router.register(r'brand', BrandViewSet)
router.register(r'model', ModelViewSet)
router.register(r'image', ImageViewSet)
router.register(r'favorite', FavoriteViewSet, basename='favorite-list')
router.register(r'favorite-detail', FavoriteViewSet, basename='favorite-detail')

router.register(r'favorite_movie', FavoriteMovieViewSet, basename='favorite_movie-list')
router.register(r'favorite_movie-detail', FavoriteMovieViewSet, basename='favorite_movie-detail')

urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('categories/', CategoryListApiVIew.as_view(), name='categories_list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='categories_detail'),

    path('car/', CarListApiView.as_view(), name='car_list'),
    path('car/<int:pk>/', CarDetailApiView.as_view(), name='car_detail'),

    path('auction', AuctionListApiVIew.as_view(), name='auctions'),
    path('bid', BidListApiView.as_view(), name='bids'),
    path('feedback', FeedBackListCreateAPIView.as_view(), name='feedbacks')

]