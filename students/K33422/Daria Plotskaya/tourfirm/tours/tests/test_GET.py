from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from ..models import *


class GetTourTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tour.objects.create(
            id=1,
            destination="Направление",
            date_from='2022-08-14',
            date_to='2022-08-21',
            hotel="Название отеля",
            prev_price=1000,
            price=2000,
            count=1,
        )

    def test_get_tour(self):
        url = reverse('tours:tours', args=['1'])

        data = {
            "count": 1,
            "next": None,
            "previous": None,
            'results': [{
                'date_from': '2022-08-14',
                'date_to': '2022-08-21',
                'destination': 'Направление',
                'empty_count': 1,
                'hotel': 'Название отеля',
                'id': 1,
                'prev_price': 1000,
                'price': 2000
            }]}

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)


class SearchReservationsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tour.objects.create(
            id=1,
            destination="Направление",
            date_from='2022-08-14',
            date_to='2022-08-21',
            hotel="Название отеля",
            prev_price=1000,
            price=2000,
            count=1,
        )

        Tour.objects.create(
            id=2,
            destination="Направление2",
            date_from='2022-08-14',
            date_to='2022-08-21',
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

        Reservation.objects.create(
            id=2,
            user=CustomUser.objects.get(id=1),
            tour=Tour.objects.get(id=1),
            count=1,
            approved=True
        )

        Reservation.objects.create(
            id=3,
            user=CustomUser.objects.get(id=1),
            tour=Tour.objects.get(id=2),
            count=1,
            approved=True
        )

    def test_search_reservations(self):
        url = reverse('tours:reservations_search2')

        data = {
            "count": 1,
            "next": None,
            "previous": None,
            'results': [
                {
                    'approved': True,
                    'count': 1,
                    'has_review': False,
                    'id': 3,
                    'total_price': 2000,
                    'tour': {
                        'date_from': '2022-08-14',
                        'date_to': '2022-08-21',
                        'destination': 'Направление2',
                        'empty_count': 0,
                        'hotel': 'Название отеля',
                        'id': 2,
                        'prev_price': 1000,
                        'price': 2000}}
            ]
        }

        response = self.client.get(url, {'search': 'Направление2'},
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)


class GetPriceRangeFilteredToursTest(TestCase):

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

        Tour.objects.create(
            id=2,
            destination="Направление2",
            date_from='2022-08-14',
            date_to='2022-08-21',
            hotel="Название отеля 2",
            prev_price=1000,
            price=2000,
            count=1,
        )

        Tour.objects.create(
            id=3,
            destination="Направление3",
            date_from='2022-08-14',
            date_to='2022-08-21',
            hotel="Название отеля 3",
            prev_price=1000,
            price=3000,
            count=1,
        )

    def test_price_range_filter_tours(self):
        url = reverse('tours:tours_price_range')

        data = {
            'count': 1,
            'links': {'next': None, 'previous': None},
            'num_pages': 1,
            'page_number': 1,
            'results': [
                {
                    'date_from': '2022-08-14',
                    'date_to': '2022-08-21',
                    'destination': 'Направление2',
                    'empty_count': 1,
                    'hotel': 'Название отеля 2',
                    'id': 2,
                    'prev_price': 1000,
                    'price': 2000
                }
            ]
        }

        response = self.client.get(url,
                                   {'price_min': '1500',
                                    'price_max': '2500',
                                    },
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)
