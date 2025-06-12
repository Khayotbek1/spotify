from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/albums/')
    created_at = models.DateTimeField(auto_now_add=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    duration = models.DurationField(blank=True, null=True)
    file = models.FileField(upload_to='files/songs/')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
