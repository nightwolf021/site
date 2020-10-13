from django.db import models


class user_model(models.Model):
    phone_number = models.CharField(max_length=16, unique=True, primary_key=True)
    key = models.CharField(max_length=128, null=True, blank=True)
    username = models.CharField(max_length=32, null=True, blank=True)
    password = models.CharField(max_length=32, null=True, blank=True)
    url = models.CharField(max_length=1024, null=True, blank=True)
    # default is equal true because we make users manually
    had_bought = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=32, choices={('reza', 'reza'), ('saeed', 'saeed')})
    customer_code = models.IntegerField(unique=True)
    introducer_code = models.IntegerField()

    def __str__(self):
        return self.phone_number


class result_model(models.Model):
    title = models.CharField(max_length=256)
    result_code = models.IntegerField(default=0)
    label = models.CharField(max_length=32, default='noting_yet')

    def __str__(self):
        return self.label


class error_model(models.Model):
    log = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return 'from {} in {}'.format(self.ip, self.created_at)
