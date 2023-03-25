from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Clients(models.Model):
    client_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True)
    phone = PhoneNumberField(blank=True)

class Salons(models.Model):
    salon_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    phone = PhoneNumberField()
    website = models.URLField(max_length = 200, blank=True)

class Stylists(models.Model):
    stylist_id = models.IntegerField(primary_key=True)
    stylist_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField(blank=True)
    salon_id = models.ForeignKey(Salons, on_delete=models.CASCADE)

class Reviews(models.Model):
    review_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    review_date = models.DateTimeField()
    salon_id = models.ForeignKey(Salons, on_delete=models.CASCADE)

class Services(models.Model):
    service_id = models.IntegerField(primary_key=True)
    service_name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    salon_id = models.ForeignKey(Salons, on_delete=models.CASCADE)

class Appointments(models.Model):
    appointment_id = models.IntegerField(primary_key=True)
    appointment_date = models.DateTimeField()
    duration = models.IntegerField()
    notes = models.TextField(blank=True)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)

class Payments(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_datetime = models.DateTimeField()
    appointment_id = models.ForeignKey(Appointments, on_delete=models.CASCADE)