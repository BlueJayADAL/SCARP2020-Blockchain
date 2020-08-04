from django.db import models


class Display_File(models.Model):
    file_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    display_file = models.FileField()

    def __str__(self):
        return self.file_name


class Display_Name(models.Model):
    file_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    display_file = models.FileField()

    def __str__(self):
        return self.file_name

