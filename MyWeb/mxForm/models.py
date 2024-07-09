from django.db import models

# Create your models here.


class FundRation(models.Model):
    name = models.CharField(max_length=30)
    pct = models.IntegerField()
    comment = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
