from django.db import models

# Create your models here.
class ShowEndAlive(models.Model):
    uuid = models.CharField(unique=True, max_length=32, blank=True, null=True)
    mac_address = models.CharField(max_length=32, blank=True, null=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    product_id = models.CharField(max_length=32, blank=True, null=True)
    os_version = models.CharField(max_length=32, blank=True, null=True)
    kernel_version = models.CharField(max_length=32, blank=True, null=True)
    cpu_model = models.CharField(max_length=64, blank=True, null=True)
    bios_version = models.CharField(max_length=16)
    graphics_model = models.CharField(max_length=128, blank=True, null=True)
    graphics_driver_version = models.CharField(max_length=32, blank=True, null=True)
    client_version = models.CharField(max_length=8, blank=True, null=True)
    online_time = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'show_end_alive'
        unique_together = (('id', 'bios_version'),)