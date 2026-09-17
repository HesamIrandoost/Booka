from django.db.models import Avg
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Review


@receiver(post_save, sender=Review)
def update_book_star(sender, instance, **kwargs):
    instance.book.update_star()


@receiver(post_delete, sender=Review)
def update_book_star(sender, instance, **kwargs):
    instance.book.update_star()