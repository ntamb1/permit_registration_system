from django.db import models


class Ugandan(models.Model):
    # Ugandan & EA
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nin = models.CharField(max_length=20)
    id_scan = models.ImageField()
    # Medicals
    medical_scan = models.ImageField()
    # Payment Form
    payment_scan = models.ImageField()
    
    def __str__(self):
        return self.first_name


class EastAfrican(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ea_nin = models.CharField(max_length=20)
    id_scan = models.ImageField()
    # Medicals
    medical_scan = models.ImageField()
    # Payment Form
    payment_scan = models.ImageField()

    def __str__(self):
        return self.first_name


class Foreigner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    visa_no = models.CharField(max_length=20)
    visa_scan = models.ImageField()
    passport_no = models.CharField(max_length=20)
    passport_scan = models.ImageField()
    work_permit_no = models.CharField(max_length=20, blank=True, null=True)
    wp_scan = models.ImageField(blank=True, null=True)
    # Medicals
    medical_scan = models.ImageField()
    # Payment Form
    payment_scan = models.ImageField()

    def __str__(self):
        return self.first_name


class Renewal(models.Model):
    c_id = models.CharField(max_length=15)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    expiry_date = models.CharField(max_length=12)
    scan = models.ImageField()
    payment_scan = models.ImageField()

    def __str__(self):
        return self.c_id




