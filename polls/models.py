from django.db import models

# Create your models here.
class Gender(models.Model):
    gender_text = models.CharField(max_length=100)

    def __str__(self):
     return self.gender_text

class Style(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    style_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.style_text

class StyleWebsite(models.Model):
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    stylewebsite_text = models.CharField(max_length=300)
    url = models.URLField("Site URL")

    def __str__(self):
        return self.stylewebsite_text



