from django.db import models

# Create your models here.

class Produtc(models.Model):
  name_product = models.CharField(max_length=200)
  value_product = models.FloatField()
  invetory_product = models.FloatField()

  def getName(self):
    return self.name_product

  def getProduct(self):
    return self.value_product

  def getInventory(self):
    return self.invetory_product   

class Delete(models.Model):
  name_product = models.CharField(max_length=200)
  value_product = models.FloatField()
  invetory_product = models.FloatField()
  
  def getName(self):
    return self.name_product

  def getProduct(self):
    return self.value_product

  def getInventory(self):
    return self.invetory_product    

# class Client(models.Model):
#   name_client = models.CharField(max_length=200)

# class Provider(models.Model):
#   name_provider = models.CharField(max_length=200)

