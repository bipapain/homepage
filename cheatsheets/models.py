from django.db import models


class Cheatsheet(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='cheatsheets/images/')
    commands = models.JSONField()
    pdf = models.FileField(blank=True, upload_to='cheatsheets/pdfs/')

    def __str__(self):
        return self.title
