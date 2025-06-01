from django.db import models

class YourModel(models.Model):
    string = models.CharField(max_length=255)
    int = models.IntegerField()
    website = models.URLField(max_length=200, blank=True, null=True)
    url = f"https://file.com/profile?name={name}&age={age}"