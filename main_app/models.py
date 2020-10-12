from django.db import models


class user_model(models.Model):
    phone_number = models.CharField(max_length=16, unique=True)
    key = models.CharField(max_length=128, null=True)
    # default is equal true because we make users manually
    had_bought = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=32, choices={('reza', 'reza'), ('saeed', 'saeed')})
    customer_code = models.IntegerField(unique=True)
    introducer_code = models.IntegerField()

    def __str__(self):
        return self.phone_number


class result_model(models.Model):
    title = models.CharField(max_length=256)
    result_code = models.IntegerField(default=0)
    label = models.CharField(max_length=32, default='noting_yet')


class error_model(models.Model):
    log = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now=True)
    ip = models.CharField(max_length=16, null=True, blank=True)
