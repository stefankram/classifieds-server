from django.db import models


class Message(models.Model):
    """
    Message Model

    A direct message between a buyer and a seller

    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        editable=False)

    _from = models.ForeignKey(
        db_column='from',
        on_delete=models.CASCADE,
        to=User)

    message = models.CharField(
        db_column='message',
        max_length=1024)

    to = models.ForeignKey(
        db_column='to',
        on_delete=models.CASCADE,
        to=User)