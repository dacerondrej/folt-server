from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
  name = models.CharField(max_length = 180)
  email = models.CharField(max_length = 240)

  def __str__(self):
      return self.name

class Courier(models.Model):
  name = models.CharField(max_length = 180)
  email = models.CharField(max_length = 240)

  def __str__(self):
      return self.name

class OfferItem(models.Model):
  name = models.CharField(max_length = 64)
  unit = models.CharField(max_length = 64)
  amount = models.FloatField()
  price = models.FloatField()

  def __str__(self):
      return self.name

class Offer(models.Model):
  offer_id = models.AutoField(primary_key=True)
  state = models.CharField(default="new", max_length = 64)
  items = models.ManyToManyField(OfferItem)

  def __str__(self):
      return str(self.offer_id)

class Pickup(models.Model):
  pickup_id = models.AutoField(primary_key=True)
  offer_id = models.PositiveIntegerField()
  courier_email = models.CharField(max_length = 240)

  def __str__(self):
      return str(self.pickup_id)
