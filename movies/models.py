from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255,verbose_name="عنوان")
    synopsis = models.TextField(verbose_name="خلاصه داستان")
    actors = models.CharField(max_length=255, verbose_name="بازیگران")
    genre = models.CharField(max_length=255, verbose_name="ژانر")
    duration = models.IntegerField(verbose_name="مدت زمان")

    class Meta:
        verbose_name="فیلم"
        verbose_name_plural = "فیلم ها"
    
    def __str__(self):
        return "{} - {}".format(self.title,self.genre)