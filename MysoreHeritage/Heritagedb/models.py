from django.db import models


class Category(models.Model):
    heritage_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Heritage(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='heritage_images/', blank=True, null=True)
    timings = models.TextField(max_length=500,blank=True,null=True)
    entry_fee = models.TextField()
    established_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Location(models.Model):
    heritage = models.OneToOneField(Heritage, on_delete=models.CASCADE, related_name='location_info')
    address = models.CharField(max_length=255)
    area = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.address
   