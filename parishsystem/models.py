from django.db import models


"""
Sacraments
"""



class Invoice(models.Model):
    date_issued = models.DateField()
    or_number = models.CharField(max_length=255)
    received_by = models.CharField(max_length=255) # name that appears on the actual invoice
    profiles_id = [] # profiles that are connected to this invoice item
    pass

class InvoiceItems(models.Model):
    invoice = models.ForeignKey(
        'Invoice', 
        on_delete=models.CASCADE,
        related_name='invoice_items',
    )
    quantity = models.IntegerField() # defaults to 1 if item type is sacrament
    balance = models.DecimalField(max_digits=16, decimal_places=2)  # the amount needed to be paid (remaining)
    amount_paid = models.DecimalField(max_digits=16, decimal_places=2) # actual amount paid
    # the next invoice item's balance is computed by this invoice items's balance and amount_paid.



class ItemType(models.Model):
    name = models.CharField(max_length=255)
    suggested_price = models.DecimalField(max_digits=16, decimal_places=2)


class PersonAbstractModel(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    suffix = models.CharField(max_length=255)
    class Meta:
        abstract=True

class Profile(PersonAbstractModel):
    birthdate = models.DateField()
    gender = models.BooleanField()
    birthplace = models.CharField(max_length=255)
    residence = models.CharField(max_length=255)

class Minister(PersonAbstractModel):
    birthdate = models.DateField()
    ministry_type = models.SmallIntegerField()
    status = models.SmallIntegerField()

class Sponsor(PersonAbstractModel):
    confirmation = models.ForeignKey(
        'Confirmation',
        on_delete=models.PROTECT,
        related_name='sponsors',
        null=True,
        blank=True,
    )
    baptism = models.ForeignKey(
        'Baptism',
        on_delete=models.PROTECT,
        related_name='sponsors',
        null=True,
        blank=True,
    )
    marriage = models.ForeignKey(
        'Marriage',
        on_delete=models.PROTECT,
        related_name='sponsors',
        null=True,
        blank=True,
    )
    residence = models.CharField(max_length=511)


