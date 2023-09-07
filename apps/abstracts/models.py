# Django
from django.db import models
from django.utils import timezone

class AbsctractDateTime(models.Model):
    """
    AbsctractDateTime model.
    """
    datetime_created = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )
    datetime_updated = models.DateTimeField(
        verbose_name='дата обновления',
        auto_now=True
    )
    datetime_deleted = models.DateTimeField(
        verbose_name='дата удаления',
        null=True,
        blank=True
    )

    # удаление песни 
    def delete(self, using=None, keep_parents=False):
        self.datetime_deleted = timezone.now()
        self.save()

    class Meta:
        abstract = True
