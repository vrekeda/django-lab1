from django.db import models

# Create your models here.


class Language (models.Model):
    name = models.CharField(max_length=60, null=True)
    ukrainian_name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Word (models.Model):
    original = models.CharField(max_length=60)
    translation = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add=True)
    learnt = models.BooleanField(default=False, null=False)
    translate_from = models.ForeignKey('Language', on_delete=models.PROTECT, null=True, related_name='translate_from')
    translate_to = models.ForeignKey('Language', on_delete=models.PROTECT, null=True, related_name='translate_to')

    def __str__(self):
        return self.original


class ConnectedUsers(models.Model):
    first_name = models.CharField(max_length=50)
    connected = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "%s connected at %s" % (self.first_name, self.connected)
