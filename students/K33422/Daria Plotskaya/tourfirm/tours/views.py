from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Tour, Reservation, Review
from .serializers import *
from .filters import *
from rest_framework import generics, filters
from .pagination import CustomPagination
from rest_framework.views import Response
from rest_framework import status


# Список доступных туров / Информация о туре + отзывы
class TourViewSet(ReadOnlyModelViewSet):
    queryset = Tour.objects.order_by(
        "destination")  # Туры сортируются по стране
    pagination_class = CustomPagination

    # Показывает только те туры где есть место
    def get_queryset(self):
        queryset = self.queryset
        # ids = [tour.id for tour in queryset if tour.empty_count > 0]
        ids = [tour.id for tour in queryset]
        return queryset.filter(pk__in=ids)

    # Выдает разный сериализатор в зависимости от того, требуется ли список
    # туров или конкретный тур
    def get_serializer_class(self):
        if self.action == 'list':
            return TourSerializer
        else:
            return TourAndReviewsSerializer


# Список резервирований пользователя
class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.none()  # Задаем queryset чтобы django не
    # выдавал ошибку
    pagination_class = CustomPagination

    # Выбирает только резервирования текущего пользователя
    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user.id)

    # Выдает разный сериализатор для чтения и для записи
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return ReservationWriteSerializer
        else:
            return ReservationReadSerializer


# Отзывы
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.none()  # Задаем queryset чтобы django не
    # выдавал ошибку
    serializer_class = ReviewSerializer
    pagination_class = CustomPagination

    # Выбирает только отзывы текущего пользователя
    def get_queryset(self):
        return Review.objects.filter(reservation__user=self.request.user.id)


# Ручные фильтры
class ToursByCountListView(generics.ListAPIView):
    serializer_class = TourSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Tour.objects.all()
        count = self.request.query_params.get('count')

        if count:
            queryset = queryset.filter(count=count)

        return queryset


class ToursByCountDestinationListView(generics.ListAPIView):
    serializer_class = TourSerializer

    def get_queryset(self):
        queryset = Tour.objects.all()
        count = self.request.query_params.get('count')
        destination = self.request.query_params.get('destination')

        if count and destination:
            queryset = queryset.filter(count=count, destination=destination)

        return queryset


class ReservationsByCountApprovedListView(generics.ListAPIView):
    serializer_class = ReservationReadSerializer

    def get_queryset(self):
        queryset = Reservation.objects.all()
        user = self.request.user

        if user.is_authenticated:
            count = self.request.query_params.get('count')
            approved = self.request.query_params.get('approved')
            if count and approved:
                queryset = queryset.filter(count=count, approved=approved)

        return queryset


# Автоматичeские фильтры
class ReviewsOrderedFilterView(generics.ListAPIView):

    # queryset = Review.objects.all()

    def get_queryset(self):
        return Review.objects.filter(
            # reservation__tour_id=self.request.query_params.tour
            reservation__tour_id=self.kwargs.get('tour')
        )

    serializer_class = ReviewSerializer
    filter_backends = (filters.OrderingFilter,)
    filterset_fields = 'stars'
    pagination_class = CustomPagination


class ReservationsSearchFilterViewAll(generics.ListAPIView):

    queryset = Reservation.objects.all()
    serializer_class = ReservationReadSerializer
    filter_backends = (filters.SearchFilter,)
    pagination_class = CustomPagination
    search_fields = ('count', 'tour__destination')


# filtered by user for front
class ReservationsSearchFilterView(generics.ListAPIView):

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user.id)

    serializer_class = ReservationReadSerializer
    filter_backends = (filters.SearchFilter,)
    pagination_class = CustomPagination
    search_fields = ('count', 'tour__destination')


class ReservationsSearchFilterView2(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationReadSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('count', 'tour__destination')


class ToursPriceRangeFilterView(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    filterset_class = ToursPriceRangeFilter
    pagination_class = CustomPagination


class ToursPriceRangeFilterView2(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    filterset_class = ToursPriceRangeFilter
    pagination_class = CustomPagination


# Вью для демонстрации в drf
class TourView2(generics.ListAPIView):
    serializer_class = TourSerializer
    queryset = Tour.objects.all()


class TourView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TourAPISerializer
    queryset = Tour.objects.all()


class ReviewView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewAPISerializer
    queryset = Review.objects.all()


class ReservationView(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user.id)

    serializer_class = ReservationAPISerializer
    queryset = Reservation.objects.all()


class ReservationView2(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReservationAPISerializer
    queryset = Reservation.objects.all()


class CreateTourView(generics.CreateAPIView):
    serializer_class = TourAPISerializer
    queryset = Tour.objects.all()


class CreateReservationView(generics.CreateAPIView):
    serializer_class = ReservationAPISerializer
    queryset = Reservation.objects.all()


class CreateReviewView(generics.CreateAPIView):
    serializer_class = ReviewAPISerializer
    queryset = Review.objects.all()


class ReviewPhotoCreateView(generics.CreateAPIView):
    queryset = ReviewPhoto.objects.all()
    serializer_class = ReviewPhotoSerializer


class MultipleReviewPhotoCreateView(generics.CreateAPIView):
    queryset = ReviewPhoto.objects.all()
    serializer_class = ReviewPhotoSerializer

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')

        for file in files:
            review_id = request.POST.get('review')
            file = ReviewPhoto(
                review=Review.objects.get(id=review_id),
                file=file)
            file.save()

        return Response(str(request.data), status=status.HTTP_201_CREATED)
