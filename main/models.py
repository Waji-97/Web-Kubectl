from django.db import models

# Create your models here.
class Session(models.Model):
    cluster_name = models.CharField(max_length=100)
    shell = models.URLField()
    prometheus = models.URLField()
    alertmanager = models.URLField()
    grafana = models.URLField()

    def __str__(self):
        return self.cluster_name