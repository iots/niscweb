from django.db import models

# Create your models here.
class ShowPushMessage(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    raw_data_id = models.IntegerField(blank=True, null=True)
    sent_message = models.TextField()
    sent_url = models.TextField(blank=True, null=True)
    sent_number = models.IntegerField(blank=True, null=True)
    recv_number = models.IntegerField(blank=True, null=True)
    open_number = models.IntegerField(blank=True, null=True)
    sent_time = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'show_push_message'