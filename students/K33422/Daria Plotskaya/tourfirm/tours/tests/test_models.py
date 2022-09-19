from django.test import TestCase
from django.db.models import DateField
import datetime

from ..models import *
from users.models import *


class TourModelCreateTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tour.objects.create(
            id=1,
            destination="Направление",
            date_from=datetime.date.today(),
            date_to=datetime.date.today(),
            hotel="Название отеля",
            prev_price=1000,
            price=2000,
            count=1,
        )

    def test_tour_destination(self):
        tour = Tour.objects.get(id=1)
        self.assertEquals(tour.destination, "Направление")


class TourModelFieldTypeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tour.objects.create(
            id=1,
            destination="Направление",
            date_from=datetime.date.today(),
            date_to=datetime.date.today(),
            hotel="Название отеля",
            prev_price=1000,
            price=2000,
            count=1,
        )

    def test_date_from_field_type(self):
        tour = Tour.objects.get(id=1)
        date_from = tour._meta.get_field('date_from')
        self.assertTrue(isinstance(date_from, DateField))


class TourModelStrTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tour.objects.create(
            id=1,
            destination="Направление",
            date_from=datetime.date.today(),
            date_to=datetime.date.today(),
            hotel="Название отеля",
            prev_price=1000,
            price=2000,
            count=1,
        )

        CustomUser.objects.create(
            id=1,
            first_name="Имя",
            last_name="Фамилия",
        )

        Reservation.objects.create(
            id=1,
            user=CustomUser.objects.get(id=1),
            tour=Tour.objects.get(id=1),
            count=1,
            approved=True
        )

    def test_tour_empty_count(self):
        tour = Tour.objects.get(id=1)
        expected_value = tour.empty_count

        self.assertEquals(expected_value, 0)

    def test_tour_adjusted_empty_count(self):
        tour = Tour.objects.get(id=1)
        expected_value = tour.adjusted_empty_count(1)

        self.assertEquals(expected_value, 1)

    def test_tour_str(self):
        tour = Tour.objects.get(id=1)

        expected_tour_str = f"Тур \"{tour.destination}\" ({tour.date_from} - {tour.date_to})"

        self.assertEquals(str(tour), expected_tour_str)
