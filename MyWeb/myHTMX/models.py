from django.db import models

import datetime


class UserEntry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    start_dt = models.DateField(default=datetime.date.today, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    description1 = models.CharField(max_length=500, blank=True)
    description2 = models.CharField(max_length=500, blank=True)
    description3 = models.CharField(max_length=500, blank=True)
    note1 = models.CharField(max_length=500, blank=True)
    note2 = models.CharField(max_length=500, blank=True)
    note3 = models.CharField(max_length=500, blank=True)
    note4 = models.CharField(max_length=500, blank=True)
    status = models.CharField(max_length=10, blank=True)
    pnl = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    content = models.TextField(blank=True)
    comment1 = models.TextField(blank=True)
    comment2 = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)
    region = models.CharField(max_length=10)

    class Meta:
        db_table = "IssuesEntry"
