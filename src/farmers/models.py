from django.db import models

class CustomerFarmLinks(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    farm = models.ForeignKey('Farm', on_delete=models.CASCADE)


class Farm(models.Model):
    external_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()


class Customer(models.Model):
    external_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    farms = models.ManyToManyField(Farm, through=CustomerFarmLinks)