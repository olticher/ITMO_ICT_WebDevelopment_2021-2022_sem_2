from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from ..models import *


class UpdateReviewTest(TestCase):

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

        Review.objects.create(
            id=1,
            reservation=Reservation.objects.get(id=1),
            text='Отзыв',
            stars=10
        )

    def test_update_review(self):
        get_url = reverse('tours:review', args=['1'])
        patch_url = reverse('tours:review', args=['1'])

        data = {
            'id': 1,
            'reservation': 1,
            'text': 'Отзыв',
            'stars': 10,
        }

        current_data = self.client.get(get_url, format='json')
        self.assertEqual(current_data.status_code, status.HTTP_200_OK)
        self.assertEqual(current_data.json(), data)

        data['stars'] = 8

        self.client.patch(patch_url, data, content_type='application/json')
        changed_data = self.client.get(get_url, format='json')
        self.assertEqual(changed_data.status_code, status.HTTP_200_OK)
        self.assertEqual(changed_data.json(), data)


class UpdateTourPriceTest(TestCase):

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

    def test_update_price(self):
        get_url = reverse('tours:tour', args=['1'])
        patch_url = reverse('tours:tour', args=['1'])

        data = {
            'date_from': '2022-08-14',
            'date_to': '2022-08-21',
            'destination': 'Направление',
            'hotel': 'Название отеля',
            'id': 1,
            'prev_price': 1000,
            'price': 2000,
            'count': 1
        }

        current_data = self.client.get(get_url, format='json')
        self.assertEqual(current_data.status_code, status.HTTP_200_OK)
        self.assertEqual(current_data.json(), data)

        data['price'] = 3000

        self.client.patch(patch_url, data,
                          content_type='application/json')

        data['prev_price'] = 2000

        changed_data = self.client.get(get_url, format='json')
        self.assertEqual(changed_data.status_code, status.HTTP_200_OK)
        self.assertEqual(changed_data.json(), data)


class UpdateReservationApprovalTest(TestCase):

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
            approved=False
        )

    def test_update_approval(self):
        get_url = reverse('tours:reservation2', args=['1'])
        patch_url = reverse('tours:reservation2', args=['1'])

        data = {
            'approved': False,
            'count': 1,
            'id': 1,
            'tour': 1,
            'user': 1
        }

        current_data = self.client.get(get_url, format='json')
        self.assertEqual(current_data.status_code, status.HTTP_200_OK)
        self.assertEqual(current_data.json(), data)

        data['approved'] = True

        self.client.patch(patch_url, data, content_type='application/json')
        changed_data = self.client.get(get_url, format='json')
        self.assertEqual(changed_data.status_code, status.HTTP_200_OK)
        self.assertEqual(changed_data.json(), data)
