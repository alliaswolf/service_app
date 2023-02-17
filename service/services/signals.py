from django.conf import settings
from django.core.cache import cache
from django.db.models.signals import post_delete
from django.dispatch import receiver

from services.models import Subscription


# receiver – The function who receives the signal and does something.
# sender – Sends the signal.
# created — Checks whether the model is created or not.
# instance — Created model instance.
# **kwargs – Wildcard keyword arguments.

@receiver(post_delete, sender=Subscription)
def delete_cache_total_sum(sender, instance, **kwargs):
    cache.delete(settings.PRICE_CACHE_NAME)
