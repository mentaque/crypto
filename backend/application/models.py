from django.db import models


class Cryptocurrency(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=25, decimal_places=4)
    volume_24h = models.DecimalField(max_digits=25, decimal_places=4)
    percent_change_1h = models.DecimalField(max_digits=25, decimal_places=4)
    percent_change_24h = models.DecimalField(max_digits=25, decimal_places=4)
    percent_change_7d = models.DecimalField(max_digits=25, decimal_places=4)
    percent_change_30d = models.DecimalField(max_digits=25, decimal_places=4)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
