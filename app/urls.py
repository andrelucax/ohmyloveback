from django.urls import path
from .views import LoginView, CloupeCreateView, CoupleMessageCreateAPIView, CoupleMessageDetailAPIView, CoupleSpecialDateCreateAPIView, CoupleSpecialDateDetailAPIView, CoupleWishListCreateAPIView, CoupleWishListDetailAPIView, CoupleImageCreateAPIView, CoupleImageDetailAPIView, CoupleMessageOfTheDayAPIView, CoupleSpecialDateListAPIView, CoupleWishListListAPIView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('couple/create/', CloupeCreateView.as_view(), name='couple-creation'),
    path('couple-messages/create/', CoupleMessageCreateAPIView.as_view(), name='create_couple_message'),
    path('couple-messages/<int:pk>/', CoupleMessageDetailAPIView.as_view(), name='couple_message_detail'),
    path('couple-specialdates/', CoupleSpecialDateListAPIView.as_view(), name='list_couple_special_date'),
    path('couple-specialdates/create/', CoupleSpecialDateCreateAPIView.as_view(), name='create_couple_special_date'),
    path('couple-specialdates/<int:pk>/', CoupleSpecialDateDetailAPIView.as_view(), name='couple_special_date_detail'),
    path('couple-wishlist/', CoupleWishListListAPIView.as_view(), name='list_couple_wishlist_item'),
    path('couple-wishlist/create/', CoupleWishListCreateAPIView.as_view(), name='create_couple_wishlist_item'),
    path('couple-wishlist/<int:pk>/', CoupleWishListDetailAPIView.as_view(), name='couple_wishlist_item_detail'),
    path('couple-images/create/', CoupleImageCreateAPIView.as_view(), name='create_couple_image'),
    path('couple-images/<int:pk>/', CoupleImageDetailAPIView.as_view(), name='couple_image_detail'),
    path('message-of-the-day/', CoupleMessageOfTheDayAPIView.as_view(), name='message_of_the_day'),
]