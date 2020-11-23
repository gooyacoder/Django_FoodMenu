from django.db import models

# Create your models here.
class Item(models.Model):
	item_name = models.CharField(max_length=200)
	item_desc = models.CharField(max_length=200)
	item_price = models.IntegerField()
	item_image = models.CharField(max_length=500, default="https://lh3.googleusercontent.com/proxy/3slo6vQK0O5jchXrrArp1JocMXYyiGBZvFDwdd7hNfzOm0yvi9tnB9VDO4jEnvpXV3LOINboqWeKbiqxqtvFaAIgs7B5NmiCULF3DQ7mzNVQcnM5Obc8tD164xOk")

	def __str__(self):
		return self.item_name