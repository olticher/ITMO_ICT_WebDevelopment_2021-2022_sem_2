from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from .models import *
from django.db.models import ObjectDoesNotExist


@receiver(post_save, sender=Tour)
def create_tour(sender, instance, created, **kwargs):
    if created:
        print(f'\n{instance} создан!')


@receiver(pre_save, sender=Tour)
def update_tour_price(sender, instance, **kwargs):
    try:
        prev_instance = Tour.objects.get(id=instance.id)
        instance.prev_price = prev_instance.price
        print(f'Цена обновлена: {instance}\n'
              f'стоил: {instance.prev_price},\n'
              f'а теперь стоит: {instance.price}\n')
    except ObjectDoesNotExist:
        pass


@receiver(pre_delete, sender=Tour)
def delete_tour(sender, instance, **kwargs):
    with open('deleted_log.txt', 'a') as f:
        f.write(f'Тур {instance} удален\n')
