from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'tours'

# Регистрируем пути
router = DefaultRouter()
router.register("tours", TourViewSet)
router.register("reservations", ReservationViewSet)
router.register("reviews", ReviewViewSet)

urlpatterns = [
    # Ручные фильтры
    path("tours/<int:pk>/", TourView2.as_view(), name='tours'),
    path("reservations", ReservationViewSet),
    path("reviews", ReviewViewSet),

    path('tours_by_count/', ToursByCountListView.as_view()),
    path('tours_by_count_destination/',
         ToursByCountDestinationListView.as_view()),
    path('reservations_by_count_approved/',
         ReservationsByCountApprovedListView.as_view()),

    # Aвтоматичеcкие фильтры
    path('reviews_ordered/<int:tour>',
         ReviewsOrderedFilterView.as_view()),
    path('reservations_search_all/',
         ReservationsSearchFilterViewAll.as_view(), name='reservations_search'),
    path('reservations_search/',
         ReservationsSearchFilterView.as_view()),
    path('tours_price_range/',
         ToursPriceRangeFilterView.as_view(), name='tours_price_range'),

    # generics
    path('tour/<int:pk>/',
         TourView.as_view(), name='tour'),
    path('review/<int:pk>/',
         ReviewView.as_view(), name='review'),
    path('reservation/<int:pk>/',
         ReservationView.as_view(), name='reservation'),

    path('create_tour/',
         CreateTourView.as_view(), name='create_tour'),
    path('create_reservation/',
         CreateReservationView.as_view(), name='create_reservation'),
    path('create_review/',
         CreateReviewView.as_view(), name='create_review'),

    path('upload_review_photo/',
         ReviewPhotoCreateView.as_view()),
    path('upload_review_photos/',
         MultipleReviewPhotoCreateView.as_view()),

    # test endpoints
    path('reservation2/<int:pk>/',
         ReservationView2.as_view(), name='reservation2'),
    path('reservations2_search/',
         ReservationsSearchFilterView2.as_view(), name='reservations_search2'),

    path("", include(router.urls)),
]
