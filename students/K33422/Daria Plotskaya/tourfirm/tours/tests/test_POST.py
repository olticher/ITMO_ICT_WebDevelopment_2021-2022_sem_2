from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from ..models import *


class CreateTourTest(TestCase):

    def test_create_tour(self):
        url = reverse('tours:create_tour')

        data = {
            'date_from': '2022-08-14',
            'date_to': '2022-08-21',
            'destination': 'Направление',
            'hotel': 'Название отеля',
            'id': 1,
            'prev_price': 1000,
            'price': 2000,
            'count': 0
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data)


class CreateReservationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tour.objects.create(
            id=1,
            destination="Направление1",
            date_from='2022-08-14',
            date_to='2022-08-21',
            hotel="Название отеля 1",
            prev_price=1000,
            price=1000,
            count=1,
        )

        CustomUser.objects.create(
            id=1,
            first_name="Имя",
            last_name="Фамилия",
        )

    def test_create_reservation(self):
        url = reverse('tours:create_reservation')

        data = {
            'approved': True,
            'count': 1,
            'id': 1,
            'tour': 1,
            'user': 1
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data)


class CreateReviewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tour.objects.create(
            id=1,
            destination="Направление1",
            date_from='2022-08-14',
            date_to='2022-08-21',
            hotel="Название отеля 1",
            prev_price=1000,
            price=1000,
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

    def test_create_review(self):
        url = reverse('tours:create_review')

        data = {
            'id': 1,
            'reservation': 1,
            'text': 'Нравится!',
            'stars': 5,
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data)
