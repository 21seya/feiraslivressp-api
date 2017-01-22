import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Feira

log = logging.getLogger('feiraslivres')


@receiver(post_save, sender=Feira)
def feira_saved_handler(sender, instance, created, **kwargs):
    if created:
        message = "Feira [id={}] was CREATED.".format(instance.id)
        log.info(message)
    else:
        message = "Feira [id={}] was UPDATED.".format(instance.id)
        log.info(message)


@receiver(post_delete, sender=Feira)
def feira_deleted_handler(sender, instance, using, **kwargs):
    message = 'Feira [id={}] was DELETED.'.format(instance.id)
    log.info(message)
