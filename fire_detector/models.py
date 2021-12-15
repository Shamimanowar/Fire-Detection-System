from django.db import models

# Create your models here.


class FireDetector(models.Model):
    node_id = models.CharField(max_length=5)
    flame = models.CharField(max_length=5)
    gas = models.CharField(max_length=5)
    temperature = models.CharField(max_length=5)
    humidity = models.CharField(max_length=5)
    light_intensity = models.CharField(max_length=5)
    captured_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Node Id {self.node_id} Flame {self.flame} Created {self.created_at}'

    class Meta:
        verbose_name_plural = 'Fire Detector Values'
